# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Quiz, bibliothèque, lecteur intégré, parcours guidés, guide d'apprentissage."""

import json
import os

from shell import page_shell, page_header
from content import CATEGORIES, QUIZZES, BOOKS, PDF_BOOKS, DICTIONNAIRE, EXPERIENCES, AUTEURS

BASE = os.path.dirname(os.path.abspath(__file__))


def _write(path, html):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)


# --------------------------------------------------------------------------
# Quiz
# --------------------------------------------------------------------------

QUIZ_GROUPS = [
    ("Les fondations", "Méthode, histoire, cognition, société : le socle commun.",
     ["fondamentaux-histoire", "cognitive", "sociale", "developpement-personnalite"]),
    ("L'individu", "Émotions, cerveau, souffrance psychique et soins.",
     ["emotions-motivation", "neurosciences", "psychopathologie", "therapies"]),
    ("Psychologie appliquée", "Le quotidien, le droit, l'animal et les champs émergents.",
     ["vie-quotidienne", "legale-comparee", "interculturelle", "langage", "psychometrie", "sport",
      "consommation", "numerique", "evolutionniste", "vieillissement", "environnementale", "politique"]),
    ("Transversaux et examen", "Vérifie que tu maîtrises les références et l'ensemble du programme.",
     ["experiences-celebres", "biais-cognitifs", "grands-auteurs", "troubles-reconnaitre",
      "chronologie-quiz", "examen-final"]),
]


def render_quiz_hub():
    by_id = {q["id"]: q for q in QUIZZES}
    total_q = sum(len(q["questions"]) for q in QUIZZES)

    sections_html = ""
    for label, desc, ids in QUIZ_GROUPS:
        cards = ""
        for qid in ids:
            quiz = by_id.get(qid)
            if not quiz:
                continue
            n = len(quiz["questions"])
            cards += f"""<a href="quiz.html?id={quiz['id']}" class="quiz-card" data-quiz-id="{quiz['id']}">
              <div class="quiz-card-top">
                <span class="quiz-icon">{quiz['icon']}</span>
                <span class="quiz-best" style="display:none">Meilleur score</span>
              </div>
              <h3>{quiz['title']}</h3>
              <p>{quiz['desc']}</p>
              <div class="quiz-meta"><span>❓ {n} questions</span><span>📊 {quiz['difficulty']}</span><span>📝 Noté /20</span></div>
            </a>"""
        sections_html += f"""
<div class="section-head" style="margin-top:2.5rem">
  <p class="section-eyebrow">{len(ids)} quiz</p>
  <h2 class="section-title" style="font-size:1.5rem">{label}</h2>
  <p class="section-desc">{desc}</p>
</div>
<div class="grid-3">{cards}</div>"""

    body = f"""
<div class="section">
  <div class="section-head">
    <p class="section-eyebrow">{len(QUIZZES)} quiz · {total_q} questions · corrigés expliqués</p>
    <h1 class="section-title">🎮 Teste tes connaissances</h1>
    <p class="section-desc">Chaque quiz est noté sur 20 et fournit un corrigé complet : pour chaque question, la
    bonne réponse et l'explication du raisonnement. Rejoue autant de fois que tu veux — ton meilleur score est
    conservé sur cet appareil et alimente ta progression globale.</p>
  </div>
  <div class="note-box">
    <strong>Conseil d'usage :</strong> passe le quiz <em>avant</em> d'avoir tout lu. Se tromper puis lire la
    correction produit un apprentissage bien plus solide que de lire d'abord et de se tester ensuite — c'est
    l'effet de « test préalable » (<em>pretesting effect</em>).
  </div>
  {sections_html}
</div>
"""
    _write("quiz/index.html", page_shell("Quiz", body, depth=1, active="Quiz",
                                         description=f"{len(QUIZZES)} quiz de psychologie notés sur 20 avec corrigé expliqué : {total_q} questions en français."))


def render_quiz_engine():
    quiz_json = json.dumps(QUIZZES, ensure_ascii=False)
    body = """
<div class="section">
  <div class="section-head" style="text-align:center">
    <p class="section-eyebrow" id="quiz-eyebrow">Quiz</p>
    <h1 class="section-title" id="quiz-title">Chargement…</h1>
  </div>
  <div class="quiz-question" id="quiz-container"></div>
  <div class="cta-row">
    <a class="btn btn-secondary" href="index.html">← Tous les quiz</a>
    <a class="btn btn-secondary" href="../index.html">📂 Catégories</a>
  </div>
</div>
<script id="quiz-data-json" type="application/json">__QUIZDATA__</script>
<script>
(function () {
  var params = new URLSearchParams(window.location.search);
  var quizId = params.get('id') || 'fondamentaux-histoire';
  var all = JSON.parse(document.getElementById('quiz-data-json').textContent);
  var quiz = all.find(function (q) { return q.id === quizId; }) || all[0];
  window.QUIZ_ID = quiz.id;
  window.QUIZ_TITLE = quiz.icon + ' ' + quiz.title;
  window.QUIZ_QUESTIONS = quiz.questions;
})();
</script>
""".replace("__QUIZDATA__", quiz_json)

    _write("quiz/quiz.html", page_shell(
        "Quiz", body, depth=1, active="Quiz",
        extra_scripts='<script src="../../../assets-ebook/js/quiz-engine.js"></script>'))


# --------------------------------------------------------------------------
# Bibliothèque
# --------------------------------------------------------------------------

def render_bibliotheque():
    cards_html = ""
    for b in BOOKS:
        is_pdf = b["path"].endswith(".pdf")
        read_href = ("lecteur.html?livre=../06-pdf-domaine-public/" + b["path"]) if is_pdf \
            else ("../06-pdf-domaine-public/" + b["path"])
        read_label = "📖 Lire dans le site" if is_pdf else "🌐 Lire le texte en ligne"
        dl = (f'<a class="book-link" style="background:var(--card);color:var(--gris);border:1px solid var(--border);margin-top:0.5rem" '
              f'href="../06-pdf-domaine-public/{b["path"]}" target="_blank" rel="noopener">📥 Télécharger le fichier</a>') if is_pdf else ""
        texte_badge = "Texte extractible" if b.get("texte") else "Scan (OCR intégré)"
        cards_html += f"""<div class="book-card">
          <div class="book-cover" style="background:var(--{b['color']})">{b['icon']}</div>
          <div class="book-body">
            <h3>{b['title']}</h3>
            <p class="author">{b['author']} · {b['year']}</p>
            <p class="desc">{b['desc']}</p>
            <div class="book-meta"><span>{b['pages']}</span><span>{b['cat']}</span><span>{texte_badge}</span><span>Domaine public</span></div>
            <a class="book-link" href="{read_href}">{read_label}</a>
            {dl}
          </div>
        </div>"""

    header = page_header(
        depth=0,
        breadcrumb=[("Accueil", "../../index.html"), ("Bibliothèque", None)],
        icon="📚", color="or", title="Bibliothèque des livres complets",
        subtitle=f"{len(BOOKS)} ouvrages du domaine public, intégralement lisibles dans le site",
        chips=[f"📕 {len(BOOKS)} ouvrages", "🔎 Lecture en ligne", "🔤 OCR et modernisation du français"],
    )

    body = f"""{header}
<div class="section">
  <div class="reader-help">
    <strong>Nouveau : tout se lit dans le site.</strong> Plus besoin de télécharger quoi que ce soit. Le
    <a href="lecteur.html">lecteur intégré</a> affiche chaque page, extrait le texte, modernise le français du
    XIXe siècle et lance une reconnaissance optique (OCR) en français sur les ouvrages qui ne sont que des images
    scannées. Tu peux aussi faire traduire la page affichée dans une autre langue.
  </div>
  <div class="cta-row" style="margin-top:0;margin-bottom:2rem">
    <a class="btn btn-primary" href="lecteur.html">📖 Ouvrir le lecteur</a>
    <button class="btn btn-secondary" data-search-open="">🔍 Chercher un livre ou un auteur</button>
  </div>
  <div class="grid-2">{cards_html}</div>

  <div class="note-box" style="margin-top:2rem">
    <strong>Sources et droit d'auteur.</strong> Tous ces textes ont été publiés avant 1928, ou leurs éditions
    numériques sont explicitement libres de diffusion. Ils proviennent d'Internet Archive, de Gallica (BnF), du
    Project Gutenberg, des Classiques des sciences sociales (UQAM) et de Darwin Online, et sont hébergés
    directement dans ce dépôt pour un accès pérenne. Les fiches pédagogiques de Psyclopédia (catégories,
    références, quiz, flashcards) sont en revanche des <strong>contenus originaux</strong> rédigés pour ce guide.
  </div>
  <div class="warn-box">
    <strong>Lire les textes anciens avec recul.</strong> Certains ouvrages ici présentés — en particulier
    <em>L'homme criminel</em> de Lombroso — défendent des thèses aujourd'hui scientifiquement invalidées et
    moralement condamnables. Ils sont proposés comme <strong>documents historiques</strong>, pour comprendre
    comment une discipline se trompe, et non comme sources de connaissance actuelle.
  </div>
</div>
"""
    _write("bibliotheque.html", page_shell("Bibliothèque PDF", body, depth=0, active="Bibliothèque",
                                           description="Bibliothèque de psychologie : 13 ouvrages du domaine public en français, lisibles directement en ligne."))


# --------------------------------------------------------------------------
# Lecteur intégré
# --------------------------------------------------------------------------

def render_lecteur():
    options = "".join(
        f'<option value="../06-pdf-domaine-public/{b["path"]}">{b["title"]} — {b["author"]} ({b["year"]})</option>'
        for b in PDF_BOOKS
    )
    html_books = "".join(
        f'<li><a href="../06-pdf-domaine-public/{b["path"]}" target="_blank" rel="noopener">{b["title"]}</a> — {b["author"]} ({b["year"]})</li>'
        for b in BOOKS if b["path"].endswith(".html")
    )

    header = page_header(
        depth=0,
        breadcrumb=[("Accueil", "../../index.html"), ("Bibliothèque", "bibliotheque.html"), ("Lecteur", None)],
        icon="📖", color="vert", title="Lecteur de livres intégré",
        subtitle="Lire les ouvrages originaux page par page, avec extraction du texte, OCR et traduction",
        chips=[f"📕 {len(PDF_BOOKS)} livres PDF", "🔤 OCR français", "✨ Français modernisé", "🌍 Traduction"],
    )

    body = f"""{header}
<div class="reader-shell" id="reader-root">
  <div class="reader-help">
    <strong>Mode d'emploi.</strong> Choisis un ouvrage, tourne les pages avec les flèches ← → du clavier ou les
    boutons, et ouvre le volet texte pour lire la transcription à côté de l'image. Si le livre est un
    <em>scan sans couche texte</em> (Taine, Durkheim, Lombroso), clique sur <strong>Reconnaître le texte</strong> :
    une reconnaissance optique française s'exécute directement dans ton navigateur, sans envoyer le fichier nulle
    part. <strong>Moderniser le français</strong> réécrit les formes du XIXe siècle (« étoit » → « était »,
    « enfans » → « enfants ») et surligne le vocabulaire ancien : survole un mot surligné pour voir son
    équivalent actuel. La page lue est mémorisée : tu reprends là où tu t'es arrêté.
  </div>

  <div class="reader-bar">
    <select id="book-select" aria-label="Choisir un ouvrage">{options}</select>
    <span class="reader-sep"></span>
    <button class="rbtn" id="btn-prev" disabled>←</button>
    <input class="reader-page-input" id="page-input" type="number" min="1" value="1" disabled aria-label="Numéro de page">
    <span class="ref-count" id="page-total">/ –</span>
    <button class="rbtn" id="btn-next" disabled>→</button>
    <span class="reader-sep"></span>
    <button class="rbtn" id="btn-zoom-out" disabled>−</button>
    <button class="rbtn" id="btn-zoom-in" disabled>+</button>
    <span class="reader-sep"></span>
    <button class="rbtn" id="btn-split" disabled>📖 Afficher le texte</button>
    <button class="rbtn" id="btn-ocr" disabled>🔤 Reconnaître le texte</button>
    <button class="rbtn active" id="btn-modern">✨ Français modernisé</button>
    <span class="reader-sep"></span>
    <select id="lang-select" aria-label="Langue de traduction" style="max-width:150px">
      <option value="fr">Français (original)</option>
      <option value="en">Anglais</option>
      <option value="es">Espagnol</option>
      <option value="de">Allemand</option>
      <option value="it">Italien</option>
      <option value="pt">Portugais</option>
      <option value="ar">Arabe</option>
    </select>
    <button class="rbtn" id="btn-translate">🌍 Traduire</button>
    <span class="reader-spacer"></span>
    <a class="rbtn" id="btn-download" href="#" target="_blank" rel="noopener">📥 Fichier</a>
  </div>

  <div class="reader-status" id="reader-status">Sélectionne un ouvrage pour commencer.</div>
  <div class="reader-status"><div class="reader-progress-track"><div class="reader-progress-fill" id="reader-prog-fill"></div></div></div>

  <div class="reader-grid" id="reader-grid">
    <div class="reader-canvas-wrap"><canvas id="pdf-canvas"></canvas></div>
    <div class="reader-text-pane">
      <h4>Texte de la page <span class="pane-badge" id="reader-badge">—</span></h4>
      <div id="reader-text"><p class="ocr-note">Ouvre le volet texte pour afficher la transcription de la page
      affichée.</p></div>
    </div>
  </div>

  <div class="note-box">
    <strong>Comment fonctionne la reconnaissance optique ?</strong> Le moteur Tesseract, entraîné sur le français,
    est téléchargé une seule fois (environ 3 Mo) puis analyse l'image de la page rendue à l'écran. Le résultat
    dépend de la qualité du scan : sur des impressions du XIXe siècle, il reste quelques confusions
    (« ſ » long lu « f », lettres collées). Le texte obtenu est nettoyé automatiquement — césures de fin de ligne
    recollées, espaces normalisés — avant d'être affiché. Aucune donnée ne quitte ton navigateur pendant l'OCR.
  </div>

  <div class="note-box">
    <strong>Et la traduction ?</strong> Les ouvrages sont déjà en français : le bouton « Traduire » sert à lire une
    page dans une autre langue, ou à aider une personne non francophone. La traduction passe par un service
    automatique gratuit et peut être indisponible ou imprécise : le texte français d'origine reste toujours
    accessible en repassant la langue sur « Français (original) ». Pour le français ancien, c'est le bouton
    <strong>« Moderniser »</strong> qu'il faut utiliser : il travaille entièrement hors ligne, à partir d'un
    glossaire de près de cent termes de psychologie du XIXe siècle.
  </div>

  <h3 style="font-family:var(--serif);margin-top:2rem">Ouvrages disponibles en texte intégral HTML</h3>
  <p style="color:var(--gris);font-size:0.9rem">Ces trois textes sont déjà transcrits : ils s'ouvrent directement
  dans le navigateur, sans lecteur PDF.</p>
  <ul style="color:var(--gris);font-size:0.9rem;padding-left:1.2rem;line-height:2">{html_books}</ul>

  <div class="cta-row">
    <a class="btn btn-secondary" href="bibliotheque.html">📚 Retour à la bibliothèque</a>
    <a class="btn btn-secondary" href="index.html">📂 Catégories</a>
  </div>
</div>
"""
    _write("lecteur.html", page_shell(
        "Lecteur de livres", body, depth=0, active="Bibliothèque",
        description="Lecteur intégré : lire en ligne les livres de psychologie du domaine public, avec OCR français et modernisation du texte.",
        extra_scripts='<script src="../../assets-ebook/js/lecteur.js"></script>'))


# --------------------------------------------------------------------------
# Parcours guidés
# --------------------------------------------------------------------------

PARCOURS = [
    {
        "id": "decouverte", "icon": "🌱", "color": "vert",
        "title": "Découverte — Je pars de zéro",
        "desc": "Le chemin le plus court pour comprendre ce qu'est vraiment la psychologie, sans prérequis. "
                "On installe la méthode, puis on visite les trois grands territoires : la pensée, les autres, le développement.",
        "meta": ["≈ 2 h de lecture", "6 étapes", "Aucun prérequis"],
        "steps": [
            ("categories/01-fondamentaux.html", "Fondamentaux : qu'est-ce que la psychologie ?", "Fiche"),
            ("categories/02-histoire.html", "Histoire : d'où viennent les idées actuelles", "Fiche"),
            ("references/chronologie.html", "Parcourir la chronologie en diagonale", "Références"),
            ("categories/03-cognitive.html", "Cognitive : mémoire, attention, décision", "Fiche"),
            ("categories/04-sociale.html", "Sociale : l'influence des autres", "Fiche"),
            ("quiz/quiz.html?id=fondamentaux-histoire", "Quiz Fondamentaux et histoire", "Quiz noté"),
        ],
    },
    {
        "id": "mieux-se-comprendre", "icon": "🪞", "color": "or",
        "title": "Mieux se comprendre soi-même",
        "desc": "Pourquoi je réagis comme ça ? D'où viennent mes émotions, mes habitudes, ma personnalité ? "
                "Un itinéraire tourné vers l'introspection outillée plutôt que vers la théorie pure.",
        "meta": ["≈ 3 h de lecture", "7 étapes", "Très applicable"],
        "steps": [
            ("categories/07-emotions.html", "Émotions et motivation", "Fiche"),
            ("categories/06-personnalite.html", "Personnalité : les Big Five", "Fiche"),
            ("references/biais.html", "Les biais qui faussent mes jugements", "Références"),
            ("categories/11-positive.html", "Psychologie positive et bien-être", "Fiche"),
            ("categories/14-sante.html", "Stress, sommeil, santé", "Fiche"),
            ("categories/05-developpement.html", "Ce que l'enfance a construit", "Fiche"),
            ("quiz/quiz.html?id=emotions-motivation", "Quiz Émotions et motivation", "Quiz noté"),
        ],
    },
    {
        "id": "clinique", "icon": "🩺", "color": "rose",
        "title": "Comprendre la souffrance psychique",
        "desc": "Reconnaître, comprendre et savoir vers quoi orienter. Ce parcours explique les troubles et, "
                "surtout, ce qui soigne réellement — thérapies validées, mécanismes, limites.",
        "meta": ["≈ 3 h 30 de lecture", "7 étapes", "Sans valeur diagnostique"],
        "steps": [
            ("categories/09-psychopathologie.html", "Psychopathologie : comprendre les troubles", "Fiche"),
            ("references/troubles.html", "Répertoire clinique détaillé", "Références"),
            ("categories/10-therapies.html", "Les thérapies et ce qui les rend efficaces", "Fiche"),
            ("categories/08-neurosciences.html", "Ce que le cerveau nous apprend", "Fiche"),
            ("references/tests.html", "Les instruments d'évaluation", "Références"),
            ("lecteur.html?livre=../06-pdf-domaine-public/psychopathologie/janet-les-nevroses-1909.pdf",
             "Lire Janet, Les névroses (1909)", "Livre original"),
            ("quiz/quiz.html?id=psychopathologie", "Quiz Psychopathologie", "Quiz noté"),
        ],
    },
    {
        "id": "etudiant", "icon": "🎓", "color": "gris",
        "title": "Réviser pour un examen de psychologie",
        "desc": "Couverture complète et efficace : les grands domaines, les expériences et auteurs qu'on cite "
                "systématiquement, la méthodologie, puis l'examen final de 20 questions.",
        "meta": ["≈ 6 h de travail", "9 étapes", "Révision intensive"],
        "steps": [
            ("categories/01-fondamentaux.html", "Méthode scientifique et épistémologie", "Fiche"),
            ("references/experiences.html", "Les expériences incontournables", "Références"),
            ("references/auteurs.html", "Les auteurs et leurs apports", "Références"),
            ("categories/19-psychometrie.html", "Psychométrie : fidélité, validité, étalonnage", "Fiche"),
            ("references/chronologie.html", "Chronologie complète", "Références"),
            ("dictionnaire.html", "Réviser le vocabulaire A-Z", "Dictionnaire"),
            ("quiz/quiz.html?id=grands-auteurs", "Quiz Grands auteurs", "Quiz noté"),
            ("quiz/quiz.html?id=experiences-celebres", "Quiz Expériences célèbres", "Quiz noté"),
            ("quiz/quiz.html?id=examen-final", "Examen final — 20 questions", "Examen"),
        ],
    },
    {
        "id": "pro", "icon": "💼", "color": "vert",
        "title": "Psychologie au travail et dans les organisations",
        "desc": "Pour manager, recruter, enseigner ou simplement survivre en open space : motivation, "
                "biais de décision collective, burn-out, influence et ergonomie.",
        "meta": ["≈ 2 h 30 de lecture", "6 étapes", "Orienté pratique"],
        "steps": [
            ("categories/12-travail.html", "Psychologie du travail et des organisations", "Fiche"),
            ("references/biais.html", "Biais de décision et de recrutement", "Références"),
            ("categories/04-sociale.html", "Conformité, autorité, dynamique de groupe", "Fiche"),
            ("categories/21-consommation.html", "Psychologie du consommateur et influence", "Fiche"),
            ("references/tests.html", "Tests utilisés en entreprise (et leurs limites)", "Références"),
            ("quiz/quiz.html?id=vie-quotidienne", "Quiz Psychologie du quotidien", "Quiz noté"),
        ],
    },
    {
        "id": "curieux", "icon": "🔭", "color": "or",
        "title": "Les frontières de la discipline",
        "desc": "Pour ceux qui connaissent déjà les bases : culture, langage, évolution, numérique, "
                "environnement, politique — là où la psychologie se renouvelle aujourd'hui.",
        "meta": ["≈ 3 h de lecture", "7 étapes", "Niveau avancé"],
        "steps": [
            ("categories/17-interculturelle.html", "Interculturelle : le biais WEIRD", "Fiche"),
            ("categories/18-langage.html", "Psycholinguistique", "Fiche"),
            ("categories/23-evolutionniste.html", "Psychologie évolutionniste", "Fiche"),
            ("categories/22-numerique.html", "Psychologie du numérique", "Fiche"),
            ("categories/25-environnementale.html", "Psychologie environnementale", "Fiche"),
            ("categories/26-politique.html", "Croyances, complotisme, polarisation", "Fiche"),
            ("quiz/quiz.html?id=interculturelle", "Quiz Psychologie interculturelle", "Quiz noté"),
        ],
    },
]


def render_parcours():
    cards = ""
    for p in PARCOURS:
        steps = "".join(
            f'<a class="path-step" href="{href}"><span class="path-step-n">{i}</span>'
            f'<span class="path-step-title">{label}</span><span class="path-step-kind">{kind}</span></a>'
            for i, (href, label, kind) in enumerate(p["steps"], 1)
        )
        meta = "".join(f"<span>{m}</span>" for m in p["meta"])
        cards += f"""<div class="path-card" id="{p['id']}">
          <div class="path-head">
            <div class="path-ico" style="background:var(--{p['color']}-light)">{p['icon']}</div>
            <div>
              <h3>{p['title']}</h3>
              <p>{p['desc']}</p>
              <div class="path-meta">{meta}</div>
            </div>
          </div>
          <div class="path-steps">{steps}</div>
        </div>"""

    header = page_header(
        depth=0,
        breadcrumb=[("Accueil", "../../index.html"), ("Parcours", None)],
        icon="🧭", color="vert", title="Parcours d'apprentissage guidés",
        subtitle="Six itinéraires balisés selon ton objectif, plutôt que 26 fiches en vrac",
        chips=[f"🧭 {len(PARCOURS)} parcours", f"📍 {sum(len(p['steps']) for p in PARCOURS)} étapes", "✅ Progression sauvegardée"],
    )

    body = f"""{header}
<div class="section">
  <p class="section-desc" style="max-width:760px">Face à une encyclopédie, la difficulté n'est pas de trouver du
  contenu : c'est de savoir par où commencer. Chaque parcours enchaîne fiches, références, livres originaux et
  quiz dans un ordre pensé pour un objectif précis. Les étapes déjà consultées apparaissent cochées, et rien ne
  t'empêche de sortir du chemin en cours de route.</p>
  {cards}
  <div class="cta-row">
    <a class="btn btn-primary" href="apprendre.html">🧠 Comment apprendre efficacement</a>
    <a class="btn btn-secondary" href="index.html">📂 Voir toutes les catégories</a>
  </div>
</div>
"""
    _write("parcours.html", page_shell("Parcours guidés", body, depth=0, active="Apprendre",
                                       description="Six parcours d'apprentissage guidés en psychologie : débutant, introspection, clinique, révision d'examen, travail, sujets avancés."))


# --------------------------------------------------------------------------
# Guide d'apprentissage
# --------------------------------------------------------------------------

def render_apprendre():
    n_sections = sum(len(c["sections"]) for c in CATEGORIES)
    n_flash = sum(len(c.get("flashcards", [])) for c in CATEGORIES)
    n_questions = sum(len(q["questions"]) for q in QUIZZES)

    header = page_header(
        depth=0,
        breadcrumb=[("Accueil", "../../index.html"), ("Apprendre", None)],
        icon="🧠", color="rose", title="Apprendre efficacement",
        subtitle="Ce que la science cognitive dit vraiment de la mémorisation — et comment l'appliquer ici",
        chips=["🔬 5 techniques validées", "🧑‍🎨 4 profils VARK", "📅 Planning de révision"],
    )

    body = f"""{header}
<div class="wrap with-toc">
  <aside class="toc-side"><h4>Sommaire</h4>
    <a href="#ressources">Ce que contient le site</a>
    <a href="#vark">Quel est ton profil ?</a>
    <a href="#techniques">5 techniques validées</a>
    <a href="#planning">Organiser ses révisions</a>
    <a href="#erreurs">Erreurs à éviter</a>
    <a href="#plan">Un plan sur 30 jours</a>
  </aside>
  <div class="content" style="max-width:none">

  <h2 id="ressources">Ce que tu as à disposition</h2>
  <p>Avant de parler méthode, un état des lieux : savoir ce qui existe évite de relire dix fois la même fiche
  en ignorant les outils les plus efficaces.</p>
  <div class="stat-strip">
    <div class="stat-cell"><div class="val">{len(CATEGORIES)}</div><div class="lbl">catégories complètes</div></div>
    <div class="stat-cell"><div class="val">{n_sections}</div><div class="lbl">chapitres rédigés</div></div>
    <div class="stat-cell"><div class="val">{n_flash}</div><div class="lbl">flashcards de rappel actif</div></div>
    <div class="stat-cell"><div class="val">{n_questions}</div><div class="lbl">questions de quiz corrigées</div></div>
    <div class="stat-cell"><div class="val">{len(DICTIONNAIRE)}</div><div class="lbl">notions au dictionnaire</div></div>
    <div class="stat-cell"><div class="val">{len(EXPERIENCES) + len(AUTEURS)}</div><div class="lbl">expériences et auteurs</div></div>
  </div>

  <h2 id="vark">🧑‍🎨 Quel est ton profil d'apprentissage ? (modèle VARK)</h2>
  <p>Le modèle VARK distingue quatre préférences perceptives. Attention : l'idée qu'il faudrait enseigner à
  chacun dans « son » style est un <strong>neuromythe</strong> — les études contrôlées ne montrent aucun gain.
  En revanche, <em>varier</em> les canaux fonctionne pour tout le monde, parce que chaque encodage
  supplémentaire crée une voie d'accès de plus au souvenir. Sers-toi donc de cette grille comme d'une liste
  d'activités à combiner, pas comme d'une étiquette.</p>

  <div class="vark-grid">
    <div class="vark-card" style="border-top-color:var(--vert)">
      <span class="emoji">👁️</span><h3>Visuel</h3>
      <p>Schémas, couleurs, images.</p>
      <ul><li>Observe les portraits et illustrations de chaque fiche</li>
      <li>Dessine ta propre carte mentale d'une catégorie</li>
      <li>Code par couleur : théorie, expérience, critique</li></ul>
    </div>
    <div class="vark-card" style="border-top-color:var(--or)">
      <span class="emoji">👂</span><h3>Auditif</h3>
      <p>Écouter, expliquer à voix haute.</p>
      <ul><li>Relis les encadrés « Le savais-tu ? » à voix haute</li>
      <li>Explique une expérience à quelqu'un qui n'y connaît rien</li>
      <li>Enregistre-toi en résumant une fiche, puis réécoute</li></ul>
    </div>
    <div class="vark-card" style="border-top-color:var(--rose)">
      <span class="emoji">✍️</span><h3>Lecture / Écriture</h3>
      <p>Lire, reformuler par écrit.</p>
      <ul><li>Résume chaque fiche en cinq lignes, sans la relire</li>
      <li>Rédige tes propres définitions avant de lire celles du dictionnaire</li>
      <li>Note les objections que tu as en lisant</li></ul>
    </div>
    <div class="vark-card" style="border-top-color:var(--gris)">
      <span class="emoji">🤸</span><h3>Kinesthésique</h3>
      <p>Manipuler, tester, pratiquer.</p>
      <ul><li>Commence par le quiz, avant même d'avoir lu</li>
      <li>Applique chaque notion à une situation que tu as vécue</li>
      <li>Refais mentalement le protocole de chaque expérience</li></ul>
    </div>
  </div>

  <h2 id="techniques">🔬 Cinq techniques réellement validées</h2>
  <div class="method-timeline">
    <div class="method-item"><div class="num">01</div><div>
      <h4>Le rappel actif (<em>testing effect</em>)</h4>
      <p>Se tester — même en échouant — ancre l'information bien plus durablement que relire. Roediger et
      Karpicke (2006) ont montré qu'un groupe ayant révisé par auto-test retenait environ 50 % du matériel une
      semaine plus tard, contre environ 25 % pour un groupe ayant relu quatre fois, alors que ce dernier se
      sentait <em>plus</em> confiant. La sensation de facilité produite par la relecture est trompeuse.
      <strong>Ici :</strong> flashcards et quiz, systématiquement, avant de regarder la réponse.</p></div></div>
    <div class="method-item"><div class="num">02</div><div>
      <h4>La répétition espacée</h4>
      <p>La courbe de l'oubli d'Ebbinghaus (1885) montre qu'on perd la majeure partie d'un contenu en quelques
      jours — sauf si l'on révise à intervalles croissants. Le rythme 1 jour / 3 jours / 1 semaine / 1 mois est
      un bon compromis. <strong>Ici :</strong> la progression enregistrée te montre les catégories déjà visitées ;
      reviens dessus au lieu d'avancer toujours vers du neuf.</p></div></div>
    <div class="method-item"><div class="num">03</div><div>
      <h4>L'entrelacement (<em>interleaving</em>)</h4>
      <p>Alterner les thèmes plutôt que d'épuiser un sujet améliore la capacité à <em>distinguer</em> les
      notions — ce qui est précisément ce qu'un examen demande. C'est plus inconfortable sur le moment et plus
      efficace à terme. <strong>Ici :</strong> alterne une fiche cognitive, une fiche sociale, une page de
      références, plutôt que de lire les 26 catégories dans l'ordre.</p></div></div>
    <div class="method-item"><div class="num">04</div><div>
      <h4>L'élaboration et l'auto-explication</h4>
      <p>Se demander « pourquoi est-ce vrai ? », « en quoi est-ce différent de ce que je viens de lire ? »,
      « à quoi ça ressemble dans ma vie ? » force à construire des liens, seule façon de transformer une
      information isolée en connaissance mobilisable. <strong>Ici :</strong> après chaque section, formule une
      question « pourquoi » et tente d'y répondre.</p></div></div>
    <div class="method-item"><div class="num">05</div><div>
      <h4>Le double codage</h4>
      <p>Associer verbal et visuel crée deux voies d'accès au souvenir. Ce n'est pas la même chose que le
      « style visuel » : le double codage fonctionne chez tout le monde. <strong>Ici :</strong> pour chaque
      expérience, visualise la scène du protocole ; pour chaque auteur, associe le visage au nom.</p></div></div>
  </div>

  <h2 id="planning">⏱️ Organiser ses sessions</h2>
  <p>La technique <strong>Pomodoro</strong> (25 minutes concentrées, 5 de pause, pause longue toutes les quatre
  sessions) aide à tenir dans la durée. Le point décisif est ailleurs : fixe un objectif <em>vérifiable</em> par
  session (« être capable de citer les cinq traits du Big Five et un exemple pour chacun ») plutôt qu'un objectif
  de temps (« réviser une heure »). Sans critère de réussite, impossible de savoir si la session a servi.</p>
  <p>Le sommeil n'est pas du temps perdu pour la révision : la consolidation mnésique s'effectue en grande partie
  pendant le sommeil lent profond. Une nuit complète après une session vaut mieux qu'une heure de révision
  supplémentaire prise sur cette nuit.</p>

  <h2 id="erreurs">🚫 Les cinq erreurs les plus coûteuses</h2>
  <div class="myth-grid">
    <div class="myth-card"><div class="myth-false"><span class="tag">❌</span><span>Surligner et relire.</span></div>
      <div class="myth-true"><span class="tag">✅</span><span>Ce sont les deux techniques les moins efficaces jamais mesurées, et les plus utilisées. Elles produisent un fort sentiment de maîtrise sans mémorisation correspondante. Remplace-les par l'auto-test.</span></div></div>
    <div class="myth-card"><div class="myth-false"><span class="tag">❌</span><span>Réviser tout d'un coup la veille.</span></div>
      <div class="myth-true"><span class="tag">✅</span><span>Le bachotage permet de passer l'épreuve et d'oublier en une semaine. À temps total égal, quatre sessions espacées battent largement une session massée.</span></div></div>
    <div class="myth-card"><div class="myth-false"><span class="tag">❌</span><span>Éviter la difficulté.</span></div>
      <div class="myth-true"><span class="tag">✅</span><span>Les « difficultés désirables » de Bjork — se tester, espacer, entrelacer — ralentissent l'apprentissage immédiat et améliorent la rétention durable. L'inconfort est un signal, pas une erreur.</span></div></div>
    <div class="myth-card"><div class="myth-false"><span class="tag">❌</span><span>Travailler en multitâche.</span></div>
      <div class="myth-true"><span class="tag">✅</span><span>Le coût de commutation attentionnelle est massif : chaque bascule vers une notification impose plusieurs minutes pour retrouver le niveau de concentration antérieur.</span></div></div>
    <div class="myth-card"><div class="myth-false"><span class="tag">❌</span><span>Confondre comprendre et retenir.</span></div>
      <div class="myth-true"><span class="tag">✅</span><span>Comprendre une explication est nécessaire mais très insuffisant : sans rappel actif, la compréhension s'efface comme le reste. Le test est la seule preuve fiable.</span></div></div>
  </div>

  <h2 id="plan">📅 Un plan concret sur 30 jours</h2>
  <p>À raison de 30 à 45 minutes par jour, ce rythme couvre l'ensemble du site tout en respectant l'espacement.</p>
  <div class="method-timeline">
    <div class="method-item"><div class="num">J1<br>J8</div><div><h4>Semaine 1 — Les socles</h4>
      <p>Une catégorie par jour parmi les fiches 1 à 8, flashcards immédiatement après chaque lecture. Le
      dimanche : quiz Fondamentaux et histoire, puis quiz Cognitive.</p></div></div>
    <div class="method-item"><div class="num">J9<br>J15</div><div><h4>Semaine 2 — Clinique et applications</h4>
      <p>Fiches 9 à 14, en alternant chaque jour avec dix minutes de révision d'une fiche de la semaine 1
      (entrelacement + espacement). Le week-end : répertoire des troubles et quiz Psychopathologie.</p></div></div>
    <div class="method-item"><div class="num">J16<br>J22</div><div><h4>Semaine 3 — Références</h4>
      <p>Expériences célèbres et grandes figures, dix fiches par jour en survol, puis quiz correspondants.
      Ajoute la chronologie et vingt entrées du dictionnaire par jour.</p></div></div>
    <div class="method-item"><div class="num">J23<br>J30</div><div><h4>Semaine 4 — Frontières et consolidation</h4>
      <p>Fiches 17 à 26, une par jour. Reprends les quiz déjà passés dont le score était inférieur à 15/20.
      Termine par l'examen final de 20 questions — sans rien relire juste avant.</p></div></div>
  </div>

  <div class="fun-box">💡 <strong>Le seul indicateur qui compte :</strong> pouvoir expliquer une notion à voix
  haute, sans notes, à quelqu'un qui n'y connaît rien. Si tu bloques, ce n'est pas « presque acquis » — c'est
  le signal exact de ce qu'il faut réviser.</div>

  <div class="cta-row">
    <a class="btn btn-primary" href="parcours.html">🧭 Choisir un parcours guidé</a>
    <a class="btn btn-secondary" href="index.html">📂 Toutes les catégories</a>
    <a class="btn btn-secondary" href="quiz/index.html">🎮 Tous les quiz</a>
  </div>
  </div>
</div>
"""
    _write("apprendre.html", page_shell("Apprendre efficacement", body, depth=0, active="Apprendre",
                                        description="Guide d'apprentissage : techniques validées par la science cognitive pour mémoriser durablement la psychologie."))


# --------------------------------------------------------------------------
# Crédits et sources
# --------------------------------------------------------------------------

def render_credits():
    from data_credits import CREDITS, SOURCES_LIVRES

    rows = "".join(
        f'<tr><td style="padding:0.5rem 0.8rem;border-bottom:1px solid var(--border)">'
        f'<img src="../05-larousse-illustre-complet/illustrations/wikimedia/{fichier}" alt="{desc}" '
        f'loading="lazy" style="width:46px;height:46px;object-fit:cover;border-radius:8px"></td>'
        f'<td style="padding:0.5rem 0.8rem;border-bottom:1px solid var(--border);font-size:0.85rem">{desc}</td>'
        f'<td style="padding:0.5rem 0.8rem;border-bottom:1px solid var(--border);font-size:0.78rem;color:var(--gris)">'
        f'<a href="https://commons.wikimedia.org/wiki/File:{commons.replace(" ", "_")}" target="_blank" rel="noopener">{commons}</a></td>'
        f'<td style="padding:0.5rem 0.8rem;border-bottom:1px solid var(--border);font-size:0.78rem;white-space:nowrap">{licence}</td></tr>'
        for fichier, commons, licence, desc in CREDITS
    )

    sources = "".join(
        f'<li style="margin-bottom:0.7rem"><a href="{url}" target="_blank" rel="noopener"><strong>{nom}</strong></a> — {desc}</li>'
        for nom, url, desc in SOURCES_LIVRES
    )

    header = page_header(
        depth=0,
        breadcrumb=[("Accueil", "../../index.html"), ("Crédits", None)],
        icon="©", color="gris", title="Crédits, sources et licences",
        subtitle="D'où vient chaque image, chaque livre et chaque texte de ce guide",
        chips=[f"🖼️ {len(CREDITS)} illustrations", f"📚 {len(SOURCES_LIVRES)} bibliothèques sources", "⚖️ Licences libres"],
    )

    body = f"""{header}
<div class="section">
  <h2 style="font-family:var(--serif);font-size:1.4rem;margin-bottom:0.8rem">Les textes de Psyclopédia</h2>
  <p style="color:var(--gris);max-width:760px">Les fiches de catégorie, les notices de références, les définitions
  du dictionnaire, les flashcards et les questions de quiz sont des <strong>contenus originaux</strong> rédigés
  spécifiquement pour ce guide. Ils synthétisent l'état des connaissances en psychologie scientifique, sans
  reproduire de texte protégé. Ils sont mis à disposition dans le même esprit que le reste du dépôt : librement
  consultables, réutilisables et modifiables à des fins pédagogiques.</p>

  <h2 style="font-family:var(--serif);font-size:1.4rem;margin:2rem 0 0.8rem">Les ouvrages</h2>
  <p style="color:var(--gris);max-width:760px">Tous les livres hébergés dans ce dépôt sont dans le domaine public :
  publiés avant 1928, ou dont les auteurs et traducteurs sont décédés depuis plus de soixante-dix ans. Ils
  proviennent des bibliothèques numériques suivantes, que nous remercions pour leur travail de numérisation.</p>
  <ul style="color:var(--gris);font-size:0.9rem;padding-left:1.2rem;line-height:1.7;margin-top:1rem">{sources}</ul>

  <h2 style="font-family:var(--serif);font-size:1.4rem;margin:2rem 0 0.8rem">Les illustrations</h2>
  <p style="color:var(--gris);max-width:760px">Toutes les images proviennent de Wikimedia Commons et sont
  soit dans le domaine public, soit sous licence libre (CC0, CC BY, CC BY-SA). Les licences CC BY et CC BY-SA
  imposent de citer la source et de conserver la même licence en cas de réutilisation : le tableau ci-dessous
  recense chaque fichier, son original sur Commons et sa licence exacte.</p>

  <div style="overflow-x:auto;margin-top:1.2rem;background:var(--card);border-radius:var(--radius);box-shadow:var(--shadow);padding:0.5rem">
    <table style="width:100%;border-collapse:collapse;min-width:640px">
      <thead><tr style="text-align:left">
        <th style="padding:0.6rem 0.8rem;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.06em;color:var(--gris)">Aperçu</th>
        <th style="padding:0.6rem 0.8rem;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.06em;color:var(--gris)">Sujet</th>
        <th style="padding:0.6rem 0.8rem;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.06em;color:var(--gris)">Fichier d'origine</th>
        <th style="padding:0.6rem 0.8rem;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.06em;color:var(--gris)">Licence</th>
      </tr></thead>
      <tbody>{rows}</tbody>
    </table>
  </div>

  <div class="note-box">
    <strong>Une erreur d'attribution ?</strong> Les métadonnées ont été relevées automatiquement via l'API de
    Wikimedia Commons, puis vérifiées une à une. Si une attribution vous semble inexacte, elle peut être
    corrigée dans <code>livres-psychologie/07-ebook-final/data_credits.py</code>.
  </div>

  <div class="cta-row">
    <a class="btn btn-secondary" href="bibliotheque.html">📚 La bibliothèque</a>
    <a class="btn btn-secondary" href="index.html">📂 Les catégories</a>
  </div>
</div>
"""
    _write("credits.html", page_shell("Crédits et sources", body, depth=0, active="Bibliothèque",
                                      description="Crédits, sources et licences des illustrations et des ouvrages de Psyclopédia."))


def render_all():
    render_quiz_hub()
    render_quiz_engine()
    render_bibliotheque()
    render_lecteur()
    render_parcours()
    render_apprendre()
    render_credits()
