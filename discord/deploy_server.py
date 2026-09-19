#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Déploie l'architecture Psyclopédia sur le serveur Discord.

Usage :
    DISCORD_BOT_TOKEN=… python3 deploy_server.py
    python3 deploy_server.py --dry-run
    python3 deploy_server.py --repost

Le jeton se lit dans DISCORD_BOT_TOKEN, discord/.env (non versionné)
ou /tmp/.psyc_discord_token — jamais dans le dépôt.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from blueprint import (
    CATEGORIES,
    COLOR_VERT,
    GUILD_ID_DEFAULT,
    GUILD_PATCH,
    LEGACY_CHANNEL_NAMES,
    LINKS,
    LOCK_SEND,
    P_CONNECT,
    P_HISTORY,
    P_SEND,
    P_SPEAK,
    P_VIEW,
    ROLES,
    SLASH_COMMANDS,
    T_CATEGORY,
    T_FORUM,
    T_NEWS,
    T_TEXT,
    T_VOICE,
    iter_channels,
)
from embeds import EMBEDS, mentionize, validate_embeds

API = "https://discord.com/api/v10"
STATE_PATH = HERE / "deploy_state.json"
TOKEN_CANDIDATES = [
    Path("/tmp/.psyc_discord_token"),
    HERE / ".env",
]


class DiscordError(RuntimeError):
    def __init__(self, status, body, path):
        super().__init__(f"HTTP {status} {path}: {body}")
        self.status = status
        self.body = body
        self.path = path


class DiscordAPI:
    def __init__(self, token):
        self.token = token.strip()
        self._reset_after = 0.0

    def _headers(self, json_body=True):
        headers = {
            "Authorization": f"Bot {self.token}",
            "User-Agent": "PsyclopediaDeploy (https://errornoname.github.io/P-S-C, 1.0)",
        }
        if json_body:
            headers["Content-Type"] = "application/json"
        return headers

    def request(self, method, path, payload=None, extra=None):
        url = API + path
        data = None if payload is None else json.dumps(payload).encode("utf-8")
        headers = self._headers(json_body=payload is not None)
        if extra:
            headers.update(extra)

        for attempt in range(8):
            wait = self._reset_after - time.time()
            if wait > 0:
                time.sleep(wait)
            req = urllib.request.Request(url, data=data, headers=headers, method=method)
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    raw = resp.read()
                    remaining = resp.headers.get("X-RateLimit-Remaining")
                    reset_after = resp.headers.get("X-RateLimit-Reset-After")
                    if remaining == "0" and reset_after:
                        self._reset_after = time.time() + float(reset_after) + 0.15
                    if not raw:
                        return {}
                    return json.loads(raw.decode("utf-8"))
            except urllib.error.HTTPError as exc:
                raw = exc.read().decode("utf-8", errors="replace")
                if exc.code == 429:
                    try:
                        retry = float(json.loads(raw).get("retry_after", 1))
                    except json.JSONDecodeError:
                        retry = 1.5
                    time.sleep(retry + 0.25)
                    continue
                if exc.code >= 500:
                    time.sleep(1.2 * (attempt + 1))
                    continue
                raise DiscordError(exc.code, raw, path) from exc
        raise DiscordError(429, "rate-limit persistante", path)

    def get(self, path):
        return self.request("GET", path)

    def post(self, path, payload):
        return self.request("POST", path, payload)

    def patch(self, path, payload):
        return self.request("PATCH", path, payload)

    def put(self, path, payload):
        return self.request("PUT", path, payload)

    def delete(self, path):
        return self.request("DELETE", path)


def load_token():
    env = os.environ.get("DISCORD_BOT_TOKEN", "").strip()
    if env:
        return env
    for path in TOKEN_CANDIDATES:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if path.name == ".env":
            for line in text.splitlines():
                line = line.strip()
                if line.startswith("DISCORD_BOT_TOKEN="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
        else:
            value = text.strip()
            if value:
                return value
    raise SystemExit(
        "Jeton introuvable. Exportez DISCORD_BOT_TOKEN ou placez-le dans "
        "/tmp/.psyc_discord_token (hors dépôt)."
    )


def load_guild_id():
    env = os.environ.get("DISCORD_GUILD_ID", "").strip()
    if env:
        return env
    env_file = HERE / ".env"
    if env_file.is_file():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            if line.startswith("DISCORD_GUILD_ID="):
                return line.split("=", 1)[1].strip()
    return GUILD_ID_DEFAULT


def overwrite_for(role_id, allow=0, deny=0):
    return {"id": role_id, "type": 0, "allow": str(allow), "deny": str(deny)}


def channel_payload(spec, parent_id, everyone_id, role_ids, community_on, staff_cat=False):
    kind = spec["type"]
    if kind == T_NEWS and not community_on:
        kind = T_TEXT
    if kind == T_FORUM and not community_on:
        kind = T_TEXT

    payload = {
        "name": spec["name"],
        "type": kind,
        "parent_id": parent_id,
    }
    if kind != T_VOICE and spec.get("topic"):
        payload["topic"] = spec["topic"][:1024]
    if spec.get("slowmode") and kind in (T_TEXT, T_NEWS):
        payload["rate_limit_per_user"] = int(spec["slowmode"])

    if kind == T_FORUM:
        payload["available_tags"] = spec.get("tags") or []
        if spec.get("default_reaction"):
            payload["default_reaction_emoji"] = {"emoji_name": spec["default_reaction"]}
        payload["default_forum_layout"] = 1
        payload["default_sort_order"] = 0

    overwrites = []
    staff_ids = [role_ids[k] for k in ("equipe", "moderation") if k in role_ids]
    locked = spec.get("locked")
    staff_only = spec.get("staff_only") or staff_cat

    if staff_only:
        overwrites.append(overwrite_for(everyone_id, deny=P_VIEW))
        for sid in staff_ids:
            overwrites.append(
                overwrite_for(sid, allow=P_VIEW | P_SEND | P_HISTORY | P_CONNECT | P_SPEAK)
            )
    elif locked:
        overwrites.append(overwrite_for(everyone_id, deny=LOCK_SEND))
        for sid in staff_ids:
            overwrites.append(overwrite_for(sid, allow=LOCK_SEND | P_VIEW | P_HISTORY))

    if overwrites:
        payload["permission_overwrites"] = overwrites
    return payload


def _norm_name(name):
    return (name or "").casefold().replace(" ", "-")


def find_by_name(items, name):
    name_l = _norm_name(name)
    for item in items:
        if _norm_name(item.get("name")) == name_l:
            return item
    return None


def ensure_role(api, guild_id, spec, existing):
    found = find_by_name(existing, spec["name"])
    body = {
        "name": spec["name"],
        "color": spec["color"],
        "hoist": spec["hoist"],
        "mentionable": spec["mentionable"],
        "permissions": spec["permissions"],
    }
    if found:
        if any(found.get(k) != body[k] for k in ("color", "hoist", "mentionable")):
            try:
                api.patch(f"/guilds/{guild_id}/roles/{found['id']}", body)
            except DiscordError as exc:
                print(f"  ! rôle {spec['name']} : {exc.status}")
        return found["id"]
    created = api.post(f"/guilds/{guild_id}/roles", body)
    print(f"  + rôle {spec['name']}")
    time.sleep(0.6)
    return created["id"]


def ensure_channel(api, guild_id, payload, existing):
    found = find_by_name(existing, payload["name"])
    wanted = payload.get("type")
    if found and wanted is not None and found.get("type") != wanted and wanted != T_CATEGORY:
        try:
            api.delete(f"/channels/{found['id']}")
            print(f"  − {payload['name']} (changement de type {found.get('type')}→{wanted})")
            time.sleep(0.7)
            found = None
        except DiscordError as exc:
            print(f"  ! recréation {payload['name']} : {exc.status}")
    if found:
        patch = {
            "parent_id": payload.get("parent_id"),
            "topic": payload.get("topic", ""),
        }
        if "permission_overwrites" in payload:
            patch["permission_overwrites"] = payload["permission_overwrites"]
        if payload.get("rate_limit_per_user"):
            patch["rate_limit_per_user"] = payload["rate_limit_per_user"]
        try:
            api.patch(f"/channels/{found['id']}", patch)
        except DiscordError as exc:
            print(f"  ! maj {payload['name']} : {exc.status}")
        return found
    created = api.post(f"/guilds/{guild_id}/channels", payload)
    print(f"  + {payload['name']}")
    time.sleep(0.85)
    return created


def enable_community(api, guild_id, rules_id, updates_id):
    body = {
        **GUILD_PATCH,
        "features": ["COMMUNITY"],
        "rules_channel_id": rules_id,
        "public_updates_channel_id": updates_id,
    }
    return api.patch(f"/guilds/{guild_id}", body)


def post_embeds(api, channel_id, channel_key, ids, forum_fallback, repost):
    keys = []
    for _, spec in iter_channels():
        if spec["key"] == channel_key:
            keys = spec.get("embeds") or []
            kind = spec["type"]
            break
    if not keys:
        return []

    if not repost:
        try:
            pinned = api.get(f"/channels/{channel_id}/pins")
            if pinned:
                return [m["id"] for m in pinned]
        except DiscordError:
            pass

    posted = []
    for key in keys:
        for embed in EMBEDS[key]:
            ready = mentionize(embed, ids)
            if forum_fallback:
                content = None
                payload = {
                    "content": content,
                    "embeds": [ready],
                    "allowed_mentions": {"parse": []},
                }
                try:
                    msg = api.post(f"/channels/{channel_id}/messages", payload)
                except DiscordError as exc:
                    print(f"  ! embed {key} : {exc.status}")
                    continue
            else:
                try:
                    msg = api.post(
                        f"/channels/{channel_id}/messages",
                        {"embeds": [ready], "allowed_mentions": {"parse": []}},
                    )
                except DiscordError as exc:
                    print(f"  ! embed {key} : {exc.status} {exc.body[:180]}")
                    continue
            posted.append(msg["id"])
            try:
                api.put(f"/channels/{channel_id}/pins/{msg['id']}", None)
            except DiscordError:
                pass
            time.sleep(0.55)
    return posted


def post_forum_guidelines_as_message(api, channel, ids, community_on):
    """Si le forum a été rétrogradé en salon texte, poster le guide en message."""
    if community_on and channel.get("type") == T_FORUM:
        return
    key = None
    for _, spec in iter_channels():
        if spec["name"] == channel.get("name"):
            key = spec["key"]
            break
    if not key:
        return
    post_embeds(api, channel["id"], key, ids, True, False)


def register_commands(api, app_id, guild_id):
    api.put(
        f"/applications/{app_id}/guilds/{guild_id}/commands",
        SLASH_COMMANDS,
    )


def delete_legacy(api, channels, keep_ids):
    removed = []
    for channel in channels:
        name = _norm_name(channel.get("name"))
        if channel["id"] in keep_ids:
            continue
        if name not in {_norm_name(n) for n in LEGACY_CHANNEL_NAMES}:
            continue
        try:
            api.delete(f"/channels/{channel['id']}")
            print(f"  − {channel['name']}")
            removed.append(channel["id"])
            time.sleep(0.7)
        except DiscordError as exc:
            print(f"  ! suppression {channel['name']} : {exc.status}")
    return removed


def write_state(state):
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def dry_run():
    print("=== Structure Psyclopédia (dry-run) ===\n")
    errors = validate_embeds()
    if errors:
        print("ERREURS EMBEDS :")
        for err in errors:
            print(" ", err)
        return 1
    for category in CATEGORIES:
        print(category["name"])
        for channel in category["channels"]:
            kind = {0: "texte", 2: "vocal", 5: "annonces", 15: "forum"}[channel["type"]]
            flags = []
            if channel.get("locked"):
                flags.append("lecture seule")
            if channel.get("staff_only") or category.get("staff_only"):
                flags.append("équipe")
            if channel.get("rules"):
                flags.append("rules")
            if channel.get("public_updates"):
                flags.append("public updates")
            extra = f" ({', '.join(flags)})" if flags else ""
            tags = channel.get("tags") or []
            tag_s = ""
            if tags:
                tag_s = "  tags: " + ", ".join(f"{t['emoji_name']}{t['name']}" for t in tags)
            print(f"  [{kind:8}] {channel['name']}{extra}{tag_s}")
        print()
    print(f"{sum(1 for _ in iter_channels())} salons · {len(CATEGORIES)} catégories · {len(ROLES)} rôles")
    print("Liens site :", LINKS["accueil"], LINKS["cours"], LINKS["aide"])
    return 0


def deploy(repost=False):
    errors = validate_embeds()
    if errors:
        print("Embeds invalides :")
        for err in errors:
            print(" ", err)
        return 1

    token = load_token()
    guild_id = load_guild_id()
    api = DiscordAPI(token)

    me = api.get("/users/@me")
    app_id = me["id"]
    print(f"Bot {me.get('username')} ({app_id}) → guild {guild_id}")

    guild = api.get(f"/guilds/{guild_id}")
    community_on = "COMMUNITY" in (guild.get("features") or [])
    print(f"Serveur actuel : {guild.get('name')} · community={community_on}")

    existing_roles = api.get(f"/guilds/{guild_id}/roles")
    role_ids = {}
    for spec in ROLES:
        role_ids[spec["key"]] = ensure_role(api, guild_id, spec, existing_roles)
        existing_roles = api.get(f"/guilds/{guild_id}/roles")

    everyone_id = guild_id
    channels = api.get(f"/guilds/{guild_id}/channels")
    ids = {}
    created_channels = []

    # 1) Catégorie accueil + salons rules / public updates pour activer Community
    accueil = next(c for c in CATEGORIES if c["key"] == "accueil")
    accueil_ch = ensure_channel(
        api,
        guild_id,
        {"name": accueil["name"], "type": T_CATEGORY},
        channels,
    )
    ids["cat_accueil"] = accueil_ch["id"]
    channels = api.get(f"/guilds/{guild_id}/channels")

    bootstrap_keys = ("regles", "journal")
    for spec in accueil["channels"]:
        if spec["key"] not in bootstrap_keys:
            continue
        payload = channel_payload(spec, accueil_ch["id"], everyone_id, role_ids, False)
        # Community a besoin de salons texte pour rules/updates
        payload["type"] = T_TEXT
        ch = ensure_channel(api, guild_id, payload, channels)
        ids[spec["key"]] = ch["id"]
        created_channels.append(ch)
        channels = api.get(f"/guilds/{guild_id}/channels")

    if not community_on:
        print("Activation de la fonctionnalité Community…")
        try:
            guild = enable_community(api, guild_id, ids["regles"], ids["journal"])
            community_on = "COMMUNITY" in (guild.get("features") or [])
            print(f"  community={community_on}")
        except DiscordError as exc:
            print(f"  ! Community refusée ({exc.status}). Forums/annonces → salons texte.")
            community_on = False
        time.sleep(1.0)

    # 2) Toutes les catégories et tous les salons
    for position, category in enumerate(CATEGORIES):
        if category["key"] == "accueil":
            cat = accueil_ch
        else:
            cat = ensure_channel(
                api,
                guild_id,
                {
                    "name": category["name"],
                    "type": T_CATEGORY,
                    "permission_overwrites": (
                        [
                            overwrite_for(everyone_id, deny=P_VIEW),
                            overwrite_for(role_ids["equipe"], allow=P_VIEW | P_SEND | P_HISTORY),
                            overwrite_for(role_ids["moderation"], allow=P_VIEW | P_SEND | P_HISTORY),
                        ]
                        if category.get("staff_only")
                        else []
                    ),
                },
                channels,
            )
            channels = api.get(f"/guilds/{guild_id}/channels")
        ids[f"cat_{category['key']}"] = cat["id"]
        try:
            api.patch(f"/channels/{cat['id']}", {"position": position})
        except DiscordError:
            pass

        for spec_index, spec in enumerate(category["channels"]):
            payload = channel_payload(
                spec,
                cat["id"],
                everyone_id,
                role_ids,
                community_on,
                staff_cat=bool(category.get("staff_only")),
            )
            try:
                ch = ensure_channel(api, guild_id, payload, channels)
            except DiscordError as exc:
                print(f"  ! {spec['name']} : {exc.status} {exc.body[:220]}")
                if "topic" in payload:
                    payload.pop("topic", None)
                    try:
                        ch = ensure_channel(api, guild_id, payload, channels)
                    except DiscordError as exc2:
                        print(f"  !! abandon {spec['name']} : {exc2.status}")
                        continue
                else:
                    continue
            ids[spec["key"]] = ch["id"]
            created_channels.append(ch)
            try:
                api.patch(f"/channels/{ch['id']}", {"position": spec_index})
            except DiscordError:
                pass
            channels = api.get(f"/guilds/{guild_id}/channels")
            time.sleep(0.15)

    # 3) Paramètres de guilde
    system_id = ids.get("bienvenue")
    patch = {
        **GUILD_PATCH,
        "system_channel_id": system_id,
        "afk_channel_id": ids.get("cafe_voc"),
        "afk_timeout": 900,
    }
    if community_on:
        patch["features"] = ["COMMUNITY"]
        patch["rules_channel_id"] = ids["regles"]
        patch["public_updates_channel_id"] = ids["journal"]
    try:
        api.patch(f"/guilds/{guild_id}", patch)
        print("Guilde mise à jour (nom, locale fr, salon système).")
    except DiscordError as exc:
        print(f"  ! patch guilde : {exc.status} {exc.body[:200]}")

    # 4) Embeds
    print("Publication des embeds…")
    messages = {}
    for _, spec in iter_channels():
        channel_id = ids.get(spec["key"])
        if not channel_id or not spec.get("embeds"):
            continue
        # Les forums n'acceptent pas les messages hors fils : on crée un fil « Accueil »
        live = next((c for c in api.get(f"/guilds/{guild_id}/channels") if c["id"] == channel_id), None)
        is_forum = live and live.get("type") == T_FORUM
        if is_forum:
            existing_thread = None
            try:
                archived = api.get(
                    f"/channels/{channel_id}/threads/archived/public"
                )
                active = api.get(f"/guilds/{guild_id}/threads/active")
                pool = (archived.get("threads") or []) + (active.get("threads") or [])
                for thread in pool:
                    if thread.get("parent_id") == channel_id and thread.get("name") == "📌 Accueil du forum":
                        existing_thread = thread
                        break
            except DiscordError:
                existing_thread = None
            if existing_thread and not repost:
                messages[spec["key"]] = [existing_thread["id"]]
                print(f"  · fil d'accueil déjà présent {spec['name']}")
                continue
            try:
                thread = api.post(
                    f"/channels/{channel_id}/threads",
                    {
                        "name": "📌 Accueil du forum",
                        "auto_archive_duration": 10080,
                        "message": {
                            "embeds": [mentionize(EMBEDS[spec["embeds"][0]][0], ids)],
                            "allowed_mentions": {"parse": []},
                        },
                    },
                )
                messages[spec["key"]] = [thread.get("id")]
                print(f"  · fil d'accueil {spec['name']}")
                time.sleep(0.6)
            except DiscordError as exc:
                print(f"  ! fil {spec['name']} : {exc.status}")
            continue
        messages[spec["key"]] = post_embeds(
            api, channel_id, spec["key"], ids, False, repost
        )
        if messages[spec["key"]]:
            print(f"  · {spec['name']} ({len(messages[spec['key']])} messages)")

    # 5) Commandes slash
    try:
        register_commands(api, app_id, guild_id)
        print(f"Commandes slash enregistrées ({len(SLASH_COMMANDS)}).")
    except DiscordError as exc:
        print(f"  ! commandes : {exc.status} {exc.body[:200]}")

    # 6) Suppression de l'ancien plan
    channels = api.get(f"/guilds/{guild_id}/channels")
    keep = set(ids.values())
    print("Suppression des salons d'origine…")
    delete_legacy(api, channels, keep)

    state = {
        "guild_id": guild_id,
        "application_id": app_id,
        "community": community_on,
        "roles": role_ids,
        "channels": ids,
        "messages": messages,
        "site": LINKS,
        "color": hex(COLOR_VERT),
    }
    write_state(state)
    print(f"État écrit dans {STATE_PATH.name}")
    print("Déploiement terminé.")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Déploie le serveur Discord Psyclopédia")
    parser.add_argument("--dry-run", action="store_true", help="Afficher la structure sans appeler l'API")
    parser.add_argument("--repost", action="store_true", help="Reposter les embeds même s'ils existent")
    args = parser.parse_args(argv)
    if args.dry_run:
        return dry_run()
    return deploy(repost=args.repost)


if __name__ == "__main__":
    sys.exit(main())
