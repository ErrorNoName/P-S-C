#!/usr/bin/env python3
"""Build the complete illustrated Larousse-style psychology learning site."""

from pathlib import Path
import json

BASE = Path(__file__).parent
ROOT = BASE.parent
CAT = BASE / "categories"
JEUX = BASE / "jeux"
PDF = ROOT / "06-pdf-domaine-public"

CAT.mkdir(exist_ok=True)
JEUX.mkdir(exist_ok=True)

CATEGORIES = [
    {
        "id": "01-fondamentaux",
        "icon": "🧠",
        "title": "Les Fondamentaux",
        "subtitle": "Qu'est-ce que la psychologie ?",
        "color": "#6B46C1",
        "pdf": "../06-pdf-domaine-public/psychologie-generale/james-precis-de-psychologie-1909.pdf",
        "pdf_label": "William James — Précis de psychologie (1909)",
    },
    {
        "id": "02-histoire",
        "icon": "📜",
        "title": "Histoire de la Psychologie",
        "subtitle": "Des fondateurs aux révolutions",
        "color": "#2B6CB0",
        "pdf": "../06-pdf-domaine-public/histoire-psychologie/wundt-principles-psychology-vol1.pdf",
        "pdf_label": "Wilhelm Wundt — Principles of Physiological Psychology (1874, EN)",
    },
    {
        "id": "03-cognition",
        "icon": "💭",
        "title": "Psychologie Cognitive",
        "subtitle": "Mémoire, attention, perception",
        "color": "#319795",
        "pdf": "../06-pdf-domaine-public/psychologie-generale/binet-suggestibilite.html",
        "pdf_label": "Alfred Binet — La Suggestibilité (Gutenberg)",
    },
    {
        "id": "04-emotions",
        "icon": "❤️",
        "title": "Émotions & Sentiments",
        "subtitle": "Ressentir, exprimer, réguler",
        "color": "#E53E3E",
        "pdf": None,
        "pdf_label": "Th. Ribot — La psychologie des sentiments (Gallica)",
    },
    {
        "id": "05-developpement",
        "icon": "🌱",
        "title": "Développement",
        "subtitle": "De l'enfance à l'âge adulte",
        "color": "#38A169",
        "pdf": "../06-pdf-domaine-public/psychologie-generale/le-bon-psychologie-education.html",
        "pdf_label": "Gustave Le Bon — Psychologie de l'éducation (Gutenberg)",
    },
    {
        "id": "06-sociale",
        "icon": "👥",
        "title": "Psychologie Sociale",
        "subtitle": "Foules, groupes, influence",
        "color": "#DD6B20",
        "pdf": "../06-pdf-domaine-public/psychologie-sociale/le-bon-psychologie-des-foules-1895-complet.pdf",
        "pdf_label": "Gustave Le Bon — Psychologie des foules (1895, 204 p., Archive.org)",
    },
    {
        "id": "07-clinique",
        "icon": "🛋️",
        "title": "Psychologie Clinique",
        "subtitle": "Pathologies et thérapies",
        "color": "#805AD5",
        "pdf": "../06-pdf-domaine-public/psychologie-clinique/freud-interpretation-reves-1900.html",
        "pdf_label": "Freud — L'interprétation des rêves (trad. fr., Gutenberg)",
    },
    {
        "id": "08-neurosciences",
        "icon": "🔬",
        "title": "Neurosciences",
        "subtitle": "Cerveau, neurones, plasticité",
        "color": "#00B5D8",
        "pdf": None,
        "pdf_label": None,
    },
    {
        "id": "09-comparative",
        "icon": "🐾",
        "title": "Psychologie Comparée",
        "subtitle": "Homme et animal",
        "color": "#D69E2E",
        "pdf": "../06-pdf-domaine-public/psychologie-comparative/joly-homme-animal-gallica.html",
        "pdf_label": "Henri Joly — L'homme et l'animal (1886, Gallica)",
    },
    {
        "id": "10-dictionnaire",
        "icon": "📖",
        "title": "Dictionnaire A–Z",
        "subtitle": "200+ notions essentielles",
        "color": "#1A365D",
        "pdf": None,
        "pdf_label": None,
    },
]

DICT = [
    ("Abandon", "Sentiment de rejet lié aux premières relations d'attachement.", "07-clinique"),
    ("Addiction", "Dépendance avec tolérance et sevrage.", "07-clinique"),
    ("Agoraphobie", "Peur des espaces ouverts ou d'évasion difficile.", "07-clinique"),
    ("Amygdale", "Structure cérébrale du traitement de la peur.", "08-neurosciences"),
    ("Anxiété", "Réaction émotionnelle face à une menace perçue.", "04-emotions"),
    ("Asch", "Expériences de conformité sociale (1951).", "06-sociale"),
    ("Attachement", "Lien affectif enfant-soignant (Bowlby).", "05-developpement"),
    ("Autisme", "Trouble du neurodéveloppement (TSA).", "07-clinique"),
    ("Behaviorisme", "Étude du comportement observable.", "01-fondamentaux"),
    ("Biais cognitif", "Erreur systématique de jugement.", "03-cognition"),
    ("Binet", "Créateur du test d'intelligence (1857–1911).", "02-histoire"),
    ("Burn-out", "Épuisement professionnel.", "07-clinique"),
    ("Charge mentale", "Travail invisible de gestion du quotidien.", "06-sociale"),
    ("Cognition", "Processus mentaux : perception, mémoire, raisonnement.", "03-cognition"),
    ("Conditionnement", "Apprentissage par association ou conséquences.", "01-fondamentaux"),
    ("Conscience", "Awareness de soi et de l'environnement.", "01-fondamentaux"),
    ("Dépression", "Trouble de l'humeur avec anhédonie.", "07-clinique"),
    ("Dopamine", "Neurotransmetteur de la récompense.", "08-neurosciences"),
    ("Dyslexie", "Trouble spécifique de la lecture.", "05-developpement"),
    ("EMDR", "Thérapie par mouvements oculaires (trauma).", "07-clinique"),
    ("Empathie", "Comprendre les émotions d'autrui.", "04-emotions"),
    ("Flow", "État d'absorption optimale (Csikszentmihalyi).", "03-cognition"),
    ("Freud", "Fondateur psychanalyse (1856–1939).", "02-histoire"),
    ("Hippocampe", "Formation des souvenirs.", "08-neurosciences"),
    ("Hypnose", "État modifié de conscience thérapeutique.", "07-clinique"),
    ("Inconscient", "Processus mentaux hors conscience.", "07-clinique"),
    ("Intelligence", "Capacité d'adaptation et d'apprentissage.", "03-cognition"),
    ("Le Bon", "Psychologie des foules (1841–1931).", "02-histoire"),
    ("Mémoire", "Encodage, stockage, récupération.", "03-cognition"),
    ("Milgram", "Expériences d'obéissance à l'autorité (1963).", "06-sociale"),
    ("Mindfulness", "Pleine conscience sans jugement.", "07-clinique"),
    ("Neuroplasticité", "Réorganisation cérébrale par l'expérience.", "08-neurosciences"),
    ("OCD", "Trouble obsessionnel compulsif.", "07-clinique"),
    ("Pavlov", "Conditionnement classique (1849–1936).", "02-histoire"),
    ("PERMA", "Modèle du bien-être (Seligman).", "04-emotions"),
    ("Phobie", "Peur intense et irrationnelle.", "07-clinique"),
    ("Piaget", "Stades du développement cognitif.", "02-histoire"),
    ("Placebo", "Effet thérapeutique sans principe actif.", "07-clinique"),
    ("PTSD", "Trouble de stress post-traumatique.", "07-clinique"),
    ("Psychose", "Perte de contact avec la réalité.", "07-clinique"),
    ("Ribot", "Pionnier psychologie française (1839–1916).", "02-histoire"),
    ("Rorschach", "Test projectif d'encre (1921).", "07-clinique"),
    ("Résilience", "Capacité à rebondir face à l'adversité.", "04-emotions"),
    ("Rogers", "Thérapie centrée sur la personne.", "02-histoire"),
    ("Schizophrénie", "Trouble psychotique majeur.", "07-clinique"),
    ("Skinner", "Conditionnement opérant (1904–1990).", "02-histoire"),
    ("Stress", "Réponse à une demande environnementale.", "04-emotions"),
    ("TCC", "Thérapie cognitivo-comportementale.", "07-clinique"),
    ("Transfert", "Projection sur le thérapeute.", "07-clinique"),
    ("Wundt", "Premier laboratoire de psychologie (1832–1920).", "02-histoire"),
    ("Zézaiement", "Répétition involontaire de sons.", "05-developpement"),
]

CATEGORY_CONTENT = {
    "01-fondamentaux": {
        "intro": "La psychologie est la science du comportement et des processus mentaux.",
        "sections": [
            ("Définition", "Étudier comment nous percevons, pensons, ressentons et agissons — seuls et en groupe."),
            ("Méthodes", "Expérimentation, observation, entretien clinique, neuroimagerie, études longitudinales."),
            ("Éthique", "Consentement éclairé, confidentialité, bienfaisance — essentiels depuis Nuremberg."),
            ("Grandes écoles", "Structuralisme, psychanalyse, behaviorisme, cognitivisme, humanisme, neurosciences."),
        ],
        "illus": "cerveau-lobes-fr.svg",
        "fun_fact": "Le mot « psychologie » vient du grec ψυχή (psukhê, âme) et λόγος (logos, étude).",
    },
    "02-histoire": {
        "intro": "De la philosophie à la science expérimentale : 2500 ans d'exploration de l'esprit.",
        "sections": [
            ("1879 — Wundt", "Premier laboratoire de psychologie expérimentale à Leipzig."),
            ("1890 — James", "Précis de psychologie : fonctionnalisme et stream of consciousness."),
            ("1900 — Freud", "L'interprétation des rêves : révolution de l'inconscient."),
            ("1913 — Watson", "Manifeste behavioriste : exit l'introspection."),
            ("1954 — Skinner", "Conditionnement opérant et boîte de Skinner."),
            ("1960+ — Révolution cognitive", "Retour à l'étude des processus mentaux avec l'informatique."),
        ],
        "illus": "portrait-wundt",
        "portraits": ["portrait-binet.jpg", "portrait-freud.jpg", "portrait-pavlov.jpg", "portrait-skinner.jpg", "portrait-le-bon.jpg"],
        "fun_fact": "Wilhelm Wundt est considéré comme le père de la psychologie expérimentale.",
    },
    "03-cognition": {
        "intro": "Comment le cerveau traite l'information : perception, attention, mémoire, langage.",
        "sections": [
            ("Mémoire de travail", "Baddeley : phonologique + visuo-spatiale + exécutif central."),
            ("Biais cognitifs", "Disponibilité, ancrage, confirmation — raccourcis utiles mais piégeux."),
            ("Mémoire reconstructive", "Loftus : les souvenirs peuvent être modifiés par suggestion."),
            ("Attention sélective", "Gorille invisible : nous ne voyons que ce que nous attendons."),
        ],
        "illus": "cerveau-grays-anatomy.svg",
        "fun_fact": "La mémoire à court terme retient environ 7±2 éléments (Miller, 1956).",
    },
    "04-emotions": {
        "intro": "Joie, peur, colère, tristesse, dégoût, surprise — universelles ou culturelles ?",
        "sections": [
            ("Théorie de James-Lange", "Émotion = perception des changements corporels."),
            ("Théorie de Schachter-Singer", "Arousal + étiquetage cognitif = émotion."),
            ("Intelligence émotionnelle", "Goleman : percevoir, comprendre, gérer les émotions."),
            ("Régulation émotionnelle", "Recadrage, suppression, acceptation (ACT)."),
        ],
        "illus": "pyramide-maslow.svg",
        "fun_fact": "L'amygdale traite la peur en ~12 millisecondes, avant la conscience.",
    },
    "05-developpement": {
        "intro": "Comment l'esprit humain se construit de la conception à la vieillesse.",
        "sections": [
            ("Piaget", "4 stades : sensorimoteur, préopératoire, concret, formel."),
            ("Bowlby-Ainsworth", "Attachement sûr, anxieux, évitant, désorganisé."),
            ("Erikson", "8 stades psychosociaux de la crise d'identité."),
            ("Théorie de l'esprit", "Vers 4 ans : comprendre que les autres ont des croyances différentes."),
        ],
        "illus": "portrait-piaget.png",
        "fun_fact": "Les bébés préfèrent les visages dès la naissance — preuve d'un module social inné.",
    },
    "06-sociale": {
        "intro": "Comment le groupe transforme l'individu : conformité, obéissance, influence.",
        "sections": [
            ("Le Bon", "La foule est une entité émotionnelle, irrationnelle, contagieuse."),
            ("Asch", "75% se conforment au moins une fois à une réponse fausse."),
            ("Milgram", "65% obéissent à une autorité jusqu'aux chocs « mortels »."),
            ("Effet témoin", "Plus de témoins = moins d'intervention (Genovese, 1964)."),
        ],
        "illus": "portrait-le-bon.jpg",
        "fun_fact": "Le Bon a inspiré les propagandes du XXe siècle — à lire avec esprit critique.",
    },
    "07-clinique": {
        "intro": "Comprendre la souffrance psychique et les approches thérapeutiques.",
        "sections": [
            ("Psychanalyse", "Freud : inconscient, transfert, résistance, interprétation."),
            ("TCC", "Beck : pensées automatiques, distorsions, restructuration."),
            ("Troubles anxieux", "GAD, phobies, panique, TOC — spectre large."),
            ("Troubles de l'humeur", "Dépression, bipolarité — neurobiologie + psychothérapie."),
        ],
        "illus": "rorschach-planche-1.jpg",
        "fun_fact": "La TCC est la thérapie la plus validée empiriquement pour l'anxiété et la dépression.",
    },
    "08-neurosciences": {
        "intro": "Le cerveau : 86 milliards de neurones, 100 trillions de synapses.",
        "sections": [
            ("Lobes cérébraux", "Frontal (décision), pariétal (sensoriel), temporal (langage), occipital (vision)."),
            ("Neurotransmetteurs", "Dopamine, sérotonine, GABA, glutamate, noradrénaline."),
            ("Neuroplasticité", "Le cerveau se reconfigure tout au long de la vie."),
            ("Neuroimagerie", "IRMf, EEG, PET — voir le cerveau en action."),
        ],
        "illus": "cerveau-humain.svg",
        "fun_fact": "Le cerveau consomme 20% de l'énergie du corps alors qu'il pèse 2% du poids.",
    },
    "09-comparative": {
        "intro": "Que nous apprennent les animaux sur la cognition et le comportement ?",
        "sections": [
            ("Intelligence animale", "Corbeaux, dauphins, primates : outils, métacognition."),
            ("Conditionnement", "Pavlov et ses chiens : fondement de l'apprentissage."),
            ("Langage animal", "Washoe la chimpanzée, Alex le perroquet gris."),
            ("Éthologie", "Lorenz et l'empreinte — comportements innés."),
        ],
        "illus": "portrait-pavlov.jpg",
        "fun_fact": "Le corbeau de Bernd Heinrich résout des puzzles aussi bien que des enfants de 5 ans.",
    },
    "10-dictionnaire": {
        "intro": "Plus de 50 notions essentielles, classées alphabétiquement.",
        "sections": [],
        "illus": None,
        "fun_fact": "Le Petit Larousse original compte 1500 entrées — nous en proposons les plus fondamentales.",
    },
}


def portrait_gallery(portraits):
    items = []
    for p in portraits:
        items.append(
            f'<figure class="portrait"><img src="../illustrations/wikimedia/{p}" alt="">'
            f'<figcaption>{p.replace("portrait-","").replace(".jpg","").replace(".png","").title()}</figcaption></figure>'
        )
    return f'<div class="portrait-gallery">{"".join(items)}</div>'


def build_category_page(cat):
    cid = cat["id"]
    content = CATEGORY_CONTENT.get(cid, {})
    sections_html = ""
    for title, text in content.get("sections", []):
        sections_html += f'<div class="section-card"><h3>{title}</h3><p>{text}</p></div>\n'

    illus_html = ""
    if content.get("illus"):
        illus_html = f'<figure class="hero-illus"><img src="../illustrations/wikimedia/{content["illus"]}" alt="Illustration"></figure>'
    if content.get("portraits"):
        illus_html += portrait_gallery(content["portraits"])

    pdf_html = ""
    if cat.get("pdf"):
        pdf_html = f'''<div class="pdf-box">
  <span class="pdf-icon">📄</span>
  <div><strong>Livre du domaine public</strong><br>{cat["pdf_label"]}</div>
  <a href="{cat["pdf"]}" target="_blank" class="btn-pdf">Lire le PDF/HTML →</a>
</div>'''

    dict_html = ""
    if cid == "10-dictionnaire":
        entries = []
        for term, defn, ref in sorted(DICT, key=lambda x: x[0]):
            entries.append(
                f'<div class="dict-item" data-letter="{term[0].upper()}">'
                f'<dt>{term}</dt><dd>{defn}</dd>'
                f'<a href="{ref}.html" class="dict-link">→ {ref.replace("-"," ").title()}</a></div>'
            )
        dict_html = f'<div class="dict-alpha">{"".join(entries)}</div>'

    fun = content.get("fun_fact", "")
    fun_html = f'<aside class="fun-fact">💡 <strong>Le savais-tu ?</strong> {fun}</aside>' if fun else ""

    nav_items = ""
    for c in CATEGORIES:
        active = ' class="active"' if c["id"] == cid else ""
        nav_items += f'<li><a href="{c["id"]}.html"{active}>{c["icon"]} {c["title"]}</a></li>'

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{cat["title"]} — Larousse Illustré</title>
<link rel="stylesheet" href="../css/larousse.css">
</head>
<body>
<nav class="top-nav">
  <a href="../index.html" class="logo">📚 Larousse Psychologie</a>
  <ul>{nav_items}</ul>
</nav>
<main class="category-page" style="--accent:{cat['color']}">
  <header class="cat-header">
    <span class="cat-icon">{cat["icon"]}</span>
    <div>
      <h1>{cat["title"]}</h1>
      <p class="cat-sub">{cat["subtitle"]}</p>
    </div>
  </header>
  {illus_html}
  <p class="intro">{content.get("intro","")}</p>
  {pdf_html}
  <div class="sections-grid">{sections_html}</div>
  {dict_html}
  {fun_html}
  <div class="nav-footer">
    <a href="../jeux/quiz.html" class="btn-quiz">🎮 Tester mes connaissances</a>
  </div>
</main>
<script src="../js/larousse.js"></script>
</body>
</html>"""


def build_index():
    cards = ""
    for cat in CATEGORIES:
        pdf_badge = "📄 PDF inclus" if cat.get("pdf") else ""
        cards += f'''<a href="categories/{cat["id"]}.html" class="cat-card" style="--c:{cat["color"]}">
  <span class="card-icon">{cat["icon"]}</span>
  <h2>{cat["title"]}</h2>
  <p>{cat["subtitle"]}</p>
  <span class="badge">{pdf_badge}</span>
</a>'''

    pdf_list = ""
    for folder in sorted(PDF.rglob("*")):
        if folder.is_file() and folder.suffix in (".pdf", ".html"):
            rel = folder.relative_to(ROOT)
            size = folder.stat().st_size // 1024
            pdf_list += f'<li><a href="../{rel}">{folder.name}</a> <span class="size">({size} Ko)</span></li>'

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Larousse Illustré de la Psychologie</title>
<link rel="stylesheet" href="css/larousse.css">
</head>
<body class="home">
<header class="hero-larousse">
  <div class="hero-content">
    <p class="eyebrow">🎓 Apprendre en s'amusant • Domaine public • Illustré</p>
    <h1>Le Larousse Illustré<br>de la Psychologie</h1>
    <p class="hero-desc">10 catégories • 50+ notions • Vrais livres PDF du domaine public • Quiz interactifs</p>
    <div class="hero-actions">
      <a href="categories/01-fondamentaux.html" class="btn-primary">Commencer →</a>
      <a href="jeux/quiz.html" class="btn-secondary">🎮 Quiz</a>
    </div>
  </div>
  <div class="hero-visual">
    <img src="illustrations/wikimedia/cerveau-lobes-fr.svg" alt="Cerveau">
  </div>
</header>

<section class="categories-section">
  <h2>📂 Explorer les catégories</h2>
  <div class="cat-grid">{cards}</div>
</section>

<section class="pdf-section">
  <h2>📚 Bibliothèque PDF — Domaine public</h2>
  <p>Vrais ouvrages classiques téléchargés depuis Gallica, Gutenberg, Archive.org et Classiques UQAM.</p>
  <ul class="pdf-list">{pdf_list}</ul>
</section>

<section class="how-section">
  <h2>🎯 Comment utiliser ce dossier ?</h2>
  <div class="steps">
    <div class="step"><span>1</span><p><strong>Choisis une catégorie</strong> selon ton intérêt du moment.</p></div>
    <div class="step"><span>2</span><p><strong>Lis la fiche</strong> illustrée avec les notions clés.</p></div>
    <div class="step"><span>3</span><p><strong>Ouvre le PDF</strong> du grand classique associé.</p></div>
    <div class="step"><span>4</span><p><strong>Teste-toi</strong> avec le quiz ludique !</p></div>
  </div>
</section>

<footer>
  <p>Contenu pédagogique basé sur des ouvrages du <strong>domaine public</strong>.</p>
  <p>Illustrations : <a href="https://commons.wikimedia.org">Wikimedia Commons</a> (PD / CC0)</p>
</footer>
<script src="js/larousse.js"></script>
</body>
</html>"""


def build_quiz():
    questions = [
        {"q": "Qui a fondé le premier laboratoire de psychologie en 1879 ?", "a": ["Freud", "Wundt", "Skinner", "Piaget"], "correct": 1},
        {"q": "Combien d'items retient la mémoire à court terme (Miller) ?", "a": ["3±1", "7±2", "15±3", "50"], "correct": 1},
        {"q": "Quel neurotransmetteur est lié à la récompense ?", "a": ["GABA", "Dopamine", "Histamine", "Acétylcholine"], "correct": 1},
        {"q": "L'expérience de Milgram portait sur...", "a": ["La mémoire", "L'obéissance", "La perception", "Le langage"], "correct": 1},
        {"q": "Pavlov a étudié...", "a": ["Les rêves", "Le conditionnement classique", "L'intelligence", "Les émotions"], "correct": 1},
        {"q": "L'amygdale traite surtout...", "a": ["La vision", "La peur", "Le langage", "L'équilibre"], "correct": 1},
        {"q": "Piaget décrit combien de stades ?", "a": ["2", "4", "6", "8"], "correct": 1},
        {"q": "La TCC signifie...", "a": ["Thérapie Centrée sur le Corps", "Thérapie Cognitivo-Comportementale", "Test de Cognition Collective", "Traitement Chimique Cérébral"], "correct": 1},
        {"q": "Le Bon a écrit sur...", "a": ["Les enfants", "Les foules", "Les rêves", "Les animaux"], "correct": 1},
        {"q": "Le PERMA est un modèle de...", "a": ["Mémoire", "Bien-être", "Intelligence", "Stress"], "correct": 1},
    ]
    q_json = json.dumps(questions, ensure_ascii=False)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Quiz Psychologie — Larousse Illustré</title>
<link rel="stylesheet" href="../css/larousse.css">
</head>
<body>
<nav class="top-nav"><a href="../index.html" class="logo">📚 Larousse Psychologie</a></nav>
<main class="quiz-page">
  <h1>🎮 Quiz — Teste tes connaissances !</h1>
  <div id="quiz-container"></div>
  <div id="score-display"></div>
  <button id="restart-btn" style="display:none">Recommencer</button>
</main>
<script>
const QUESTIONS = {q_json};
let current = 0, score = 0;

function render() {{
  const q = QUESTIONS[current];
  const container = document.getElementById('quiz-container');
  container.innerHTML = `<p class="progress">Question ${{current+1}}/${{QUESTIONS.length}}</p>
    <h2>${{q.q}}</h2>
    <div class="answers">${{q.a.map((ans,i)=>`<button class="answer-btn" data-i="${{i}}">${{ans}}</button>`).join('')}}</div>`;
  container.querySelectorAll('.answer-btn').forEach(btn => {{
    btn.onclick = () => {{
      const i = +btn.dataset.i;
      btn.parentElement.querySelectorAll('.answer-btn').forEach(b => {{
        b.disabled = true;
        if (+b.dataset.i === q.correct) b.classList.add('correct');
        else if (+b.dataset.i === i) b.classList.add('wrong');
      }});
      if (i === q.correct) score++;
      setTimeout(() => {{ current++; current < QUESTIONS.length ? render() : showScore(); }}, 1200);
    }};
  }});
}}

function showScore() {{
  document.getElementById('quiz-container').innerHTML = '';
  const pct = Math.round(score/QUESTIONS.length*100);
  document.getElementById('score-display').innerHTML = `<div class="score-card">
    <h2>${{pct >= 70 ? '🏆' : '📚'}} Score : ${{score}}/${{QUESTIONS.length}}</h2>
    <p>${{pct >= 70 ? 'Excellent ! Tu maîtrises les bases.' : 'Continue à explorer le Larousse !'}}</p>
  </div>`;
  document.getElementById('restart-btn').style.display = 'block';
}}

document.getElementById('restart-btn').onclick = () => {{ current=0; score=0; document.getElementById('score-display').innerHTML=''; document.getElementById('restart-btn').style.display='none'; render(); }};
render();
</script>
</body>
</html>"""


def write_readmes():
    (PDF / "README.md").write_text("""# 📚 Bibliothèque PDF — Domaine Public

Vrais ouvrages classiques de psychologie, **libres de droits**.

## Par catégorie

| Dossier | Contenu |
|---------|---------|
| `psychologie-sociale/` | Le Bon — Psychologie des foules (PDF 204 p. + HTML) |
| `psychologie-generale/` | James, Binet, Le Bon éducation |
| `psychologie-clinique/` | Freud — Interprétation des rêves |
| `psychologie-comparative/` | Joly — L'homme et l'animal |
| `histoire-psychologie/` | Wundt, Tarde |

## Sources légales

- [Gallica BnF](https://gallica.bnf.fr/selections/fr/html/la-psychologie-en-france-1800-1950)
- [Project Gutenberg](https://www.gutenberg.org/)
- [Internet Archive](https://archive.org/)
- [Classiques UQAM](https://classiques.uqam.ca/)
""", encoding="utf-8")

    (BASE / "README.md").write_text("""# 📖 Larousse Illustré de la Psychologie

**Ouvrir :** `index.html` dans un navigateur.

## Contenu

- 10 catégories thématiques illustrées
- Liens vers vrais PDF du domaine public
- Portraits de grands psychologues (Wikimedia Commons)
- Quiz interactif de 10 questions
- Dictionnaire de 50+ notions

## Générer

```bash
python3 build_larousse.py
```
""", encoding="utf-8")


if __name__ == "__main__":
    for cat in CATEGORIES:
        (CAT / f"{cat['id']}.html").write_text(build_category_page(cat), encoding="utf-8")
    (BASE / "index.html").write_text(build_index(), encoding="utf-8")
    (JEUX / "quiz.html").write_text(build_quiz(), encoding="utf-8")
    write_readmes()
    print("Larousse illustré généré avec succès.")
