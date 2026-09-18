# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Pages v3 : théories, cas cliniques, débats, méthodes, lexique,
psychologie pratique et métiers.
"""

import os

from shell import page_shell, page_header, slugify, strip_html
from content import (
    THEORIES, CAS, DEBATS, METHODES_CHAPITRES, METHODES_NOTIONS,
    LEXIQUE_EN, FAUX_AMIS, PRATIQUES, METIERS, PARCOURS_ETUDES,
)

BASE = os.path.dirname(os.path.abspath(__file__))
REFS = os.path.join(BASE, "references")

COLORS = ["vert", "or", "rose", "gris"]


def _write(path, html):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)


def _toolbar(placeholder, familles, count, mot="fiches"):
    chips = '<button class="search-filter active" data-famille="all">Toutes</button>'
    chips += "".join(
        f'<button class="search-filter" data-famille="{f}">{f}</button>' for f in familles
    )
    return f"""
<div class="ref-toolbar" data-ref-filter>
  <input type="search" placeholder="{placeholder}" aria-label="Filtrer la liste">
  <span class="ref-count">{count} {mot}</span>
</div>
<div class="search-filters" data-ref-filter style="padding:0 0 1.2rem;border:none">{chips}</div>"""


def _crumb_ref(label):
    return [("Accueil", "../../../index.html"), ("Références", "index.html"), (label, None)]


def _crumb_root(label):
    return [("Accueil", "../../index.html"), ("Catégories", "index.html"), (label, None)]


# --------------------------------------------------------------------------
# Théories et modèles
# --------------------------------------------------------------------------

def render_theories():
    familles = sorted(set(t[4] for t in THEORIES))

    cards = ""
    for i, (tid, nom, auteur, annee, domaine, idee, mecanisme, application, limite) in enumerate(THEORIES, 1):
        color = COLORS[i % len(COLORS)]
        cards += f"""<div class="ref-card {color}" data-ref-id="{tid}" data-famille="{domaine}" data-search="{nom} {auteur} {annee} {strip_html(idee)}">
          <div class="ref-card-head">
            <span class="ref-n">{i:02d}</span>
            <div class="ref-h"><h3>{nom}</h3><p class="ref-sub">{auteur} · {annee} · {domaine}</p></div>
            <span class="ref-chev">▾</span>
          </div>
          <div class="ref-card-body">
            <div class="ref-field"><h5>L'idée en une phrase</h5><p>{idee}</p></div>
            <div class="ref-field"><h5>Comment ça marche</h5><p>{mecanisme}</p></div>
            <div class="ref-field"><h5>À quoi ça sert</h5><p>{application}</p></div>
            <div class="ref-field"><h5>Ce que la théorie n'explique pas</h5><p>{limite}</p></div>
            <div class="ref-tags"><span>{annee}</span><span>{auteur}</span><span>{domaine}</span></div>
          </div>
        </div>"""

    header = page_header(
        depth=1, breadcrumb=_crumb_ref("Théories"), icon="🧩", color="vert",
        title="Les grandes théories de la psychologie",
        subtitle=f"{len(THEORIES)} modèles expliqués : l'idée, le mécanisme, les usages et les limites",
        chips=[f"🧩 {len(THEORIES)} théories", f"🗂️ {len(familles)} domaines", "⚖️ Limites systématiques"],
    )

    body = f"""{header}
<div class="section">
  <p class="section-desc" style="max-width:760px">Une théorie n'est pas une vérité : c'est un outil qui rend
  certains phénomènes prévisibles et en laisse d'autres dans l'ombre. Les quatre rubriques de chaque fiche sont
  conçues pour qu'on puisse la <em>manipuler</em> et non seulement la réciter : ce qu'elle affirme, par quel
  mécanisme, dans quels cas elle sert, et où elle cesse de fonctionner.</p>
  {_toolbar("Filtrer par nom de théorie, auteur, domaine…", familles, len(THEORIES), "théories")}
  {cards}

  <div class="note-box">
    <strong>Comment retenir une théorie.</strong> Essayez de l'appliquer à une situation que vous avez vécue
    cette semaine, puis cherchez délibérément une situation où elle échoue. Une théorie qu'on ne sait pas mettre
    en défaut n'est pas comprise — elle est seulement mémorisée.
  </div>
</div>
"""
    _write("references/theories.html", page_shell(
        "Théories et modèles", body, depth=1, active="Références",
        description=f"{len(THEORIES)} grandes théories de la psychologie expliquées en français : idée, mécanisme, applications et limites."))


# --------------------------------------------------------------------------
# Cas cliniques
# --------------------------------------------------------------------------

def render_cas():
    familles = sorted(set(c[3] for c in CAS))

    cards = ""
    for i, (cid, nom, periode, domaine, resume, histoire, apport, aujourdhui) in enumerate(CAS, 1):
        color = COLORS[i % len(COLORS)]
        cards += f"""<div class="ref-card {color}" data-ref-id="{cid}" data-famille="{domaine}" data-search="{nom} {periode} {domaine} {strip_html(resume)}">
          <div class="ref-card-head">
            <span class="ref-n">{i:02d}</span>
            <div class="ref-h"><h3>{nom}</h3><p class="ref-sub">{periode} · {domaine}</p></div>
            <span class="ref-chev">▾</span>
          </div>
          <div class="ref-card-body">
            <div class="ref-field"><h5>En une phrase</h5><p>{resume}</p></div>
            <div class="ref-field"><h5>L'histoire</h5><p>{histoire}</p></div>
            <div class="ref-field"><h5>Ce que ce cas a apporté</h5><p>{apport}</p></div>
            <div class="ref-field"><h5>Ce qu'on en dit aujourd'hui</h5><p>{aujourdhui}</p></div>
            <div class="ref-tags"><span>{periode}</span><span>{domaine}</span></div>
          </div>
        </div>"""

    header = page_header(
        depth=1, breadcrumb=_crumb_ref("Cas cliniques"), icon="🗃️", color="rose",
        title="Les cas qui ont fait la psychologie",
        subtitle=f"{len(CAS)} histoires singulières devenues des connaissances générales",
        chips=[f"🗃️ {len(CAS)} cas", f"🗂️ {len(familles)} domaines", "👤 Des personnes, pas des objets"],
    )

    body = f"""{header}
<div class="section">
  <p class="section-desc" style="max-width:760px">Une grande partie de ce que nous savons sur la mémoire, le
  langage ou les émotions vient de quelques dizaines de personnes dont la vie a basculé. Ces cas uniques ne
  prouvent rien statistiquement, mais ils démontrent ce qui est <em>possible</em> — et c'est souvent ce qui
  renverse une théorie.</p>

  <div class="warn-box">
    <strong>Une remarque avant de lire.</strong> Ces fiches parlent de personnes réelles, dont beaucoup n'ont
    jamais consenti à devenir célèbres, et dont plusieurs ont été traitées d'une façon aujourd'hui inacceptable.
    L'histoire de la psychologie est aussi celle de ces dettes. Les fiches mentionnent donc systématiquement ce
    que la recherche doit à ces personnes — et ce qu'elle leur a coûté.
  </div>

  {_toolbar("Filtrer par nom, époque, domaine…", familles, len(CAS), "cas")}
  {cards}
</div>
"""
    _write("references/cas.html", page_shell(
        "Cas cliniques célèbres", body, depth=1, active="Références",
        description=f"{len(CAS)} cas cliniques célèbres de psychologie et de neuropsychologie expliqués en français."))


# --------------------------------------------------------------------------
# Débats
# --------------------------------------------------------------------------

def render_debats():
    familles = sorted(set(d[2] for d in DEBATS))

    cards = ""
    for i, (did, titre, famille, question, pa_t, pa, pb_t, pb, etat) in enumerate(DEBATS, 1):
        cards += f"""<div class="debat-card" id="{did}" data-ref-id="{did}" data-famille="{famille}" data-search="{titre} {famille} {strip_html(question)}">
          <div class="debat-head">
            <h3>{i:02d}. {titre}</h3>
            <p class="debat-question">{question}</p>
          </div>
          <div class="debat-cols">
            <div class="debat-col">
              <p class="debat-side">Une position</p>
              <h4>{pa_t}</h4>
              <p>{pa}</p>
            </div>
            <div class="debat-col">
              <p class="debat-side">La position adverse</p>
              <h4>{pb_t}</h4>
              <p>{pb}</p>
            </div>
          </div>
          <div class="debat-etat">
            <p class="debat-side">⚖️ Où en est-on réellement ?</p>
            <p>{etat}</p>
          </div>
        </div>"""

    header = page_header(
        depth=1, breadcrumb=_crumb_ref("Débats"), icon="⚖️", color="or",
        title="Les grands débats de la psychologie",
        subtitle=f"{len(DEBATS)} controverses présentées de façon contradictoire, puis arbitrées par les données",
        chips=[f"⚖️ {len(DEBATS)} débats", f"🗂️ {len(familles)} domaines", "🔀 Les deux camps au meilleur"],
    )

    body = f"""{header}
<div class="section">
  <p class="section-desc" style="max-width:760px">Une discipline vivante se reconnaît à ses désaccords. Chaque
  dossier présente les deux positions dans leur version la plus solide — pas une caricature qu'il serait facile
  de réfuter — puis fait le point sur ce que les données permettent réellement de conclure. Dans plusieurs cas,
  la réponse honnête reste : « on ne sait pas encore ».</p>

  <div class="note-box">
    <strong>Exercice.</strong> Avant de lire l'arbitrage, choisissez votre camp, puis relisez l'argument
    adverse en cherchant sincèrement ce qu'il a de juste. C'est l'entraînement le plus efficace contre le biais
    de confirmation, et l'un des rares qui fonctionne encore quand on connaît le biais.
  </div>

  {_toolbar("Filtrer par sujet, domaine…", familles, len(DEBATS), "débats")}
  {cards}
</div>
"""
    _write("references/debats.html", page_shell(
        "Débats et controverses", body, depth=1, active="Références",
        description=f"{len(DEBATS)} grands débats de la psychologie présentés de façon contradictoire, avec l'état actuel des connaissances."))


# --------------------------------------------------------------------------
# Méthodes et statistiques
# --------------------------------------------------------------------------

def render_methodes():
    toc = "".join(f'<a href="#{anc}">{titre}</a>' for anc, titre, _ in METHODES_CHAPITRES)
    toc += '<a href="#notions">Fiches de référence</a>'

    chapitres = ""
    for anc, titre, html in METHODES_CHAPITRES:
        chapitres += f'\n<h2 id="{anc}">{titre}</h2>\n{html}'

    familles = sorted(set(n[2] for n in METHODES_NOTIONS))
    notions = ""
    for i, (nid, nom, famille, definition, exemple, piege) in enumerate(METHODES_NOTIONS, 1):
        color = COLORS[i % len(COLORS)]
        notions += f"""<div class="ref-card {color}" data-ref-id="{nid}" data-famille="{famille}" data-search="{nom} {famille} {strip_html(definition)}">
          <div class="ref-card-head">
            <span class="ref-n">{i:02d}</span>
            <div class="ref-h"><h3>{nom}</h3><p class="ref-sub">{famille}</p></div>
            <span class="ref-chev">▾</span>
          </div>
          <div class="ref-card-body">
            <div class="ref-field"><h5>Définition</h5><p>{definition}</p></div>
            <div class="ref-field"><h5>Exemple</h5><p>{exemple}</p></div>
            <div class="ref-field"><h5>Le piège</h5><p>{piege}</p></div>
            <div class="ref-tags"><span>{famille}</span></div>
          </div>
        </div>"""

    header = page_header(
        depth=0, breadcrumb=[("Accueil", "../../index.html"), ("Méthodes", None)],
        icon="🔬", color="vert",
        title="Méthodes, statistiques et esprit critique",
        subtitle="Le cours qui permet de lire n'importe quelle étude — et de repérer ce qui cloche",
        chips=[f"📖 {len(METHODES_CHAPITRES)} chapitres", f"🗂️ {len(METHODES_NOTIONS)} notions", "🧪 Applicable partout"],
    )

    body = f"""{header}
<div class="wrap with-toc">
  <aside class="toc-side"><h4>Sommaire</h4>{toc}</aside>
  <div class="content" style="max-width:none">
    <p>C'est le chapitre le plus utile du site, et de loin celui qui se transfère le mieux hors de la
    psychologie. Savoir lire une étude protège contre les titres trompeurs, les vendeurs de méthodes miracle
    et — plus difficile — contre ses propres certitudes.</p>
    {chapitres}

    <h2 id="notions">Fiches de référence</h2>
    <p>Les {len(METHODES_NOTIONS)} notions ci-dessous se consultent à la demande. Chacune donne la définition,
    un exemple concret et le piège classique associé.</p>
    {_toolbar("Filtrer par notion, famille…", familles, len(METHODES_NOTIONS), "notions")}
    {notions}

    <div class="cta-row">
      <a class="btn btn-primary" href="references/debats.html">⚖️ Voir les débats en cours</a>
      <a class="btn btn-secondary" href="references/biais.html">🌀 Les biais de raisonnement</a>
      <a class="btn btn-secondary" href="categories/01-fondamentaux.html">📘 Fiche Fondamentaux</a>
    </div>
  </div>
</div>
"""
    _write("methodes.html", page_shell(
        "Méthodes et statistiques", body, depth=0, active="Méthodes",
        description="Cours complet de méthodologie et de statistiques en psychologie : plans de recherche, valeur p, taille d'effet, réplication, éthique et lecture critique d'un article."))


# --------------------------------------------------------------------------
# Lexique bilingue
# --------------------------------------------------------------------------

def render_lexique():
    familles = sorted(set(t[2] for t in LEXIQUE_EN))

    rows = ""
    for en, fr, domaine, note in LEXIQUE_EN:
        rows += f"""<tr data-ref-id="lex-{slugify(en)}" data-famille="{domaine}" data-search="{en} {fr} {domaine} {strip_html(note)}">
          <td class="lex-en">{en}</td>
          <td class="lex-fr">{fr}</td>
          <td class="col-dom"><span class="lex-dom">{domaine}</span></td>
          <td class="lex-note">{note}</td>
        </tr>"""

    faux_amis = "".join(
        f'<div class="ref-field"><h5>{mot}</h5><p><strong>{trad}</strong> — {note}</p></div>'
        for mot, trad, note in FAUX_AMIS
    )

    header = page_header(
        depth=0, breadcrumb=[("Accueil", "../../index.html"), ("Lexique anglais", None)],
        icon="🌍", color="or",
        title="Lexique anglais-français de la psychologie",
        subtitle=f"{len(LEXIQUE_EN)} termes traduits et commentés, {len(FAUX_AMIS)} faux amis signalés",
        chips=[f"🔤 {len(LEXIQUE_EN)} termes", f"⚠️ {len(FAUX_AMIS)} faux amis", "📚 Pour lire les articles"],
    )

    body = f"""{header}
<div class="section">
  <p class="section-desc" style="max-width:760px">La quasi-totalité de la recherche est publiée en anglais, et
  une traduction approximative suffit à créer un contresens durable. Ce lexique donne l'équivalent français
  usuel, signale les termes qu'on laisse habituellement en anglais, et met en garde sur les faux amis — qui
  sont ici particulièrement traîtres, puisque plusieurs d'entre eux sont des concepts techniques.</p>

  <div class="warn-box">
    <strong>Les trois faux amis les plus coûteux.</strong> <em>Reliability</em> ne veut pas dire fiabilité mais
    <strong>fidélité</strong> au sens psychométrique. <em>Evidence</em> ne veut pas dire évidence mais
    <strong>données probantes</strong>. <em>Distress</em> ne veut pas dire stress mais
    <strong>détresse</strong>. À eux seuls, ces trois mots expliquent une bonne part des contresens dans les
    traductions d'articles.
  </div>

  {_toolbar("Filtrer par terme anglais, français, domaine…", familles, len(LEXIQUE_EN), "termes")}

  <div class="lex-wrap">
    <table class="lex-table">
      <thead><tr><th>Anglais</th><th>Français</th><th class="col-dom">Domaine</th><th>Remarque</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>
  </div>

  <div class="section-head" style="margin-top:3rem">
    <p class="section-eyebrow">{len(FAUX_AMIS)} pièges</p>
    <h2 class="section-title" style="font-size:1.5rem">⚠️ Les faux amis à connaître par cœur</h2>
    <p class="section-desc">Ces mots ressemblent à un mot français et signifient autre chose. Dans un article
    scientifique, l'erreur ne se voit pas : la phrase reste grammaticalement correcte et devient fausse.</p>
  </div>
  <div class="ref-card vert open" style="cursor:default">
    <div class="ref-card-body" style="display:block;padding:1.3rem">{faux_amis}</div>
  </div>

  <div class="cta-row">
    <a class="btn btn-primary" href="dictionnaire.html">📖 Dictionnaire français</a>
    <a class="btn btn-secondary" href="methodes.html">🔬 Lire un article scientifique</a>
  </div>
</div>
"""
    _write("lexique.html", page_shell(
        "Lexique anglais-français", body, depth=0, active="Lexique",
        description=f"Lexique anglais-français de la psychologie : {len(LEXIQUE_EN)} termes traduits et {len(FAUX_AMIS)} faux amis expliqués."))


# --------------------------------------------------------------------------
# Psychologie pratique
# --------------------------------------------------------------------------

def render_pratique():
    familles = sorted(set(p[2] for p in PRATIQUES))

    cards = ""
    for i, (pid, titre, famille, situation, recherche, etapes, piege) in enumerate(PRATIQUES, 1):
        color = COLORS[i % len(COLORS)]
        etapes_html = "".join(f"<li>{e}</li>" for e in etapes)
        cards += f"""<div class="ref-card {color}" data-ref-id="{pid}" data-famille="{famille}" data-search="{titre} {famille} {strip_html(situation)}">
          <div class="ref-card-head">
            <span class="ref-n">{i:02d}</span>
            <div class="ref-h"><h3>{titre}</h3><p class="ref-sub">{famille}</p></div>
            <span class="ref-chev">▾</span>
          </div>
          <div class="ref-card-body">
            <div class="ref-field"><h5>La situation</h5><p>{situation}</p></div>
            <div class="ref-field"><h5>Ce que dit la recherche</h5><p>{recherche}</p></div>
            <div class="ref-field"><h5>Le protocole</h5><ol class="etapes">{etapes_html}</ol></div>
            <div class="piege-box"><strong>⚠️ Le piège classique :</strong> {piege}</div>
            <div class="ref-tags"><span>{famille}</span></div>
          </div>
        </div>"""

    header = page_header(
        depth=0, breadcrumb=[("Accueil", "../../index.html"), ("Psychologie pratique", None)],
        icon="🧰", color="vert",
        title="La psychologie appliquée au quotidien",
        subtitle=f"{len(PRATIQUES)} situations concrètes, ce que dit la recherche, et un protocole en étapes",
        chips=[f"🧰 {len(PRATIQUES)} fiches", f"🗂️ {len(familles)} domaines", "✅ Protocoles concrets"],
    )

    body = f"""{header}
<div class="section">
  <p class="section-desc" style="max-width:760px">Savoir n'est pas pouvoir faire. Ces fiches partent d'une
  situation reconnaissable, rappellent honnêtement ce que les données permettent d'affirmer — y compris quand
  l'effet est modeste — puis proposent des étapes exécutables dès aujourd'hui. Chaque fiche se termine par le
  piège dans lequel presque tout le monde tombe.</p>

  <div class="warn-box">
    <strong>Ce que ces fiches ne sont pas.</strong> Ni un traitement, ni un substitut à un accompagnement
    professionnel. Elles décrivent des leviers utiles pour des difficultés ordinaires. Si une difficulté dure,
    s'aggrave ou retentit sur votre vie quotidienne, parlez-en à un médecin ou à un psychologue. En cas de
    détresse aiguë en France : <strong>3114</strong> (prévention du suicide, gratuit, 24 h/24) ou le
    <strong>15</strong>.
  </div>

  {_toolbar("Filtrer par situation, domaine…", familles, len(PRATIQUES), "fiches")}
  {cards}

  <div class="cta-row">
    <a class="btn btn-primary" href="apprendre.html">🎓 Les méthodes d'apprentissage</a>
    <a class="btn btn-secondary" href="references/biais.html">🌀 Les biais à connaître</a>
    <a class="btn btn-secondary" href="references/troubles.html">🩺 Répertoire des troubles</a>
  </div>
</div>
"""
    _write("pratique.html", page_shell(
        "Psychologie pratique", body, depth=0, active="Pratique",
        description=f"{len(PRATIQUES)} fiches de psychologie appliquée au quotidien : sommeil, stress, apprentissage, relations, travail — avec protocoles concrets."))


# --------------------------------------------------------------------------
# Métiers et études
# --------------------------------------------------------------------------

def render_metiers():
    familles = sorted(set(m[2] for m in METIERS))

    cards = ""
    for i, (mid, nom, famille, mission, formation, quotidien, ou, savoir) in enumerate(METIERS, 1):
        color = COLORS[i % len(COLORS)]
        cards += f"""<div class="ref-card {color}" data-ref-id="{mid}" data-famille="{famille}" data-search="{nom} {famille} {strip_html(mission)}">
          <div class="ref-card-head">
            <span class="ref-n">{i:02d}</span>
            <div class="ref-h"><h3>{nom}</h3><p class="ref-sub">{famille}</p></div>
            <span class="ref-chev">▾</span>
          </div>
          <div class="ref-card-body">
            <div class="ref-field"><h5>La mission</h5><p>{mission}</p></div>
            <div class="ref-field"><h5>La formation</h5><p>{formation}</p></div>
            <div class="ref-field"><h5>Le quotidien</h5><p>{quotidien}</p></div>
            <div class="ref-field"><h5>Où exercer</h5><p>{ou}</p></div>
            <div class="piege-box"><strong>💡 Bon à savoir :</strong> {savoir}</div>
            <div class="ref-tags"><span>{famille}</span></div>
          </div>
        </div>"""

    etudes = ""
    for anc, titre, html in PARCOURS_ETUDES:
        etudes += f'\n<h2 id="{anc}">{titre}</h2>\n{html}'

    header = page_header(
        depth=0, breadcrumb=[("Accueil", "../../index.html"), ("Métiers et études", None)],
        icon="🎓", color="or",
        title="Métiers, études et titres en psychologie",
        subtitle=f"{len(METIERS)} métiers détaillés et le parcours réel des études, sans idéalisation",
        chips=[f"💼 {len(METIERS)} métiers", "🎓 Licence → master → titre", "⚠️ Titres protégés expliqués"],
    )

    body = f"""{header}
<div class="section">
  <p class="section-desc" style="max-width:760px">La psychologie attire beaucoup, et le parcours réel surprend
  souvent : beaucoup de statistiques, une sélection forte à l'entrée du master, et des métiers bien plus variés
  que la seule consultation en cabinet. Cette page décrit le cadre des titres, le contenu des études et vingt
  métiers accessibles — y compris ceux qui utilisent la psychologie sans relever du titre de psychologue.</p>

  {etudes}

  <div class="section-head" style="margin-top:3rem">
    <p class="section-eyebrow">{len(METIERS)} métiers</p>
    <h2 class="section-title" style="font-size:1.5rem">💼 Les métiers en détail</h2>
    <p class="section-desc">Mission, formation requise, quotidien réel, lieux d'exercice et point de vigilance.</p>
  </div>

  {_toolbar("Filtrer par métier, secteur…", familles, len(METIERS), "métiers")}
  {cards}

  <div class="note-box">
    <strong>Vérifier avant de s'engager.</strong> Les cadres légaux évoluent et diffèrent selon les pays. Pour
    la France, référez-vous aux sites officiels du ministère de l'Enseignement supérieur, de l'ONISEP et des
    organisations professionnelles de psychologues ; en Belgique, à la Commission des psychologues ; en Suisse,
    à la loi fédérale sur les professions de la psychologie ; au Québec, à l'Ordre des psychologues.
  </div>
</div>
"""
    _write("metiers.html", page_shell(
        "Métiers et études", body, depth=0, active="Métiers",
        description="Métiers et études de psychologie : 20 métiers détaillés, parcours licence-master, titres protégés et cadre déontologique."))


def render_all():
    render_theories()
    render_cas()
    render_debats()
    render_methodes()
    render_lexique()
    render_pratique()
    render_metiers()
