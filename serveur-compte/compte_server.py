#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""API de comptes étudiants Psyclopédia — SQLite, e-mail/mot de passe et Google.

Stdlib uniquement. Les secrets (PSYCLOPEDIA_JWT_SECRET, identifiants Google)
viennent de l'environnement, jamais du dépôt.

Lancer, depuis la racine du dépôt :

    python3 serveur-compte/compte_server.py --static .

Puis ouvrir http://127.0.0.1:8787/
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import json
import os
import re
import secrets
import sqlite3
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any, Callable

try:
    import psycopg
    from psycopg.errors import IntegrityError as PgIntegrityError
    from psycopg.rows import dict_row
except ImportError:
    psycopg = None  # type: ignore[assignment]
    PgIntegrityError = None  # type: ignore[assignment]
    dict_row = None  # type: ignore[assignment]

INTEGRITY_ERRORS: tuple[type[BaseException], ...] = (sqlite3.IntegrityError,)
if PgIntegrityError is not None:
    INTEGRITY_ERRORS = (sqlite3.IntegrityError, PgIntegrityError)

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DB = os.path.join(HERE, "data", "compte.sqlite")
DEFAULT_PORT = 8787
# Identifiant OAuth public (pas un secret). Surcharge possible via PSYCLOPEDIA_GOOGLE_CLIENT_ID.
PUBLIC_GOOGLE_CLIENT_ID = (
    "340597672237-fscmcisrorgrkh3uppbvtj69848gj6nc.apps.googleusercontent.com"
)
PBKDF2_ITERS = 210_000
SESSION_DAYS = 30
MAX_BODY = 1_048_576
MAX_AVATAR_CHARS = 350_000
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
AVATAR_DATA_RE = re.compile(
    r"^data:image/(jpeg|jpg|png|webp);base64,[A-Za-z0-9+/=\s]+$",
    re.IGNORECASE,
)

# Vérificateur Google remplaçable par les tests.
GoogleVerifier = Callable[[str, str], dict]


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def iso(dt: datetime | None = None) -> str:
    return (dt or utcnow()).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_iso(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


class AuthError(Exception):
    def __init__(self, message: str, status: int = 401):
        super().__init__(message)
        self.status = status
        self.message = message


def hash_password(password: str, salt: bytes | None = None) -> str:
    salt = salt or secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, PBKDF2_ITERS)
    return f"pbkdf2$sha256${PBKDF2_ITERS}${salt.hex()}${digest.hex()}"


def verify_password(password: str, stored: str) -> bool:
    try:
        scheme, algo, iters_s, salt_hex, digest_hex = stored.split("$")
    except ValueError:
        return False
    if scheme != "pbkdf2" or algo != "sha256":
        return False
    try:
        iters = int(iters_s)
        salt = bytes.fromhex(salt_hex)
        expected = bytes.fromhex(digest_hex)
    except ValueError:
        return False
    got = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iters)
    return hmac.compare_digest(got, expected)


def normalize_email(email: str) -> str:
    return (email or "").strip().lower()


def validate_email(email: str) -> str:
    email = normalize_email(email)
    if not EMAIL_RE.match(email) or len(email) > 254:
        raise AuthError("Adresse e-mail invalide.", 400)
    return email


def validate_password(password: str) -> str:
    if not isinstance(password, str) or len(password) < 8:
        raise AuthError("Le mot de passe doit contenir au moins 8 caractères.", 400)
    if len(password) > 200:
        raise AuthError("Mot de passe trop long.", 400)
    return password


def validate_name(name: str) -> str:
    name = (name or "").strip()
    if not name:
        raise AuthError("Le nom affiché est obligatoire.", 400)
    if len(name) > 80:
        name = name[:80]
    return name


def verify_google_token(id_token: str, expected_aud: str) -> dict:
    """Vérifie un jeton d'identité Google auprès de tokeninfo."""
    if not expected_aud:
        raise AuthError("La connexion Google n'est pas configurée sur ce serveur.", 503)
    if not id_token or len(id_token) > 8192:
        raise AuthError("Jeton Google manquant.", 400)
    url = "https://oauth2.googleapis.com/tokeninfo?id_token=" + urllib.parse.quote(id_token)
    try:
        req = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        raise AuthError("Impossible de vérifier le jeton Google.") from exc
    if data.get("error") or data.get("error_description"):
        raise AuthError("Jeton Google invalide.")
    if data.get("aud") != expected_aud:
        raise AuthError("Jeton Google destiné à une autre application.")
    verified = str(data.get("email_verified", "")).lower()
    if verified not in ("true", "1"):
        raise AuthError("Adresse Google non vérifiée.")
    email = normalize_email(data.get("email") or "")
    sub = str(data.get("sub") or "")
    if not email or not sub:
        raise AuthError("Jeton Google incomplet.")
    name = (data.get("name") or email.split("@")[0])[:80]
    picture = validate_google_picture(str(data.get("picture") or ""))
    return {"sub": sub, "email": email, "name": name, "picture": picture}


def validate_google_picture(url: str) -> str:
    url = (url or "").strip()
    if not url or len(url) > 512:
        return ""
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https":
        return ""
    host = (parsed.hostname or "").lower()
    if host != "lh3.googleusercontent.com" and not host.endswith(".googleusercontent.com"):
        return ""
    return url


def validate_custom_avatar(image: str) -> str:
    image = (image or "").strip()
    if not image:
        return ""
    compact = image.replace("\n", "").replace("\r", "").replace(" ", "")
    if len(compact) > MAX_AVATAR_CHARS:
        raise AuthError("Photo trop volumineuse (maximum environ 250 Ko).", 400)
    if not AVATAR_DATA_RE.match(compact):
        raise AuthError("Format de photo invalide. JPEG, PNG ou WebP uniquement.", 400)
    header, b64 = compact.split(",", 1)
    try:
        raw = base64.b64decode(b64, validate=True)
    except Exception as exc:
        raise AuthError("Photo illisible.", 400) from exc
    if len(raw) < 32 or len(raw) > 280_000:
        raise AuthError("Photo trop volumineuse.", 400)
    jpeg = raw[:3] == b"\xff\xd8\xff"
    png = raw[:8] == b"\x89PNG\r\n\x1a\n"
    webp = raw[:4] == b"RIFF" and raw[8:12] == b"WEBP"
    if not (jpeg or png or webp):
        raise AuthError("Format de photo invalide.", 400)
    return header + "," + b64


GOOGLE_TOKEN_VERIFIER: GoogleVerifier = verify_google_token


def prepare_database_url(url: str) -> str:
    """Normalise l'URL Postgres sans jamais l'afficher.

    `postgres://` devient `postgresql://`. L'hôte externe Render (*.render.com)
    exige SSL ; l'hôte interne du même compte n'en a pas.
    """
    raw = (url or "").strip()
    if raw.startswith("postgres://"):
        raw = "postgresql://" + raw[len("postgres://"):]
    parts = urllib.parse.urlsplit(raw)
    host = (parts.hostname or "").lower()
    query = urllib.parse.parse_qsl(parts.query, keep_blank_values=True)
    keys = {key for key, _ in query}
    if host.endswith(".render.com") and "sslmode" not in keys:
        query.append(("sslmode", "require"))
    return urllib.parse.urlunsplit((parts.scheme, parts.netloc, parts.path, urllib.parse.urlencode(query), parts.fragment))


def database_host_label(url: str) -> str:
    """Hôte seul, sans identifiants, pour les journaux."""
    raw = (url or "").strip()
    if raw.startswith("postgres://"):
        raw = "postgresql://" + raw[len("postgres://"):]
    parts = urllib.parse.urlsplit(raw)
    host = parts.hostname or "inconnu"
    if parts.port:
        return f"{host}:{parts.port}"
    return host


class Store:
    """Base réelle : PostgreSQL en production, SQLite en local et dans les tests."""

    def __init__(self, path: str, database_url: str = "", *, connect: bool = True):
        self.lock = threading.RLock()
        self.database_url = (database_url or "").strip()
        self.ready = False
        self.last_error = ""
        self._closed = False
        self._dial: threading.Thread | None = None
        self.conn = None
        if self.database_url:
            if psycopg is None:
                raise RuntimeError("Le module psycopg est requis pour PostgreSQL.")
            self.kind = "postgres"
            self.path = "postgres:" + database_host_label(self.database_url)
            if connect:
                self.connect_with_retry(forever=False)
                if not self.ready:
                    raise RuntimeError(f"PostgreSQL injoignable ({self.last_error or 'timeout'}).")
        else:
            directory = os.path.dirname(path)
            if directory:
                os.makedirs(directory, exist_ok=True)
            self.kind = "sqlite"
            self.path = path
            self.conn = sqlite3.connect(path, check_same_thread=False)
            self.conn.row_factory = sqlite3.Row
            self._execute("PRAGMA foreign_keys = ON")
            self._execute("PRAGMA journal_mode = WAL")
            self._init_schema()
            self.ready = True

    def connect_with_retry(self, forever: bool = False, attempts: int = 4) -> None:
        """Ouvre Postgres. `forever` retente tant que le processus tourne."""
        delay = 1.0
        n = 0
        while not self.ready and not self._closed:
            n += 1
            if not forever and n > attempts:
                return
            print(f"Connexion Postgres {self.path} (tentative {n})…", flush=True)
            try:
                conn = self._open_postgres()
                print(f"Connexion Postgres établie ({self.path}).", flush=True)
            except Exception as exc:
                self.last_error = type(exc).__name__
                print(
                    f"Postgres {self.path} tentative {n} : {self.last_error}",
                    flush=True,
                )
                time.sleep(delay)
                delay = min(delay * 2, 15.0)
                continue
            try:
                with self.lock:
                    if self._closed:
                        conn.close()
                        return
                    self.conn = conn
                    self._init_schema()
                    self.ready = True
                    self.last_error = ""
            except Exception as exc:
                self.last_error = type(exc).__name__
                try:
                    conn.close()
                except Exception:
                    pass
                with self.lock:
                    if self.conn is conn:
                        self.conn = None
                    self.ready = False
                print(
                    f"Postgres {self.path} schéma : {self.last_error}",
                    flush=True,
                )
                if not forever:
                    return
                time.sleep(delay)
                delay = min(delay * 2, 15.0)
                continue
            print(f"Postgres prêt ({self.path}).", flush=True)
            return

    def _open_postgres(self):
        """Connexion bornée : un DNS ou un TCP bloqué ne fige pas le serveur."""
        if self._dial is not None and self._dial.is_alive():
            raise TimeoutError("connexion en cours")
        url = prepare_database_url(self.database_url)
        box: dict[str, Any] = {}

        def dial() -> None:
            try:
                box["conn"] = psycopg.connect(
                    url, row_factory=dict_row, connect_timeout=15, autocommit=True,
                )
            except Exception as exc:
                box["error"] = exc

        self._dial = threading.Thread(target=dial, name="postgres-dial", daemon=True)
        self._dial.start()
        self._dial.join(20)
        if self._dial.is_alive():
            raise TimeoutError("connexion Postgres trop longue")
        if "error" in box:
            raise box["error"]
        conn = box.get("conn")
        if conn is None:
            raise TimeoutError("connexion Postgres vide")
        return conn

    def close(self) -> None:
        with self.lock:
            self._closed = True
            self.ready = False
            if self.conn is not None:
                self.conn.close()
                self.conn = None

    def _commit(self) -> None:
        # Postgres est en autocommit : pas de transaction oisive qui bloquerait
        # le CREATE TABLE du prochain déploiement.
        if self.kind == "postgres":
            return
        self.conn.commit()

    def _sql(self, sql: str) -> str:
        if self.kind == "postgres":
            sql = sql.replace("?", "%s")
            sql = sql.replace("ON CONFLICT(", "ON CONFLICT (")
        return sql

    def _execute(self, sql: str, params: tuple[Any, ...] = ()):
        return self.conn.execute(self._sql(sql), params)

    def _row(self, row: Any) -> dict | None:
        if row is None:
            return None
        return dict(row)

    def _init_schema(self) -> None:
        print("Vérification du schéma…", flush=True)
        if self.kind == "postgres":
            # L'instance encore en service peut tenir un verrou de lecture.
            # On n'attend pas : si les tables existent, on sert quand même.
            self._execute("SET lock_timeout = '4s'")
        try:
            self._apply_schema()
        except Exception as exc:
            if self.kind != "postgres":
                raise
            print(f"Migration reportée ({type(exc).__name__}).", flush=True)
            self._execute("SET lock_timeout = '0'")
            self._execute("SELECT 1 FROM users LIMIT 1").fetchone()
            print("Tables déjà présentes, service utilisable.", flush=True)
            return
        if self.kind == "postgres":
            self._execute("SET lock_timeout = '0'")

    def _apply_schema(self) -> None:
        schema = """
                CREATE TABLE IF NOT EXISTS users (
                    id TEXT PRIMARY KEY,
                    email TEXT NOT NULL UNIQUE,
                    password_hash TEXT,
                    google_sub TEXT UNIQUE,
                    name TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS sessions (
                    token TEXT PRIMARY KEY,
                    user_id TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    expires_at TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                );
                CREATE TABLE IF NOT EXISTS notes (
                    id TEXT PRIMARY KEY,
                    user_id TEXT NOT NULL,
                    course_id TEXT NOT NULL,
                    title TEXT NOT NULL DEFAULT '',
                    body TEXT NOT NULL DEFAULT '',
                    updated_at TEXT NOT NULL,
                    UNIQUE (user_id, course_id),
                    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                );
                CREATE TABLE IF NOT EXISTS grades (
                    id TEXT PRIMARY KEY,
                    user_id TEXT NOT NULL,
                    quiz_id TEXT NOT NULL,
                    score INTEGER NOT NULL,
                    total INTEGER NOT NULL,
                    pct INTEGER NOT NULL,
                    source TEXT NOT NULL,
                    at TEXT NOT NULL,
                    UNIQUE (user_id, quiz_id, source),
                    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                );
                CREATE TABLE IF NOT EXISTS snapshots (
                    user_id TEXT PRIMARY KEY,
                    progress_json TEXT NOT NULL,
                    cours_json TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                );
                CREATE INDEX IF NOT EXISTS idx_sessions_user ON sessions(user_id);
                CREATE INDEX IF NOT EXISTS idx_notes_user ON notes(user_id);
                CREATE INDEX IF NOT EXISTS idx_grades_user ON grades(user_id);
                """
        with self.lock:
            if self.kind == "sqlite":
                self.conn.executescript(schema)
            else:
                for stmt in schema.split(";"):
                    stmt = stmt.strip()
                    if stmt:
                        self._execute(stmt)
            self._migrate_avatars()
            self._commit()

    def _migrate_avatars(self) -> None:
        if self.kind == "sqlite":
            cols = {r[1] for r in self._execute("PRAGMA table_info(users)")}
            if "avatar_url" not in cols:
                self._execute("ALTER TABLE users ADD COLUMN avatar_url TEXT")
            if "avatar_custom" not in cols:
                self._execute("ALTER TABLE users ADD COLUMN avatar_custom TEXT")
            return
        self._execute("ALTER TABLE users ADD COLUMN IF NOT EXISTS avatar_url TEXT")
        self._execute("ALTER TABLE users ADD COLUMN IF NOT EXISTS avatar_custom TEXT")

    def user_count(self) -> int:
        with self.lock:
            row = self._execute("SELECT COUNT(*) AS n FROM users").fetchone()
            return int(row["n"])

    def create_user(
        self,
        email: str,
        name: str,
        password: str | None = None,
        google_sub: str | None = None,
        avatar_url: str = "",
    ) -> dict:
        uid = uuid.uuid4().hex
        now = iso()
        pw = hash_password(password) if password else None
        with self.lock:
            self._execute(
                "INSERT INTO users (id, email, password_hash, google_sub, name, avatar_url, "
                "avatar_custom, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (uid, email, pw, google_sub, name, avatar_url or None, None, now, now),
            )
            self._commit()
        user = self.get_user(uid)
        assert user is not None
        return user

    def get_user(self, user_id: str) -> dict | None:
        with self.lock:
            row = self._execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        return self._row(row)

    def get_user_by_email(self, email: str) -> dict | None:
        with self.lock:
            row = self._execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        return self._row(row)

    def get_user_by_google(self, sub: str) -> dict | None:
        with self.lock:
            row = self._execute("SELECT * FROM users WHERE google_sub = ?", (sub,)).fetchone()
        return self._row(row)

    def link_google(self, user_id: str, sub: str, name: str | None = None) -> dict:
        now = iso()
        with self.lock:
            if name:
                self._execute(
                    "UPDATE users SET google_sub = ?, name = ?, updated_at = ? WHERE id = ?",
                    (sub, name, now, user_id),
                )
            else:
                self._execute(
                    "UPDATE users SET google_sub = ?, updated_at = ? WHERE id = ?",
                    (sub, now, user_id),
                )
            self._commit()
        user = self.get_user(user_id)
        assert user is not None
        return user

    def set_google_picture(self, user_id: str, url: str) -> dict:
        url = validate_google_picture(url)
        if not url:
            user = self.get_user(user_id)
            assert user is not None
            return user
        now = iso()
        with self.lock:
            self._execute(
                "UPDATE users SET avatar_url = ?, updated_at = ? WHERE id = ?",
                (url, now, user_id),
            )
            self._commit()
        user = self.get_user(user_id)
        assert user is not None
        return user

    def set_custom_avatar(self, user_id: str, image: str | None) -> dict:
        stored = validate_custom_avatar(image or "") if image else ""
        now = iso()
        with self.lock:
            self._execute(
                "UPDATE users SET avatar_custom = ?, updated_at = ? WHERE id = ?",
                (stored or None, now, user_id),
            )
            self._commit()
        user = self.get_user(user_id)
        assert user is not None
        return user

    def create_session(self, user_id: str) -> dict:
        token = secrets.token_urlsafe(32)
        now = utcnow()
        expires = now + timedelta(days=SESSION_DAYS)
        with self.lock:
            self._execute(
                "INSERT INTO sessions (token, user_id, created_at, expires_at) VALUES (?, ?, ?, ?)",
                (token, user_id, iso(now), iso(expires)),
            )
            self._commit()
        return {"token": token, "expiresAt": iso(expires)}

    def delete_session(self, token: str) -> None:
        with self.lock:
            self._execute("DELETE FROM sessions WHERE token = ?", (token,))
            self._commit()

    def user_from_token(self, token: str) -> dict:
        if not token:
            raise AuthError("Session manquante.")
        with self.lock:
            row = self._execute(
                "SELECT u.*, s.expires_at FROM sessions s JOIN users u ON u.id = s.user_id WHERE s.token = ?",
                (token,),
            ).fetchone()
        if not row:
            raise AuthError("Session invalide.")
        expires = parse_iso(row["expires_at"])
        if expires < utcnow():
            self.delete_session(token)
            raise AuthError("Session expirée.")
        return self._row(row)

    def public_user(self, user: dict) -> dict:
        custom = (user.get("avatar_custom") or "").strip()
        google = (user.get("avatar_url") or "").strip()
        return {
            "id": user["id"],
            "email": user["email"],
            "name": user["name"],
            "hasPassword": bool(user.get("password_hash")),
            "google": bool(user.get("google_sub")),
            "createdAt": user["created_at"],
            "avatarUrl": custom or google,
            "avatarCustom": bool(custom),
        }

    def get_snapshot(self, user_id: str) -> dict:
        with self.lock:
            row = self._execute(
                "SELECT progress_json, cours_json, updated_at FROM snapshots WHERE user_id = ?",
                (user_id,),
            ).fetchone()
        if not row:
            return {
                "progress": {"visited": {}, "quizBest": {}},
                "cours": {"watched": {}, "attendance": {}, "quizzes": {}, "notes": {}},
                "updatedAt": None,
            }
        return {
            "progress": json.loads(row["progress_json"]),
            "cours": json.loads(row["cours_json"]),
            "updatedAt": row["updated_at"],
        }

    def put_snapshot(self, user_id: str, progress: dict, cours: dict) -> dict:
        now = iso()
        payload_p = json.dumps(progress, ensure_ascii=False)
        payload_c = json.dumps(cours, ensure_ascii=False)
        with self.lock:
            self._execute(
                "INSERT INTO snapshots (user_id, progress_json, cours_json, updated_at) VALUES (?, ?, ?, ?) "
                "ON CONFLICT(user_id) DO UPDATE SET progress_json = excluded.progress_json, "
                "cours_json = excluded.cours_json, updated_at = excluded.updated_at",
                (user_id, payload_p, payload_c, now),
            )
            self._commit()
        self._ingest_snapshot(user_id, progress, cours)
        return self.get_snapshot(user_id)

    def _ingest_snapshot(self, user_id: str, progress: dict, cours: dict) -> None:
        quiz_best = (progress or {}).get("quizBest") or {}
        for quiz_id, rec in quiz_best.items():
            if not isinstance(rec, dict):
                continue
            try:
                score = int(rec.get("score", 0))
                total = int(rec.get("total", 0))
                pct = int(rec.get("pct", round(100 * score / total) if total else 0))
            except (TypeError, ValueError, ZeroDivisionError):
                continue
            self.upsert_grade(user_id, str(quiz_id)[:80], score, total, pct, "quiz")
        quizzes = (cours or {}).get("quizzes") or {}
        for quiz_id, rec in quizzes.items():
            if not isinstance(rec, dict):
                continue
            try:
                score = int(rec.get("score", 0))
                total = int(rec.get("total", 0))
                pct = int(round(100 * score / total) if total else 0)
            except (TypeError, ValueError, ZeroDivisionError):
                continue
            self.upsert_grade(user_id, str(quiz_id)[:80], score, total, pct, "cours")
        notes = (cours or {}).get("notes") or {}
        for course_id, body in notes.items():
            if body is None:
                continue
            self.upsert_note(user_id, str(course_id)[:80], str(body)[:50_000], title="")

    def list_notes(self, user_id: str) -> list[dict]:
        with self.lock:
            rows = self._execute(
                "SELECT id, course_id, title, body, updated_at FROM notes WHERE user_id = ? ORDER BY updated_at DESC",
                (user_id,),
            ).fetchall()
        return [self._note(r) for r in rows]

    def get_note(self, user_id: str, note_id: str) -> dict | None:
        with self.lock:
            row = self._execute(
                "SELECT id, course_id, title, body, updated_at FROM notes WHERE id = ? AND user_id = ?",
                (note_id, user_id),
            ).fetchone()
        return self._note(row) if row else None

    def upsert_note(self, user_id: str, course_id: str, body: str, title: str = "", note_id: str | None = None) -> dict:
        now = iso()
        course_id = (course_id or "general").strip()[:80] or "general"
        title = (title or "")[:120]
        body = body if isinstance(body, str) else str(body)
        if len(body) > 50_000:
            body = body[:50_000]
        with self.lock:
            existing = self._execute(
                "SELECT id, title FROM notes WHERE user_id = ? AND course_id = ?",
                (user_id, course_id),
            ).fetchone()
            if note_id:
                owned = self._execute(
                    "SELECT id, title FROM notes WHERE id = ? AND user_id = ?",
                    (note_id, user_id),
                ).fetchone()
                if not owned:
                    raise AuthError("Note introuvable.", 404)
                if not title:
                    title = owned["title"] or ""
                self._execute(
                    "UPDATE notes SET course_id = ?, title = ?, body = ?, updated_at = ? WHERE id = ? AND user_id = ?",
                    (course_id, title, body, now, note_id, user_id),
                )
                nid = note_id
            elif existing:
                nid = existing["id"]
                if not title:
                    title = existing["title"] or ""
                self._execute(
                    "UPDATE notes SET title = ?, body = ?, updated_at = ? WHERE id = ?",
                    (title, body, now, nid),
                )
            else:
                nid = uuid.uuid4().hex
                self._execute(
                    "INSERT INTO notes (id, user_id, course_id, title, body, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
                    (nid, user_id, course_id, title, body, now),
                )
            self._commit()
        note = self.get_note(user_id, nid)
        assert note is not None
        return note

    def delete_note(self, user_id: str, note_id: str) -> None:
        with self.lock:
            cur = self._execute(
                "DELETE FROM notes WHERE id = ? AND user_id = ?",
                (note_id, user_id),
            )
            self._commit()
            if cur.rowcount == 0:
                raise AuthError("Note introuvable.", 404)

    def list_grades(self, user_id: str) -> list[dict]:
        with self.lock:
            rows = self._execute(
                "SELECT id, quiz_id, score, total, pct, source, at FROM grades "
                "WHERE user_id = ? ORDER BY at DESC",
                (user_id,),
            ).fetchall()
        return [self._grade(r) for r in rows]

    def upsert_grade(
        self,
        user_id: str,
        quiz_id: str,
        score: int,
        total: int,
        pct: int | None,
        source: str,
    ) -> dict:
        quiz_id = (quiz_id or "").strip()[:80]
        if not quiz_id:
            raise AuthError("Identifiant de quiz manquant.", 400)
        if source not in ("quiz", "cours"):
            source = "quiz"
        try:
            score = int(score)
            total = int(total)
        except (TypeError, ValueError) as exc:
            raise AuthError("Score invalide.", 400) from exc
        if total <= 0 or score < 0 or score > total:
            raise AuthError("Score invalide.", 400)
        pct = int(pct if pct is not None else round(100 * score / total))
        pct = max(0, min(100, pct))
        now = iso()
        with self.lock:
            row = self._execute(
                "SELECT id, pct FROM grades WHERE user_id = ? AND quiz_id = ? AND source = ?",
                (user_id, quiz_id, source),
            ).fetchone()
            if row:
                if pct < int(row["pct"]):
                    return self._grade(
                        self._execute(
                            "SELECT id, quiz_id, score, total, pct, source, at FROM grades WHERE id = ?",
                            (row["id"],),
                        ).fetchone()
                    )
                self._execute(
                    "UPDATE grades SET score = ?, total = ?, pct = ?, at = ? WHERE id = ?",
                    (score, total, pct, now, row["id"]),
                )
                gid = row["id"]
            else:
                gid = uuid.uuid4().hex
                self._execute(
                    "INSERT INTO grades (id, user_id, quiz_id, score, total, pct, source, at) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    (gid, user_id, quiz_id, score, total, pct, source, now),
                )
            self._commit()
            out = self._execute(
                "SELECT id, quiz_id, score, total, pct, source, at FROM grades WHERE id = ?",
                (gid,),
            ).fetchone()
        return self._grade(out)

    @staticmethod
    def _note(row: sqlite3.Row) -> dict:
        return {
            "id": row["id"],
            "courseId": row["course_id"],
            "title": row["title"],
            "body": row["body"],
            "updatedAt": row["updated_at"],
        }

    @staticmethod
    def _grade(row: sqlite3.Row) -> dict:
        return {
            "id": row["id"],
            "quizId": row["quiz_id"],
            "score": row["score"],
            "total": row["total"],
            "pct": row["pct"],
            "source": row["source"],
            "at": row["at"],
        }


def public_error(message: str) -> dict:
    return {"error": message}


class CompteHandler(BaseHTTPRequestHandler):
    store: Store
    google_client_id: str = ""
    static_root: str | None = None
    rate: dict
    rate_lock: threading.Lock

    def log_message(self, fmt: str, *args: Any) -> None:
        sys_stderr = __import__("sys").stderr
        sys_stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def _cors(self) -> None:
        origin = self.headers.get("Origin", "*") or "*"
        self.send_header("Access-Control-Allow-Origin", origin)
        self.send_header("Vary", "Origin")
        self.send_header("Access-Control-Allow-Headers", "Authorization, Content-Type")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Max-Age", "600")

    def _json(self, status: int, payload: dict | list) -> None:
        raw = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self._cors()
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(raw)

    def _read_json(self) -> dict:
        length = int(self.headers.get("Content-Length") or 0)
        if length > MAX_BODY:
            raise AuthError("Requête trop volumineuse.", 413)
        raw = self.rfile.read(length) if length else b"{}"
        if not raw:
            return {}
        try:
            data = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise AuthError("JSON invalide.", 400) from exc
        if not isinstance(data, dict):
            raise AuthError("JSON invalide.", 400)
        return data

    def _bearer(self) -> str:
        header = self.headers.get("Authorization") or ""
        if header.lower().startswith("bearer "):
            return header[7:].strip()
        return ""

    def _auth(self) -> dict:
        return self.store.user_from_token(self._bearer())

    def _limited(self, bucket: str, limit: int = 30, window: int = 300) -> None:
        if os.environ.get("PSYCLOPEDIA_TESTING") == "1":
            return
        ip = self.client_address[0]
        key = f"{bucket}:{ip}"
        now = time.time()
        with self.rate_lock:
            stamps = [t for t in self.rate.get(key, []) if now - t < window]
            if len(stamps) >= limit:
                raise AuthError("Trop de tentatives. Réessayez dans quelques minutes.", 429)
            stamps.append(now)
            self.rate[key] = stamps

    def do_OPTIONS(self) -> None:  # noqa: N802
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self) -> None:  # noqa: N802
        self._dispatch("GET")

    def do_POST(self) -> None:  # noqa: N802
        self._dispatch("POST")

    def do_PUT(self) -> None:  # noqa: N802
        self._dispatch("PUT")

    def do_DELETE(self) -> None:  # noqa: N802
        self._dispatch("DELETE")

    def _path(self) -> str:
        return urllib.parse.urlparse(self.path).path

    def _dispatch(self, method: str) -> None:
        path = self._path()
        try:
            if path.startswith("/api/"):
                self._api(method, path)
                return
            if method == "GET" and self.static_root:
                self._serve_static(path)
                return
            self._json(404, public_error("Introuvable."))
        except AuthError as exc:
            self._json(exc.status, public_error(exc.message))
        except INTEGRITY_ERRORS:
            self._json(409, public_error("Cette adresse est déjà utilisée."))
        except Exception:
            self._json(500, public_error("Erreur interne."))

    def _api(self, method: str, path: str) -> None:
        if path == "/api/health" and method == "GET":
            if not self.store.ready:
                self._json(503, {
                    "ok": False,
                    "db": "starting",
                    "error": self.store.last_error,
                })
                return
            self._json(200, {
                "ok": True,
                "db": self.store.kind,
                "users": self.store.user_count(),
                "google": bool(self.google_client_id),
            })
            return
        if path == "/api/config" and method == "GET":
            self._json(200, {"googleClientId": self.google_client_id or ""})
            return
        if not self.store.ready:
            self._json(503, public_error("Le service démarre, réessayez dans un instant."))
            return
        if path == "/api/auth/register" and method == "POST":
            self._limited("register", 10)
            body = self._read_json()
            email = validate_email(body.get("email") or "")
            password = validate_password(body.get("password") or "")
            name = validate_name(body.get("name") or email.split("@")[0])
            if self.store.get_user_by_email(email):
                raise AuthError("Cette adresse est déjà utilisée.", 409)
            user = self.store.create_user(email, name, password=password)
            session = self.store.create_session(user["id"])
            self._json(201, {"user": self.store.public_user(user), "token": session["token"],
                             "expiresAt": session["expiresAt"]})
            return
        if path == "/api/auth/login" and method == "POST":
            self._limited("login", 20)
            body = self._read_json()
            email = validate_email(body.get("email") or "")
            password = body.get("password") or ""
            user = self.store.get_user_by_email(email)
            if not user or not user.get("password_hash") or not verify_password(password, user["password_hash"]):
                raise AuthError("E-mail ou mot de passe incorrect.")
            session = self.store.create_session(user["id"])
            self._json(200, {"user": self.store.public_user(user), "token": session["token"],
                             "expiresAt": session["expiresAt"]})
            return
        if path == "/api/auth/google" and method == "POST":
            self._limited("google", 20)
            body = self._read_json()
            info = GOOGLE_TOKEN_VERIFIER(body.get("credential") or "", self.google_client_id)
            picture = validate_google_picture(str(info.get("picture") or ""))
            user = self.store.get_user_by_google(info["sub"])
            if not user:
                existing = self.store.get_user_by_email(info["email"])
                if existing:
                    user = self.store.link_google(existing["id"], info["sub"], info["name"])
                else:
                    user = self.store.create_user(
                        info["email"], info["name"], password=None, google_sub=info["sub"],
                        avatar_url=picture,
                    )
            if picture:
                user = self.store.set_google_picture(user["id"], picture)
            session = self.store.create_session(user["id"])
            self._json(200, {"user": self.store.public_user(user), "token": session["token"],
                             "expiresAt": session["expiresAt"]})
            return
        if path == "/api/auth/logout" and method == "POST":
            token = self._bearer()
            if token:
                self.store.delete_session(token)
            self._json(200, {"ok": True})
            return
        if path == "/api/me" and method == "GET":
            user = self._auth()
            self._json(200, {"user": self.store.public_user(user)})
            return
        if path == "/api/me/avatar" and method == "PUT":
            user = self._auth()
            body = self._read_json()
            image = body.get("image")
            if image is None:
                user = self.store.set_custom_avatar(user["id"], "")
            else:
                user = self.store.set_custom_avatar(user["id"], str(image))
            self._json(200, {"user": self.store.public_user(user)})
            return
        if path == "/api/data" and method == "GET":
            user = self._auth()
            snap = self.store.get_snapshot(user["id"])
            self._json(200, snap)
            return
        if path == "/api/data" and method == "PUT":
            user = self._auth()
            body = self._read_json()
            progress = body.get("progress") if isinstance(body.get("progress"), dict) else {}
            cours = body.get("cours") if isinstance(body.get("cours"), dict) else {}
            snap = self.store.put_snapshot(user["id"], progress, cours)
            self._json(200, snap)
            return
        if path == "/api/notes" and method == "GET":
            user = self._auth()
            self._json(200, {"notes": self.store.list_notes(user["id"])})
            return
        if path == "/api/notes" and method == "POST":
            user = self._auth()
            body = self._read_json()
            note = self.store.upsert_note(
                user["id"],
                str(body.get("courseId") or "general"),
                str(body.get("body") or ""),
                title=str(body.get("title") or ""),
            )
            self._json(201, {"note": note})
            return
        m = re.fullmatch(r"/api/notes/([0-9a-f]{32})", path)
        if m and method == "PUT":
            user = self._auth()
            body = self._read_json()
            note = self.store.upsert_note(
                user["id"],
                str(body.get("courseId") or "general"),
                str(body.get("body") or ""),
                title=str(body.get("title") or ""),
                note_id=m.group(1),
            )
            self._json(200, {"note": note})
            return
        if m and method == "DELETE":
            user = self._auth()
            self.store.delete_note(user["id"], m.group(1))
            self._json(200, {"ok": True})
            return
        if path == "/api/grades" and method == "GET":
            user = self._auth()
            self._json(200, {"grades": self.store.list_grades(user["id"])})
            return
        if path == "/api/grades" and method == "POST":
            user = self._auth()
            body = self._read_json()
            grade = self.store.upsert_grade(
                user["id"],
                str(body.get("quizId") or ""),
                body.get("score", 0),
                body.get("total", 0),
                body.get("pct"),
                str(body.get("source") or "quiz"),
            )
            self._json(201, {"grade": grade})
            return
        self._json(404, public_error("Introuvable."))

    def _serve_static(self, path: str) -> None:
        rel = urllib.parse.unquote(path.lstrip("/"))
        if not rel or rel.endswith("/"):
            rel = (rel or "") + "index.html"
        root = os.path.realpath(self.static_root or "")
        target = os.path.realpath(os.path.join(root, rel))
        if target != root and not target.startswith(root + os.sep):
            self._json(403, public_error("Interdit."))
            return
        norm = target.replace("\\", "/")
        if "/serveur-compte/data/" in norm or norm.endswith(".sqlite") or norm.endswith(".sqlite-wal"):
            self._json(403, public_error("Interdit."))
            return
        if os.path.isdir(target):
            target = os.path.join(target, "index.html")
        if not os.path.isfile(target):
            self._json(404, public_error("Introuvable."))
            return
        ext = os.path.splitext(target)[1].lower()
        types = {
            ".html": "text/html; charset=utf-8",
            ".js": "application/javascript; charset=utf-8",
            ".css": "text/css; charset=utf-8",
            ".json": "application/json; charset=utf-8",
            ".svg": "image/svg+xml",
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".webp": "image/webp",
            ".woff2": "font/woff2",
            ".pdf": "application/pdf",
            ".xml": "application/xml",
            ".txt": "text/plain; charset=utf-8",
        }
        ctype = types.get(ext, "application/octet-stream")
        with open(target, "rb") as fh:
            data = fh.read()
        self.send_response(200)
        self._cors()
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def make_server(
    host: str,
    port: int,
    db_path: str,
    google_client_id: str = "",
    static_root: str | None = None,
    database_url: str = "",
    connect_db: bool = True,
) -> tuple[ThreadingHTTPServer, Store]:
    # Le socket est ouvert avant Postgres : un connect lent ne doit pas
    # laisser Render sans port (scan « No open ports »).
    store = Store(db_path, database_url=database_url, connect=connect_db)
    CompteHandler.store = store
    CompteHandler.google_client_id = google_client_id
    CompteHandler.static_root = os.path.abspath(static_root) if static_root else None
    CompteHandler.rate = {}
    CompteHandler.rate_lock = threading.Lock()
    httpd = ThreadingHTTPServer((host, port), CompteHandler)
    return httpd, store


def _env_host() -> str:
    if os.environ.get("PORT"):
        return os.environ.get("PSYCLOPEDIA_COMPTE_HOST", "0.0.0.0")
    return os.environ.get("PSYCLOPEDIA_COMPTE_HOST", "127.0.0.1")


def _env_port() -> int:
    raw = os.environ.get("PORT") or os.environ.get("PSYCLOPEDIA_COMPTE_PORT") or str(DEFAULT_PORT)
    return int(raw)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="API de comptes étudiants Psyclopédia")
    parser.add_argument("--host", default=_env_host())
    parser.add_argument("--port", type=int, default=_env_port())
    parser.add_argument("--db", default=os.environ.get("PSYCLOPEDIA_COMPTE_DB", DEFAULT_DB))
    parser.add_argument("--static", default=os.environ.get("PSYCLOPEDIA_COMPTE_STATIC", ""),
                        help="Racine du site statique (dépôt) pour tout servir sur le même port")
    args = parser.parse_args(argv)
    google_id = os.environ.get("PSYCLOPEDIA_GOOGLE_CLIENT_ID", "").strip() or PUBLIC_GOOGLE_CLIENT_ID
    static_root = args.static or None
    database_url = os.environ.get("DATABASE_URL", "").strip()
    print(f"Démarrage Psyclopédia comptes sur {args.host}:{args.port}", flush=True)
    # Postgres est branché après listen() : Render exige un port ouvert
    # même si la base met quelques secondes à répondre.
    httpd, store = make_server(
        args.host, args.port, args.db, google_id, static_root, database_url,
        connect_db=not bool(database_url),
    )
    print(f"Psyclopédia comptes — {store.kind} {store.path}", flush=True)
    print(f"Écoute http://{args.host}:{args.port}/api/health", flush=True)
    print(f"Google Sign-In : client {google_id[:20]}…", flush=True)
    if static_root:
        print(f"Fichiers statiques : {os.path.abspath(static_root)}", flush=True)
    if database_url and not store.ready:
        threading.Thread(
            target=store.connect_with_retry,
            kwargs={"forever": True},
            name="postgres-connect",
            daemon=True,
        ).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêt.")
    finally:
        httpd.server_close()
        store.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
