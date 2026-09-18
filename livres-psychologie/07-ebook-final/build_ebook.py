# -*- coding: utf-8 -*-
"""
PSYCLOPÉDIA — Générateur du site Ebook complet.
Construit : catégories, quiz, page apprendre, bibliothèque, à partir de data_categories.py et data_quiz.py.
La page d'accueil (racine du repo) est écrite séparément (../../index.html côté repo root).
"""
import os
import json
from data_categories import CATEGORIES, DICTIONNAIRE
from data_quiz import QUIZZES

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT_ASSETS = "../../../assets-ebook"  # from categories/ or quiz/

NAV_ITEMS = [
    ("Accueil", "root:index.html"),
    ("Catégories", "self:index.html"),
    ("Quiz", "quiz:index.html"),
    ("Apprendre", "self:apprendre.html"),
    ("Bibliothèque", "self:bibliotheque.html"),
]


def page_shell(title, body, depth=0, active="", extra_head="", extra_scripts="", assets_prefix=None):
    if assets_prefix is None:
        assets_prefix = "../../assets-ebook" if depth == 0 else "../../../assets-ebook"
    root_prefix = "../../" if depth == 0 else "../../../"
    links_html = ""
    for label, target in NAV_ITEMS:
        kind, page = target.split(":")
        if kind == "root":
            href = root_prefix + page
        elif kind == "quiz":
            href = ("../quiz/" if depth == 1 else "quiz/") + page
        else:
            href = ("../" if depth == 1 else "") + page
        cls = "active" if label == active else ""
        links_html += f'<a href="{href}" class="{cls}">{label}</a>'

    home_href = root_prefix + "index.html"

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Psyclopédia</title>
<meta name="description" content="Psyclopédia : l'encyclopédie vivante et illustrée de la psychologie, en français, avec quiz et fiches de révision.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@500;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{assets_prefix}/css/style.css">
{extra_head}
</head>
<body>
<div class="topbar">
  <nav class="nav-pill">
    <a class="brand" href="{home_href}"><span class="brand-mark"></span>Psyclopédia</a>
    <ul class="nav-links">{links_html}</ul>
    <div class="nav-side">
      <span class="nav-badge">🔥 Apprentissage actif</span>
    </div>
  </nav>
</div>
{body}
<footer>
  <div class="foot-links">
    <a href="{root_prefix}index.html">Accueil</a>
    <a href="{('../' if depth==1 else '')}index.html">Catégories</a>
    <a href="{('../' if depth==1 else '')}quiz/index.html">Quiz</a>
    <a href="{('../' if depth==1 else '')}bibliotheque.html">Bibliothèque PDF</a>
    <a href="{root_prefix}livres-psychologie/README.md">Code source &amp; sources</a>
  </div>
  <p>Psyclopédia — Projet pédagogique open source. Textes originaux rédigés pour ce guide ; livres du domaine public
  hébergés dans <code>06-pdf-domaine-public/</code> avec mention de leur source (Gallica, Internet Archive, Gutenberg, UQAM, Darwin Online).
  Illustrations : Wikimedia Commons (domaine public).</p>
</footer>
<script src="{assets_prefix}/js/app.js"></script>
{extra_scripts}
</body>
</html>"""


def figure_person_html(figures):
    if not figures:
        return ""
    items = []
    for f in figures:
        img, name = f.split(":")
        items.append(f'<div class="figure-person"><img src="{IMG}/{img}" alt="{name}" loading="lazy"><span>{name}</span></div>')
    IMGP = "../../05-larousse-illustre-complet/illustrations/wikimedia"
    items = [i.replace(f"{IMG}/", f"{IMGP}/") for i in items]
    return f'<div class="figures-people">{"".join(items)}</div>'


IMG = "../../05-larousse-illustre-complet/illustrations/wikimedia"


def render_category(cat, idx, total):
    prev_cat = CATEGORIES[idx - 1] if idx > 0 else None
    next_cat = CATEGORIES[idx + 1] if idx < len(CATEGORIES) - 1 else None
    # dictionnaire is the "18th" virtual next after last category
    if next_cat is None:
        next_html = '<a class="next" href="../dictionnaire.html">Suivant<strong>📖 Dictionnaire A-Z</strong></a>'
    else:
        next_html = f'<a class="next" href="{next_cat["id"]}.html">Suivant<strong>{next_cat["icon"]} {next_cat["title"]}</strong></a>'
    if prev_cat is None:
        prev_html = '<a href="../index.html">← Retour<strong>🏠 Accueil</strong></a>'
    else:
        prev_html = f'<a href="{prev_cat["id"]}.html">← Précédent<strong>{prev_cat["icon"]} {prev_cat["title"]}</strong></a>'

    sections_html = ""
    for title, body in cat["sections"]:
        sections_html += f"<h2>{title}</h2>\n{body}\n"

    figures_html = figure_person_html(cat.get("figures", []))

    pdf_html = ""
    for p in cat.get("pdfs", []):
        ext = "🌐" if p["path"].endswith(".html") else "📕"
        pdf_html += f"""<div class="pdf-block">
          <div class="pdf-block-icon">{ext}</div>
          <div class="pdf-block-info"><strong>{p['title']}</strong><span>{p['author']} — {p['desc']}</span></div>
          <a class="pdf-block-btn" href="{p['path']}" target="_blank" rel="noopener">Lire le livre complet →</a>
        </div>"""

    flash_html = ""
    for i, (q, a) in enumerate(cat.get("flashcards", [])):
        flash_html += f"""<div class="flashcard">
          <div class="flashcard-inner">
            <div class="flashcard-face flashcard-front"><span class="flashcard-tag">Question</span>{q}</div>
            <div class="flashcard-face flashcard-back"><span class="flashcard-tag">Réponse</span>{a}</div>
          </div>
        </div>"""

    quiz_map = {
        "01-fondamentaux": "fondamentaux-histoire", "02-histoire": "fondamentaux-histoire",
        "03-cognitive": "cognitive", "04-sociale": "sociale",
        "05-developpement": "developpement-personnalite", "06-personnalite": "developpement-personnalite",
        "07-emotions": "emotions-motivation", "08-neurosciences": "neurosciences",
        "09-psychopathologie": "psychopathologie", "10-therapies": "therapies",
        "11-positive": "vie-quotidienne", "12-travail": "vie-quotidienne",
        "13-education": "vie-quotidienne", "14-sante": "vie-quotidienne",
        "15-legale": "legale-comparee", "16-comparee": "legale-comparee",
    }
    quiz_id = quiz_map.get(cat["id"], "fondamentaux-histoire")

    objectives_html = "".join(f"<li>{o}</li>" for o in cat["objectives"])

    body = f"""
<div class="page-header">
  <p class="breadcrumb"><a href="../index.html">Accueil</a> → <a href="../index.html">Catégories</a> → {cat['title']}</p>
  <div class="page-hero">
    <div class="page-hero-icon" style="background:var(--{cat['color']}-light)">{cat['icon']}</div>
    <div>
      <h1>{cat['title']}</h1>
      <p class="subtitle">{cat['subtitle']}</p>
    </div>
  </div>
  <div class="meta-row">
    <span class="meta-chip">⏱ {cat['read_time']} de lecture</span>
    <span class="meta-chip">📂 Catégorie {cat['num']}/16</span>
    <span class="meta-chip">🎮 Quiz associé disponible</span>
  </div>
</div>
<div class="content">
  <div class="objectives-box">
    <h3>🎯 À l'issue de cette fiche, tu sauras :</h3>
    <ul>{objectives_html}</ul>
  </div>

  {sections_html}
  {figures_html}
  {pdf_html}

  <div class="fun-box">💡 <strong>Le savais-tu ?</strong> {cat['fun_fact']}</div>

  <div class="learn-tip-box">
    <span class="emoji">🧠</span>
    <p><strong>Astuce d'apprentissage :</strong> lis d'abord cette fiche en entier, puis teste-toi immédiatement avec
    les flashcards ci-dessous SANS regarder le texte. Ce rappel actif ("testing effect") ancre bien mieux les
    connaissances qu'une simple relecture. Reviens réviser cette fiche dans 2 jours, puis dans 1 semaine
    (répétition espacée) pour une mémorisation durable.</p>
  </div>

  <h2>🔄 Fiches de révision — Rappel actif</h2>
  <p>Clique sur chaque carte pour révéler la réponse. Essaie de répondre <strong>avant</strong> de cliquer !</p>
  <div class="flash-grid">{flash_html}</div>

  <div class="cta-row">
    <a class="btn btn-primary" href="../quiz/quiz.html?id={quiz_id}">🎮 Faire le quiz de cette catégorie</a>
    <a class="btn btn-secondary" href="../apprendre.html">📚 Techniques d'apprentissage</a>
  </div>

  <div class="page-nav">
    {prev_html}
    {next_html}
  </div>
</div>
"""
    html = page_shell(cat["title"], body, depth=1, active="Catégories")
    html = html.replace('data-mark-visited=""', "")
    html = html.replace("<body>", f'<body data-mark-visited="{cat["id"]}">')
    with open(os.path.join(BASE, "categories", f"{cat['id']}.html"), "w", encoding="utf-8") as f:
        f.write(html)


def render_dictionnaire():
    letters = sorted(set(d[0][0].upper() for d in DICTIONNAIRE))
    entries_html = ""
    for term, definition, cat_id in sorted(DICTIONNAIRE, key=lambda x: x[0].lower()):
        letter = term[0].upper()
        entries_html += f"""<div class="dict-entry" data-letter="{letter}" style="padding:1.1rem 0;border-bottom:1px solid var(--border)">
          <strong style="font-family:var(--serif);font-size:1.05rem">{term}</strong>
          <p style="font-size:0.9rem;color:var(--gris);margin-top:0.3rem">{definition}</p>
          <a href="categories/{cat_id}.html" style="font-size:0.75rem;color:var(--vert);text-decoration:none">→ Voir la catégorie liée</a>
        </div>"""

    letter_nav = "".join(f'<button class="style-tab" data-letter="{l}">{l}</button>' for l in letters)

    body = f"""
<div class="page-header">
  <p class="breadcrumb"><a href="index.html">Accueil</a> → Dictionnaire</p>
  <div class="page-hero">
    <div class="page-hero-icon" style="background:var(--vert-light)">📖</div>
    <div><h1>Dictionnaire général A-Z</h1><p class="subtitle">{len(DICTIONNAIRE)} notions clés de la psychologie, toutes catégories confondues</p></div>
  </div>
</div>
<div class="content">
  <div class="style-tabs" id="letter-filter">
    <button class="style-tab active" data-letter="all">Tout afficher</button>
    {letter_nav}
  </div>
  <div id="dict-list">{entries_html}</div>
</div>
<script>
document.querySelectorAll('#letter-filter .style-tab').forEach(btn => {{
  btn.addEventListener('click', () => {{
    document.querySelectorAll('#letter-filter .style-tab').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const letter = btn.dataset.letter;
    document.querySelectorAll('.dict-entry').forEach(entry => {{
      entry.style.display = (letter === 'all' || entry.dataset.letter === letter) ? 'block' : 'none';
    }});
  }});
}});
</script>
"""
    html = page_shell("Dictionnaire A-Z", body, depth=0, active="Catégories")
    with open(os.path.join(BASE, "dictionnaire.html"), "w", encoding="utf-8") as f:
        f.write(html)


def render_categories_index():
    cards_html = ""
    for cat in CATEGORIES:
        cards_html += f"""<a href="categories/{cat['id']}.html" class="cat-card" data-cat-id="{cat['id']}">
          <span class="cat-check">✅</span>
          <div class="cat-card-icon" style="background:var(--{cat['color']}-light)">{cat['icon']}</div>
          <h3>{cat['num']} · {cat['title']}</h3>
          <p>{cat['subtitle']}</p>
          <div class="cat-progress-track"><div class="cat-progress-fill" data-cat-key="{cat['id']}"></div></div>
        </a>"""
    cards_html += f"""<a href="dictionnaire.html" class="cat-card" data-cat-id="17-dictionnaire">
      <span class="cat-check">✅</span>
      <div class="cat-card-icon" style="background:var(--vert-light)">📖</div>
      <h3>17 · Dictionnaire A-Z</h3>
      <p>{len(DICTIONNAIRE)} notions clés reliées à toutes les catégories</p>
      <div class="cat-progress-track"><div class="cat-progress-fill" data-cat-key="17-dictionnaire"></div></div>
    </a>"""

    body = f"""
<div class="section">
  <div class="section-head">
    <p class="section-eyebrow">17 domaines complets</p>
    <h1 class="section-title">Toutes les catégories de la psychologie</h1>
    <p class="section-desc">Explore librement, dans l'ordre que tu préfères. Chaque fiche est illustrée, contient un
    livre du domaine public à télécharger, des flashcards de révision et un quiz noté.</p>
  </div>
  <div class="cat-grid">{cards_html}</div>
</div>
"""
    html = page_shell("Catégories", body, depth=0, active="Catégories")
    with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


def render_quiz_hub():
    cards_html = ""
    for quiz in QUIZZES:
        n = len(quiz["questions"])
        cards_html += f"""<a href="quiz.html?id={quiz['id']}" class="quiz-card" data-quiz-id="{quiz['id']}">
          <div class="quiz-card-top">
            <span class="quiz-icon">{quiz['icon']}</span>
            <span class="quiz-best" style="display:none">Meilleur score</span>
          </div>
          <h3>{quiz['title']}</h3>
          <p>{quiz['desc']}</p>
          <div class="quiz-meta"><span>❓ {n} questions</span><span>📊 {quiz['difficulty']}</span><span>📝 Noté /20</span></div>
        </a>"""

    body = f"""
<div class="section">
  <div class="section-head">
    <p class="section-eyebrow">{sum(len(q['questions']) for q in QUIZZES)} questions au total</p>
    <h1 class="section-title">🎮 Quiz — Teste tes connaissances</h1>
    <p class="section-desc">Chaque quiz est noté sur 20, avec un corrigé complet et une explication détaillée pour
    chaque question. Rejoue autant de fois que tu veux : ton meilleur score est conservé sur cet appareil.</p>
  </div>
  <div class="grid-3">{cards_html}</div>
</div>
"""
    html = page_shell("Quiz", body, depth=1, active="Quiz")
    with open(os.path.join(BASE, "quiz", "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


def render_quiz_engine_page():
    body = """
<div class="section">
  <div class="section-head" style="text-align:center">
    <p class="section-eyebrow" id="quiz-eyebrow">Quiz</p>
    <h1 class="section-title" id="quiz-title">Chargement…</h1>
  </div>
  <div class="quiz-question" id="quiz-container"></div>
</div>
<script id="quiz-data-json" type="application/json">__QUIZDATA__</script>
<script>
(function() {
  const params = new URLSearchParams(window.location.search);
  const quizId = params.get('id') || 'fondamentaux-histoire';
  const ALL_QUIZZES = JSON.parse(document.getElementById('quiz-data-json').textContent);
  const quiz = ALL_QUIZZES.find(q => q.id === quizId) || ALL_QUIZZES[0];
  window.QUIZ_ID = quiz.id;
  window.QUIZ_TITLE = quiz.icon + " " + quiz.title;
  window.QUIZ_QUESTIONS = quiz.questions;
})();
</script>
"""
    quiz_json = json.dumps(QUIZZES, ensure_ascii=False)
    body = body.replace("__QUIZDATA__", quiz_json)
    html = page_shell("Quiz", body, depth=1, active="Quiz",
                       extra_scripts='<script src="../../../assets-ebook/js/quiz-engine.js"></script>')
    with open(os.path.join(BASE, "quiz", "quiz.html"), "w", encoding="utf-8") as f:
        f.write(html)


def render_apprendre():
    body = """
<div class="section">
  <div class="section-head">
    <p class="section-eyebrow">Apprendre à apprendre</p>
    <h1 class="section-title">📚 Comment apprendre efficacement la psychologie</h1>
    <p class="section-desc">La science de l'apprentissage a identifié des méthodes bien plus efficaces que la
    relecture passive. Ce guide t'aide à choisir les bonnes techniques selon ton profil, et à les appliquer
    directement dans Psyclopédia.</p>
  </div>

  <h2 style="font-family:var(--serif);font-size:1.5rem;margin-bottom:1rem">🧑‍🎨 Quel est ton profil d'apprentissage ? (modèle VARK)</h2>
  <p style="color:var(--gris);margin-bottom:1rem">Le modèle VARK distingue 4 grandes préférences perceptives. La
  plupart des gens combinent plusieurs styles — l'essentiel est de varier les approches pour renforcer la mémorisation
  (« encodage multiple »).</p>

  <div class="vark-grid">
    <div class="vark-card" style="border-top-color:var(--vert)">
      <span class="emoji">👁️</span>
      <h3>Visuel</h3>
      <p>Tu retiens mieux avec des schémas, couleurs et images.</p>
      <ul>
        <li>Observe attentivement les illustrations et diagrammes de chaque fiche</li>
        <li>Dessine tes propres schémas ou cartes mentales</li>
        <li>Utilise des couleurs différentes pour chaque grande notion</li>
      </ul>
    </div>
    <div class="vark-card" style="border-top-color:var(--or)">
      <span class="emoji">👂</span>
      <h3>Auditif</h3>
      <p>Tu retiens mieux en écoutant ou en parlant à voix haute.</p>
      <ul>
        <li>Lis les résumés à voix haute après ta lecture silencieuse</li>
        <li>Explique une notion à quelqu'un (ou même à voix haute, seul)</li>
        <li>Enregistre-toi en train de résumer une fiche et réécoute-toi</li>
      </ul>
    </div>
    <div class="vark-card" style="border-top-color:var(--rose)">
      <span class="emoji">✍️</span>
      <h3>Lecture / Écriture</h3>
      <p>Tu retiens mieux en lisant et en reformulant par écrit.</p>
      <ul>
        <li>Prends des notes avec tes propres mots après chaque section</li>
        <li>Rédige un résumé de 5 lignes à la fin de chaque fiche</li>
        <li>Complète le dictionnaire en écrivant tes propres définitions</li>
      </ul>
    </div>
    <div class="vark-card" style="border-top-color:var(--gris)">
      <span class="emoji">🤸</span>
      <h3>Kinesthésique</h3>
      <p>Tu retiens mieux en manipulant, testant, pratiquant.</p>
      <ul>
        <li>Fais les flashcards de chaque catégorie en priorité</li>
        <li>Passe le quiz avant même d'avoir tout lu, pour repérer tes lacunes</li>
        <li>Applique une notion à une situation vécue personnellement</li>
      </ul>
    </div>
  </div>

  <h2 style="font-family:var(--serif);font-size:1.5rem;margin:2.5rem 0 1rem">🔬 5 techniques validées par la science cognitive</h2>

  <div class="method-timeline">
    <div class="method-item">
      <div class="num">01</div>
      <div>
        <h4>Le rappel actif (testing effect)</h4>
        <p>Se tester activement sur un contenu — même en échouant — ancre l'information beaucoup plus durablement
        que de relire le même texte plusieurs fois. C'est l'une des découvertes les plus robustes de la psychologie
        cognitive (Roediger &amp; Karpicke, 2006). <strong>Dans Psyclopédia :</strong> utilise systématiquement les
        flashcards et les quiz après chaque lecture, sans regarder la réponse en premier.</p>
      </div>
    </div>
    <div class="method-item">
      <div class="num">02</div>
      <div>
        <h4>La répétition espacée</h4>
        <p>La « courbe de l'oubli » d'Ebbinghaus (1885) montre que l'on oublie très vite après un apprentissage — sauf
        si on révise à intervalles progressivement croissants (ex. après 1 jour, puis 3 jours, puis 1 semaine, puis
        1 mois). <strong>Dans Psyclopédia :</strong> reviens régulièrement sur les catégories déjà visitées plutôt que
        de tout lire une seule fois.</p>
      </div>
    </div>
    <div class="method-item">
      <div class="num">03</div>
      <div>
        <h4>L'entrelacement (interleaving)</h4>
        <p>Alterner entre plusieurs thèmes (plutôt que d'épuiser un seul sujet avant de passer au suivant) améliore
        la capacité à distinguer et transférer les connaissances. <strong>Dans Psyclopédia :</strong> alterne par
        exemple une fiche de psychologie cognitive, puis une de psychologie sociale, plutôt que de lire les
        17 catégories dans un ordre strictement linéaire.</p>
      </div>
    </div>
    <div class="method-item">
      <div class="num">04</div>
      <div>
        <h4>L'élaboration et l'auto-explication</h4>
        <p>Expliquer un concept avec ses propres mots, en le reliant à ce que l'on connaît déjà (une expérience
        personnelle, une autre notion apprise), renforce considérablement la compréhension et la mémorisation à
        long terme. <strong>Dans Psyclopédia :</strong> pour chaque section lue, demande-toi « à quel exemple de ma
        vie cela correspond-il ? »</p>
      </div>
    </div>
    <div class="method-item">
      <div class="num">05</div>
      <div>
        <h4>Le double codage (dual coding)</h4>
        <p>Associer une information verbale à une représentation visuelle (schéma, image, portrait) crée deux voies
        d'accès au souvenir dans le cerveau, ce qui améliore la mémorisation par rapport au texte seul.
        <strong>Dans Psyclopédia :</strong> observe systématiquement les illustrations et portraits qui accompagnent
        chaque notion, ne te contente pas du texte.</p>
      </div>
    </div>
  </div>

  <h2 style="font-family:var(--serif);font-size:1.5rem;margin:2.5rem 0 1rem">⏱️ Organiser ses sessions de révision</h2>
  <p>La technique <strong>Pomodoro</strong> (25 minutes de travail concentré, 5 minutes de pause, répété 4 fois puis
  pause longue) aide à maintenir l'attention sur la durée. Combine-la avec un objectif clair par session : par
  exemple, « lire et faire les flashcards d'une catégorie », plutôt qu'un vague « réviser la psychologie ».</p>

  <div class="fun-box" style="margin-top:2rem">💡 <strong>Objectif suggéré :</strong> une catégorie par jour (lecture +
  flashcards), avec un quiz de révision une fois par semaine sur les catégories déjà vues. En 3 semaines, tu peux
  couvrir l'ensemble des 17 catégories tout en les ancrant durablement grâce à la répétition espacée.</div>

  <div class="cta-row">
    <a class="btn btn-primary" href="index.html">📂 Retour aux catégories</a>
    <a class="btn btn-secondary" href="quiz/index.html">🎮 Voir tous les quiz</a>
  </div>
</div>
"""
    html = page_shell("Apprendre efficacement", body, depth=0, active="Apprendre")
    with open(os.path.join(BASE, "apprendre.html"), "w", encoding="utf-8") as f:
        f.write(html)


BOOKS = [
    {"title": "Précis de psychologie", "author": "William James", "year": "1909", "pages": "≈ 500 p.",
     "cat": "Fondamentaux", "color": "vert", "icon": "🧩",
     "desc": "Le texte fondateur du fonctionnalisme, traduit en français : perception, habitude, conscience, émotion.",
     "path": "psychologie-generale/james-precis-de-psychologie-1909.pdf"},
    {"title": "De l'intelligence", "author": "Hippolyte Taine", "year": "1870", "pages": "512 p.",
     "cat": "Histoire", "color": "gris", "icon": "📜",
     "desc": "Une somme philosophique majeure du XIXe siècle sur la connaissance et l'intelligence humaine.",
     "path": "histoire-psychologie/taine-de-lintelligence-1870.pdf"},
    {"title": "La Suggestibilité", "author": "Alfred Binet", "year": "1900", "pages": "≈ 200 p.",
     "cat": "Cognitive", "color": "vert", "icon": "💭",
     "desc": "L'étude pionnière sur l'influence et la suggestion, aux racines de la psychologie cognitive moderne.",
     "path": "psychologie-generale/binet-suggestibilite.html"},
    {"title": "Psychologie des foules", "author": "Gustave Le Bon", "year": "1895", "pages": "204 p.",
     "cat": "Sociale", "color": "or", "icon": "👥",
     "desc": "L'ouvrage fondateur sur la psychologie collective et l'influence de masse.",
     "path": "psychologie-sociale/le-bon-psychologie-des-foules-1895-complet.pdf"},
    {"title": "Le Suicide : étude de sociologie", "author": "Émile Durkheim", "year": "1897", "pages": "≈ 460 p.",
     "cat": "Sociale", "color": "or", "icon": "👥",
     "desc": "L'étude classique démontrant l'influence des structures sociales sur les comportements individuels.",
     "path": "psychologie-sociale/durkheim-le-suicide-1897.pdf"},
    {"title": "Les maladies de la volonté", "author": "Théodule Ribot", "year": "1883", "pages": "≈ 170 p.",
     "cat": "Personnalité", "color": "rose", "icon": "🎭",
     "desc": "L'étude pionnière sur les troubles de la volonté, aux racines de la psychologie de la personnalité.",
     "path": "psychopathologie/ribot-maladies-volonte-1883.pdf"},
    {"title": "Les maladies de la mémoire", "author": "Théodule Ribot", "year": "1898", "pages": "188 p.",
     "cat": "Psychopathologie", "color": "rose", "icon": "🩺",
     "desc": "L'étude fondatrice sur les troubles de la mémoire et la célèbre « loi de régression ».",
     "path": "psychopathologie/ribot-maladies-memoire-1898.pdf"},
    {"title": "Les névroses", "author": "Pierre Janet", "year": "1909", "pages": "397 p.",
     "cat": "Psychopathologie", "color": "rose", "icon": "🩺",
     "desc": "Référence historique majeure sur l'hystérie, l'automatisme psychologique et les troubles dissociatifs.",
     "path": "psychopathologie/janet-les-nevroses-1909.pdf"},
    {"title": "Leçons sur les maladies du système nerveux", "author": "Jean-Martin Charcot", "year": "1884", "pages": "568 p.",
     "cat": "Neurosciences", "color": "vert", "icon": "🧠",
     "desc": "L'œuvre fondatrice de la neurologie clinique moderne, observée à la Salpêtrière.",
     "path": "psychopathologie/charcot-lecons-systeme-nerveux-1884.pdf"},
    {"title": "L'interprétation des rêves", "author": "Sigmund Freud", "year": "1900", "pages": "≈ 500 p.",
     "cat": "Thérapies", "color": "or", "icon": "🛋️",
     "desc": "Le texte fondateur de la psychanalyse, en intégralité (format HTML).",
     "path": "psychologie-clinique/freud-interpretation-reves-1900.html"},
    {"title": "Psychologie de l'éducation", "author": "Gustave Le Bon", "year": "≈ 1910", "pages": "≈ 300 p.",
     "cat": "Éducation", "color": "vert", "icon": "🎓",
     "desc": "Un plaidoyer historique pour une pédagogie active, à lire avec regard critique.",
     "path": "psychologie-generale/le-bon-psychologie-education.html"},
    {"title": "L'homme criminel", "author": "Cesare Lombroso", "year": "1887", "pages": "682 p.",
     "cat": "Légale", "color": "gris", "icon": "⚖️",
     "desc": "Document historique sur la naissance (controversée) de la criminologie — à lire avec recul critique.",
     "path": "psychologie-legale/lombroso-homme-criminel-1887.pdf"},
    {"title": "L'expression des émotions chez l'homme et les animaux", "author": "Charles Darwin", "year": "1877 (trad.)", "pages": "≈ 400 p.",
     "cat": "Comparée / Émotions", "color": "or", "icon": "🐾",
     "desc": "L'ouvrage fondateur, richement illustré, sur les racines évolutives de nos émotions.",
     "path": "psychologie-comparative/darwin-expression-emotions-1877.pdf"},
]


def render_bibliotheque():
    cards_html = ""
    for b in BOOKS:
        ext = "🌐 Lire en ligne" if b["path"].endswith(".html") else "📥 Télécharger le PDF"
        cards_html += f"""<div class="book-card">
          <div class="book-cover" style="background:var(--{b['color']})">{b['icon']}</div>
          <div class="book-body">
            <h3>{b['title']}</h3>
            <p class="author">{b['author']} · {b['year']}</p>
            <p class="desc">{b['desc']}</p>
            <div class="book-meta"><span>{b['pages']}</span><span>{b['cat']}</span><span>Domaine public</span></div>
            <a class="book-link" href="../06-pdf-domaine-public/{b['path']}" target="_blank" rel="noopener">{ext}</a>
          </div>
        </div>"""

    body = f"""
<div class="section">
  <div class="section-head">
    <p class="section-eyebrow">{len(BOOKS)} ouvrages complets, domaine public</p>
    <h1 class="section-title">📚 Bibliothèque des livres complets</h1>
    <p class="section-desc">Tous ces ouvrages sont dans le domaine public (auteurs décédés depuis plus de 70 ans ou
    droits explicitement libérés) et proviennent de bibliothèques numériques reconnues : Internet Archive, Gallica
    (BnF), Project Gutenberg, Les Classiques des sciences sociales (UQAM) et Darwin Online. Ils sont hébergés
    directement dans ce dépôt pour un accès garanti et pérenne.</p>
  </div>
  <div class="grid-2">{cards_html}</div>

  <div class="fun-box" style="margin-top:2rem">
    ℹ️ <strong>Note sur les sources et le droit d'auteur :</strong> tous ces textes ont été publiés avant 1928 (à
    l'exception de traductions dont les traducteurs historiques sont eux-mêmes hors droits ou dont les éditions
    numériques sont explicitement libres de diffusion). Les fiches pédagogiques de ce guide (catégories, quiz,
    flashcards) sont des <strong>contenus originaux</strong> rédigés spécifiquement pour Psyclopédia.
  </div>
</div>
"""
    html = page_shell("Bibliothèque PDF", body, depth=0, active="Bibliothèque")
    with open(os.path.join(BASE, "bibliotheque.html"), "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    render_categories_index()
    for i, cat in enumerate(CATEGORIES):
        render_category(cat, i, len(CATEGORIES))
    render_dictionnaire()
    render_quiz_hub()
    render_quiz_engine_page()
    render_apprendre()
    render_bibliotheque()
    print(f"✅ Généré : {len(CATEGORIES)} catégories + dictionnaire + {len(QUIZZES)} quiz + apprendre + bibliothèque")
