# -*- coding: utf-8 -*-
"""Télécharge les illustrations Wikimedia Commons manquantes (domaine public / CC)."""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request

from data_credits import CREDITS
from data_decouverte import GALLERIE

HERE = os.path.dirname(os.path.abspath(__file__))
DEST = os.path.abspath(os.path.join(HERE, "..", "05-larousse-illustre-complet", "illustrations", "wikimedia"))
API = "https://commons.wikimedia.org/w/api.php"
UA = "PsyclopediaBot/1.0 (educational static site; https://errornoname.github.io/P-S-C/)"


def _targets():
    seen = {}
    for row in CREDITS:
        seen[row[0]] = row[1]
    for row in GALLERIE:
        seen[row[0]] = row[1]
    return seen


def _info(commons_name):
    title = commons_name if commons_name.startswith("File:") else "File:" + commons_name
    params = {
        "action": "query",
        "titles": title,
        "prop": "imageinfo",
        "iiprop": "url|size|mime",
        "iiurlwidth": "1100",
        "format": "json",
    }
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=40) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    pages = data.get("query", {}).get("pages", {})
    for page in pages.values():
        infos = page.get("imageinfo") or []
        if not infos:
            return None
        info = infos[0]
        return info.get("thumburl") or info.get("url")
    return None


def _fetch(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as resp:
        payload = resp.read()
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "wb") as fh:
        fh.write(payload)
    return len(payload)


def main():
    os.makedirs(DEST, exist_ok=True)
    ok = skip = fail = 0
    for local, commons in _targets().items():
        dest = os.path.join(DEST, local)
        if os.path.isfile(dest) and os.path.getsize(dest) > 200:
            skip += 1
            continue
        try:
            src = _info(commons)
            if not src:
                print("MANQUE", local, commons)
                fail += 1
                continue
            n = _fetch(src, dest)
            print("OK", local, n)
            ok += 1
        except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
            print("ECHEC", local, exc)
            fail += 1
    print(f"téléchargés={ok} déjà={skip} échecs={fail}")


if __name__ == "__main__":
    main()
