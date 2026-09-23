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

# Éléments de la barre de navigation : (libellé, chemin relatif à 07-ebook-final/)
NAV_ITEMS = [
    ("Accueil", "@root:index.html"),
    ("Catégories", "index.html"),
    ("Découverte", "decouverte.html"),
    ("Références", "references/index.html"),
    ("Méthodes", "methodes.html"),
    ("Pratique", "pratique.html"),
    ("Bibliothèque", "bibliotheque.html"),
    ("Quiz", "quiz/index.html"),
    ("Apprendre", "apprendre.html"),
    ("Cours", "emploi-du-temps.html"),
    ("Cahier", "cahier.html"),
    ("Aide", "aide.html"),
]

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


def media(depth, path):
    """Lien vers une illustration ou un PDF rangé hors de 07-ebook-final/."""
    return ("../" * depth) + path


def page_shell(title, body, depth=0, active="", description="", extra_head="",
               extra_scripts="", body_attrs="", wide=False):
    links_html = ""
    for label, target in NAV_ITEMS:
        extra_attr = ""
        if target.startswith("@ext:"):
            href = target[5:]
            extra_attr = ' target="_blank" rel="noopener"'
        elif target.startswith("@root:"):
            href = repo_root(depth) + target[6:]
        else:
            href = ebook(depth, target)
        cls = ' class="active"' if label == active else ""
        links_html += f'<a href="{href}"{cls}{extra_attr}>{label}</a>'

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
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@500;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{asset(depth, 'css/style.css')}">
<link rel="stylesheet" href="{asset(depth, 'css/v2.css')}">
<link rel="stylesheet" href="{asset(depth, 'css/v3.css')}">
<link rel="stylesheet" href="{asset(depth, 'css/v4.css')}">
<link rel="stylesheet" href="{asset(depth, 'css/plates.css')}">
<link rel="stylesheet" href="{asset(depth, 'css/lycee.css')}">
<link rel="stylesheet" href="{asset(depth, 'css/assistant.css')}">
<link rel="stylesheet" href="{asset(depth, 'css/compte.css')}">
{extra_head}
</head>
<body data-root="{repo_root(depth)}"{(' ' + body_attrs) if body_attrs else ''}>
<div class="topbar">
  <nav class="nav-pill">
    <a class="brand" href="{repo_root(depth)}index.html"><span class="brand-mark"></span>Psyclopédia</a>
    <ul class="nav-links">{links_html}</ul>
    <div class="nav-side">
      <a class="nav-compte-btn" id="nav-compte" href="{ebook(depth, 'compte.html')}" aria-label="Compte étudiant">
        <span class="nav-compte-mark" aria-hidden="true">👤</span><span class="nav-compte-label">Compte</span>
      </a>
      <a class="nav-discord-btn" href="{DISCORD_INVITE}" target="_blank" rel="noopener" aria-label="Rejoindre le serveur Discord">
        <span aria-hidden="true">💬</span><span class="nav-discord-label">Discord</span>
      </a>
      <button class="nav-notify-btn" type="button" data-notify-open="" aria-label="Rappels et pensées du jour">
        <span aria-hidden="true">🔔</span><span class="nav-notify-label">Rappels</span>
        <span class="nav-notify-badge" hidden>0</span>
      </button>
      <button class="nav-search-btn" data-search-open="" aria-label="Rechercher">
        <span>🔍</span><span>Rechercher</span><kbd>Ctrl</kbd><kbd>K</kbd>
      </button>
    </div>
  </nav>
</div>
{body}
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
  <p style="margin-top:0.75rem;font-size:0.78rem">⚠️ Contenu pédagogique de vulgarisation : il ne remplace
  ni un diagnostic, ni un avis médical, ni un suivi psychologique professionnel.</p>
</footer>
<script src="{asset(depth, 'js/app.js')}"></script>
<script src="{asset(depth, 'js/ui-v2.js')}"></script>
<script src="{asset(depth, 'js/search.js')}"></script>
<script src="{asset(depth, 'js/daily.js')}"></script>
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
    return f"""
<div class="page-header">
  <p class="breadcrumb">{crumb}</p>
  <div class="page-hero">
    <div class="page-hero-icon" style="background:var(--{color}-light)">{icon}</div>
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
