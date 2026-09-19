# -*- coding: utf-8 -*-
"""Contrôles statiques de l'architecture Discord — sans réseau, sans jeton."""

from __future__ import annotations

import unittest
from pathlib import Path

from blueprint import (
    CATEGORIES,
    LINKS,
    ROLES,
    SLASH_COMMANDS,
    T_FORUM,
    T_NEWS,
    T_TEXT,
    T_VOICE,
    all_channel_names,
    flatten_structure,
    iter_channels,
)
from embeds import EMBEDS, validate_embeds

HERE = Path(__file__).resolve().parent


class StructureTests(unittest.TestCase):
    def test_categories_ordonnees_et_completes(self):
        keys = [c["key"] for c in CATEGORIES]
        self.assertEqual(
            keys,
            ["accueil", "cours", "fiches", "thematiques", "entraide", "vocaux", "equipe_cat"],
        )
        self.assertGreaterEqual(len(list(iter_channels())), 30)

    def test_noms_de_salons_uniques(self):
        names = all_channel_names()
        self.assertEqual(len(names), len(set(names)), names)

    def test_cles_de_salons_uniques(self):
        keys = [ch["key"] for _, ch in iter_channels()]
        self.assertEqual(len(keys), len(set(keys)))

    def test_emojis_systematiques(self):
        for _, channel in iter_channels():
            self.assertTrue(
                channel["name"][0] >= "\u0080" or channel["name"][0] in "📌🎓📚💬🤝🎤🔒",
                channel["name"],
            )
            self.assertIn("-", channel["name"])

    def test_accueil_contient_guide_et_regles(self):
        accueil = next(c for c in CATEGORIES if c["key"] == "accueil")
        names = [ch["name"] for ch in accueil["channels"]]
        self.assertIn("👋-bienvenue", names)
        self.assertIn("📜-regles", names)
        self.assertIn("🧭-guide-et-orientation", names)
        self.assertIn("🗺️-guide-du-serveur", names)
        self.assertTrue(any(ch.get("rules") for ch in accueil["channels"]))
        self.assertTrue(any(ch.get("public_updates") for ch in accueil["channels"]))

    def test_forums_thematiques(self):
        them = next(c for c in CATEGORIES if c["key"] == "thematiques")
        self.assertEqual(len(them["channels"]), 5)
        for channel in them["channels"]:
            self.assertEqual(channel["type"], T_FORUM)
            self.assertGreaterEqual(len(channel["tags"]), 5)
            for tag in channel["tags"]:
                self.assertLessEqual(len(tag["name"]), 20, tag["name"])
                self.assertTrue(tag["emoji_name"])

    def test_cours_synchronises(self):
        cours = next(c for c in CATEGORIES if c["key"] == "cours")
        names = [ch["name"] for ch in cours["channels"]]
        self.assertIn("📣-annonces-cours", names)
        self.assertIn("🗓️-planning-50min", names)
        self.assertIn("💬-apres-cours", names)
        self.assertIn("📎-ressources-de-seance", names)
        self.assertIn("📝-forum-revision", names)
        self.assertIn("🆘-entraide-niveaux", names)

    def test_soutien_a_un_slowmode(self):
        _, soutien = next((c, ch) for c, ch in iter_channels() if ch["key"] == "soutien")
        self.assertEqual(soutien["type"], T_TEXT)
        self.assertGreaterEqual(soutien.get("slowmode", 0), 10)

    def test_vocaux(self):
        vocaux = next(c for c in CATEGORIES if c["key"] == "vocaux")
        self.assertTrue(all(ch["type"] == T_VOICE for ch in vocaux["channels"]))
        self.assertEqual(len(vocaux["channels"]), 4)

    def test_annonces_sont_news(self):
        news = [ch["name"] for _, ch in iter_channels() if ch["type"] == T_NEWS]
        self.assertIn("📢-annonces", news)
        self.assertIn("📣-annonces-cours", news)

    def test_roles_accueil_et_interets(self):
        names = [r["name"] for r in ROLES]
        self.assertIn("🌱 Nouveau", names)
        self.assertIn("🏛️ Équipe", names)
        self.assertGreaterEqual(sum(1 for r in ROLES if r.get("interest")), 5)

    def test_slash_commands(self):
        names = {c["name"] for c in SLASH_COMMANDS}
        self.assertEqual(
            names,
            {"guide", "regles", "planning", "site", "aide", "cours", "roles", "ressource"},
        )

    def test_embeds_limites_discord(self):
        self.assertEqual(validate_embeds(), [])

    def test_chaque_salon_info_a_des_embeds(self):
        for _cat, channel in iter_channels():
            if channel.get("embeds"):
                for key in channel["embeds"]:
                    self.assertIn(key, EMBEDS, key)

    def test_orientation_complete(self):
        accueil = next(c for c in CATEGORIES if c["key"] == "accueil")
        guide = next(ch for ch in accueil["channels"] if ch["key"] == "guide_orientation")
        self.assertEqual(len(guide["embeds"]), 7)
        chunks = []
        for key in guide["embeds"]:
            for embed in EMBEDS[key]:
                chunks.append(embed.get("description") or "")
                for field in embed.get("fields") or []:
                    chunks.append(field.get("value") or "")
        text = " ".join(chunks)
        self.assertIn("50 minutes", text)
        self.assertIn("3114", text)
        self.assertIn("tag", text.lower())

    def test_liens_site(self):
        self.assertTrue(LINKS["accueil"].startswith("https://errornoname.github.io/P-S-C"))
        self.assertIn("emploi-du-temps.html", LINKS["cours"])
        self.assertIn("aide.html", LINKS["aide"])
        self.assertTrue(LINKS["discord"].startswith("https://discord.gg/"))
        shell = (HERE.parent / "livres-psychologie/07-ebook-final/shell.py").read_text(encoding="utf-8")
        self.assertIn(f'DISCORD_INVITE = "{LINKS["discord"]}"', shell)
        self.assertIn("nav-discord-btn", shell)
        self.assertIn("{DISCORD_INVITE}", shell)

    def test_aucun_jeton_dans_le_dossier(self):
        import re

        secret = re.compile(r"[A-Za-z0-9_-]{24}\.[A-Za-z0-9_-]{6}\.[A-Za-z0-9_-]{27,}")
        assigned = re.compile(r"DISCORD_BOT_TOKEN=\S+")
        for path in HERE.rglob("*"):
            if path.suffix in {".pyc"} or path.name == ".env" or not path.is_file():
                continue
            if path.name == "deploy_state.json":
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            self.assertIsNone(secret.search(text), path.name)
            if path.name == ".env.example":
                self.assertNotRegex(text, r"DISCORD_BOT_TOKEN=\S+")
                continue
            leaked = assigned.search(text)
            if not leaked:
                continue
            value = leaked.group(0).split("=", 1)[1].strip().strip("'\"")
            if len(value) >= 50 and "." in value:
                self.fail(f"jeton possible dans {path.name}")

    def test_catalogue_forums(self):
        from forum_catalog import build_catalog, validate_catalog

        catalog = build_catalog()
        self.assertGreaterEqual(len(catalog), 80)
        forums = {item["forum"] for item in catalog}
        for key in (
            "fiches_synthese", "livres_dp", "fiches_cliniques", "citations",
            "glossaire", "forum_revision", "articles", "esprit",
        ):
            self.assertIn(key, forums)
        self.assertEqual(validate_catalog(catalog), [])
        titles = [(i["forum"], i["title"]) for i in catalog]
        self.assertEqual(len(titles), len(set(titles)))

    def test_flatten_structure_couvre_tout(self):
        rows = flatten_structure()
        cats = [r for r in rows if r["kind"] == "category"]
        channels = [r for r in rows if r["kind"] != "category"]
        self.assertEqual(len(cats), len(CATEGORIES))
        self.assertEqual(len(channels), len(list(iter_channels())))


if __name__ == "__main__":
    unittest.main()
