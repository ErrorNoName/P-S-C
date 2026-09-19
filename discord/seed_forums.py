#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pré-remplit les forums Discord avec les données Psyclopédia.

    python3 seed_forums.py
    python3 seed_forums.py --dry-run

Idempotent : un fil du même titre n'est pas recréé.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from deploy_server import DiscordAPI, DiscordError, load_guild_id, load_token
from forum_catalog import build_catalog, validate_catalog

STATE_PATH = HERE / "deploy_state.json"
SEED_PATH = HERE / "seed_state.json"


def _load_json(path):
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _tag_ids(channel, names):
    available = channel.get("available_tags") or []
    by_name = {t["name"]: t["id"] for t in available if t.get("id")}
    return [by_name[n] for n in names if n in by_name]


def _existing_titles(api, channel_id, guild_id):
    titles = set()
    try:
        active = api.get(f"/guilds/{guild_id}/threads/active")
        for thread in active.get("threads") or []:
            if thread.get("parent_id") == channel_id:
                titles.add(thread.get("name") or "")
    except DiscordError:
        pass
    try:
        archived = api.get(f"/channels/{channel_id}/threads/archived/public")
        for thread in archived.get("threads") or []:
            titles.add(thread.get("name") or "")
    except DiscordError:
        pass
    return titles


def seed(dry_run=False):
    catalog = build_catalog()
    errors = validate_catalog(catalog)
    if errors:
        print("Catalogue invalide :")
        for err in errors:
            print(" ", err)
        return 1

    counts = {}
    for item in catalog:
        counts[item["forum"]] = counts.get(item["forum"], 0) + 1
    print(f"{len(catalog)} fils prévus")
    for key, n in sorted(counts.items()):
        print(f"  {key}: {n}")
    if dry_run:
        return 0

    token = load_token()
    guild_id = load_guild_id()
    api = DiscordAPI(token)
    state = _load_json(STATE_PATH)
    channel_ids = state.get("channels") or {}
    seed_state = _load_json(SEED_PATH)
    created = seed_state.get("threads") or {}

    channels = {c["id"]: c for c in api.get(f"/guilds/{guild_id}/channels")}
    posted = 0
    skipped = 0

    for item in catalog:
        parent_id = channel_ids.get(item["forum"])
        if not parent_id:
            print(f"  ! salon manquant {item['forum']}")
            continue
        parent = channels.get(parent_id)
        if not parent:
            print(f"  ! salon introuvable {item['forum']}")
            continue

        key = f"{item['forum']}::{item['title']}"
        if key in created:
            skipped += 1
            continue

        titles = _existing_titles(api, parent_id, guild_id)
        if item["title"] in titles:
            skipped += 1
            created[key] = "existing"
            continue

        payload = {
            "name": item["title"],
            "auto_archive_duration": 10080,
            "message": {
                "embeds": item["embeds"],
                "allowed_mentions": {"parse": []},
            },
        }
        tags = _tag_ids(parent, item["tags"])
        if tags:
            payload["applied_tags"] = tags

        try:
            thread = api.post(f"/channels/{parent_id}/threads", payload)
        except DiscordError as exc:
            print(f"  ! {item['title'][:60]} : {exc.status} {exc.body[:160]}")
            time.sleep(1.2)
            continue

        created[key] = thread.get("id")
        posted += 1
        print(f"  + [{item['forum']}] {item['title']}")
        time.sleep(0.75)

        if posted % 15 == 0:
            SEED_PATH.write_text(
                json.dumps({"threads": created}, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

    SEED_PATH.write_text(
        json.dumps({"threads": created, "posted": posted, "skipped": skipped},
                   ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Terminé : {posted} créés, {skipped} déjà présents.")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    return seed(dry_run=args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
