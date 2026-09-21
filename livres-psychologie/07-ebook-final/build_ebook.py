# -*- coding: utf-8 -*-
"""
PSYCLOPÉDIA — Générateur du site.

Orchestre la construction complète : catégories, dictionnaire, base de
références, quiz, bibliothèque, lecteur intégré, parcours guidés, guide
d'apprentissage, puis l'index de recherche.

    python3 build_ebook.py
"""

import build_autoeval
import build_categories
import build_compte
import build_cours
import build_decouverte
import build_home
import build_pages
import build_plates
import build_outils
import build_references
import build_savoirs
import build_savoirs2
import build_sitemap
import build_lycee
import build_assistant
from build_index import write_index
from content import (
    CATEGORIES, DICTIONNAIRE, QUIZZES, BOOKS, EXPERIENCES, AUTEURS, TROUBLES, BIAIS,
    TESTS, CHRONOLOGIE_TRIEE, THEORIES, CAS, DEBATS, METHODES_NOTIONS, LEXIQUE_EN,
    PRATIQUES, METIERS,
)
from data_laboratoire import EXPERIENCES_LAB
from data_courants import COURANTS
from data_mythes import MYTHES
from data_faq import FAQ


def main():
    build_categories.render_categories_index()
    for i, cat in enumerate(CATEGORIES):
        build_categories.render_category(cat, i)
    build_categories.render_dictionnaire()

    build_references.render_all()
    build_savoirs.render_all()
    build_savoirs2.render_all()
    n_evals, n_eval_items = build_autoeval.render_all()
    n_cards, cards_kb, n_index = build_outils.render_all()
    build_pages.render_all()
    n_lycee = build_lycee.render_all()
    n_ai, ai_kb = build_assistant.render_all()
    n_gal, n_xp = build_decouverte.render_decouverte()
    n_cours = build_cours.render_all()
    n_compte = build_compte.render_all()
    n_svg, n_pensees, n_plates, _n_cat = build_plates.render_all()
    build_home.render_home()

    n_entries, size_kb, n_pdf = write_index()
    n_pages = build_sitemap.render_sitemap()

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
    print(f"   • Repères : {len(COURANTS)} courants, {len(MYTHES)} idées reçues, {len(FAQ)} questions fréquentes, "
          f"aide et ressources")
    print(f"   • Auto-évaluations : {n_evals} questionnaires, {n_eval_items} affirmations")
    print(f"   • {len(QUIZZES)} quiz, {n_questions} questions")
    print(f"   • {len(BOOKS)} ouvrages ({n_pdf} lisibles dans le lecteur intégré)")
    print(f"   • Outils : {len(EXPERIENCES_LAB)} expériences jouables, {n_cards} cartes de révision "
          f"({cards_kb:.0f} Ko), {len(CATEGORIES)} fiches imprimables, index A-Z de {n_index} entrées")
    print(f"   • Index de recherche : {n_entries} entrées ({size_kb:.0f} Ko)")
    print(f"   • Cursus : {n_cours} séances de 50 min (emploi du temps, archives, lecteur)")
    print(f"   • Compte étudiant : {n_compte} pages (connexion, espace, API SQLite)")
    print(f"   • Rappels : {n_pensees} pensées, {n_plates} planches ({n_svg} gravures SVG)")
    print(f"   • Études + 4 branches : {n_lycee} pages")
    print(f"   • Assistant : corpus {n_ai} extraits ({ai_kb:.0f} Ko)")
    print(f"   • Découverte : {n_gal} images, {n_xp} planches d'expériences")
    print(f"   • sitemap.xml : {n_pages} pages référencées, robots.txt écrit")


if __name__ == "__main__":
    main()
