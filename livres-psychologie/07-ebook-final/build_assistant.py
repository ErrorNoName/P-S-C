# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Assistant IA ancré dans le corpus du site + page dédiée."""

import json
import os

from shell import page_shell, page_header, strip_html
from content import (
    CATEGORIES, DICTIONNAIRE, EXPERIENCES, AUTEURS, TROUBLES, BIAIS,
    THEORIES, CAS, METIERS, CATEGORY_TITLE,
)
from data_lycee import BRANCHES, SPECIALITES, GRAND_ORAL, ATTENDUS_L1
from data_mythes import MYTHES
from data_faq import FAQ as FAQ_LIST

BASE = os.path.dirname(os.path.abspath(__file__))
EBOOK = "livres-psychologie/07-ebook-final/"


def _chunk(title, kind, url, text, tags=""):
    txt = strip_html(text).strip()
    if len(txt) < 40:
        return None
    if len(txt) > 900:
        txt = txt[:900].rsplit(" ", 1)[0] + "…"
    return {"t": title, "k": kind, "u": url, "x": txt, "g": tags}


def build_corpus():
    rows = []

    for cat in CATEGORIES:
        url = EBOOK + "categories/" + cat["id"] + ".html"
        rows.append(_chunk(cat["title"], "categorie", url,
                           cat["subtitle"] + " " + " ".join(cat["objectives"]),
                           " ".join(cat["objectives"])))
        for title, body in cat["sections"]:
            rows.append(_chunk(title, "section", url, body, cat["title"]))
        for q, a in cat.get("flashcards", []):
            rows.append(_chunk(q, "notion", url + "#flashcards", a, cat["title"]))

    for term, definition, cat_id in DICTIONNAIRE:
        rows.append(_chunk(term, "notion",
                           EBOOK + "dictionnaire.html",
                           definition, CATEGORY_TITLE.get(cat_id, "")))

    for eid, titre, chercheur, annee, cat_id, resume, protocole, resultat, portee, _c in EXPERIENCES:
        rows.append(_chunk(titre, "experience",
                           EBOOK + "references/experiences.html#" + eid,
                           f"{chercheur}, {annee}. {resume} Résultat : {resultat} Portée : {portee}",
                           chercheur))

    for aid, nom, dates, pays, courant, apport, bio, citation, _o in AUTEURS:
        rows.append(_chunk(nom, "auteur",
                           EBOOK + "references/auteurs.html#" + aid,
                           f"{dates}, {pays}, {courant}. {apport} {strip_html(bio)[:400]}",
                           courant))

    for tid, nom, famille, prev, signes, comprendre, traitements in TROUBLES:
        rows.append(_chunk(nom, "trouble",
                           EBOOK + "references/troubles.html#" + tid,
                           f"{famille} ({prev}). Signes pédagogiques : {', '.join(signes[:4])}. {comprendre}",
                           famille))

    for bid, nom, famille, definition, exemple, parade in BIAIS:
        rows.append(_chunk(nom, "biais",
                           EBOOK + "references/biais.html#" + bid,
                           f"{definition} Exemple : {exemple} Parade : {parade}", famille))

    for tid, nom, auteur, annee, domaine, idee, mecanisme, application, limite in THEORIES:
        rows.append(_chunk(nom, "theorie",
                           EBOOK + "references/theories.html#" + tid,
                           f"{auteur}, {annee}. {idee} {mecanisme} Limite : {limite}", domaine))

    for cid, nom, periode, domaine, resume, histoire, apport, auj in CAS:
        rows.append(_chunk(nom, "cas",
                           EBOOK + "references/cas.html#" + cid,
                           f"{periode}. {resume} {histoire} {apport}", domaine))

    for fid, question, famille, reponse in FAQ_LIST:
        rows.append(_chunk(question, "faq",
                           EBOOK + "faq.html#" + fid, reponse, famille))

    for mid, affirmation, famille, verdict, savoir, origine, nuance in MYTHES:
        rows.append(_chunk(affirmation, "mythe",
                           EBOOK + "references/mythes.html#" + mid,
                           f"Verdict : {verdict}. {savoir} {nuance}", famille))

    for mid, nom, famille, mission, formation, quotidien, ou, savoir in METIERS:
        rows.append(_chunk(nom, "metier",
                           EBOOK + "metiers.html#" + mid,
                           f"{famille}. {mission} Formation : {formation} {savoir}", famille))

    rows.append(_chunk(
        "Lycée Condorcet Saint-Priest et psychologie",
        "lycee", EBOOK + "lycee.html",
        "Le lycée Condorcet (Saint-Priest, 69) n'offre pas de spécialité Psychologie. "
        "On y prépare une L1 via SES, HLP, SVT, maths, HGGSP, philo et le Grand oral. "
        "Le CIO (5 impasse Jacques Brel) accueille les PsyEN. La suite naturelle est "
        "la licence de psychologie à Lyon 2 : clinique, sociale, développement, cognitive, "
        "statistiques et psychobiologie. Le titre de psychologue exige un master.",
        "saint-priest condorcet lyon 2 parcoursup",
    ))
    rows.append(_chunk(
        "Attendus d'une L1 de psychologie",
        "lycee", EBOOK + "lycee.html#calendrier",
        " ".join(ATTENDUS_L1) + " La licence seule ne donne pas le titre.",
        "parcoursup lyon2",
    ))

    for code, nom, lycee, psycho, href in SPECIALITES:
        rows.append(_chunk(
            f"Spécialité {code} et psychologie",
            "lycee", EBOOK + "lycee.html#specialites",
            f"{nom} : au lycée on fait {lycee} Cela prépare {psycho}.",
            code + " " + nom,
        ))

    for b in BRANCHES:
        url = EBOOK + f"branches/{b['id']}.html"
        rows.append(_chunk(b["title"], "branche", url, b["objet"] + " " + b["l1"], b["question"]))
        for n, d in b["notions"]:
            rows.append(_chunk(n, "notion", url, d, b["title"]))
        for t, html in b["modules"]:
            rows.append(_chunk(t, "section", url, html, b["title"]))
        for q, a in b["flashcards"]:
            rows.append(_chunk(q, "notion", url, a, b["title"]))

    for q, pistes, _lien in GRAND_ORAL:
        rows.append(_chunk(q, "oral", EBOOK + "lycee.html#dissertation", pistes, "grand oral"))

    rows.append(_chunk(
        "Assistant Psyclopédia",
        "page", EBOOK + "assistant.html",
        "L'assistant répond uniquement à partir des pages du site : catégories, dictionnaire, "
        "références, lycée, quiz. Il ne diagnostique pas et n'invente pas de sources externes.",
        "ia recherche questions",
    ))

    return [r for r in rows if r]


def write_corpus():
    corpus = build_corpus()
    path = os.path.join(BASE, "ai-corpus.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(corpus, f, ensure_ascii=False, separators=(",", ":"))
    return len(corpus), os.path.getsize(path) / 1024


def render_page():
    exemples = [
        "Quelle est la différence entre conformité et obéissance ?",
        "Que faut-il comme spécialités à Condorcet pour faire psycho ?",
        "C'est quoi la zone proximale de développement ?",
        "Pourquoi la L1 a-t-elle autant de statistiques ?",
        "Que montre l'expérience de Milgram, et quelles sont ses limites ?",
        "Psychologue ou psychiatre ?",
    ]
    chips = "".join(
        f'<button type="button" class="ai-chip" data-ai-q="{q}">{q}</button>'
        for q in exemples
    )
    header = page_header(
        depth=0,
        breadcrumb=[("Accueil", "../../index.html"), ("Assistant IA", None)],
        icon="🤖", color="vert",
        title="Assistant Psyclopédia",
        subtitle="Pose une question : la réponse est construite à partir de tout ce que contient le site, avec les pages sources",
        chips=["Ancré dans le corpus", "Réponses complètes", "Sans diagnostic"],
    )
    body = f"""{header}
<div class="section ai-page">
  <p class="section-desc" style="max-width:760px">Pas un chatbot qui invente. L'assistant cherche
  dans les catégories, le dictionnaire, les expériences, les quatre branches L1 et le parcours
  lycée Saint-Priest, puis rédige une réponse claire avec des liens pour aller plus loin.
  Raccourci : <kbd>Ctrl</kbd> + <kbd>J</kbd> depuis n'importe quelle page.</p>

  <div class="ai-box" data-ai-root>
    <form class="ai-form" data-ai-form>
      <label class="sr-only" for="ai-q">Votre question</label>
      <textarea id="ai-q" data-ai-input rows="2" placeholder="Ex. : Qu'est-ce que la dissonance cognitive, et quel exemple lycée ?" required></textarea>
      <button type="submit" class="btn btn-primary">Répondre</button>
    </form>
    <div class="ai-chips">{chips}</div>
    <div class="ai-out" data-ai-out>
      <div class="ai-empty">Écris une question, ou choisis un exemple. La première recherche charge le corpus du site.</div>
    </div>
  </div>

  <div class="note-box">
    <strong>Ce que l'assistant sait faire :</strong> définir, comparer deux notions, relier une
    matière de Condorcet à une branche, résumer une expérience, orienter vers un quiz ou une fiche.
    <strong>Ce qu'il refuse :</strong> poser un diagnostic, conseiller un traitement, citer une
    page qui n'est pas sur Psyclopédia.
  </div>
  <div class="cta-row">
    <a class="btn btn-secondary" href="lycee.html">🎓 Parcours lycée</a>
    <a class="btn btn-secondary" href="branches/index.html">🧭 Quatre branches</a>
    <button class="btn btn-secondary" data-search-open="">🔍 Recherche classique (Ctrl + K)</button>
  </div>
</div>
"""
    path = os.path.join(BASE, "assistant.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(page_shell(
            "Assistant IA", body, depth=0, active="IA",
            description="Assistant intégré : réponses complètes et sourcées à partir de tout le contenu de Psyclopédia."))
    return path


def render_all():
    n, kb = write_corpus()
    render_page()
    return n, kb
