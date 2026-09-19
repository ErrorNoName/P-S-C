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

from shell import DISCORD_INVITE, slugify, strip_html
from content import (
    CATEGORIES, DICTIONNAIRE, QUIZZES, BOOKS, PDF_BOOKS,
    EXPERIENCES, AUTEURS, TROUBLES, BIAIS, TESTS, CHRONOLOGIE_TRIEE,
    CATEGORY_TITLE, THEORIES, CAS, DEBATS, METHODES_CHAPITRES, METHODES_NOTIONS,
    LEXIQUE_EN, PRATIQUES, METIERS,
)
from data_laboratoire import EXPERIENCES_LAB
from data_courants import COURANTS
from data_mythes import MYTHES
from data_faq import FAQ
from data_aide import PARCOURS_SOIN
from data_autoeval import EVALUATIONS
from data_cours import get_cours

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
        ("Méthodes et statistiques", "Plans de recherche, valeur p, taille d'effet, réplication, éthique et lecture critique d'un article.", EBOOK + "methodes.html", "methodologie statistiques p-value experience protocole esprit critique"),
        ("Psychologie pratique", f"{len(PRATIQUES)} fiches concrètes : sommeil, stress, apprentissage, relations, travail, décision.", EBOOK + "pratique.html", "pratique quotidien conseils protocole appliquee"),
        ("Lexique anglais-français", f"{len(LEXIQUE_EN)} termes traduits et les faux amis de la psychologie.", EBOOK + "lexique.html", "anglais traduction vocabulaire faux amis english"),
        ("Métiers et études", f"{len(METIERS)} métiers, le parcours licence-master et les titres protégés.", EBOOK + "metiers.html", "metier orientation etudes psychologue formation carriere"),
        ("Laboratoire d'expériences", f"{len(EXPERIENCES_LAB)} expériences classiques jouables directement dans le navigateur.", EBOOK + "laboratoire.html", "laboratoire experience interactive stroop test jouer"),
        ("Révision espacée", "Réviser toutes les notions du site en cartes replanifiées automatiquement.", EBOOK + "revision.html", "revision flashcards espacee memorisation anki"),
        ("Fiches de révision imprimables", f"Les {len(CATEGORIES)} domaines condensés en fiches prêtes à imprimer.", EBOOK + "fiches/index.html", "fiches revision imprimer resume synthese"),
        ("Les grands courants", f"{len(COURANTS)} écoles de pensée : postulat, méthode, apports, critiques et héritage.", EBOOK + "references/courants.html", "courant ecole behaviorisme gestalt psychanalyse cognitivisme humanisme structuralisme"),
        ("Idées reçues et neuromythes", f"{len(MYTHES)} affirmations très répandues passées au crible des données.", EBOOK + "references/mythes.html", "mythe idee recue faux neuromythe croyance 10% cerveau styles apprentissage"),
        ("Questions fréquentes", f"{len(FAQ)} questions sur la psychologie, le cerveau, l'apprentissage et la santé mentale.", EBOOK + "faq.html", "faq questions reponses frequentes"),
        ("Auto-évaluations pédagogiques", f"{len(EVALUATIONS)} questionnaires pour comprendre la psychométrie de l'intérieur, sans valeur diagnostique.", EBOOK + "auto-evaluations.html", "test questionnaire auto evaluation personnalite big five chronotype"),
        ("Aide et ressources", "Numéros d'urgence et d'écoute, parcours de soin, remboursement, ressources libres.", EBOOK + "aide.html", "aide urgence 3114 ecoute consulter psychologue psychiatre cmp remboursement"),
        ("Serveur Discord Psyclopédia", "Communauté : cours de 50 min, forums thématiques, fiches et entraide. Pas un soin.", DISCORD_INVITE, "discord communaute forum serveur entraide"),
        ("Plan du site et index A-Z", "Toutes les pages et l'index alphabétique général de Psyclopédia.", EBOOK + "plan.html", "plan sommaire index alphabetique sitemap"),
        ("Crédits et sources", "Origine et licence de chaque illustration et de chaque ouvrage utilisé.", EBOOK + "credits.html", "credits sources licences attribution domaine public"),
        ("Emploi du temps et cours", "Cursus annuel de cours magistraux et travaux dirigés de 50 minutes, calendrier, compte à rebours et progression locale.", EBOOK + "emploi-du-temps.html", "cours emploi du temps calendrier cm td magistral replay countdown"),
        ("Cours et archives", "Médiathèque des séances : replays par catégorie, thème et intervenant, notes exportables.", EBOOK + "cours/index.html", "archives mediatheque replay cours notes"),
        ("Lecteur de cours synchronisé", "Vidéo francophone, fiches Psyclopédia en direct, surlignage et quiz flash.", EBOOK + "cours/lecteur.html", "lecteur youtube synchronisation karaoke ressources cinema"),
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

    # -- Savoirs v3 ---------------------------------------------------------
    for tid, nom, auteur, annee, domaine, idee, mecanisme, application, limite in THEORIES:
        entries.append(_entry(
            nom, f"{auteur}, {annee} — {idee}", "theorie",
            EBOOK + "references/theories.html#" + tid,
            f"{domaine} {strip_html(mecanisme)[:200]} {strip_html(application)[:150]} {strip_html(limite)[:120]}",
        ))

    for cid, nom, periode, domaine, resume, histoire, apport, aujourdhui in CAS:
        entries.append(_entry(
            nom, f"{periode} · {domaine} — {resume}", "cas",
            EBOOK + "references/cas.html#" + cid,
            f"{strip_html(histoire)[:220]} {strip_html(apport)[:180]} {strip_html(aujourdhui)[:120]}",
        ))

    for did, titre, famille, question, pa_t, pa, pb_t, pb, etat in DEBATS:
        entries.append(_entry(
            titre, question, "debat",
            EBOOK + "references/debats.html#" + did,
            f"{famille} {pa_t} {pb_t} {strip_html(pa)[:150]} {strip_html(pb)[:150]} {strip_html(etat)[:150]}",
        ))

    for anc, titre, html in METHODES_CHAPITRES:
        entries.append(_entry(titre, _summary(html), "section", EBOOK + "methodes.html#" + anc,
                              "methodologie statistiques recherche"))

    for nid, nom, famille, definition, exemple, piege in METHODES_NOTIONS:
        entries.append(_entry(nom, definition, "notion", EBOOK + "methodes.html#notions",
                              f"{famille} methodologie {exemple} {piege}"))

    for en, fr, domaine, note in LEXIQUE_EN:
        entries.append(_entry(f"{en} → {fr}", f"{domaine} — {strip_html(note)}", "anglais",
                              EBOOK + "lexique.html", f"traduction anglais {en} {fr}"))

    for pid, titre, famille, situation, recherche, etapes, piege in PRATIQUES:
        entries.append(_entry(
            titre, situation, "pratique", EBOOK + "pratique.html#" + pid,
            f"{famille} {strip_html(recherche)[:180]} {' '.join(strip_html(e) for e in etapes)[:220]}",
        ))

    for mid, nom, famille, mission, formation, quotidien, ou, savoir in METIERS:
        entries.append(_entry(
            nom, f"{famille} — {mission}", "metier", EBOOK + "metiers.html#" + mid,
            f"{formation} {quotidien} {ou} orientation etudes",
        ))

    for lid, titre, icone, couleur, duree, accroche, consigne, explication, _liens in EXPERIENCES_LAB:
        entries.append(_entry(
            titre, accroche, "labo", EBOOK + f"laboratoire/{lid}.html",
            f"experience interactive jouable {duree} {strip_html(explication)[:200]}",
        ))

    # -- Repères v4 ---------------------------------------------------------
    for cid, nom, periode, figures, postulat, methode, apport, critique, heritage in COURANTS:
        entries.append(_entry(
            nom, f"{periode} · {figures} — {strip_html(postulat)[:160]}", "courant",
            EBOOK + "references/courants.html#" + cid,
            f"{strip_html(apport)[:180]} {strip_html(critique)[:150]} {strip_html(heritage)[:120]} ecole courant",
        ))

    for mid, affirmation, famille, verdict, savoir, origine, nuance in MYTHES:
        entries.append(_entry(
            affirmation, f"{famille} — {strip_html(savoir)[:170]}", "mythe",
            EBOOK + "references/mythes.html#" + mid,
            f"idee recue neuromythe {verdict} {strip_html(origine)[:150]} {strip_html(nuance)[:150]}",
        ))

    for fid, question, famille, reponse in FAQ:
        entries.append(_entry(
            question, _summary(reponse), "faq", EBOOK + "faq.html#" + fid,
            f"question frequente {famille} {strip_html(reponse)[:250]}",
        ))

    for pid, titre, contenu in PARCOURS_SOIN:
        entries.append(_entry(
            titre, _summary(contenu), "aide", EBOOK + "aide.html#" + pid,
            "aide ressources soin consultation psychologue psychiatre orientation",
        ))

    for ev in EVALUATIONS:
        entries.append(_entry(
            ev["titre"], ev["accroche"], "eval",
            EBOOK + f"auto-evaluations/{ev['id']}.html",
            f"questionnaire auto-evaluation {ev['duree']} "
            + " ".join(d[1] for d in ev["dimensions"]),
        ))

    entries.append(_entry(
        "Aide, orientation et ressources",
        "Numéros d'urgence et d'écoute, parcours de soin, remboursement et ressources en accès libre.",
        "aide", EBOOK + "aide.html",
        "urgence 3114 suicide 15 112 3919 119 ecoute soutien psychologue consultation CMP remboursement",
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

    # -- Cours magistraux et TD --------------------------------------------
    for course in get_cours():
        entries.append(_entry(
            course["kind"] + " — " + course["title"],
            f"Semaine {course['week']} · {course['module']} · {course['guest']} — séance de 50 minutes.",
            "cours",
            EBOOK + "cours/lecteur.html?id=" + course["id"],
            f"{course['theme']} {course['cat']} {course['video']['title']} {course['video']['speaker']} "
            f"{' '.join(course['pages'])} cm td replay",
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
                  "theorie": 5, "courant": 6, "trouble": 7, "biais": 8, "test": 9, "cas": 10,
                  "debat": 11, "mythe": 12, "faq": 13, "pratique": 14, "aide": 15, "metier": 16,
                  "labo": 17, "eval": 18, "anglais": 19, "date": 20, "livre": 21, "quiz": 22,
                  "cours": 23, "page": 24}
    entries.sort(key=lambda e: kind_order.get(e["k"], 99))
    return entries


def write_index():
    entries = build_index()
    path = os.path.join(BASE, "search-index.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, separators=(",", ":"))
    size_kb = os.path.getsize(path) / 1024
    return len(entries), size_kb, len(PDF_BOOKS)
