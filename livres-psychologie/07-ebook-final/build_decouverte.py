# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Zone de découverte : images, planches, projets, cave."""

import os

from data_decouverte import CACHE, GALLERIE, PLANCHES_EXPERIENCES, PROJETS, SOURCES, TECHNIQUES
from shell import page_header, page_shell

BASE = os.path.dirname(os.path.abspath(__file__))
IMG = "../05-larousse-illustre-complet/illustrations/wikimedia"


def _write(path, html):
    full = os.path.join(BASE, path)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(html)


def _img_src(filename):
    return f"{IMG}/{filename}"


def render_decouverte():
    gallery = []
    for fichier, commons, licence, titre, caption, links in GALLERIE:
        pills = "".join(
            f'<a class="pill-link" href="{href}">{label}</a>' for href, label in links
        )
        commons_href = "https://commons.wikimedia.org/wiki/File:" + commons.replace(" ", "_")
        gallery.append(
            f'<figure class="disco-card" id="img-{fichier.split(".")[0]}">'
            f'<img src="{_img_src(fichier)}" alt="{titre}" loading="lazy">'
            f"<figcaption><span class=\"geo-fig\">{licence}</span>"
            f"<strong>{titre}</strong>"
            f"<p>{caption}</p>"
            f'<div class="pill-row">{pills}'
            f'<a class="pill-link" href="{commons_href}" target="_blank" rel="noopener">Source Commons</a>'
            f"</div></figcaption></figure>"
        )

    plates = []
    for eid, fig, titre, annee, proto, resultat, href, image in PLANCHES_EXPERIENCES:
        plates.append(
            f'<article class="xp-plate" id="planche-{eid}">'
            f'<div class="xp-fig"><img src="{_img_src(image)}" alt="{titre}" loading="lazy">'
            f'<span>Fig. {fig} · {annee}</span></div>'
            f"<div><h3>{titre}</h3>"
            f"<p><strong>Protocole.</strong> {proto}</p>"
            f"<p><strong>Résultat.</strong> {resultat}</p>"
            f'<p><a class="pill-link" href="{href}">Ouvrir la fiche complète</a></p>'
            f"</div></article>"
        )

    techs = "".join(
        f'<a class="tech-card" href="{href}"><h3>{name}</h3>'
        f"<p class=\"tech-k\">{kind}</p><p>{desc}</p></a>"
        for name, kind, desc, href in TECHNIQUES
    )

    projects = "".join(
        f'<article class="project-card">'
        f"<h3>{name}</h3><p>{desc}</p>"
        f"<p class=\"tech-k\">{credit}</p>"
        f'<p><a class="pill-link" href="{url}" target="_blank" rel="noopener">Ouvrir le projet</a></p>'
        f"</article>"
        for name, url, desc, credit in PROJETS
    )

    hidden = "".join(
        f'<article class="myth-card disco-hidden">'
        f'<img src="{_img_src(image)}" alt="" loading="lazy">'
        f"<div><h3>{titre}</h3><p>{texte}</p>"
        f'<a class="pill-link" href="{href}">Lire autour</a></div></article>'
        for titre, texte, image, href in CACHE
    )

    sources = "".join(
        f"<li><a href=\"{url}\" target=\"_blank\" rel=\"noopener\">{name}</a> — {desc}</li>"
        for name, url, desc in SOURCES
    )

    header = page_header(
        depth=0,
        breadcrumb=[("Accueil", "../../index.html"), ("Zone de découverte", None)],
        icon="🔭", color="vert",
        title="Zone de découverte",
        subtitle="Planches d'expériences, vraies images du cerveau, techniques, cave des mythes, projets ouverts — avec leurs sources",
        chips=[
            f"🖼️ {len(GALLERIE)} images libres",
            f"🔬 {len(PLANCHES_EXPERIENCES)} planches d'expériences",
            f"🛠️ {len(TECHNIQUES)} techniques",
            f"🌐 {len(PROJETS)} projets ouverts",
        ],
    )

    body = f"""{header}
<div class="wrap content" style="max-width:1100px">
  <div class="objectives-box">
    <h3>🎯 Un cabinet, pas un fil d'actualité</h3>
    <p>Toutes les images viennent de <strong>Wikimedia Commons</strong> (domaine public ou licence libre).
    Chaque planche renvoie à une fiche du site : on ne collectionne pas pour décorer, on collectionne
    pour <em>comprendre</em>. Rien ici n'est un diagnostic, ni un protocole à reproduire chez soi.</p>
    <div class="pill-row">
      <a class="pill-link" href="categories/27-science-psychologique.html">Fiche Science psychologique</a>
      <a class="pill-link" href="categories/08-neurosciences.html">Neurosciences</a>
      <a class="pill-link" href="references/experiences.html">Expériences</a>
      <a class="pill-link" href="references/cas.html">Cas</a>
      <a class="pill-link" href="references/mythes.html">Mythes</a>
      <a class="pill-link" href="credits.html">Crédits des images</a>
    </div>
  </div>

  <h2 id="planches">🔬 Planches d'expériences</h2>
  <p>Douze protocoles dessinés comme des planches de cabinet : ce qu'on a fait, ce qui est apparu,
  où lire le détail et les critiques.</p>
  <div class="xp-grid">{''.join(plates)}</div>

  <h2 id="galerie">🖼️ Galerie — images réelles, sources citées</h2>
  <p>{len(GALLERIE)} fichiers libres : portraits, coupes, colorations, IRM, illusions, tests.
  Clique la source Commons pour le fichier original.</p>
  <div class="disco-grid">{''.join(gallery)}</div>

  <h2 id="techniques">🛠️ Techniques : ce que chacune voit</h2>
  <div class="tech-grid">{techs}</div>

  <h2 id="projets">🌐 Projets complets, données ouvertes</h2>
  <p>Des sites et des jeux de données entiers, pas des extraits. On peut y entrer sans payer
  un article : atlas, IRM brutes, cartes statistiques, logiciels.</p>
  <div class="project-grid">{projects}</div>

  <h2 id="cache">🕯️ La cave : caché, exagéré, abandonné</h2>
  <p>Ce que les manuels grand public lissent : doctrines mortes, techniques brutales, récits trop beaux.</p>
  <div class="hidden-grid">{hidden}</div>

  <h2 id="sources">📚 Sources et portes de sortie</h2>
  <ul class="source-list">{sources}</ul>
  <div class="cta-row">
    <a class="btn btn-primary" href="categories/27-science-psychologique.html">Lire la fiche Science psychologique</a>
    <a class="btn btn-secondary" href="quiz/quiz.html?id=science-psychologique">Quiz noté</a>
    <a class="btn btn-secondary" href="laboratoire.html">Laboratoire jouable</a>
  </div>
</div>
"""
    _write("decouverte.html", page_shell(
        "Zone de découverte", body, depth=0, active="Découverte",
        description=(
            "Planches d'expériences sur le cerveau, galerie d'images libres, techniques "
            "d'exploration, projets ouverts (Connectome, OpenNeuro, Allen, BigBrain) et cave des mythes."
        ),
    ))
    return len(GALLERIE), len(PLANCHES_EXPERIENCES)
