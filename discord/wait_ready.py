#!/usr/bin/env python3
"""Attend que le superviseur ait connecté le bot (fichier /tmp/psyc-bot.ready)."""

from __future__ import annotations

import sys
import time
from pathlib import Path

READY = Path("/tmp/psyc-bot.ready")


def main():
    deadline = time.time() + 45
    while time.time() < deadline:
        if READY.is_file() and READY.stat().st_size > 0:
            print("Bot prêt.")
            return 0
        time.sleep(1)
    print("Le bot n'a pas signalé sa connexion (jeton manquant ou intent).", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
