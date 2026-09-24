# -*- coding: utf-8 -*-
"""
PSYCLOPÉDIA — Coque commune des pages (navigation, en-tête, pied de page).

Toutes les pages du site sont générées à partir de `page_shell`. Deux
profondeurs existent : 0 pour les pages posées dans `07-ebook-final/`,
1 pour celles rangées dans `categories/`, `quiz/` ou `references/`.
"""

import html
import re
import unicodedata

# Invitation permanente vers le serveur communautaire (salon 👋-bienvenue).
DISCORD_INVITE = "https://discord.gg/sX3TAqH4pD"

# Menu en trois groupes : (libellé, chemin, sticker). @root: racine, @ext: lien externe.
NAV_GROUPS = [
    ("Lire", [
        ("Accueil", "@root:index.html", "oeil-bleu.png"),
        ("Catégories", "index.html", "cerveau-petit.png"),
        ("Découverte", "decouverte.html", "iris.png"),
        ("Références", "references/index.html", "livres.png"),
        ("Bibliothèque", "bibliotheque.html", "livre.png"),
    ]),
    ("Étudier", [
        ("Cours", "emploi-du-temps.html", "horloge.png"),
        ("Apprendre", "apprendre.html", "stylo.png"),
        ("Cahier", "cahier.html", "machine.png"),
        ("Quiz", "quiz/index.html", "trophee.png"),
        ("Méthodes", "methodes.html", "loupe.png"),
    ]),
    ("Autour", [
        ("Pratique", "pratique.html", "mains.png"),
        ("Aide", "aide.html", "coeur.png"),
        ("Compte", "compte.html", "tete.png"),
        ("Discord", "@ext:" + DISCORD_INVITE, "voix.png"),
        ("Rappels", "rappels.html", "soleil.png"),
    ]),
]

# Ancien appelant : liste plate (libellé, chemin).
NAV_ITEMS = [(label, target) for _title, links in NAV_GROUPS for label, target, _img in links]

# Sticker par identifiant de catégorie (évite les collisions d'emoji).
CAT_STICKERS = {
    "01-fondamentaux": "loupe.png",
    "02-histoire": "time.png",
    "03-cognitive": "memoire.png",
    "04-sociale": "lien.png",
    "05-developpement": "croissance.png",
    "06-personnalite": "tete.png",
    "07-emotions": "coeur.png",
    "08-neurosciences": "cerveau-petit.png",
    "09-psychopathologie": "pince.png",
    "10-therapies": "mains.png",
    "11-positive": "soleil.png",
    "12-travail": "ordi.png",
    "13-education": "stylo.png",
    "14-sante": "coeur-rouge.png",
    "15-legale": "globe.png",
    "16-comparee": "colibri.png",
    "17-interculturelle": "globe.png",
    "18-langage": "parole.png",
    "19-psychometrie": "loupe.png",
    "20-sport": "trophee.png",
    "21-consommation": "livre.png",
    "22-numerique": "ecran.png",
    "23-evolutionniste": "papillon.png",
    "24-vieillissement": "lune.png",
    "25-environnementale": "colibri.png",
    "26-politique": "voix.png",
    "27-science-psychologique": "oeil.png",
}

EMOJI_STICKERS = {
    "🧑\u200d🎨": "stylo.png",
    "🎓": "stylo.png", "🗂️": "livres.png", "🔬": "loupe.png", "📖": "livre.png",
    "👤": "tete.png", "🩺": "pince.png", "⚖️": "globe.png", "🧭": "iris.png",
    "📊": "loupe.png", "🎮": "trophee.png", "📚": "livres.png", "🧠": "cerveau-petit.png",
    "🔍": "loupe.png", "❓": "parole.png", "🧪": "camera.png", "🤖": "machine.png",
    "📝": "stylo.png", "⚠️": "oeil.png", "🖼️": "camera.png", "👥": "lien.png",
    "🌱": "croissance.png", "🧩": "loupe.png", "📂": "livres.png", "📜": "time.png",
    "💼": "ordi.png", "🔤": "parole.png", "🔁": "horloge.png", "💭": "memoire.png",
    "🌍": "globe.png", "🌀": "oeil.png", "🔭": "iris.png", "💬": "voix.png",
    "📕": "livre.png", "🖨️": "machine.png", "📅": "horloge.png", "🗃️": "livres.png",
    "🏛️": "time.png", "🧹": "oeil.png", "🔔": "soleil.png", "🌐": "globe.png",
    "🎯": "trophee.png", "📋": "stylo.png", "🗓️": "horloge.png", "⚡": "soleil.png",
    "🧰": "mains.png", "🔄": "horloge.png", "📼": "horloge.png", "📏": "loupe.png",
    "📱": "ecran.png", "🃏": "oeil.png", "🔗": "lien.png", "🛋️": "mains.png",
    "❤️": "coeur.png", "🤝": "mains.png", "💡": "soleil.png", "🎬": "camera.png",
    "🗣️": "parole.png", "🏃": "trophee.png", "🛒": "livre.png", "🧬": "papillon.png",
    "🌿": "lune.png", "🗳️": "voix.png", "🎭": "tete.png", "🐾": "colibri.png",
    "🔎": "loupe.png", "👁️": "oeil.png", "✍️": "stylo.png", "🌤️": "soleil.png",
    "🏥": "coeur-rouge.png", "🕰️": "horloge.png", "👂": "parole.png", "📥": "livre.png",
    "✨": "soleil.png", "🔀": "lien.png", "🗺️": "globe.png", "🛠️": "mains.png",
    "🧯": "coeur.png", "🟢": "soleil.png", "💾": "machine.png", "📄": "livre.png",
    "🎤": "voix.png", "🎒": "livre.png", "🏷️": "loupe.png", "🛡️": "globe.png",
    "☎️": "voix.png", "🎨": "papillon.png", "🔢": "loupe.png", "➡️": "lien.png",
    "⚓": "time.png", "🪞": "oeil.png", "📍": "globe.png", "🤸": "trophee.png",
    "🚫": "oeil.png", "📘": "livre.png", "🧫": "camera.png", "📦": "livres.png",
    "🕯️": "lune.png", "🔒": "tete.png", "🚀": "papillon.png", "🏆": "trophee.png",
    "🎲": "trophee.png", "🆕": "soleil.png", "🏠": "oeil-bleu.png", "👋": "mains.png",
    "🌙": "lune.png", "🌊": "colibri.png",
}

# Chemins relatifs à 07-ebook-final/ vers les ressources partagées du dépôt.
IMG_DIR = "../05-larousse-illustre-complet/illustrations/wikimedia"
PDF_DIR = "../06-pdf-domaine-public"


EBOOK_DIR = "livres-psychologie/07-ebook-final/"


def ebook(depth, path):
    """Lien vers une page de l'ebook, exprimé depuis une page de profondeur donnée.

    La profondeur -2 désigne la racine du dépôt (page d'accueil), 0 le dossier
    `07-ebook-final/`, 1 ses sous-dossiers.
    """
    if depth < 0:
        return EBOOK_DIR + path
    return ("../" * depth) + path


def repo_root(depth):
    """Préfixe menant à la racine du dépôt."""
    return "../" * (depth + 2)


def asset(depth, path):
    return repo_root(depth) + "assets-ebook/" + path


def sticker_img(filename, depth, alt=""):
    """Image du pack, dimensionnée par la classe .stk."""
    src = asset(depth, "collage/" + filename)
    return f'<img class="stk" src="{src}" alt="{html.escape(alt)}">'


def dress(fragment, depth):
    """Remplace les emoji d'interface par le sticker le plus proche."""
    if not fragment:
        return fragment
    for emo in sorted(EMOJI_STICKERS, key=len, reverse=True):
        if emo in fragment:
            fragment = fragment.replace(emo, sticker_img(EMOJI_STICKERS[emo], depth))
    return fragment


def _nav_href(depth, target):
    if target.startswith("@ext:"):
        return target[5:], ' target="_blank" rel="noopener"'
    if target.startswith("@root:"):
        return repo_root(depth) + target[6:], ""
    return ebook(depth, target), ""


def media(depth, path):
    """Lien vers une illustration ou un PDF rangé hors de 07-ebook-final/."""
    return ("../" * depth) + path


def page_shell(title, body, depth=0, active="", description="", extra_head="",
               extra_scripts="", body_attrs="", wide=False):
    groups_html = ""
    for title, links in NAV_GROUPS:
        bits = ""
        for label, target, img in links:
            href, extra_attr = _nav_href(depth, target)
            cls = ' class="is-on"' if label == active else ""
            bits += f'<a href="{href}"{cls}{extra_attr}>{sticker_img(img, depth)}{label}</a>'
        groups_html += f'<div class="nav-group"><p>{title}</p>{bits}</div>'

    desc = description or ("Psyclopédia : l'encyclopédie vivante et illustrée de la psychologie, "
                           "en français — 27 catégories, références, bibliothèque et quiz notés.")
    full_title = title if "Psyclopédia" in title else f"{title} — Psyclopédia"

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="icon" type="image/svg+xml" href="{asset(depth, 'favicon.svg')}">
<link rel="manifest" href="{repo_root(depth)}manifest.webmanifest">
<meta name="theme-color" content="#1c1915">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Psyclopédia">
<link rel="apple-touch-icon" href="{repo_root(depth)}assets-ebook/icons/icon-192.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,620&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{asset(depth, 'css/style.css')}">
<link rel="stylesheet" href="{asset(depth, 'css/v2.css')}">
<link rel="stylesheet" href="{asset(depth, 'css/v3.css')}">
<link rel="stylesheet" href="{asset(depth, 'css/v4.css')}">
<link rel="stylesheet" href="{asset(depth, 'css/plates.css')}">
<link rel="stylesheet" href="{asset(depth, 'css/lycee.css')}">
<link rel="stylesheet" href="{asset(depth, 'css/assistant.css')}">
<link rel="stylesheet" href="{asset(depth, 'css/compte.css')}">
<link rel="stylesheet" href="{asset(depth, 'css/collage.css')}">
{extra_head}
</head>
<body data-root="{repo_root(depth)}"{(' ' + body_attrs) if body_attrs else ''}>
<header class="desk">
  <div class="desk-bar">
    <a class="mark" href="{repo_root(depth)}index.html">{sticker_img("oeil-bleu.png", depth)}<span>Psyclopédia</span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="sheet">Menu</button>
    <div class="desk-tools">
      <button class="tool nav-notify-btn" type="button" data-notify-open="" aria-label="Rappels et pensées du jour">
        {sticker_img("soleil.png", depth)}<span class="long nav-notify-label">Rappels</span>
        <span class="nav-notify-badge" hidden>0</span>
      </button>
      <button class="tool" type="button" data-search-open="" aria-label="Rechercher">
        {sticker_img("loupe.png", depth)}<span class="long">Rechercher</span>
      </button>
      <a class="tool" id="nav-compte" href="{ebook(depth, 'compte.html')}" aria-label="Compte étudiant">
        <span class="nav-compte-mark" aria-hidden="true">{sticker_img("tete.png", depth)}</span>
        <span class="nav-compte-label long">Compte</span>
      </a>
    </div>
  </div>
  <nav class="sheet" id="sheet">{groups_html}</nav>
</header>
{dress(body, depth)}
<footer>
  <div class="foot-links">
    <a href="{repo_root(depth)}index.html">Accueil</a>
    <a href="{ebook(depth, 'index.html')}">Catégories</a>
    <a href="{ebook(depth, 'decouverte.html')}">Zone de découverte</a>
    <a href="{ebook(depth, 'lycee.html')}">Du lycée à la licence</a>
    <a href="{ebook(depth, 'branches/index.html')}">Quatre branches</a>
    <a href="{ebook(depth, 'assistant.html')}">Assistant</a>
    <a href="{ebook(depth, 'references/index.html')}">Références</a>
    <a href="{ebook(depth, 'dictionnaire.html')}">Dictionnaire</a>
    <a href="{ebook(depth, 'bibliotheque.html')}">Bibliothèque</a>
    <a href="{ebook(depth, 'lecteur.html')}">Lecteur en ligne</a>
    <a href="{ebook(depth, 'methodes.html')}">Méthodes</a>
    <a href="{ebook(depth, 'pratique.html')}">Psychologie pratique</a>
    <a href="{ebook(depth, 'lexique.html')}">Lexique anglais</a>
    <a href="{ebook(depth, 'metiers.html')}">Métiers &amp; études</a>
    <a href="{ebook(depth, 'quiz/index.html')}">Quiz</a>
    <a href="{ebook(depth, 'laboratoire.html')}">Laboratoire</a>
    <a href="{ebook(depth, 'revision.html')}">Révision espacée</a>
    <a href="{ebook(depth, 'fiches/index.html')}">Fiches de révision</a>
    <a href="{ebook(depth, 'parcours.html')}">Parcours</a>
    <a href="{ebook(depth, 'apprendre.html')}">Apprendre</a>
    <a href="{ebook(depth, 'emploi-du-temps.html')}">Emploi du temps &amp; cours</a>
    <a href="{ebook(depth, 'cours/index.html')}">Cours &amp; archives</a>
    <a href="{ebook(depth, 'rappels.html')}">Rappels &amp; planches</a>
    <a href="{ebook(depth, 'references/courants.html')}">Grands courants</a>
    <a href="{ebook(depth, 'references/mythes.html')}">Idées reçues</a>
    <a href="{ebook(depth, 'faq.html')}">Questions fréquentes</a>
    <a href="{ebook(depth, 'auto-evaluations.html')}">Auto-évaluations</a>
    <a href="{ebook(depth, 'aide.html')}">Aide &amp; ressources</a>
    <a href="{ebook(depth, 'l1-psychologie.html')}">Psychologie de licence</a>
    <a href="{ebook(depth, 'cahier.html')}">Cahier</a>
    <a href="{ebook(depth, 'compte.html')}">Compte étudiant</a>
    <a href="{ebook(depth, 'espace.html')}">Espace d'apprentissage</a>
    <a href="{DISCORD_INVITE}" target="_blank" rel="noopener">Communauté Discord</a>
    <a href="{ebook(depth, 'plan.html')}">Plan du site</a>
    <a href="{ebook(depth, 'credits.html')}">Crédits &amp; sources</a>
  </div>
  <p>Psyclopédia — encyclopédie pédagogique libre de la psychologie, entièrement en français.
  Textes de synthèse rédigés pour ce guide ; ouvrages du domaine public hébergés dans
  <code>06-pdf-domaine-public/</code> avec mention de leur source (Gallica, Internet Archive,
  Project Gutenberg, Les Classiques des sciences sociales, Darwin Online).
  Illustrations : Wikimedia Commons (domaine public).</p>
  <p style="margin-top:0.75rem;font-size:0.78rem">{sticker_img("oeil.png", depth)} Contenu pédagogique de vulgarisation : il ne remplace
  ni un diagnostic, ni un avis médical, ni un suivi psychologique professionnel.</p>
</footer>
<script>
(function () {{
  var btn = document.querySelector(".menu-btn");
  var sheet = document.getElementById("sheet");
  if (!btn || !sheet) return;
  btn.addEventListener("click", function () {{
    var open = sheet.classList.toggle("is-open");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
  }});
}})();
</script>
<script src="{asset(depth, 'js/app.js')}"></script>
<script src="{asset(depth, 'js/ui-v2.js')}"></script>
<script src="{asset(depth, 'js/search.js')}"></script>
<script src="{asset(depth, 'js/daily.js')}"></script>
<script src="{asset(depth, 'js/pwa.js')}"></script>
<script src="{asset(depth, 'js/assistant.js')}"></script>
<script src="{asset(depth, 'js/compte-config.js')}"></script>
<script src="{asset(depth, 'js/compte.js')}"></script>
{extra_scripts}
</body>
</html>"""


def page_header(depth, breadcrumb, icon, color, title, subtitle, chips=()):
    """En-tête standard d'une page de contenu."""
    crumb = " → ".join(
        f'<a href="{href}">{label}</a>' if href else label for label, href in breadcrumb
    )
    chips_html = "".join(f'<span class="meta-chip">{c}</span>' for c in chips)
    chips_block = f'<div class="meta-row">{chips_html}</div>' if chips_html else ""
    if icon in CAT_STICKERS:
        mark = sticker_img(CAT_STICKERS[icon], depth)
    elif isinstance(icon, str) and icon.endswith(".png"):
        mark = sticker_img(icon, depth)
    elif icon in EMOJI_STICKERS:
        mark = sticker_img(EMOJI_STICKERS[icon], depth)
    else:
        mark = html.escape(icon or "")
    return f"""
<div class="page-header">
  <p class="breadcrumb">{crumb}</p>
  <div class="page-hero">
    <div class="page-hero-icon">{mark}</div>
    <div>
      <h1>{title}</h1>
      <p class="subtitle">{subtitle}</p>
    </div>
  </div>
  {chips_block}
</div>"""


def slugify(text):
    txt = unicodedata.normalize("NFD", text)
    txt = "".join(c for c in txt if unicodedata.category(c) != "Mn")
    txt = re.sub(r"[^a-zA-Z0-9]+", "-", txt).strip("-").lower()
    return txt[:60] or "section"


def strip_html(source):
    """Retire les balises pour produire un texte indexable ou un résumé."""
    txt = re.sub(r"<[^>]+>", " ", source or "")
    txt = html.unescape(txt)
    return re.sub(r"\s+", " ", txt).strip()
