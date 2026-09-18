# -*- coding: utf-8 -*-
"""
PSYCLOPÉDIA — Génération de l'index de recherche.

Produit `search-index.json` : une entrée par élément consultable du site
(catégorie, section, notion, expérience, auteur, trouble, biais, test, date,
livre, quiz, page). Chaque entrée porte un titre, une description, un type,
une URL relative à la racine du dépôt et des mots-clés supplémentaires.
"""

import json
import os

from shell import slugify, strip_html
from content import (
    CATEGORIES, DICTIONNAIRE, QUIZZES, BOOKS, PDF_BOOKS,
    EXPERIENCES, AUTEURS, TROUBLES, BIAIS, TESTS, CHRONOLOGIE_TRIEE,
    CATEGORY_TITLE,
)

BASE = os.path.dirname(os.path.abspath(__file__))
EBOOK = "livres-psychologie/07-ebook-final/"
PDF_ROOT = "livres-psychologie/06-pdf-domaine-public/"


def _entry(title, desc, kind, url, keywords=""):
    return {"t": title, "d": desc, "k": kind, "u": url, "g": keywords}


def _summary(html, limit=260):
    txt = strip_html(html)
    return txt[:limit] + ("…" if len(txt) > limit else "")


def build_index():
    entries = []

    # -- Pages principales ------------------------------------------------
    static_pages = [
        ("Accueil de Psyclopédia", "Tableau de bord de l'encyclopédie : progression, accès rapide aux catégories, aux références et à la bibliothèque.", "index.html", "accueil dashboard sommaire"),
        ("Toutes les catégories", f"Les {len(CATEGORIES)} domaines de la psychologie, regroupés par grande famille.", EBOOK + "index.html", "categories domaines sommaire"),
        ("Dictionnaire A-Z", f"{len(DICTIONNAIRE)} notions de psychologie définies et reliées à leur catégorie.", EBOOK + "dictionnaire.html", "glossaire lexique vocabulaire definitions"),
        ("Base de références", "Expériences, auteurs, troubles, biais, tests et chronologie réunis.", EBOOK + "references/index.html", "references base donnees"),
        ("Bibliothèque des livres", f"{len(BOOKS)} ouvrages du domaine public en français, lisibles en ligne.", EBOOK + "bibliotheque.html", "livres pdf domaine public bibliotheque"),
        ("Lecteur de livres intégré", "Lire les ouvrages page par page avec extraction du texte, OCR français et modernisation.", EBOOK + "lecteur.html", "lecteur pdf ocr traduction scan lire en ligne"),
        ("Tous les quiz", f"{len(QUIZZES)} quiz notés sur 20 avec corrigé expliqué.", EBOOK + "quiz/index.html", "quiz test evaluation note"),
        ("Parcours guidés", "Six itinéraires d'apprentissage selon ton objectif.", EBOOK + "parcours.html", "parcours itineraire programme debutant"),
        ("Apprendre efficacement", "Techniques de mémorisation validées par la science cognitive et plan de révision sur 30 jours.", EBOOK + "apprendre.html", "methode memorisation revision vark pomodoro"),
        ("Chronologie de la psychologie", "Les dates clés de la discipline, de l'Antiquité à aujourd'hui.", EBOOK + "references/chronologie.html", "histoire frise dates"),
    ]
    for title, desc, url, kw in static_pages:
        entries.append(_entry(title, desc, "page", url, kw))

    # -- Catégories et leurs sections -------------------------------------
    for cat in CATEGORIES:
        url = EBOOK + "categories/" + cat["id"] + ".html"
        keywords = " ".join(cat["objectives"]) + " " + cat["subtitle"]
        entries.append(_entry(cat["title"], cat["subtitle"], "categorie", url, keywords))
        for section_title, section_body in cat["sections"]:
            entries.append(_entry(
                section_title,
                _summary(section_body),
                "section",
                f"{url}#{slugify(section_title)}",
                cat["title"],
            ))
        for question, answer in cat.get("flashcards", []):
            entries.append(_entry(question, answer, "notion", url + "#flashcards", cat["title"]))

    # -- Dictionnaire ------------------------------------------------------
    for term, definition, cat_id in DICTIONNAIRE:
        entries.append(_entry(
            term, definition, "notion",
            EBOOK + "dictionnaire.html#def-" + slugify(term),
            CATEGORY_TITLE.get(cat_id, ""),
        ))

    # -- Références --------------------------------------------------------
    for eid, titre, chercheur, annee, cat_id, resume, protocole, resultat, portee, _critique in EXPERIENCES:
        entries.append(_entry(
            titre, f"{chercheur}, {annee} — {resume}", "experience",
            EBOOK + "references/experiences.html#" + eid,
            f"{chercheur} {annee} {CATEGORY_TITLE.get(cat_id, '')} {strip_html(protocole)[:150]} {strip_html(resultat)[:150]} {strip_html(portee)[:120]}",
        ))

    for aid, nom, dates, pays, courant, apport, bio, citation, oeuvres in AUTEURS:
        entries.append(_entry(
            nom, f"{dates} · {pays} · {courant} — {apport}", "auteur",
            EBOOK + "references/auteurs.html#" + aid,
            f"{courant} {oeuvres} {citation} {strip_html(bio)[:200]}",
        ))

    for tid, nom, famille, prevalence, signes, comprendre, traitements in TROUBLES:
        entries.append(_entry(
            nom, f"{famille} ({prevalence}) — " + "; ".join(signes[:3]), "trouble",
            EBOOK + "references/troubles.html#" + tid,
            f"{famille} {strip_html(comprendre)[:200]} {strip_html(traitements)[:150]}",
        ))

    for bid, nom, famille, definition, exemple, parade in BIAIS:
        entries.append(_entry(
            nom, definition, "biais",
            EBOOK + "references/biais.html#" + bid,
            f"{famille} {exemple} {parade}",
        ))

    for tid, nom, categorie, auteur_annee, mesure, passation, interpretation, limites in TESTS:
        entries.append(_entry(
            nom, f"{categorie} · {auteur_annee} — {mesure}", "test",
            EBOOK + "references/tests.html#" + tid,
            f"{categorie} {auteur_annee} {passation} {interpretation} {limites}",
        ))

    for annee, titre, description, categorie in CHRONOLOGIE_TRIEE:
        label = ("−" + str(annee)[1:] + " av. J.-C.") if str(annee).startswith("-") else str(annee)
        entries.append(_entry(
            f"{label} — {titre}", description, "date",
            EBOOK + "references/chronologie.html#date-" + slugify(str(annee) + "-" + titre),
            categorie,
        ))

    # -- Livres -------------------------------------------------------------
    for book in BOOKS:
        is_pdf = book["path"].endswith(".pdf")
        url = (EBOOK + "lecteur.html?livre=../06-pdf-domaine-public/" + book["path"]) if is_pdf \
            else (PDF_ROOT + book["path"])
        entries.append(_entry(
            book["title"], f"{book['author']} ({book['year']}) — {book['desc']}", "livre", url,
            f"{book['author']} {book['year']} {book['cat']} domaine public livre complet",
        ))

    # -- Quiz ---------------------------------------------------------------
    for quiz in QUIZZES:
        entries.append(_entry(
            "Quiz — " + quiz["title"],
            f"{len(quiz['questions'])} questions · {quiz['difficulty']} — {quiz['desc']}",
            "quiz", EBOOK + "quiz/quiz.html?id=" + quiz["id"],
            " ".join(q["q"] for q in quiz["questions"][:8]),
        ))

    # L'ordre des types pilote le regroupement visuel dans la modale.
    kind_order = {"categorie": 0, "notion": 1, "section": 2, "experience": 3, "auteur": 4,
                  "trouble": 5, "biais": 6, "test": 7, "date": 8, "livre": 9, "quiz": 10, "page": 11}
    entries.sort(key=lambda e: kind_order.get(e["k"], 99))
    return entries


def write_index():
    entries = build_index()
    path = os.path.join(BASE, "search-index.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, separators=(",", ":"))
    size_kb = os.path.getsize(path) / 1024
    return len(entries), size_kb, len(PDF_BOOKS)
