# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Pages d'auto-évaluation pédagogique."""

import json
import os

from shell import page_shell, page_header, asset
from data_autoeval import EVALUATIONS

BASE = os.path.dirname(os.path.abspath(__file__))

AVERTISSEMENT = """
<div class="warn-box">
  <strong>Ce ne sont pas des tests diagnostiques.</strong> Les affirmations ont été rédigées pour ce site afin
  d'illustrer la construction d'une mesure en psychologie : items équilibrés, items inversés, échelle de Likert,
  score par dimension. Elles ne reproduisent aucun instrument publié, n'ont fait l'objet d'aucune validation et
  ne permettent d'établir aucun diagnostic. Aucune réponse n'est enregistrée ni transmise : tout se passe dans
  votre navigateur, et fermer la page efface tout.
</div>"""


def _write(path, html_content):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full) or BASE, exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html_content)


def render_hub():
    cards = "".join(
        f"""<a class="eval-card {ev['couleur']}" href="auto-evaluations/{ev['id']}.html">
          <span class="eval-ico">{ev['icone']}</span>
          <h3>{ev['titre']}</h3>
          <p>{ev['accroche']}</p>
          <span class="eval-meta">⏱️ {ev['duree']} · {len(ev['items'])} affirmations · {len(ev['dimensions'])} dimensions</span>
        </a>"""
        for ev in EVALUATIONS
    )

    n_items = sum(len(ev["items"]) for ev in EVALUATIONS)

    header = page_header(
        depth=0,
        breadcrumb=[("Accueil", "../../index.html"), ("Auto-évaluations", None)],
        icon="📋", color="vert",
        title="Auto-évaluations pédagogiques",
        subtitle="Comprendre la psychométrie de l'intérieur, en répondant vous-même à des questionnaires construits pour l'occasion",
        chips=[f"📋 {len(EVALUATIONS)} questionnaires", f"❓ {n_items} affirmations", "🔒 Rien n'est enregistré"],
    )

    body = f"""{header}
<div class="section">
  <p class="section-desc" style="max-width:760px">Un questionnaire de personnalité n'est pas un miroir : c'est un
  instrument de mesure, avec une construction, des défauts connus et une marge d'erreur. Le meilleur moyen de
  comprendre comment il fonctionne — et pourquoi il faut se méfier des tests qui rangent les gens en types — est
  d'en passer un en observant sa mécanique.</p>

  <p class="section-desc" style="max-width:760px">Chaque questionnaire ci-dessous affiche des scores par
  dimension continue, jamais un « type ». Vous verrez apparaître des items formulés à l'envers : ils servent à
  neutraliser la tendance à toujours acquiescer, un biais de réponse bien documenté.</p>

  {AVERTISSEMENT}

  <div class="eval-grid" style="margin-top:1.6rem">{cards}</div>

  <div class="note-box" style="margin-top:2rem">
    <strong>Ce qu'un bon questionnaire doit démontrer.</strong> Trois propriétés au minimum : la fidélité — il
    donne un résultat semblable si on le repasse quinze jours plus tard ; la validité de construit — il mesure
    bien ce qu'il prétend mesurer et pas autre chose ; la validité prédictive — son score prédit réellement
    quelque chose d'observable. Les questionnaires de magazine n'en vérifient aucune, et beaucoup de tests
    utilisés en entreprise échouent sur au moins deux. La page
    <a href="references/tests.html">tests et instruments</a> détaille ces notions.
  </div>
</div>
"""
    _write("auto-evaluations.html", page_shell(
        "Auto-évaluations", body, depth=0, active="Apprendre",
        description=f"{len(EVALUATIONS)} auto-évaluations pédagogiques en français : cinq grands facteurs, chronotype, méthodes d'apprentissage, régulation émotionnelle, procrastination. Sans valeur diagnostique."))


def render_evaluation(ev):
    payload = {
        "echelle": ev["echelle"],
        "items": [[texte, dim, bool(inv)] for texte, dim, inv in ev["items"]],
        "dimensions": [
            {"cle": cle, "nom": nom, "couleur": couleur, "description": desc, "bas": bas, "haut": haut}
            for cle, nom, couleur, desc, bas, haut in ev["dimensions"]
        ],
        "note": ev["note_html"],
    }

    header = page_header(
        depth=1,
        breadcrumb=[("Accueil", "../../../index.html"),
                    ("Auto-évaluations", "../auto-evaluations.html"),
                    (ev["titre"], None)],
        icon=ev["icone"], color=ev["couleur"],
        title=ev["titre"],
        subtitle=ev["accroche"],
        chips=[f"⏱️ {ev['duree']}", f"❓ {len(ev['items'])} affirmations",
               f"📊 {len(ev['dimensions'])} dimensions"],
    )

    dimensions_list = "".join(
        f"<li><b>{nom}</b> — {desc}</li>" for _cle, nom, _c, desc, _b, _h in ev["dimensions"]
    )

    body = f"""{header}
<div class="section" style="max-width:820px;margin:0 auto">
  <div class="aide-bloc">{ev['intro_html']}
    <p style="margin-top:0.9rem"><b>Ce questionnaire mesure :</b></p>
    <ul style="font-size:0.88rem;line-height:1.7;padding-left:1.2rem">{dimensions_list}</ul>
  </div>

  {AVERTISSEMENT}

  <div class="eval-shell" id="eval-shell" style="margin-top:1.6rem">
    <p>Chargement du questionnaire…</p>
  </div>
  <script type="application/json" id="eval-data">{json.dumps(payload, ensure_ascii=False)}</script>

  <div class="cta-row" style="margin-top:1.6rem">
    <a class="btn btn-secondary" href="../auto-evaluations.html">← Toutes les auto-évaluations</a>
    <a class="btn btn-secondary" href="../references/tests.html">📊 Les vrais tests psychométriques</a>
  </div>
</div>
"""
    _write(f"auto-evaluations/{ev['id']}.html", page_shell(
        ev["titre"], body, depth=1, active="Apprendre",
        description=f"{ev['titre']} : auto-évaluation pédagogique en français. {ev['accroche']} Sans valeur diagnostique.",
        extra_scripts=f'<script src="{asset(1, "js/autoeval.js")}"></script>'))


def render_all():
    render_hub()
    for ev in EVALUATIONS:
        render_evaluation(ev)
    return len(EVALUATIONS), sum(len(ev["items"]) for ev in EVALUATIONS)
