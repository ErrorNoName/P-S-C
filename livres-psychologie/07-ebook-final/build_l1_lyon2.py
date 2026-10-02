# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — L1 SDE + Psychologie, Université Lumière Lyon 2."""

import os

from shell import page_shell, page_header
from data_l1_lyon2 import PROGRAMME, OFFICIAL_SOURCES, MODULES, MODULES_S2, SEMESTRE2_APERCU

BASE = os.path.dirname(os.path.abspath(__file__))


def _write(path, html):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)


def _exam_badge(exam):
    if "QCM" in exam:
        return "QCM"
    if "oral" in exam.lower():
        return "Oral + dossier"
    if "écrit" in exam.lower() or "Écrit" in exam:
        return "Écrit + dossier"
    return "Terminal"


def _render_module(m, expanded=False):
    seances = ""
    for i, (titre, points) in enumerate(m.get("seances", []), 1):
        pts = "".join(f"<li>{p}</li>" for p in points)
        seances += f"""<div class="method-item"><div class="num">{i:02d}</div><div>
          <h4>{titre}</h4><ul>{pts}</ul></div></div>"""

    psyclo = "".join(
        f'<a class="path-step" href="{href}"><span class="path-step-title">{label}</span>'
        f'<span class="path-step-kind">Psyclopédia</span></a>'
        for label, href in m.get("psyclo", [])
    )
    externe = m.get("externe", [])
    ext_html = ""
    if externe:
        ext_html = "<p class=\"muted\">Sources publiques : " + ", ".join(
            f'<a href="{url}" target="_blank" rel="noopener">{nom}</a>'
            for nom, url in externe
        ) + "</p>"

    coeff = f"<span class=\"lycee-chip lycee-chip-site\">Coeff. {m['coeff']}</span>" if m.get("coeff") else ""
    fmt = m.get("format", "CM")
    open_attr = " open" if expanded else ""

    return f"""<details class="l1-module-card"{open_attr} id="{m['id']}">
      <summary>
        <span class="l1-module-code">{m['code']}</span>
        <span class="l1-module-fmt">{fmt}</span>
        <strong>{m['titre']}</strong>
        {coeff}
        <span class="l1-module-exam">{_exam_badge(m.get('exam', ''))}</span>
      </summary>
      <div class="l1-module-body">
        <p class="l1-module-bloc muted">{m['bloc']}</p>
        <p>{m['resume']}</p>
        <p class="muted"><strong>Évaluation :</strong> {m.get('exam', '—')}</p>
        {f'<div class="method-timeline">{seances}</div>' if seances else ''}
        {ext_html}
        <h4>Continuer sur Psyclopédia</h4>
        <div class="path-steps">{psyclo}</div>
      </div>
    </details>"""


def _render_module_s2(m):
    psyclo = "".join(
        f'<a class="path-step" href="{href}"><span class="path-step-title">{label}</span>'
        f'<span class="path-step-kind">Psyclopédia</span></a>'
        for label, href in m.get("psyclo", [])
    )
    return f"""<article class="ref-card gris" id="{m['id']}">
      <div class="ref-h">
        <span class="l1-module-code">{m['code']}</span>
        <h3>{m['titre']}</h3>
        <p class="ref-sub">{m['bloc']}</p>
      </div>
      <p>{m['resume']}</p>
      <div class="path-steps">{psyclo}</div>
    </article>"""


def render_all():
    sources = "".join(
        f'<li><a href="{url}" target="_blank" rel="noopener">{nom}</a></li>'
        for nom, url in OFFICIAL_SOURCES
    )

    s2_ue = "".join(
        f"<li><strong>{titre}</strong> — {codes}</li>"
        for titre, codes in SEMESTRE2_APERCU
    )

    modules_s1 = "".join(_render_module(m, expanded=(i == 0)) for i, m in enumerate(MODULES))
    modules_s2 = "".join(_render_module_s2(m) for m in MODULES_S2)

    # Tableau récapitulatif S1
    rows = ""
    for m in MODULES:
        rows += f"""<tr>
          <td><code>{m['code']}</code></td>
          <td>{m['format']}</td>
          <td><a href="#{m['id']}">{m['titre']}</a></td>
          <td>{m['bloc'].split('(')[0].strip()}</td>
          <td>{_exam_badge(m.get('exam', ''))}</td>
        </tr>"""

    header = page_header(
        depth=0,
        breadcrumb=[
            ("Accueil", "../../index.html"),
            ("Du lycée à la licence", "lycee.html"),
            ("L1 Lyon 2 SDE + Psycho", None),
        ],
        icon="🏛️",
        color="vert",
        title="L1 Sciences de l'éducation + Psychologie — Lyon 2",
        subtitle=f"Parcours {PROGRAMME['titre']} ({PROGRAMME['annee']}) — campus {PROGRAMME['campus']}",
        chips=[
            f"📋 {PROGRAMME['id'].upper()}",
            f"📚 {len(MODULES)} modules S1",
            "🔗 Relié à Psyclopédia",
            "📄 Sources MCCC officielles",
        ],
    )

    toc = """<aside class="toc-side"><h4>Sommaire</h4>
      <a href="#presentation">Présentation</a>
      <a href="#tableau">Tableau S1</a>
      <a href="#modules-s1">Modules semestre 1</a>
      <a href="#modules-s2">Aperçu semestre 2</a>
      <a href="#sources">Sources officielles</a>
    </aside>"""

    body = f"""{header}
<div class="wrap with-toc">
  {toc}
  <div class="content" style="max-width:none">

  <div class="note-box" id="presentation">
    <strong>{PROGRAMME['composante']}</strong> — {PROGRAMME['intro']}
    Parcours compensable selon le MCCC 2026-2027. Cette page recense les unités d'enseignement,
    leurs modalités d'évaluation et des liens vers les fiches Psyclopédia correspondantes.
    Elle ne remplace pas le MCCC ni l'inscription pédagogique.
  </div>

  <h2 id="tableau">Semestre 1 — tableau des modules</h2>
  <div class="lycee-table-wrap">
    <table class="lycee-table">
      <thead><tr><th>Code</th><th>Format</th><th>Intitulé</th><th>Bloc</th><th>Éval.</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>
  </div>

  <h2 id="modules-s1">Modules du semestre 1</h2>
  <p class="section-desc">Sciences de l'éducation (majeure), psychologie (mineure) et accompagnement.
  Cliquez sur un module pour voir le plan de séances et les liens vers le site.</p>
  <div class="l1-modules">{modules_s1}</div>

  <h2 id="modules-s2">Semestre 2 — aperçu</h2>
  <p>Le second semestre ouvre l'anthropologie, la psychologie et la sociologie de l'éducation,
  plus la suite de la mineure psychologie (méthode expérimentale, cognitive, sociale).</p>
  <ul>{s2_ue}</ul>
  <div class="grid-2">{modules_s2}</div>

  <div class="cta-row">
    <a class="btn btn-primary" href="lycee.html">🎓 Du lycée à la licence</a>
    <a class="btn btn-secondary" href="branches/index.html">🧭 Quatre branches de psycho</a>
    <a class="btn btn-secondary" href="methodes.html">🔬 Méthodes scientifiques</a>
    <a class="btn btn-secondary" href="emploi-du-temps.html">📅 Cursus 50 min Psyclopédia</a>
  </div>

  <h2 id="sources">Sources officielles</h2>
  <ul>{sources}</ul>
  <p class="muted">Maquettes et modalités d'examen peuvent évoluer. Consultez toujours le MCCC
  publié sur le site de l'université avant une session.</p>
  </div>
</div>
<style>
.l1-modules {{ display: flex; flex-direction: column; gap: 0.75rem; margin: 1.5rem 0; }}
.l1-module-card {{
  border: 1px solid var(--border, #e2e8f0);
  border-radius: 12px;
  background: var(--card, #fff);
  overflow: hidden;
}}
.l1-module-card summary {{
  cursor: pointer;
  padding: 1rem 1.25rem;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem 0.75rem;
  list-style: none;
}}
.l1-module-card summary::-webkit-details-marker {{ display: none; }}
.l1-module-code {{
  font-family: ui-monospace, monospace;
  font-size: 0.8rem;
  background: var(--vert-light, #ecfdf5);
  color: var(--vert, #059669);
  padding: 0.15rem 0.5rem;
  border-radius: 6px;
}}
.l1-module-fmt {{
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--muted, #64748b);
}}
.l1-module-exam {{
  margin-left: auto;
  font-size: 0.8rem;
  background: var(--gris-light, #f1f5f9);
  padding: 0.15rem 0.5rem;
  border-radius: 6px;
}}
.l1-module-body {{ padding: 0 1.25rem 1.25rem; }}
.l1-module-bloc {{ margin-bottom: 0.75rem; }}
</style>
"""
    _write("l1-lyon2.html", page_shell(
        "L1 SDE + Psychologie — Lyon 2", body, depth=0, active="Apprendre",
        description=(
            "Programme L1 Sciences de l'éducation et mineure Psychologie à Lyon 2 (1PAF02) : "
            "modules, évaluations MCCC, plans de séances et liens Psyclopédia."
        ),
    ))
    return 1
