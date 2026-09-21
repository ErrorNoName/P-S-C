# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Outils d'apprentissage : laboratoire d'expériences jouables,
révision espacée, fiches de révision imprimables, plan du site et index A-Z.
"""

import json
import os
import re
import unicodedata

from shell import DISCORD_INVITE, page_shell, page_header, slugify, strip_html
from content import (
    CATEGORIES, DICTIONNAIRE, QUIZZES, BOOKS, QUIZ_FOR_CATEGORY,
    EXPERIENCES, AUTEURS, TROUBLES, BIAIS, TESTS, CHRONOLOGIE_TRIEE,
    THEORIES, CAS, DEBATS, METHODES_NOTIONS, LEXIQUE_EN, PRATIQUES, METIERS,
)
from data_laboratoire import EXPERIENCES_LAB
from data_courants import COURANTS
from data_mythes import MYTHES
from data_faq import FAQ

BASE = os.path.dirname(os.path.abspath(__file__))


def _write(path, html):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)


# --------------------------------------------------------------------------
# Laboratoire
# --------------------------------------------------------------------------

def render_laboratoire_hub():
    cards = "".join(
        f'<a class="lab-card {couleur}" href="laboratoire/{lid}.html">'
        f'<span class="lab-ico">{icone}</span><h3>{titre}</h3><p>{accroche}</p>'
        f'<span class="lab-time">⏱ {duree}</span></a>'
        for lid, titre, icone, couleur, duree, accroche, _c, _e, _l in EXPERIENCES_LAB
    )

    header = page_header(
        depth=0, breadcrumb=[("Accueil", "../../index.html"), ("Laboratoire", None)],
        icon="🧪", color="vert",
        title="Le laboratoire",
        subtitle=f"{len(EXPERIENCES_LAB)} expériences classiques à vivre sur vous-même, directement dans le navigateur",
        chips=[f"🧪 {len(EXPERIENCES_LAB)} expériences", "⏱ 1 à 4 minutes chacune", "📊 Résultats commentés"],
    )

    body = f"""{header}
<div class="section">
  <p class="section-desc" style="max-width:760px">Lire qu'un effet existe et le sentir agir sur soi sont deux
  expériences très différentes. Ces sept mini-protocoles reproduisent des expériences devenues classiques. Vous
  obtenez vos propres mesures, puis l'explication complète de ce qui vient de se passer et des raisons pour
  lesquelles ce résultat a compté dans l'histoire de la discipline.</p>

  <div class="lab-grid">{cards}</div>

  <div class="warn-box">
    <strong>Ce que ces mesures valent — et ne valent pas.</strong> Un navigateur n'est pas un dispositif de
    chronométrie : votre écran, votre souris et le moteur de rendu ajoutent leur propre latence, de l'ordre de
    plusieurs dizaines de millisecondes. Et surtout, un essai unique sur une seule personne n'est pas une
    expérience : c'est une démonstration. Comparez vos conditions entre elles plutôt que vos valeurs absolues à
    des normes, et voyez plutôt ces protocoles comme une façon de comprendre de l'intérieur ce que mesurent
    réellement les études.
  </div>

  <div class="note-box">
    <strong>Pour en tirer le maximum.</strong> Faites l'expérience <em>avant</em> de lire l'explication, et
    notez votre prédiction. Se tromper en ayant prédit produit un apprentissage bien plus solide que lire la
    bonne réponse d'emblée — c'est l'effet de génération, l'un des résultats les mieux établis de la psychologie
    de l'apprentissage.
  </div>

  <div class="cta-row">
    <a class="btn btn-primary" href="methodes.html">🔬 Comprendre la méthode expérimentale</a>
    <a class="btn btn-secondary" href="references/experiences.html">🧫 Les expériences célèbres</a>
  </div>
</div>
"""
    _write("laboratoire.html", page_shell(
        "Laboratoire", body, depth=0, active="Laboratoire",
        description=f"{len(EXPERIENCES_LAB)} expériences de psychologie à faire soi-même en ligne : effet Stroop, empan mnésique, temps de réaction, illusion de Müller-Lyer, position sérielle, flanker, ancrage."))


def render_laboratoire_pages():
    for lid, titre, icone, couleur, duree, accroche, consigne, explication, liens in EXPERIENCES_LAB:
        liens_html = "".join(f'<a class="pill-link" href="{href}">{label}</a>' for label, href in liens)

        header = page_header(
            depth=1,
            breadcrumb=[("Accueil", "../../../index.html"), ("Laboratoire", "../laboratoire.html"), (titre, None)],
            icon=icone, color=couleur, title=titre, subtitle=accroche,
            chips=[f"⏱ {duree}", "🧪 Expérience jouable", "📊 Résultat personnel"],
        )

        body = f"""{header}
<div class="section" style="max-width:820px;margin:0 auto">
  <div class="note-box" style="margin-top:0">{consigne}</div>

  <div class="lab-stage" data-lab="{lid}"></div>

  <div class="lab-explain" id="lab-result" style="display:none"></div>

  <details style="margin-top:1.6rem">
    <summary style="cursor:pointer;font-weight:600;font-size:0.95rem;padding:0.6rem 0">
      📖 L'explication scientifique (à lire après avoir joué)
    </summary>
    <div class="lab-explain" style="margin-top:0.6rem">{explication}</div>
  </details>

  <div class="pill-row" style="margin-top:1.6rem">{liens_html}</div>

  <div class="cta-row">
    <a class="btn btn-secondary" href="../laboratoire.html">← Toutes les expériences</a>
    <a class="btn btn-secondary" href="../methodes.html">🔬 Méthodes et statistiques</a>
  </div>
</div>
"""
        _write(f"laboratoire/{lid}.html", page_shell(
            titre, body, depth=1, active="Laboratoire",
            description=f"{titre} : {accroche} Expérience de psychologie jouable en ligne, avec résultats personnels et explication complète.",
            extra_scripts='<script src="../../../assets-ebook/js/laboratoire.js"></script>'))


# --------------------------------------------------------------------------
# Révision espacée
# --------------------------------------------------------------------------

def _collect_cards():
    """Rassemble toutes les cartes révisables du site."""
    cards = []

    for cat in CATEGORIES:
        for question, answer in cat.get("flashcards", []):
            cards.append({
                "id": "fc-" + slugify(cat["id"] + "-" + question)[:48],
                "q": question,
                "a": strip_html(answer),
                "c": cat["title"],
                "p": "categories/" + cat["id"] + ".html",
                "t": "Flashcard",
            })

    for term, definition, cat_id in DICTIONNAIRE:
        cards.append({
            "id": "df-" + slugify(term),
            "q": f"Que signifie « {term} » ?",
            "a": strip_html(definition),
            "c": "Dictionnaire",
            "p": "dictionnaire.html#def-" + slugify(term),
            "t": "Définition",
        })

    for eid, titre, chercheur, annee, _cat, resume, _pr, resultat, _po, _cr in EXPERIENCES:
        cards.append({
            "id": "ex-" + eid,
            "q": f"Expérience : « {titre} » — qui, quand, et qu'a-t-elle montré ?",
            "a": f"{chercheur}, {annee}. {strip_html(resultat)}",
            "c": "Expériences",
            "p": "references/experiences.html#" + eid,
            "t": "Expérience",
        })

    for bid, nom, famille, definition, _ex, parade in BIAIS:
        cards.append({
            "id": "bi-" + bid,
            "q": f"Biais : qu'est-ce que « {nom} » ?",
            "a": f"{strip_html(definition)} <em>Parade :</em> {strip_html(parade)}",
            "c": "Biais cognitifs",
            "p": "references/biais.html#" + bid,
            "t": "Biais",
        })

    for tid, nom, auteur, annee, domaine, idee, _me, _ap, _li in THEORIES:
        cards.append({
            "id": "th-" + tid,
            "q": f"Théorie : « {nom} » — de qui, et quelle idée centrale ?",
            "a": f"{auteur}, {annee} ({domaine}). {strip_html(idee)}",
            "c": "Théories",
            "p": "references/theories.html#" + tid,
            "t": "Théorie",
        })

    for aid, nom, dates, _pays, courant, apport, _bio, _cit, _oeuv in AUTEURS:
        cards.append({
            "id": "au-" + aid,
            "q": f"Auteur : quel est l'apport de {nom} ?",
            "a": f"{dates}, {courant}. {strip_html(apport)}",
            "c": "Auteurs",
            "p": "references/auteurs.html#" + aid,
            "t": "Auteur",
        })

    for nid, nom, famille, definition, _ex, _pi in METHODES_NOTIONS:
        cards.append({
            "id": "me-" + nid,
            "q": f"Méthode : que signifie « {nom} » ?",
            "a": strip_html(definition),
            "c": "Méthodes",
            "p": "methodes.html#notions",
            "t": "Méthode",
        })

    for en, fr, domaine, _note in LEXIQUE_EN:
        cards.append({
            "id": "en-" + slugify(en),
            "q": f"Traduire « {en} » en psychologie",
            "a": f"{fr} ({domaine})",
            "c": "Anglais",
            "p": "lexique.html",
            "t": "Anglais",
        })

    return cards


def render_revision():
    cards = _collect_cards()
    path = os.path.join(BASE, "revision-cards.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cards, f, ensure_ascii=False, separators=(",", ":"))
    size_kb = os.path.getsize(path) / 1024

    paquets = sorted(set(c["c"] for c in cards))
    options = "".join(f'<option value="{p}">{p}</option>' for p in paquets)

    header = page_header(
        depth=0, breadcrumb=[("Accueil", "../../index.html"), ("Révision espacée", None)],
        icon="🔁", color="or",
        title="Révision espacée",
        subtitle=f"{len(cards)} cartes, replanifiées automatiquement selon ce que vous savez déjà",
        chips=[f"🗂️ {len(cards)} cartes", f"📦 {len(paquets)} paquets", "🧠 Algorithme d'espacement"],
    )

    body = f"""{header}
<div class="section" style="max-width:820px;margin:0 auto">
  <p class="section-desc">Ce module applique les deux techniques les mieux établies de la psychologie de
  l'apprentissage : la <strong>récupération active</strong> (vous répondez avant de voir la réponse) et
  l'<strong>espacement</strong> (l'intervalle avant la prochaine présentation s'allonge à chaque succès et se
  réinitialise à chaque oubli). C'est le principe des logiciels de répétition espacée, appliqué à l'ensemble du
  contenu du site.</p>

  <div class="rev-stats">
    <div class="rev-stat due"><div class="n" id="rev-n-due">—</div><div class="l">À réviser</div></div>
    <div class="rev-stat new"><div class="n" id="rev-n-new">—</div><div class="l">Nouvelles</div></div>
    <div class="rev-stat ok"><div class="n" id="rev-n-known">—</div><div class="l">Acquises</div></div>
    <div class="rev-stat"><div class="n" id="rev-n-total">—</div><div class="l">Total</div></div>
  </div>

  <div class="ref-toolbar" style="position:static">
    <select id="rev-deck" aria-label="Choisir un paquet"
            style="flex:1;padding:0.55rem 0.8rem;border:1px solid var(--border);border-radius:10px;
                   font-family:var(--sans);font-size:0.86rem;background:var(--card);color:var(--noir)">
      <option value="all">Tous les paquets</option>
      {options}
    </select>
    <button class="print-btn" id="rev-reset">Réinitialiser</button>
  </div>

  <div class="rev-shell" id="rev-shell">
    <p class="lab-prompt">Chargement des cartes…</p>
  </div>

  <div class="note-box">
    <strong>Comment fonctionne l'espacement ici.</strong> Chaque carte porte un intervalle et un facteur de
    facilité, inspirés de l'algorithme SM-2. « Je ne savais pas » remet l'intervalle à un jour ; « hésitant »
    l'allonge modérément ; « facile » le multiplie. Les cartes bien sues reviennent donc de plus en plus
    rarement, et le temps se concentre sur celles qui résistent. Votre progression est stockée uniquement dans
    ce navigateur : rien n'est envoyé nulle part, et effacer les données du site remet tout à zéro.
  </div>

  <div class="tip-inline">
    <strong>Le bon réflexe :</strong> formulez votre réponse à voix haute ou par écrit <em>avant</em> de
    retourner la carte. Se contenter de penser « oui, je sais » suffit à produire l'illusion de maîtrise que
    cette méthode sert justement à dissiper.
  </div>

  <div class="cta-row">
    <a class="btn btn-primary" href="quiz/index.html">🎮 Passer un quiz noté</a>
    <a class="btn btn-secondary" href="fiches/index.html">🗂️ Fiches de révision imprimables</a>
    <a class="btn btn-secondary" href="apprendre.html">🎓 Méthodes d'apprentissage</a>
  </div>
</div>
"""
    _write("revision.html", page_shell(
        "Révision espacée", body, depth=0, active="Révision",
        description=f"Révision espacée de {len(cards)} cartes de psychologie : flashcards, définitions, expériences, biais, théories et vocabulaire anglais.",
        extra_scripts='<script src="../../assets-ebook/js/revision.js"></script>'))

    return len(cards), size_kb


# --------------------------------------------------------------------------
# Fiches de révision imprimables
# --------------------------------------------------------------------------

def _first_sentences(html, count=2):
    txt = strip_html(html)
    parts = re.split(r"(?<=[.!?])\s+", txt)
    return " ".join(parts[:count])


def render_fiches():
    index_cards = ""
    for i, cat in enumerate(CATEGORIES):
        n_sections = len(cat["sections"])
        n_flash = len(cat.get("flashcards", []))
        index_cards += f"""<a class="cat-card" href="{cat['id']}.html">
          <div class="cat-card-icon" style="background:var(--{cat['color']}-light)">{cat['icon']}</div>
          <h3>{cat['title']}</h3>
          <p>{n_sections} chapitres · {n_flash} points de rappel</p>
        </a>"""

    header = page_header(
        depth=1, breadcrumb=[("Accueil", "../../../index.html"), ("Fiches de révision", None)],
        icon="🗂️", color="vert",
        title="Fiches de révision",
        subtitle=f"{len(CATEGORIES)} fiches condensées, conçues pour être imprimées ou relues juste avant une évaluation",
        chips=[f"🗂️ {len(CATEGORIES)} fiches", "🖨️ Optimisées pour l'impression", "⚡ 5 minutes chacune"],
    )

    body = f"""{header}
<div class="section">
  <p class="section-desc" style="max-width:760px">Chaque fiche tient sur une page : les objectifs du domaine,
  l'essentiel de chaque chapitre en deux phrases, les chiffres clés, les notions à connaître et les questions de
  rappel. Utilisez-les en <strong>dernière relecture</strong>, pas comme support principal : une fiche est un
  aide-mémoire, elle ne remplace pas la compréhension construite en lisant la catégorie complète.</p>

  <div class="tip-inline">
    <strong>Meilleure façon de s'en servir :</strong> masquez la colonne de droite, essayez de reconstituer le
    contenu de mémoire, puis vérifiez. Relire une fiche passivement donne l'impression de savoir sans produire
    de mémoire durable.
  </div>

  <div class="cta-row" style="margin-bottom:1.5rem">
    <a class="btn btn-primary" href="tout.html">🖨️ Fiche complète : les 26 domaines</a>
    <a class="btn btn-secondary" href="../revision.html">🔁 Réviser en cartes espacées</a>
  </div>

  <div class="cat-grid">{index_cards}</div>
</div>
"""
    _write("fiches/index.html", page_shell(
        "Fiches de révision", body, depth=1, active="Apprendre",
        description=f"{len(CATEGORIES)} fiches de révision de psychologie à imprimer : l'essentiel de chaque domaine sur une page."))

    for cat in CATEGORIES:
        _write(f"fiches/{cat['id']}.html", _fiche_page(cat))

    _write("fiches/tout.html", _fiche_tout())


def _fiche_body(cat, level=2):
    tag = f"h{level}"
    objectifs = "".join(f"<li>{o}</li>" for o in cat["objectives"])

    essentiel = "".join(
        f"<li><b>{titre}</b> — {_first_sentences(corps)}</li>"
        for titre, corps in cat["sections"]
    )

    chiffres = ""
    if cat.get("chiffres"):
        cells = "".join(
            f'<div class="fiche-def"><b>{val}</b> — {lbl}</div>'
            for val, lbl in cat["chiffres"]
        )
        chiffres = f'<div class="fiche-block"><h4>Chiffres clés</h4><div class="fiche-defs">{cells}</div></div>'

    mythes = ""
    if cat.get("mythes"):
        items = "".join(f"<li><b>Faux :</b> {faux} → <em>{vrai}</em></li>" for faux, vrai in cat["mythes"])
        mythes = f'<div class="fiche-block"><h4>Idées reçues à corriger</h4><ul>{items}</ul></div>'

    rappel = ""
    if cat.get("flashcards"):
        items = "".join(
            f'<div class="fiche-def"><b>{q}</b><br>{strip_html(a)}</div>'
            for q, a in cat["flashcards"]
        )
        rappel = f'<div class="fiche-block"><h4>Questions de rappel</h4><div class="fiche-defs">{items}</div></div>'

    termes = [t for t in DICTIONNAIRE if t[2] == cat["id"]][:14]
    lexique = ""
    if termes:
        items = "".join(f'<div class="fiche-def"><b>{t}</b> — {strip_html(d)}</div>' for t, d, _c in termes)
        lexique = f'<div class="fiche-block"><h4>Vocabulaire</h4><div class="fiche-defs">{items}</div></div>'

    return f"""
<{tag}>{cat['icon']} {cat['title']}</{tag}>
<p style="color:var(--gris);font-size:0.88rem;margin-bottom:1.2rem">{cat['subtitle']}</p>
<div class="fiche-block"><h4>Objectifs</h4><ul>{objectifs}</ul></div>
<div class="fiche-block"><h4>L'essentiel, chapitre par chapitre</h4><ul>{essentiel}</ul></div>
{chiffres}
{mythes}
{lexique}
{rappel}
"""


def _fiche_page(cat):
    quiz_id = QUIZ_FOR_CATEGORY.get(cat["id"], "examen-final")

    header = page_header(
        depth=1,
        breadcrumb=[("Accueil", "../../../index.html"), ("Fiches", "index.html"), (cat["title"], None)],
        icon="🗂️", color=cat["color"],
        title="Fiche de révision — " + cat["title"],
        subtitle="L'essentiel du domaine, condensé pour une relecture rapide ou une impression",
        chips=[f"📖 {len(cat['sections'])} chapitres", f"🔁 {len(cat.get('flashcards', []))} rappels", "🖨️ Imprimable"],
    )

    body = f"""{header}
<div class="section" style="max-width:900px;margin:0 auto">
  <div class="cta-row" style="margin-bottom:1.2rem">
    <button class="print-btn" onclick="window.print()">🖨️ Imprimer cette fiche</button>
    <a class="btn btn-secondary" href="../categories/{cat['id']}.html">📖 Lire la fiche complète</a>
    <a class="btn btn-secondary" href="../quiz/quiz.html?id={quiz_id}">🎮 Quiz du domaine</a>
  </div>

  <div class="fiche-sheet">{_fiche_body(cat)}</div>

  <div class="cta-row">
    <a class="btn btn-secondary" href="index.html">← Toutes les fiches</a>
    <a class="btn btn-secondary" href="../revision.html">🔁 Révision espacée</a>
  </div>
</div>
"""
    return page_shell(
        "Fiche — " + cat["title"], body, depth=1, active="Apprendre",
        description=f"Fiche de révision imprimable : {cat['title']}. Objectifs, essentiel des chapitres, chiffres clés, vocabulaire et questions de rappel.")


def _fiche_tout():
    sheets = "".join(
        f'<div class="fiche-sheet" id="{cat["id"]}">{_fiche_body(cat)}</div>' for cat in CATEGORIES
    )
    sommaire = "".join(
        f'<a class="pill-link" href="#{cat["id"]}">{cat["icon"]} {cat["title"]}</a>' for cat in CATEGORIES
    )

    header = page_header(
        depth=1,
        breadcrumb=[("Accueil", "../../../index.html"), ("Fiches", "index.html"), ("Tout le programme", None)],
        icon="📚", color="or",
        title="Fiche complète — les 26 domaines",
        subtitle="L'intégralité du programme condensée en un seul document, prêt à imprimer",
        chips=[f"📚 {len(CATEGORIES)} domaines", "🖨️ Un seul document", "⚡ Relecture finale"],
    )

    body = f"""{header}
<div class="section" style="max-width:900px;margin:0 auto">
  <div class="cta-row" style="margin-bottom:1rem">
    <button class="print-btn" onclick="window.print()">🖨️ Imprimer tout le programme</button>
    <a class="btn btn-secondary" href="index.html">← Fiches par domaine</a>
  </div>
  <div class="warn-box">
    <strong>Document long.</strong> Cette page rassemble les 26 fiches : l'impression représente plusieurs
    dizaines de pages. Pour une révision ciblée, préférez la fiche du domaine concerné.
  </div>
  <div class="pill-row">{sommaire}</div>
  {sheets}
</div>
"""
    return page_shell(
        "Fiche complète du programme", body, depth=1, active="Apprendre",
        description="L'intégralité du programme de psychologie en fiches de révision imprimables : 26 domaines condensés.")


# --------------------------------------------------------------------------
# Plan du site et index A-Z
# --------------------------------------------------------------------------

def _az_entries():
    """Toutes les entrées indexables du site, pour l'index alphabétique."""
    entries = []

    for cat in CATEGORIES:
        entries.append((cat["title"], "categories/" + cat["id"] + ".html", "Catégorie"))
    for term, _d, _c in DICTIONNAIRE:
        entries.append((term, "dictionnaire.html#def-" + slugify(term), "Notion"))
    for eid, titre, *_ in EXPERIENCES:
        entries.append((titre, "references/experiences.html#" + eid, "Expérience"))
    for aid, nom, *_ in AUTEURS:
        entries.append((nom, "references/auteurs.html#" + aid, "Auteur"))
    for tid, nom, *_ in TROUBLES:
        entries.append((nom, "references/troubles.html#" + tid, "Trouble"))
    for bid, nom, *_ in BIAIS:
        entries.append((nom, "references/biais.html#" + bid, "Biais"))
    for tid, nom, *_ in TESTS:
        entries.append((nom, "references/tests.html#" + tid, "Test"))
    for tid, nom, *_ in THEORIES:
        entries.append((nom, "references/theories.html#" + tid, "Théorie"))
    for cid, nom, *_ in CAS:
        entries.append((nom, "references/cas.html#" + cid, "Cas"))
    for did, titre, *_ in DEBATS:
        entries.append((titre, "references/debats.html#" + did, "Débat"))
    for cid, nom, *_ in COURANTS:
        entries.append((nom, "references/courants.html#" + cid, "Courant"))
    for mid, affirmation, *_ in MYTHES:
        entries.append((affirmation.strip("«» "), "references/mythes.html#" + mid, "Idée reçue"))
    for fid, question, *_ in FAQ:
        entries.append((question, "faq.html#" + fid, "Question"))
    for pid, titre, *_ in PRATIQUES:
        entries.append((titre, "pratique.html#" + pid, "Fiche pratique"))
    for mid, nom, *_ in METIERS:
        entries.append((nom, "metiers.html#" + mid, "Métier"))
    for book in BOOKS:
        entries.append((book["title"], "bibliotheque.html", "Ouvrage"))

    seen = set()
    unique = []
    for label, href, kind in entries:
        key = (label.lower(), kind)
        if key in seen:
            continue
        seen.add(key)
        unique.append((label, href, kind))
    return sorted(unique, key=lambda e: _sort_key(e[0]))


def _sort_key(text):
    txt = unicodedata.normalize("NFD", text.lower())
    return "".join(c for c in txt if unicodedata.category(c) != "Mn")


def render_plan():
    entries = _az_entries()

    lettres = {}
    for label, href, kind in entries:
        first = _sort_key(label)[:1].upper()
        if not first.isalpha():
            first = "#"
        lettres.setdefault(first, []).append((label, href, kind))

    az_html = ""
    nav_lettres = ""
    for letter in sorted(lettres):
        nav_lettres += f'<a class="pill-link" href="#lettre-{letter}">{letter}</a>'
        items = "".join(
            f'<a href="{href}">{label} <span class="lex-dom">{kind}</span></a>'
            for label, href, kind in lettres[letter]
        )
        az_html += f'<div class="az-letter" id="lettre-{letter}">{letter}</div>{items}'

    colonnes = [
        ("Parcourir le contenu", [
            ("Toutes les catégories", "index.html"),
            ("Dictionnaire A-Z", "dictionnaire.html"),
            ("Méthodes et statistiques", "methodes.html"),
            ("Psychologie pratique", "pratique.html"),
            ("Lexique anglais-français", "lexique.html"),
            ("Métiers et études", "metiers.html"),
            ("Questions fréquentes", "faq.html"),
            ("Aide et ressources", "aide.html"),
            ("Communauté Discord", DISCORD_INVITE),
            ("Rappels et planches", "rappels.html"),
            ("Zone de découverte", "decouverte.html"),
        ]),
        ("Base de références", [
            ("Hub des références", "references/index.html"),
            ("Expériences célèbres", "references/experiences.html"),
            ("Grandes figures", "references/auteurs.html"),
            ("Théories et modèles", "references/theories.html"),
            ("Cas cliniques", "references/cas.html"),
            ("Débats et controverses", "references/debats.html"),
            ("Les grands courants", "references/courants.html"),
            ("Idées reçues et neuromythes", "references/mythes.html"),
            ("Répertoire des troubles", "references/troubles.html"),
            ("Biais cognitifs", "references/biais.html"),
            ("Tests et instruments", "references/tests.html"),
            ("Chronologie", "references/chronologie.html"),
        ]),
        ("S'entraîner", [
            ("Tous les quiz", "quiz/index.html"),
            ("Révision espacée", "revision.html"),
            ("Fiches de révision", "fiches/index.html"),
            ("Fiche complète du programme", "fiches/tout.html"),
            ("Laboratoire d'expériences", "laboratoire.html"),
            ("Auto-évaluations", "auto-evaluations.html"),
            ("Parcours guidés", "parcours.html"),
            ("Apprendre efficacement", "apprendre.html"),
            ("Emploi du temps & cours", "emploi-du-temps.html"),
            ("Cours & archives", "cours/index.html"),
            ("Compte étudiant", "compte.html"),
            ("Espace d'apprentissage", "espace.html"),
            ("Activer l'API SQLite", "api-compte.html"),
        ]),
        ("Lire les ouvrages", [
            ("Bibliothèque", "bibliotheque.html"),
            ("Lecteur intégré", "lecteur.html"),
            ("Crédits et sources", "credits.html"),
        ]),
    ]

    cols_html = "".join(
        f'<div class="plan-col"><h3>{titre}</h3>'
        + "".join(
            f'<a href="{href}"'
            + (' target="_blank" rel="noopener"' if href.startswith("http") else "")
            + f">{label}</a>"
            for label, href in liens
        )
        + "</div>"
        for titre, liens in colonnes
    )

    labo_links = "".join(
        f'<a class="pill-link" href="laboratoire/{lid}.html">{icone} {titre}</a>'
        for lid, titre, icone, *_ in EXPERIENCES_LAB
    )

    header = page_header(
        depth=0, breadcrumb=[("Accueil", "../../index.html"), ("Plan du site", None)],
        icon="🗺️", color="gris",
        title="Plan du site et index général",
        subtitle=f"Toutes les pages, et {len(entries)} entrées classées par ordre alphabétique",
        chips=[f"🔤 {len(entries)} entrées", f"🗂️ {len(lettres)} lettres", "🔍 Ctrl + K pour chercher"],
    )

    body = f"""{header}
<div class="section">
  <div class="plan-grid">{cols_html}</div>

  <div class="section-head" style="margin-top:2.5rem">
    <p class="section-eyebrow">{len(EXPERIENCES_LAB)} expériences</p>
    <h2 class="section-title" style="font-size:1.4rem">🧪 Le laboratoire</h2>
  </div>
  <div class="pill-row">{labo_links}</div>

  <div class="section-head" style="margin-top:2.5rem">
    <p class="section-eyebrow">{len(entries)} entrées</p>
    <h2 class="section-title" style="font-size:1.4rem">🔤 Index alphabétique général</h2>
    <p class="section-desc">Toutes les notions, expériences, auteurs, troubles, biais, tests, théories, cas,
    débats, fiches pratiques, métiers et ouvrages du site, dans un seul index.</p>
  </div>
  <div class="pill-row">{nav_lettres}</div>
  <div class="az-index">{az_html}</div>
</div>
"""
    _write("plan.html", page_shell(
        "Plan du site", body, depth=0, active="Plan",
        description=f"Plan du site Psyclopédia et index alphabétique de {len(entries)} entrées : notions, expériences, auteurs, troubles, biais, théories et ouvrages."))

    return len(entries)


def render_all():
    render_laboratoire_hub()
    render_laboratoire_pages()
    n_cards, size_kb = render_revision()
    render_fiches()
    n_index = render_plan()
    return n_cards, size_kb, n_index
