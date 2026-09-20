# -*- coding: utf-8 -*-
"""Contrôles du cabinet de planches et du catalogue de pensées."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from build_plates import FIGURES, PAPERS, plate_records, render_svg, write_svgs
from data_pensees import PENSEES, PLATES_CATEGORIES, PLATES_STATIQUES, SLOTS

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]


class PlateEngineTests(unittest.TestCase):
    def test_chaque_figure_produit_un_svg(self):
        for name in FIGURES:
            svg = render_svg(name, "cream", "1", "Essai", seed=3)
            self.assertIn("<svg", svg)
            self.assertIn("Fig. 1.", svg)
            self.assertIn("viewBox", svg)

    def test_figure_inconnue_echoue(self):
        with self.assertRaises(ValueError):
            render_svg("inconnu", "cream", "1", "x")

    def test_papiers_connus(self):
        self.assertEqual(set(PAPERS), {"cream", "blue", "red", "peach", "sage"})

    def test_une_planche_par_categorie(self):
        cats = [row[0] for row in PLATES_CATEGORIES]
        self.assertEqual(len(cats), 27)
        self.assertEqual(len(set(cats)), 27)
        for _cid, figure, paper, title in PLATES_CATEGORIES:
            self.assertIn(figure, FIGURES)
            self.assertIn(paper, PAPERS)
            self.assertTrue(title)

    def test_ecriture_svg(self):
        n = write_svgs()
        self.assertEqual(n, 27)
        missing = [
            cid for cid, *_ in PLATES_CATEGORIES
            if not (REPO / "assets-ebook/plates/svg" / f"cat-{cid}.svg").is_file()
        ]
        self.assertEqual(missing, [])


class PenseesTests(unittest.TestCase):
    def test_pensees_completes(self):
        ids = [p[0] for p in PENSEES]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertGreaterEqual(len(PENSEES), 30)
        slots = {s[0] for s in SLOTS}
        plate_ids = {p["id"] for p in PLATES_STATIQUES} | {f"cat-{c[0]}" for c in PLATES_CATEGORIES}
        for pid, kind, slot, text, by, href, plate, _kw in PENSEES:
            self.assertIn(kind, {"citation", "prompt"})
            self.assertIn(slot, slots)
            self.assertGreater(len(text), 20)
            self.assertTrue(by)
            self.assertTrue(href)
            self.assertIn(plate, plate_ids)

    def test_quatre_creneaux(self):
        self.assertEqual([s[0] for s in SLOTS], ["matin", "midi", "apres-midi", "soir"])

    def test_fichiers_statiques_presents(self):
        missing = [p["file"] for p in PLATES_STATIQUES if not (REPO / p["file"]).is_file()]
        self.assertEqual(missing, [])

    def test_records_json_serialisables(self):
        records = plate_records()
        json.dumps(records, ensure_ascii=False)
        self.assertGreaterEqual(len(records), 27 + len(PLATES_STATIQUES))


if __name__ == "__main__":
    unittest.main()
