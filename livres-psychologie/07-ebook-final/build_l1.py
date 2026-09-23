# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Sommaire de licence : les chapitres sont dans les fiches."""

import os

from data_l1_chapitres import L1_EXTRA
from data_l1_psycho import L1_EXPERIENCES
from shell import page_header, page_shell, slugify

BASE = os.path.dirname(os.path.abspath(__file__))

BLOCS = [
    ("01-fondamentaux", "Démarche scientifique",
     "Ce qui rend une psychologie systématique, précise et communicable."),
    ("09-psychopathologie", "Psychologie clinique",
     "Une personne singulière, deux boîtes à outils, un titre protégé."),
    ("05-developpement", "Psychologie du développement",
     "Toute la vie, trois horloges, et comment étudier un nourrisson."),
    ("03-cognitive", "Lectures cognitives",
     "Attention, listes, oubli, état, amorçage, carte spatiale."),
    ("04-sociale", "Mémoire partagée",
     "Dans un groupe proche, on retient qui sait quoi."),
    ("16-comparee", "Continuité animale",
     "Le geai, l'outil gardé, l'écart social avec les grands singes."),
    ("22-numerique", "Mémoire et moteurs de recherche",
     "Quatre études : on encode le chemin quand le fait reste accessible."),
]


def _write(name, html):
    path = os.path.join(BASE, name)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)


def render():
    header = page_header(
        depth=0,
        breadcrumb=[("Accueil", "../../index.html"), ("Psychologie de licence", None)],
        icon="🎓", color="vert",
        title="Psychologie de licence",
        subtitle="Le sommaire des chapitres. Le texte, les planches et les fiches sont dans les catégories.",
        chips=["Sommaire", "7 fiches", "Expériences", "Quiz"],
    )
    blocs = ""
    for cid, titre, intro in BLOCS:
        extra = L1_EXTRA[cid]
        liens = "".join(
            f'<a class="path-step" href="categories/{cid}.html#{slugify(section)}">'
            f'<span class="path-step-n">→</span>'
            f'<span class="path-step-title">{section}</span>'
            f'<span class="path-step-kind">Dans la fiche</span></a>'
            for section, _body in extra["sections"]
        )
        blocs += f"""<h2 id="{cid}">{titre}</h2>
        <p>{intro}</p>
        <div class="path-card"><div class="path-steps">{liens}</div></div>"""

    lectures = "".join(
        f'<a class="path-step" href="references/experiences.html#{eid}">'
        f'<span class="path-step-n">🔬</span>'
        f'<span class="path-step-title">{titre}</span>'
        f'<span class="path-step-kind">{chercheur}, {annee}</span></a>'
        for eid, titre, chercheur, annee, *_rest in L1_EXPERIENCES
    )
    body = f"""{header}
<div class="wrap with-toc">
  <aside class="toc-side"><h4>Où lire</h4>
    {"".join(f'<a href="#{cid}">{titre}</a>' for cid, titre, _i in BLOCS)}
    <a href="#experiences">Expériences</a>
    <a href="#quiz">Quiz</a>
  </aside>
  <div class="content" style="max-width:none">
    <div class="objectives-box" id="objectifs">
      <h3>Ce que cette page ne refait pas</h3>
      <ul>
        <li>Les chapitres sont dans les fiches, avec le même sommaire, les chiffres, les idées reçues, les planches et les flashcards que le reste du site.</li>
        <li>Les protocoles sont dans les expériences, chacun avec son résultat, sa portée et sa limite.</li>
        <li>Rien ici n'est un polycopié, un diagnostic, ni le cours officiel d'une université.</li>
      </ul>
    </div>
    <div class="warn-box">
      <strong>Comment s'en servir.</strong> Choisis une fiche. Le chapitre s'y lit avec le reste du domaine,
      pas à part. Les manuels et les articles restent à leurs auteurs.
    </div>
    {blocs}
    <h2 id="experiences">Les expériences de ce corpus</h2>
    <p>Chaque lien ouvre la fiche déjà rédigée : dispositif, observation, portée, limite.</p>
    <div class="path-card"><div class="path-steps">{lectures}</div></div>
    <h2 id="quiz">S'entraîner</h2>
    <p><a class="btn btn-primary" href="quiz/quiz.html?id=l1-psychologie">Quiz noté de ce corpus</a></p>
  </div>
</div>
"""
    _write("l1-psychologie.html", page_shell(
        "Psychologie de licence",
        body,
        depth=0,
        description="Sommaire de licence : démarche, clinique, développement et lectures, à lire dans les fiches de catégorie.",
    ))
    return 1


if __name__ == "__main__":
    print(render(), "page L1")
