# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Génération des 26 fiches de catégorie, de l'index et du dictionnaire."""

import os

from shell import CAT_STICKERS, page_shell, page_header, slugify, sticker_img, strip_html
from content import (
    CATEGORIES, DICTIONNAIRE, QUIZ_FOR_CATEGORY, CATEGORY_TITLE,
    EXPERIENCES, AUTEURS,
)
from data_pensees import PLATES_CATEGORIES
from data_schemas import SCHEMAS

BASE = os.path.dirname(os.path.abspath(__file__))
TOTAL = len(CATEGORIES)
IMG = "../../05-larousse-illustre-complet/illustrations/wikimedia"


def _lecteur_href(pdf_path):
    """Convertit un chemin de PDF vu depuis categories/ en lien vers le lecteur intégré."""
    if not pdf_path.endswith(".pdf"):
        return None
    return "../lecteur.html?livre=" + pdf_path.replace("../../", "../", 1)


def _figures_html(figures):
    if not figures:
        return ""
    items = []
    for f in figures:
        img, name = f.split(":", 1)
        items.append(
            f'<div class="figure-person">'
            f'<img src="{IMG}/{img}" alt="Portrait de {name}" loading="lazy">'
            f"<span>{name}</span></div>"
        )
    return (
        '<h2 id="figures">🖼️ Les visages de ce domaine</h2>'
        f'<div class="figures-people">{"".join(items)}</div>'
    )


def _geo_plate_html(cat_id):
    spec = next((row for row in PLATES_CATEGORIES if row[0] == cat_id), None)
    if not spec:
        return ""
    _cid, _figure, paper, title = spec
    return (
        f'<figure class="geo-plate {paper}" style="max-width:460px;margin:1.5rem 0 1.8rem">'
        f'<img src="../../../assets-ebook/plates/svg/cat-{cat_id}.svg" alt="{title}">'
        f'<figcaption><span class="geo-fig">Planche du domaine</span>'
        f"<strong>{title}</strong>"
        f"<em>Gravure générée pour illustrer ce cours — cabinet de psychologie géométrique.</em>"
        f"</figcaption></figure>"
    )


def _schemas_html(cat_id):
    schemas = SCHEMAS.get(cat_id)
    if not schemas:
        return ""
    blocks = "".join(
        f'<figure class="figure-box">'
        f'<img src="{IMG}/{fichier}" alt="{legende}" loading="lazy">'
        f"<figcaption><strong>{legende}</strong><br>{commentaire}</figcaption>"
        f"</figure>"
        for fichier, legende, commentaire in schemas
    )
    return (
        f'<h2 id="schemas">🖼️ {len(schemas)} planches et schémas commentés</h2>'
        "<p>Une image ne se suffit pas à elle-même : chaque planche est accompagnée de ce qu'il faut "
        "y voir, et de ce qu'elle démontre.</p>"
        f"{blocks}"
    )


def _chiffres_html(chiffres):
    if not chiffres:
        return ""
    cells = "".join(
        f'<div class="stat-cell"><div class="val">{val}</div><div class="lbl">{lbl}</div></div>'
        for val, lbl in chiffres
    )
    return (
        '<h2 id="chiffres-cles">📊 Les chiffres à retenir</h2>'
        f'<div class="stat-strip">{cells}</div>'
    )


def _mythes_html(mythes):
    if not mythes:
        return ""
    cards = "".join(
        f'<div class="myth-card">'
        f'<div class="myth-false"><span class="tag">❌ Idée reçue —</span><span>{faux}</span></div>'
        f'<div class="myth-true"><span class="tag">✅ En réalité —</span><span>{vrai}</span></div>'
        f"</div>"
        for faux, vrai in mythes
    )
    return (
        '<h2 id="idees-recues">🧯 Idées reçues à corriger</h2>'
        "<p>La psychologie est la discipline la plus exposée aux « neuromythes ». "
        "Voici ce que dit réellement la recherche.</p>"
        f'<div class="myth-grid">{cards}</div>'
    )


def _pdfs_html(pdfs):
    if not pdfs:
        return ""
    blocks = ""
    for p in pdfs:
        icon = "🌐" if p["path"].endswith(".html") else "📕"
        lecteur = _lecteur_href(p["path"])
        actions = (
            f'<a class="pdf-block-btn" href="{lecteur}">📖 Lire dans le site</a>'
            if lecteur else
            f'<a class="pdf-block-btn" href="{p["path"]}" target="_blank" rel="noopener">🌐 Lire le texte complet</a>'
        )
        blocks += f"""<div class="pdf-block">
          <div class="pdf-block-icon">{icon}</div>
          <div class="pdf-block-info"><strong>{p['title']}</strong><span>{p['author']} — {p['desc']}</span></div>
          {actions}
        </div>"""
    return (
        '<h2 id="livres">📕 Lire les sources originales</h2>'
        "<p>Ces ouvrages du domaine public sont hébergés dans ce dépôt et se lisent directement "
        "dans le site, page par page, avec extraction du texte, modernisation du français ancien "
        "et reconnaissance optique pour les pages scannées.</p>"
        f"{blocks}"
    )


def _flashcards_html(flashcards):
    if not flashcards:
        return ""
    cards = "".join(
        f"""<div class="flashcard">
          <div class="flashcard-inner">
            <div class="flashcard-face flashcard-front"><span class="flashcard-tag">Question</span>{q}</div>
            <div class="flashcard-face flashcard-back"><span class="flashcard-tag">Réponse</span>{a}</div>
          </div>
        </div>"""
        for q, a in flashcards
    )
    return (
        f'<h2 id="flashcards">🔄 {len(flashcards)} fiches de révision — rappel actif</h2>'
        "<p>Clique sur chaque carte pour révéler la réponse. Essaie de répondre "
        "<strong>avant</strong> de cliquer : c'est l'effort de rappel qui fixe la mémoire.</p>"
        f'<div class="flash-grid">{cards}</div>'
    )


def _experiences_html(cat_id):
    liees = [e for e in EXPERIENCES if e[4] == cat_id]
    if not liees:
        return ""
    items = "".join(
        f'<a class="path-step" href="../references/experiences.html#{e[0]}">'
        f'<span class="path-step-n">🔬</span>'
        f'<span class="path-step-title">{e[1]}</span>'
        f'<span class="path-step-kind">{e[2]}, {e[3]}</span></a>'
        for e in liees
    )
    return (
        f'<h2 id="experiences">🔬 {len(liees)} expériences fondatrices de ce domaine</h2>'
        "<p>Chaque fiche détaille le protocole, les résultats, la portée et les critiques adressées à l'étude.</p>"
        f'<div class="path-card"><div class="path-steps">{items}</div></div>'
    )


def _toc_html(sections, cat):
    links = ['<a href="#objectifs">🎯 Objectifs</a>']
    for title, _body in sections:
        links.append(f'<a href="#{slugify(title)}">{title}</a>')
    if cat.get("chiffres"):
        links.append('<a href="#chiffres-cles">📊 Chiffres clés</a>')
    if cat.get("mythes"):
        links.append('<a href="#idees-recues">🧯 Idées reçues</a>')
    if SCHEMAS.get(cat["id"]):
        links.append('<a href="#schemas">🖼️ Planches commentées</a>')
    if cat.get("figures"):
        links.append('<a href="#figures">👤 Les visages</a>')
    if [e for e in EXPERIENCES if e[4] == cat["id"]]:
        links.append('<a href="#experiences">🔬 Expériences</a>')
    if cat.get("pdfs"):
        links.append('<a href="#livres">📕 Livres sources</a>')
    links.append('<a href="#flashcards">🔄 Révision</a>')
    return (
        '<aside class="toc-side"><h4>Sommaire de la fiche</h4>'
        + "".join(links)
        + "</aside>"
    )


def render_category(cat, idx):
    prev_cat = CATEGORIES[idx - 1] if idx > 0 else None
    next_cat = CATEGORIES[idx + 1] if idx < TOTAL - 1 else None

    prev_html = (
        f'<a href="{prev_cat["id"]}.html">← Précédent<strong>{prev_cat["icon"]} {prev_cat["title"]}</strong></a>'
        if prev_cat else '<a href="../index.html">← Retour<strong>🏠 Toutes les catégories</strong></a>'
    )
    next_html = (
        f'<a class="next" href="{next_cat["id"]}.html">Suivant<strong>{next_cat["icon"]} {next_cat["title"]}</strong></a>'
        if next_cat else '<a class="next" href="../references/index.html">Suivant<strong>🗂️ Base de références</strong></a>'
    )

    sections_html = "".join(
        f'<h2 id="{slugify(title)}">{title}</h2>\n{body}\n' for title, body in cat["sections"]
    )

    objectives_html = "".join(f"<li>{o}</li>" for o in cat["objectives"])
    quiz_id = QUIZ_FOR_CATEGORY.get(cat["id"], "fondamentaux-histoire")
    n_words = len(strip_html(sections_html).split())

    header = page_header(
        depth=1,
        breadcrumb=[("Accueil", "../../../index.html"), ("Catégories", "../index.html"), (cat["title"], None)],
        icon=CAT_STICKERS.get(cat["id"], cat["icon"]), color=cat["color"], title=cat["title"], subtitle=cat["subtitle"],
        chips=[
            f"⏱ {cat['read_time']} de lecture",
            f"📂 Catégorie {cat['num']}/{TOTAL}",
            f"📝 ≈ {n_words:,} mots".replace(",", " "),
            f"🔄 {len(cat.get('flashcards', []))} flashcards",
            "🎮 Quiz noté /20",
        ],
    )

    body = f"""{header}
<div class="wrap with-toc">
  {_toc_html(cat["sections"], cat)}
  <div class="content" style="max-width:none">
    <div class="objectives-box" id="objectifs">
      <h3>🎯 À l'issue de cette fiche, tu sauras :</h3>
      <ul>{objectives_html}</ul>
    </div>
    {_geo_plate_html(cat["id"])}

    {sections_html}
    {_chiffres_html(cat.get("chiffres"))}
    {_mythes_html(cat.get("mythes"))}
    {_schemas_html(cat["id"])}
    {_figures_html(cat.get("figures", []))}
    {_experiences_html(cat["id"])}
    {_pdfs_html(cat.get("pdfs", []))}

    <div class="fun-box">💡 <strong>Le savais-tu ?</strong> {cat['fun_fact']}</div>

    <div class="learn-tip-box">
      <span class="emoji">🧠</span>
      <p><strong>Astuce d'apprentissage :</strong> lis la fiche en entier, puis teste-toi immédiatement avec
      les flashcards <em>sans</em> regarder le texte. Ce rappel actif ancre bien mieux les connaissances
      qu'une relecture. Reviens réviser dans 2 jours, puis dans 1 semaine, puis dans 1 mois.</p>
    </div>

    {_flashcards_html(cat.get("flashcards", []))}

    <div class="cta-row">
      <a class="btn btn-primary" href="../quiz/quiz.html?id={quiz_id}">🎮 Passer le quiz noté</a>
      <a class="btn btn-secondary" href="../references/index.html">🗂️ Explorer les références</a>
      <a class="btn btn-secondary" href="../dictionnaire.html">📖 Dictionnaire A-Z</a>
    </div>

    <div class="page-nav">
      {prev_html}
      {next_html}
    </div>
  </div>
</div>
"""
    html = page_shell(
        cat["title"], body, depth=1, active="Catégories",
        description=f"{cat['title']} — {cat['subtitle']}. Fiche complète, illustrée, avec flashcards, sources du domaine public et quiz noté.",
        body_attrs=f'data-mark-visited="{cat["id"]}"',
    )
    with open(os.path.join(BASE, "categories", f"{cat['id']}.html"), "w", encoding="utf-8") as f:
        f.write(html)


def render_categories_index():
    groups = [
        ("Socles de la discipline", "loupe.png", "Méthode, histoire, pensée, groupe.", CATEGORIES[0:4]),
        ("La personne", "cerveau.png", "Développement, personnalité, émotions, cerveau.", CATEGORIES[4:8]),
        ("Souffrance et soin", "pince.png", "Comprendre sans stigmatiser.", CATEGORIES[8:10]),
        ("La vie quotidienne", "soleil.png", "Bien-être, travail, école, santé, justice, animal.", CATEGORIES[10:16]),
        ("Frontières", "papillon.png", "Culture, langage, mesure, écrans, âge, politique.", CATEGORIES[16:]),
    ]

    sections_html = ""
    for label, img, desc, cats in groups:
        cards = "".join(
            f"""<a href="categories/{c['id']}.html" class="cat" data-cat-id="{c['id']}">
              {sticker_img(CAT_STICKERS.get(c['id'], 'loupe.png'), 0)}
              <div><strong>{c['num']} · {c['title']}</strong><span>{c['subtitle']}</span>
              <div class="cat-progress-track"><div class="cat-progress-fill" data-cat-key="{c['id']}"></div></div></div>
            </a>"""
            for c in cats
        )
        sections_html += f"""
<div class="block">{sticker_img(img, 0)}<div><h2>{label}</h2><p>{desc}</p></div></div>
<div class="cats">{cards}</div>"""

    n_sections = sum(len(c["sections"]) for c in CATEGORIES)
    n_flash = sum(len(c.get("flashcards", [])) for c in CATEGORIES)

    body = f"""
<main class="wrap">
  <p class="kicker">{TOTAL} domaines · {n_sections} chapitres · {n_flash} flashcards</p>
  <h1>Les catégories, par questions.</h1>
  <p class="lede">Chaque fiche a un sommaire, des chiffres, des idées reçues, des livres du domaine public,
  des flashcards et un quiz. Pour un itinéraire balisé, suis un <a href="parcours.html">parcours guidé</a>.</p>
  <div class="cta-row" style="margin-bottom:0">
    <button class="btn btn-primary" data-search-open="">🔍 Rechercher dans tout le site</button>
    <a class="btn btn-secondary" href="parcours.html">🧭 Parcours guidés</a>
    <a class="btn btn-secondary" href="references/index.html">🗂️ Base de références</a>
  </div>
  {sections_html}

  <div class="section-head" style="margin-top:2.5rem">
    <p class="section-eyebrow">Transversal</p>
    <h2 class="section-title" style="font-size:1.5rem">Ressources qui traversent toutes les catégories</h2>
  </div>
  <div class="hub-grid">
    <a class="hub-card" href="dictionnaire.html"><span class="hub-ico">📖</span><h3>Dictionnaire A-Z</h3>
      <p>Toutes les notions clés définies et reliées à leur catégorie.</p><span class="hub-n">{len(DICTIONNAIRE)} entrées</span></a>
    <a class="hub-card or" href="references/index.html"><span class="hub-ico">🗂️</span><h3>Base de références</h3>
      <p>Expériences, auteurs, troubles, biais, tests et chronologie.</p><span class="hub-n">{len(EXPERIENCES) + len(AUTEURS)} fiches et plus</span></a>
    <a class="hub-card rose" href="lecteur.html"><span class="hub-ico">📕</span><h3>Lecteur de livres</h3>
      <p>Lire les ouvrages originaux page par page, texte extrait et modernisé.</p><span class="hub-n">13 ouvrages</span></a>
    <a class="hub-card gris" href="quiz/index.html"><span class="hub-ico">🎮</span><h3>Quiz notés</h3>
      <p>Un quiz par domaine, corrigé et expliqué, noté sur 20.</p><span class="hub-n">26 quiz</span>    </a>
  </div>
</main>
"""
    html = page_shell("Catégories", body, depth=0, active="Catégories",
                      description=f"Les {TOTAL} catégories de la psychologie expliquées en français : {n_sections} chapitres illustrés, flashcards et quiz.")
    with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


def render_dictionnaire():
    def letter_of(term):
        import unicodedata
        base = unicodedata.normalize("NFD", term[0].upper())
        return "".join(c for c in base if unicodedata.category(c) != "Mn") or term[0].upper()

    letters = sorted(set(letter_of(t) for t, _d, _c in DICTIONNAIRE))
    entries_html = ""
    for term, definition, cat_id in DICTIONNAIRE:
        cat_label = CATEGORY_TITLE.get(cat_id, "Psychologie générale")
        entries_html += f"""<div class="ref-card" id="def-{slugify(term)}" data-letter-key="{letter_of(term)}" data-ref-id="def-{slugify(term)}" data-search="{term} {strip_html(definition)}">
          <div class="ref-card-head">
            <span class="ref-n">{letter_of(term)}</span>
            <div class="ref-h"><h3>{term}</h3><p class="ref-sub">{definition[:110]}{'…' if len(definition) > 110 else ''}</p></div>
            <span class="ref-chev">▾</span>
          </div>
          <div class="ref-card-body">
            <div class="ref-field"><h5>Définition</h5><p>{definition}</p></div>
            <a class="ref-link" href="categories/{cat_id}.html">→ Approfondir dans « {cat_label} »</a>
          </div>
        </div>"""

    letter_nav = "".join(f'<button data-letter="{l}">{l}</button>' for l in letters)

    header = page_header(
        depth=0,
        breadcrumb=[("Accueil", "../../index.html"), ("Catégories", "index.html"), ("Dictionnaire", None)],
        icon="📖", color="vert", title="Dictionnaire général A-Z",
        subtitle=f"{len(DICTIONNAIRE)} notions de psychologie définies, toutes catégories confondues",
        chips=[f"🔤 {len(letters)} lettres", "🔗 Chaque entrée renvoie à sa catégorie", "🔍 Recherche intégrée"],
    )

    body = f"""{header}
<div class="section">
  <div class="ref-toolbar" data-ref-filter>
    <input type="search" placeholder="Filtrer les notions (ex. « mémoire », « biais », « attachement »)…" aria-label="Filtrer le dictionnaire">
    <span class="ref-count" data-alpha-count>{len(DICTIONNAIRE)} entrées</span>
  </div>
  <div class="alpha-nav">
    <button class="active" data-letter="all">Tout</button>
    {letter_nav}
  </div>
  {entries_html}
</div>
"""
    html = page_shell("Dictionnaire A-Z", body, depth=0, active="Catégories",
                      description=f"Dictionnaire de psychologie en français : {len(DICTIONNAIRE)} notions définies et reliées à leur domaine.")
    with open(os.path.join(BASE, "dictionnaire.html"), "w", encoding="utf-8") as f:
        f.write(html)
