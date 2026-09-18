# -*- coding: utf-8 -*-
"""
PSYCLOPÉDIA — Générateur du site.

Orchestre la construction complète : catégories, dictionnaire, base de
références, quiz, bibliothèque, lecteur intégré, parcours guidés, guide
d'apprentissage, puis l'index de recherche.

    python3 build_ebook.py
"""

import build_categories
import build_home
import build_pages
import build_outils
import build_references
import build_savoirs
from build_index import write_index
from content import (
    CATEGORIES, DICTIONNAIRE, QUIZZES, BOOKS, EXPERIENCES, AUTEURS, TROUBLES, BIAIS,
    TESTS, CHRONOLOGIE_TRIEE, THEORIES, CAS, DEBATS, METHODES_NOTIONS, LEXIQUE_EN,
    PRATIQUES, METIERS,
)
from data_laboratoire import EXPERIENCES_LAB


def main():
    build_categories.render_categories_index()
    for i, cat in enumerate(CATEGORIES):
        build_categories.render_category(cat, i)
    build_categories.render_dictionnaire()

    build_references.render_all()
    build_savoirs.render_all()
    n_cards, cards_kb, n_index = build_outils.render_all()
    build_pages.render_all()
    build_home.render_home()

    n_entries, size_kb, n_pdf = write_index()

    n_sections = sum(len(c["sections"]) for c in CATEGORIES)
    n_flash = sum(len(c.get("flashcards", [])) for c in CATEGORIES)
    n_questions = sum(len(q["questions"]) for q in QUIZZES)

    print("✅ Psyclopédia générée")
    print(f"   • {len(CATEGORIES)} catégories, {n_sections} chapitres, {n_flash} flashcards")
    print(f"   • {len(DICTIONNAIRE)} entrées de dictionnaire")
    print(f"   • Références : {len(EXPERIENCES)} expériences, {len(AUTEURS)} auteurs, "
          f"{len(TROUBLES)} troubles, {len(BIAIS)} biais, {len(TESTS)} tests, {len(CHRONOLOGIE_TRIEE)} dates")
    print(f"   • Savoirs : {len(THEORIES)} théories, {len(CAS)} cas cliniques, {len(DEBATS)} débats, "
          f"{len(METHODES_NOTIONS)} notions de méthode, {len(LEXIQUE_EN)} termes bilingues, "
          f"{len(PRATIQUES)} fiches pratiques, {len(METIERS)} métiers")
    print(f"   • {len(QUIZZES)} quiz, {n_questions} questions")
    print(f"   • {len(BOOKS)} ouvrages ({n_pdf} lisibles dans le lecteur intégré)")
    print(f"   • Outils : {len(EXPERIENCES_LAB)} expériences jouables, {n_cards} cartes de révision "
          f"({cards_kb:.0f} Ko), {len(CATEGORIES)} fiches imprimables, index A-Z de {n_index} entrées")
    print(f"   • Index de recherche : {n_entries} entrées ({size_kb:.0f} Ko)")


if __name__ == "__main__":
    main()
