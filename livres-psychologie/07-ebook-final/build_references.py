# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Génération des pages de la base de références."""

import os

from shell import page_shell, page_header, slugify, strip_html
from content import (
    EXPERIENCES, AUTEURS, TROUBLES, BIAIS, TESTS,
    CHRONOLOGIE_TRIEE, PERIODES, periode_of, CATEGORY_TITLE,
)

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "references")

COLORS = ["vert", "or", "rose", "gris"]


def _toolbar(placeholder, familles, count):
    chips = '<button class="search-filter active" data-famille="all">Toutes</button>'
    chips += "".join(
        f'<button class="search-filter" data-famille="{f}">{f}</button>' for f in familles
    )
    return f"""
<div class="ref-toolbar" data-ref-filter>
  <input type="search" placeholder="{placeholder}" aria-label="Filtrer la liste">
  <span class="ref-count">{count} fiches</span>
</div>
<div class="search-filters" data-ref-filter style="padding:0 0 1.2rem;border:none">{chips}</div>"""


def _write(filename, html):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(html)


def _crumb(label):
    return [("Accueil", "../../../index.html"), ("Références", "index.html"), (label, None)]


# --------------------------------------------------------------------------
# Hub
# --------------------------------------------------------------------------

def render_hub():
    cards = [
        ("experiences.html", "🔬", "vert", "Expériences célèbres", len(EXPERIENCES),
         "Protocole, résultats, portée et critiques des études qui ont fait la psychologie."),
        ("auteurs.html", "👤", "or", "Grandes figures", len(AUTEURS),
         "Biographies, apports décisifs, citations et œuvres majeures des pionniers et des contemporains."),
        ("troubles.html", "🩺", "rose", "Répertoire des troubles", len(TROUBLES),
         "Signes, mécanismes et prises en charge validées, expliqués sans jargon et sans dramatisation."),
        ("biais.html", "🌀", "gris", "Biais et heuristiques", len(BIAIS),
         "Définition, exemple concret et parade pour chaque erreur systématique de raisonnement."),
        ("tests.html", "📊", "vert", "Tests et instruments", len(TESTS),
         "Ce que mesure chaque test, comment il se passe, comment l'interpréter et ses limites."),
        ("chronologie.html", "🗓️", "or", "Chronologie de la discipline", len(CHRONOLOGIE_TRIEE),
         "Des humeurs d'Hippocrate aux neurosciences computationnelles, en six grandes périodes."),
    ]
    grid = "".join(
        f'<a class="hub-card {color}" href="{href}"><span class="hub-ico">{ico}</span>'
        f"<h3>{title}</h3><p>{desc}</p><span class=\"hub-n\">{n} fiches</span></a>"
        for href, ico, color, title, n, desc in cards
    )
    total = sum(c[4] for c in cards)

    header = page_header(
        depth=1,
        breadcrumb=[("Accueil", "../../../index.html"), ("Références", None)],
        icon="🗂️", color="or", title="Base de références",
        subtitle="Tout ce qu'on cherche quand on étudie la psychologie, réuni et consultable en un endroit",
        chips=[f"📚 {total} fiches détaillées", "🔍 Filtrage instantané", "🔗 Liens vers les catégories"],
    )

    body = f"""{header}
<div class="section">
  <p class="section-desc" style="max-width:760px;margin-bottom:2rem">Cette base rassemble les connaissances
  factuelles de la discipline : les expériences qu'il faut connaître, les personnes qui les ont menées, les
  troubles rencontrés en clinique, les biais qui faussent nos jugements, les tests utilisés par les
  professionnels, et la chronologie qui relie le tout. Chaque fiche se déplie, se filtre et se partage
  par son lien direct.</p>
  <div class="hub-grid">{grid}</div>

  <div class="note-box" style="margin-top:2.5rem">
    <strong>Comment s'en servir ?</strong> Utilise la recherche globale (<kbd>Ctrl</kbd> + <kbd>K</kbd>) pour
    retrouver instantanément une notion où qu'elle se trouve. Sur chaque page, le champ de filtre restreint la
    liste en direct, et les onglets permettent de n'afficher qu'une famille. Les fiches se replient pour survoler
    l'ensemble, puis se déplient pour approfondir.
  </div>
</div>
"""
    _write("index.html", page_shell("Base de références", body, depth=1, active="Références",
                                    description="Base de références de psychologie : expériences célèbres, auteurs, troubles, biais cognitifs, tests et chronologie."))


# --------------------------------------------------------------------------
# Expériences
# --------------------------------------------------------------------------

def render_experiences():
    cats = sorted(set(e[4] for e in EXPERIENCES))
    familles = [CATEGORY_TITLE.get(c, c) for c in cats]

    cards = ""
    for i, (eid, titre, chercheur, annee, cat_id, resume, protocole, resultat, portee, critique) in enumerate(EXPERIENCES, 1):
        color = COLORS[i % len(COLORS)]
        fam = CATEGORY_TITLE.get(cat_id, cat_id)
        cards += f"""<div class="ref-card {color}" data-ref-id="{eid}" data-famille="{fam}" data-search="{titre} {chercheur} {annee} {strip_html(resume)}">
          <div class="ref-card-head">
            <span class="ref-n">{i:02d}</span>
            <div class="ref-h"><h3>{titre}</h3><p class="ref-sub">{chercheur} · {annee} · {fam}</p></div>
            <span class="ref-chev">▾</span>
          </div>
          <div class="ref-card-body">
            <div class="ref-field"><h5>En une phrase</h5><p>{resume}</p></div>
            <div class="ref-field"><h5>Protocole</h5><p>{protocole}</p></div>
            <div class="ref-field"><h5>Résultat</h5><p>{resultat}</p></div>
            <div class="ref-field"><h5>Pourquoi cela compte</h5><p>{portee}</p></div>
            <div class="ref-field"><h5>Limites et critiques</h5><p>{critique}</p></div>
            <div class="ref-tags"><span>{annee}</span><span>{chercheur}</span><span>{fam}</span></div>
            <a class="ref-link" href="../categories/{cat_id}.html">→ Lire la fiche « {fam} »</a>
          </div>
        </div>"""

    header = page_header(
        depth=1, breadcrumb=_crumb("Expériences"), icon="🔬", color="vert",
        title="Les expériences qui ont fait la psychologie",
        subtitle=f"{len(EXPERIENCES)} études fondatrices : protocole, résultats, portée et critiques",
        chips=[f"🔬 {len(EXPERIENCES)} expériences", f"📂 {len(cats)} domaines", "⚖️ Critiques incluses"],
    )

    body = f"""{header}
<div class="section">
  <p class="section-desc" style="max-width:760px">Une expérience ne se résume pas à son résultat : ce sont son
  protocole et ses limites qui disent ce qu'elle prouve vraiment. Chaque fiche présente donc les cinq mêmes
  rubriques, y compris les critiques méthodologiques et les échecs de réplication quand il y en a.</p>
  {_toolbar("Filtrer par titre, chercheur, année ou mot-clé…", familles, len(EXPERIENCES))}
  {cards}
</div>
"""
    _write("experiences.html", page_shell("Expériences célèbres", body, depth=1, active="Références",
                                          description=f"{len(EXPERIENCES)} expériences célèbres de psychologie expliquées en français : protocole, résultats, portée, critiques."))


# --------------------------------------------------------------------------
# Auteurs
# --------------------------------------------------------------------------

def render_auteurs():
    familles = sorted(set(a[4] for a in AUTEURS))

    cards = ""
    for i, (aid, nom, dates, pays, courant, apport, bio, citation, oeuvres) in enumerate(AUTEURS, 1):
        color = COLORS[i % len(COLORS)]
        citation_html = f'<div class="ref-quote">{citation}</div>' if citation else ""
        cards += f"""<div class="ref-card {color}" data-ref-id="{aid}" data-famille="{courant}" data-search="{nom} {pays} {courant} {strip_html(apport)}">
          <div class="ref-card-head">
            <span class="ref-n">{i:02d}</span>
            <div class="ref-h"><h3>{nom}</h3><p class="ref-sub">{dates} · {pays} · {courant}</p></div>
            <span class="ref-chev">▾</span>
          </div>
          <div class="ref-card-body">
            <div class="ref-field"><h5>Apport décisif</h5><p>{apport}</p></div>
            <div class="ref-field"><h5>Parcours et idées</h5><p>{bio}</p></div>
            <div class="ref-field"><h5>Œuvre de référence</h5><p>{oeuvres}</p></div>
            {citation_html}
            <div class="ref-tags"><span>{dates}</span><span>{pays}</span><span>{courant}</span></div>
          </div>
        </div>"""

    header = page_header(
        depth=1, breadcrumb=_crumb("Auteurs"), icon="👤", color="or",
        title="Les grandes figures de la psychologie",
        subtitle=f"{len(AUTEURS)} chercheurs et cliniciens, de Wundt aux contemporains",
        chips=[f"👤 {len(AUTEURS)} biographies", f"🏷️ {len(familles)} courants", "💬 Citations d'origine"],
    )

    body = f"""{header}
<div class="section">
  <p class="section-desc" style="max-width:760px">Derrière chaque théorie, il y a une trajectoire, un contexte et
  souvent une controverse. Ces fiches racontent l'apport décisif de chaque figure, son parcours, son œuvre de
  référence et, quand elle existe, une phrase qui résume sa pensée.</p>
  {_toolbar("Filtrer par nom, pays, courant…", familles, len(AUTEURS))}
  {cards}
</div>
"""
    _write("auteurs.html", page_shell("Grandes figures", body, depth=1, active="Références",
                                      description=f"{len(AUTEURS)} grandes figures de la psychologie : biographie, apport décisif, œuvres et citations."))


# --------------------------------------------------------------------------
# Troubles
# --------------------------------------------------------------------------

def render_troubles():
    familles = sorted(set(t[2] for t in TROUBLES))

    cards = ""
    for i, (tid, nom, famille, prevalence, signes, comprendre, traitements) in enumerate(TROUBLES, 1):
        color = COLORS[i % len(COLORS)]
        signes_html = "".join(f"<li>{s}</li>" for s in signes)
        cards += f"""<div class="ref-card {color}" data-ref-id="{tid}" data-famille="{famille}" data-search="{nom} {famille} {strip_html(comprendre)}">
          <div class="ref-card-head">
            <span class="ref-n">{i:02d}</span>
            <div class="ref-h"><h3>{nom}</h3><p class="ref-sub">{famille} · {prevalence}</p></div>
            <span class="ref-chev">▾</span>
          </div>
          <div class="ref-card-body">
            <div class="ref-field"><h5>Signes principaux</h5><ul>{signes_html}</ul></div>
            <div class="ref-field"><h5>Comprendre le trouble</h5><p>{comprendre}</p></div>
            <div class="ref-field"><h5>Prises en charge validées</h5><p>{traitements}</p></div>
            <div class="ref-tags"><span>{famille}</span><span>Prévalence : {prevalence}</span></div>
          </div>
        </div>"""

    header = page_header(
        depth=1, breadcrumb=_crumb("Troubles"), icon="🩺", color="rose",
        title="Répertoire des troubles psychiques",
        subtitle=f"{len(TROUBLES)} tableaux cliniques expliqués simplement, sans jargon ni dramatisation",
        chips=[f"🩺 {len(TROUBLES)} troubles", f"🗂️ {len(familles)} familles", "✅ Traitements validés"],
    )

    body = f"""{header}
<div class="section">
  <div class="warn-box">
    <strong>Avertissement important.</strong> Ces fiches sont des repères de vulgarisation. Elles ne permettent
    ni de poser un diagnostic, ni de s'auto-diagnostiquer, ni de diagnostiquer autrui. Reconnaître quelques signes
    chez soi est extrêmement fréquent et ne signifie rien en soi : un diagnostic repose sur un entretien clinique
    approfondi, une durée d'évolution, un retentissement fonctionnel et l'exclusion d'autres causes. En cas de
    souffrance, parles-en à un médecin ou à un psychologue. En cas d'urgence en France : le <strong>3114</strong>
    (numéro national de prévention du suicide, gratuit, 24 h/24) ou le <strong>15</strong>.
  </div>
  {_toolbar("Filtrer par nom de trouble, famille, symptôme…", familles, len(TROUBLES))}
  {cards}
</div>
"""
    _write("troubles.html", page_shell("Répertoire des troubles", body, depth=1, active="Références",
                                       description=f"{len(TROUBLES)} troubles psychiques expliqués en français : signes, mécanismes et prises en charge validées."))


# --------------------------------------------------------------------------
# Biais
# --------------------------------------------------------------------------

def render_biais():
    familles = sorted(set(b[2] for b in BIAIS))

    cards = ""
    for i, (bid, nom, famille, definition, exemple, parade) in enumerate(BIAIS, 1):
        color = COLORS[i % len(COLORS)]
        cards += f"""<div class="ref-card {color}" data-ref-id="{bid}" data-famille="{famille}" data-search="{nom} {famille} {strip_html(definition)}">
          <div class="ref-card-head">
            <span class="ref-n">{i:02d}</span>
            <div class="ref-h"><h3>{nom}</h3><p class="ref-sub">{famille}</p></div>
            <span class="ref-chev">▾</span>
          </div>
          <div class="ref-card-body">
            <div class="ref-field"><h5>Définition</h5><p>{definition}</p></div>
            <div class="ref-field"><h5>Exemple concret</h5><p>{exemple}</p></div>
            <div class="ref-field"><h5>La parade</h5><p>{parade}</p></div>
            <div class="ref-tags"><span>{famille}</span></div>
          </div>
        </div>"""

    header = page_header(
        depth=1, breadcrumb=_crumb("Biais"), icon="🌀", color="gris",
        title="Biais cognitifs, heuristiques et effets",
        subtitle=f"{len(BIAIS)} erreurs systématiques de raisonnement — et comment s'en défendre",
        chips=[f"🌀 {len(BIAIS)} biais", f"🗂️ {len(familles)} familles", "🛡️ Une parade par biais"],
    )

    body = f"""{header}
<div class="section">
  <p class="section-desc" style="max-width:760px">Un biais n'est pas une bêtise : c'est le prix d'un cerveau
  rapide et économe. Les heuristiques fonctionnent bien la plupart du temps, et échouent de façon prévisible dans
  certaines situations. Connaître ces situations ne suffit pas à annuler le biais, mais permet de mettre en place
  des garde-fous — c'est l'objet de la rubrique « parade ».</p>
  {_toolbar("Filtrer par nom de biais, famille, exemple…", familles, len(BIAIS))}
  {cards}

  <div class="note-box">
    <strong>Le piège du « point aveugle ».</strong> Chacun croit être moins biaisé que la moyenne — y compris après
    avoir lu cette page. C'est le <em>bias blind spot</em>. La seule protection réellement efficace n'est pas
    individuelle : elle est procédurale (critères fixés à l'avance, avis contradictoires, décisions à froid,
    données plutôt qu'impressions).
  </div>
</div>
"""
    _write("biais.html", page_shell("Biais cognitifs", body, depth=1, active="Références",
                                    description=f"{len(BIAIS)} biais cognitifs expliqués en français : définition, exemple concret et parade."))


# --------------------------------------------------------------------------
# Tests
# --------------------------------------------------------------------------

def render_tests():
    familles = sorted(set(t[2] for t in TESTS))

    cards = ""
    for i, (tid, nom, categorie, auteur_annee, mesure, passation, interpretation, limites) in enumerate(TESTS, 1):
        color = COLORS[i % len(COLORS)]
        cards += f"""<div class="ref-card {color}" data-ref-id="{tid}" data-famille="{categorie}" data-search="{nom} {categorie} {auteur_annee} {strip_html(mesure)}">
          <div class="ref-card-head">
            <span class="ref-n">{i:02d}</span>
            <div class="ref-h"><h3>{nom}</h3><p class="ref-sub">{categorie} · {auteur_annee}</p></div>
            <span class="ref-chev">▾</span>
          </div>
          <div class="ref-card-body">
            <div class="ref-field"><h5>Ce que le test mesure</h5><p>{mesure}</p></div>
            <div class="ref-field"><h5>Comment il se passe</h5><p>{passation}</p></div>
            <div class="ref-field"><h5>Comment on l'interprète</h5><p>{interpretation}</p></div>
            <div class="ref-field"><h5>Limites</h5><p>{limites}</p></div>
            <div class="ref-tags"><span>{categorie}</span><span>{auteur_annee}</span></div>
          </div>
        </div>"""

    header = page_header(
        depth=1, breadcrumb=_crumb("Tests"), icon="📊", color="vert",
        title="Tests et instruments de mesure",
        subtitle=f"{len(TESTS)} outils psychométriques : ce qu'ils mesurent vraiment, et ce qu'ils ne mesurent pas",
        chips=[f"📊 {len(TESTS)} instruments", f"🗂️ {len(familles)} domaines", "⚠️ Limites explicitées"],
    )

    body = f"""{header}
<div class="section">
  <div class="warn-box">
    <strong>Un test n'est pas un verdict.</strong> Les instruments présentés ici sont, pour la plupart, réservés à
    des professionnels formés : leur valeur vient autant de la passation standardisée et de l'étalonnage que du
    questionnaire lui-même. Les versions « gratuites en ligne » n'ont généralement aucune validité. Cette page
    explique la logique des outils, elle ne permet pas de se tester soi-même.
  </div>
  {_toolbar("Filtrer par nom de test, domaine, auteur…", familles, len(TESTS))}
  {cards}

  <div class="note-box">
    <strong>Les trois qualités d'un bon test.</strong> La <em>fidélité</em> (il donne le même résultat si on le
    repasse dans des conditions comparables), la <em>validité</em> (il mesure bien ce qu'il prétend mesurer) et
    l'<em>étalonnage</em> (on dispose de normes de référence sur une population comparable à celle de la personne
    évaluée). Un questionnaire qui n'affiche aucune de ces trois informations n'est pas un test psychométrique.
  </div>
</div>
"""
    _write("tests.html", page_shell("Tests psychométriques", body, depth=1, active="Références",
                                    description=f"{len(TESTS)} tests psychologiques expliqués : ce qu'ils mesurent, comment ils se passent, leurs limites."))


# --------------------------------------------------------------------------
# Chronologie
# --------------------------------------------------------------------------

def render_chronologie():
    par_periode = {pid: [] for pid, *_ in PERIODES}
    for annee, titre, description, categorie in CHRONOLOGIE_TRIEE:
        par_periode[periode_of(annee)].append((annee, titre, description, categorie))

    sections = ""
    toc_links = ""
    for pid, label, desc, _start, _end in PERIODES:
        events = par_periode[pid]
        if not events:
            continue
        toc_links += f'<a href="#{pid}">{label}</a>'
        items = "".join(
            f'<div class="tl-item" data-cat="{pid}" id="date-{slugify(str(a) + "-" + t)}">'
            f'<span class="tl-year">{"−" + str(a)[1:] + " av. J.-C." if str(a).startswith("-") else a}</span>'
            f"<h4>{t}</h4><p>{d}</p></div>"
            for a, t, d, _c in events
        )
        sections += f"""
<h2 id="{pid}">{label}</h2>
<p style="color:var(--gris);margin-bottom:1rem">{desc} — {len(events)} jalons.</p>
<div class="timeline">{items}</div>"""

    header = page_header(
        depth=1, breadcrumb=_crumb("Chronologie"), icon="🗓️", color="or",
        title="Chronologie de la psychologie",
        subtitle=f"{len(CHRONOLOGIE_TRIEE)} dates clés, d'Hippocrate aux neurosciences computationnelles",
        chips=[f"🗓️ {len(CHRONOLOGIE_TRIEE)} jalons", f"📜 {len(PERIODES)} grandes périodes", "🔗 Reliée aux catégories"],
    )

    body = f"""{header}
<div class="wrap with-toc">
  <aside class="toc-side"><h4>Périodes</h4>{toc_links}</aside>
  <div class="content" style="max-width:none">
    <p>L'histoire de la psychologie n'est pas une marche linéaire vers la vérité : c'est une succession de
    ruptures, de programmes concurrents et de retours en arrière. Les humeurs d'Hippocrate ont tenu vingt siècles ;
    l'introspection a été rejetée puis partiellement réhabilitée ; le behaviorisme a dominé quarante ans avant d'être
    débordé par la révolution cognitive. Lire cette frise dans l'ordre aide à comprendre <em>pourquoi</em> les
    concepts actuels ont la forme qu'ils ont.</p>
    {sections}
    <div class="cta-row">
      <a class="btn btn-primary" href="../quiz/quiz.html?id=chronologie-quiz">🎮 Quiz chronologie</a>
      <a class="btn btn-secondary" href="auteurs.html">👤 Les figures derrière ces dates</a>
      <a class="btn btn-secondary" href="../categories/02-histoire.html">📜 Fiche Histoire de la psychologie</a>
    </div>
  </div>
</div>
"""
    _write("chronologie.html", page_shell("Chronologie", body, depth=1, active="Références",
                                          description=f"Chronologie de la psychologie en {len(CHRONOLOGIE_TRIEE)} dates clés, de l'Antiquité à aujourd'hui."))


def render_all():
    render_hub()
    render_experiences()
    render_auteurs()
    render_troubles()
    render_biais()
    render_tests()
    render_chronologie()
