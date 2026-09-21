#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests de l'API de comptes : auth, isolation, notes, notes de quiz, instantanés."""

from __future__ import annotations

import json
import os
import sys
import tempfile
import threading
import time
import unittest
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

os.environ["PSYCLOPEDIA_TESTING"] = "1"

import compte_server  # noqa: E402


def _start(db_path: str, google_id: str = "test-google-client"):
    httpd, store = compte_server.make_server("127.0.0.1", 0, db_path, google_id, static_root=None)
    port = httpd.server_address[1]
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    deadline = time.time() + 3
    while time.time() < deadline:
        try:
            urllib.request.urlopen(f"http://127.0.0.1:{port}/api/health", timeout=0.3)
            break
        except OSError:
            time.sleep(0.05)
    return httpd, store, port


class ApiClient:
    def __init__(self, port: int):
        self.base = f"http://127.0.0.1:{port}"
        self.token = ""

    def call(self, method: str, path: str, body=None, token=None):
        data = None if body is None else json.dumps(body).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        tok = self.token if token is None else token
        if tok:
            headers["Authorization"] = "Bearer " + tok
        req = urllib.request.Request(self.base + path, data=data, method=method, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=5) as resp:
                raw = resp.read().decode("utf-8")
                payload = json.loads(raw) if raw else {}
                return resp.status, payload
        except urllib.error.HTTPError as exc:
            raw = exc.read().decode("utf-8")
            payload = json.loads(raw) if raw else {"error": str(exc)}
            return exc.code, payload


class CompteApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.db = str(Path(cls.tmp.name) / "test.sqlite")
        cls.httpd, cls.store, cls.port = _start(cls.db)
        cls.saved_verifier = compte_server.GOOGLE_TOKEN_VERIFIER

        def fake_google(token: str, aud: str):
            if token == "ok-google":
                return {"sub": "gid-ada", "email": "ada.google@example.com", "name": "Ada Google"}
            if token == "ok-link":
                return {"sub": "gid-link", "email": "deja@example.com", "name": "Déjà Inscrite"}
            raise compte_server.AuthError("Jeton Google invalide.")

        compte_server.GOOGLE_TOKEN_VERIFIER = fake_google

    @classmethod
    def tearDownClass(cls):
        compte_server.GOOGLE_TOKEN_VERIFIER = cls.saved_verifier
        cls.httpd.shutdown()
        cls.httpd.server_close()
        cls.store.close()
        cls.tmp.cleanup()

    def client(self) -> ApiClient:
        return ApiClient(self.port)

    def test_health(self):
        c = self.client()
        status, body = c.call("GET", "/api/health")
        self.assertEqual(status, 200)
        self.assertTrue(body["ok"])
        self.assertEqual(body["db"], "sqlite")

    def test_register_login_me_logout(self):
        c = self.client()
        status, body = c.call("POST", "/api/auth/register", {
            "email": "etudiant@example.com",
            "password": "motdepasse1",
            "name": "Camille",
        })
        self.assertEqual(status, 201, body)
        self.assertEqual(body["user"]["email"], "etudiant@example.com")
        self.assertEqual(body["user"]["name"], "Camille")
        self.assertTrue(body["token"])
        c.token = body["token"]
        status, me = c.call("GET", "/api/me")
        self.assertEqual(status, 200)
        self.assertEqual(me["user"]["name"], "Camille")
        status, _ = c.call("POST", "/api/auth/logout")
        self.assertEqual(status, 200)
        status, err = c.call("GET", "/api/me")
        self.assertEqual(status, 401)
        self.assertIn("error", err)

    def test_duplicate_email(self):
        c = self.client()
        payload = {"email": "double@example.com", "password": "motdepasse1", "name": "A"}
        self.assertEqual(c.call("POST", "/api/auth/register", payload)[0], 201)
        status, body = c.call("POST", "/api/auth/register", payload)
        self.assertEqual(status, 409)
        self.assertIn("déjà", body["error"].lower())

    def test_login_wrong_password(self):
        c = self.client()
        c.call("POST", "/api/auth/register", {
            "email": "secret@example.com", "password": "motdepasse1", "name": "S",
        })
        status, body = c.call("POST", "/api/auth/login", {
            "email": "secret@example.com", "password": "mauvais-mot",
        })
        self.assertEqual(status, 401)
        self.assertIn("error", body)

    def test_weak_password_and_bad_email(self):
        c = self.client()
        status, body = c.call("POST", "/api/auth/register", {
            "email": "pas-un-mail", "password": "motdepasse1", "name": "X",
        })
        self.assertEqual(status, 400)
        status, body = c.call("POST", "/api/auth/register", {
            "email": "ok@example.com", "password": "court", "name": "X",
        })
        self.assertEqual(status, 400)
        self.assertIn("8", body["error"])

    def test_unauthenticated(self):
        c = self.client()
        self.assertEqual(c.call("GET", "/api/data")[0], 401)
        self.assertEqual(c.call("GET", "/api/notes")[0], 401)
        self.assertEqual(c.call("GET", "/api/grades")[0], 401)

    def test_notes_crud(self):
        c = self.client()
        _, body = c.call("POST", "/api/auth/register", {
            "email": "notes@example.com", "password": "motdepasse1", "name": "N",
        })
        c.token = body["token"]
        status, created = c.call("POST", "/api/notes", {
            "courseId": "cm-01", "title": "Cours 1", "body": "James, 1890.",
        })
        self.assertEqual(status, 201, created)
        nid = created["note"]["id"]
        status, listed = c.call("GET", "/api/notes")
        self.assertEqual(status, 200)
        self.assertEqual(len(listed["notes"]), 1)
        status, updated = c.call("PUT", f"/api/notes/{nid}", {
            "courseId": "cm-01", "title": "Cours 1", "body": "James, 1890, chapitre 1.",
        })
        self.assertEqual(status, 200)
        self.assertIn("chapitre", updated["note"]["body"])
        status, _ = c.call("DELETE", f"/api/notes/{nid}")
        self.assertEqual(status, 200)
        self.assertEqual(c.call("GET", "/api/notes")[1]["notes"], [])

    def test_grades_keep_best(self):
        c = self.client()
        _, body = c.call("POST", "/api/auth/register", {
            "email": "notes-quiz@example.com", "password": "motdepasse1", "name": "Q",
        })
        c.token = body["token"]
        status, g1 = c.call("POST", "/api/grades", {
            "quizId": "03-cognitive", "score": 8, "total": 10, "source": "quiz",
        })
        self.assertEqual(status, 201)
        self.assertEqual(g1["grade"]["pct"], 80)
        status, g2 = c.call("POST", "/api/grades", {
            "quizId": "03-cognitive", "score": 5, "total": 10, "source": "quiz",
        })
        self.assertEqual(status, 201)
        self.assertEqual(g2["grade"]["pct"], 80)
        status, g3 = c.call("POST", "/api/grades", {
            "quizId": "03-cognitive", "score": 10, "total": 10, "source": "quiz",
        })
        self.assertEqual(status, 201)
        self.assertEqual(g3["grade"]["pct"], 100)
        grades = c.call("GET", "/api/grades")[1]["grades"]
        self.assertEqual(len(grades), 1)
        self.assertEqual(grades[0]["pct"], 100)

    def test_snapshot_and_ingest(self):
        c = self.client()
        _, body = c.call("POST", "/api/auth/register", {
            "email": "snap@example.com", "password": "motdepasse1", "name": "Snap",
        })
        c.token = body["token"]
        payload = {
            "progress": {
                "visited": {"03-cognitive": True},
                "quizBest": {"03-cognitive": {"score": 9, "total": 10, "pct": 90}},
            },
            "cours": {
                "watched": {"s01": {"seconds": 40, "completed": True}},
                "attendance": {"s01": True},
                "quizzes": {"s01": {"score": 4, "total": 5}},
                "notes": {"s01": "Stroop : l'encre compte plus que le mot."},
            },
        }
        status, snap = c.call("PUT", "/api/data", payload)
        self.assertEqual(status, 200, snap)
        status, got = c.call("GET", "/api/data")
        self.assertEqual(status, 200)
        self.assertTrue(got["progress"]["visited"]["03-cognitive"])
        self.assertEqual(got["cours"]["notes"]["s01"][:6], "Stroop")
        grades = c.call("GET", "/api/grades")[1]["grades"]
        sources = {g["source"] for g in grades}
        self.assertEqual(sources, {"quiz", "cours"})
        notes = c.call("GET", "/api/notes")[1]["notes"]
        self.assertEqual(len(notes), 1)
        self.assertIn("Stroop", notes[0]["body"])
        self.assertEqual(notes[0]["courseId"], "s01")

    def test_snapshot_keeps_note_title(self):
        c = self.client()
        _, body = c.call("POST", "/api/auth/register", {
            "email": "titre@example.com", "password": "motdepasse1", "name": "T",
        })
        c.token = body["token"]
        c.call("POST", "/api/notes", {
            "courseId": "s01", "title": "Courant de conscience", "body": "James 1890",
        })
        c.call("PUT", "/api/data", {
            "progress": {"visited": {}, "quizBest": {}},
            "cours": {"watched": {}, "attendance": {}, "quizzes": {},
                      "notes": {"s01": "James 1890, chapitre 9."}},
        })
        notes = c.call("GET", "/api/notes")[1]["notes"]
        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0]["title"], "Courant de conscience")
        self.assertIn("chapitre", notes[0]["body"])

    def test_user_isolation(self):
        a = self.client()
        b = self.client()
        _, ua = a.call("POST", "/api/auth/register", {
            "email": "alice@example.com", "password": "motdepasse1", "name": "Alice",
        })
        _, ub = b.call("POST", "/api/auth/register", {
            "email": "bob@example.com", "password": "motdepasse1", "name": "Bob",
        })
        a.token = ua["token"]
        b.token = ub["token"]
        a.call("POST", "/api/notes", {"courseId": "secret", "body": "journal d'Alice"})
        a.call("POST", "/api/grades", {"quizId": "final", "score": 20, "total": 20, "source": "quiz"})
        notes_b = b.call("GET", "/api/notes")[1]["notes"]
        grades_b = b.call("GET", "/api/grades")[1]["grades"]
        self.assertEqual(notes_b, [])
        self.assertEqual(grades_b, [])
        nid = a.call("GET", "/api/notes")[1]["notes"][0]["id"]
        status, _ = b.call("DELETE", f"/api/notes/{nid}")
        self.assertEqual(status, 404)
        self.assertEqual(len(a.call("GET", "/api/notes")[1]["notes"]), 1)

    def test_google_login_and_link(self):
        c = self.client()
        status, body = c.call("POST", "/api/auth/google", {"credential": "ok-google"})
        self.assertEqual(status, 200, body)
        self.assertEqual(body["user"]["email"], "ada.google@example.com")
        self.assertTrue(body["user"]["google"])
        self.assertFalse(body["user"]["hasPassword"])
        c.call("POST", "/api/auth/register", {
            "email": "deja@example.com", "password": "motdepasse1", "name": "Déjà",
        })
        status, linked = c.call("POST", "/api/auth/google", {"credential": "ok-link"})
        self.assertEqual(status, 200, linked)
        self.assertEqual(linked["user"]["email"], "deja@example.com")
        self.assertTrue(linked["user"]["google"])
        self.assertTrue(linked["user"]["hasPassword"])
        status, bad = c.call("POST", "/api/auth/google", {"credential": "junk"})
        self.assertEqual(status, 401)

    def test_login_sql_payload_rejected(self):
        c = self.client()
        c.call("POST", "/api/auth/register", {
            "email": "safe@example.com", "password": "motdepasse1", "name": "S",
        })
        status, body = c.call("POST", "/api/auth/login", {
            "email": "' OR 1=1 --@x.com", "password": "x",
        })
        self.assertIn(status, (400, 401))
        self.assertIn("error", body)

    def test_sql_payload_not_injected(self):
        c = self.client()
        _, body = c.call("POST", "/api/auth/register", {
            "email": "inject@example.com", "password": "motdepasse1", "name": "I",
        })
        c.token = body["token"]
        evil = "'; DROP TABLE notes; --"
        status, created = c.call("POST", "/api/notes", {"courseId": evil, "body": evil})
        self.assertEqual(status, 201, created)
        status, listed = c.call("GET", "/api/notes")
        self.assertEqual(status, 200)
        self.assertEqual(listed["notes"][0]["courseId"], evil[:80])
        health = c.call("GET", "/api/health")[1]
        self.assertTrue(health["ok"])


class PasswordHashTests(unittest.TestCase):
    def test_roundtrip(self):
        stored = compte_server.hash_password("sésame-12")
        self.assertTrue(stored.startswith("pbkdf2$sha256$"))
        self.assertTrue(compte_server.verify_password("sésame-12", stored))
        self.assertFalse(compte_server.verify_password("autre", stored))

    def test_distinct_salts(self):
        a = compte_server.hash_password("motdepasse1")
        b = compte_server.hash_password("motdepasse1")
        self.assertNotEqual(a, b)


class PaasBindTests(unittest.TestCase):
    def test_port_env_paas(self):
        old = os.environ.get("PORT")
        os.environ["PORT"] = "9999"
        try:
            self.assertEqual(compte_server._env_port(), 9999)
            self.assertEqual(compte_server._env_host(), "0.0.0.0")
        finally:
            if old is None:
                os.environ.pop("PORT", None)
            else:
                os.environ["PORT"] = old


class FrontendConfigTests(unittest.TestCase):
    def test_client_id_public_dans_le_js(self):
        cfg = (HERE.parent / "assets-ebook/js/compte-config.js").read_text(encoding="utf-8")
        self.assertIn(compte_server.PUBLIC_GOOGLE_CLIENT_ID, cfg)
        self.assertNotIn("GOCSPX-", cfg)
        self.assertNotIn("client_secret", cfg)

    def test_secret_json_pas_dans_le_depot(self):
        repo = HERE.parent
        leaks = list(repo.rglob("client_secret*.json"))
        leaks = [p for p in leaks if ".git" not in p.parts]
        self.assertEqual(leaks, [])


class GoogleLiveTests(unittest.TestCase):
    """Vérifie tokeninfo Google réel + /api/config, sans mock."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.db = str(Path(cls.tmp.name) / "google.sqlite")
        root = str(HERE.parent)
        httpd, store = compte_server.make_server(
            "127.0.0.1", 0, cls.db,
            google_client_id=compte_server.PUBLIC_GOOGLE_CLIENT_ID,
            static_root=root,
        )
        cls.httpd = httpd
        cls.store = store
        cls.port = httpd.server_address[1]
        thread = threading.Thread(target=httpd.serve_forever, daemon=True)
        thread.start()
        deadline = time.time() + 3
        while time.time() < deadline:
            try:
                urllib.request.urlopen(f"http://127.0.0.1:{cls.port}/api/health", timeout=0.3)
                break
            except OSError:
                time.sleep(0.05)

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()
        cls.store.close()
        cls.tmp.cleanup()

    def client(self) -> ApiClient:
        return ApiClient(self.port)

    def test_config_expose_l_id_public(self):
        status, body = self.client().call("GET", "/api/config")
        self.assertEqual(status, 200)
        self.assertEqual(body["googleClientId"], compte_server.PUBLIC_GOOGLE_CLIENT_ID)
        health = self.client().call("GET", "/api/health")[1]
        self.assertTrue(health["google"])

    def test_jeton_google_invalide_rejete_par_tokeninfo(self):
        status, body = self.client().call("POST", "/api/auth/google", {"credential": "pas.un.jwt"})
        self.assertEqual(status, 401)
        self.assertIn("error", body)

    def test_page_compte_et_script_config(self):
        html = urllib.request.urlopen(
            f"http://127.0.0.1:{self.port}/livres-psychologie/07-ebook-final/compte.html",
            timeout=5,
        ).read().decode("utf-8")
        self.assertIn('id="google-btn"', html)
        self.assertIn("compte-config.js", html)
        js = urllib.request.urlopen(
            f"http://127.0.0.1:{self.port}/assets-ebook/js/compte-config.js",
            timeout=5,
        ).read().decode("utf-8")
        self.assertIn(compte_server.PUBLIC_GOOGLE_CLIENT_ID, js)

    def test_parcours_complet_email_notes_notes_de_quiz(self):
        c = self.client()
        status, body = c.call("POST", "/api/auth/register", {
            "email": "integration@univ.fr",
            "password": "psychology1",
            "name": "Lina Martin",
        })
        self.assertEqual(status, 201, body)
        c.token = body["token"]
        self.assertEqual(c.call("POST", "/api/notes", {
            "courseId": "s01",
            "title": "Courant de conscience",
            "body": "James 1890 : le courant n'est pas un train de wagons.",
        })[0], 201)
        self.assertEqual(c.call("POST", "/api/grades", {
            "quizId": "03-cognitive", "score": 18, "total": 20, "source": "quiz",
        })[0], 201)
        self.assertEqual(c.call("PUT", "/api/data", {
            "progress": {
                "visited": {"03-cognitive": True},
                "quizBest": {"03-cognitive": {"score": 18, "total": 20, "pct": 90}},
            },
            "cours": {
                "watched": {"s01": {"seconds": 50, "completed": True}},
                "attendance": {"s01": True},
                "quizzes": {},
                "notes": {"s01": "James 1890 : le courant n'est pas un train de wagons."},
            },
        })[0], 200)
        login = c.call("POST", "/api/auth/login", {
            "email": "integration@univ.fr", "password": "psychology1",
        })
        self.assertEqual(login[0], 200)
        c.token = login[1]["token"]
        notes = c.call("GET", "/api/notes")[1]["notes"]
        self.assertEqual(notes[0]["title"], "Courant de conscience")
        grades = c.call("GET", "/api/grades")[1]["grades"]
        self.assertTrue(any(g["quizId"] == "03-cognitive" and g["pct"] == 90 for g in grades))

    def test_cors_origine_pages(self):
        req = urllib.request.Request(
            f"http://127.0.0.1:{self.port}/api/health",
            headers={"Origin": "https://errornoname.github.io"},
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            self.assertEqual(resp.headers.get("Access-Control-Allow-Origin"), "https://errornoname.github.io")


if __name__ == "__main__":
    unittest.main()

    def test_roundtrip(self):
        stored = compte_server.hash_password("sésame-12")
        self.assertTrue(stored.startswith("pbkdf2$sha256$"))
        self.assertTrue(compte_server.verify_password("sésame-12", stored))
        self.assertFalse(compte_server.verify_password("autre", stored))

    def test_distinct_salts(self):
        a = compte_server.hash_password("motdepasse1")
        b = compte_server.hash_password("motdepasse1")
        self.assertNotEqual(a, b)


if __name__ == "__main__":
    unittest.main()
