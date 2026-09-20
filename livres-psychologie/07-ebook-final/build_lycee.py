# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Hub lycée Saint-Priest, liste d'études et quatre branches."""

import os

from shell import page_shell, page_header, slugify
from data_lycee import (
    ETABLISSEMENTS, SPECIALITES, TRONC, ATTENDUS_L1, LISTE_COMPLETE, GRAND_ORAL,
    DISSERTATION, BRANCHES, COMPARAISON, PLAN_SEMAINES, SOURCES_LYCEE,
)

BASE = os.path.dirname(os.path.abspath(__file__))


def _write(path, html):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)


def _statut_chip(statut):
    if statut == "fait":
        return '<span class="lycee-chip lycee-chip-new">Ajouté ici</span>'
    return '<span class="lycee-chip lycee-chip-site">Déjà sur le site</span>'


def render_hub():
    etab = ""
    for e in ETABLISSEMENTS:
        faits = "".join(f"<li>{f}</li>" for f in e["fait"])
        etab += f"""
        <article class="lycee-card" id="{e['id']}">
          <p class="section-eyebrow">{e['type']} · {e['ville']}</p>
          <h3>{e['nom']}</h3>
          <p class="lycee-role">{e['role']}</p>
          <p class="lycee-addr">{e['adresse']} · académie de {e['academie']}</p>
          <ul>{faits}</ul>
          <p><a href="{e['lien']}" target="_blank" rel="noopener">Source officielle / fiche</a></p>
        </article>"""

    specs = "".join(
        f"""<tr>
          <td><strong>{code}</strong><br><span class="muted">{nom}</span></td>
          <td>{lycee}</td>
          <td>{psycho}</td>
          <td><a href="categories/{href}.html">Fiche</a></td>
        </tr>"""
        for code, nom, lycee, psycho, href in SPECIALITES
    )

    tronc = "".join(
        f"""<div class="method-item"><div class="num">{annee}</div><div>
          <h4>{titre}</h4><p>{texte}</p></div></div>"""
        for annee, titre, texte in TRONC
    )

    attendus = "".join(f"<li>{a}</li>" for a in ATTENDUS_L1)

    branches = "".join(
        f"""<a class="hub-card {b['color']}" href="branches/{b['id']}.html">
          <span class="hub-ico">{b['icon']}</span>
          <h3>{b['title']}</h3>
          <p>{b['subtitle']}</p>
          <span class="hub-n">Parcours L1</span>
        </a>"""
        for b in BRANCHES
    )

    liste = ""
    for theme, items in LISTE_COMPLETE:
        rows = "".join(
            f"<li>{_statut_chip(st)} {label}</li>" for label, st in items
        )
        liste += f"""<div class="lycee-list-block" id="{slugify(theme)}">
          <h3>{theme}</h3><ul class="lycee-check">{rows}</ul></div>"""

    oraux = "".join(
        f"""<div class="ref-card {['vert','or','rose','gris'][i % 4]}">
          <div class="ref-h"><h3>{q}</h3>
          <p class="ref-sub">{lien}</p></div>
          <p>{pistes}</p>
        </div>"""
        for i, (q, pistes, lien) in enumerate(GRAND_ORAL)
    )

    diss = "".join(
        f"""<div class="method-item"><div class="num">{i:02d}</div><div>
          <h4>{t}</h4><p>{d}</p></div></div>"""
        for i, (t, d) in enumerate(DISSERTATION, 1)
    )

    plan = "".join(
        f"""<div class="method-item"><div class="num">{sem}</div><div>
          <h4>{titre}</h4><p>{desc} {' · '.join(f'<a href="{h}">ouvrir</a>' for h in hrefs)}</p>
        </div></div>"""
        for sem, titre, desc, hrefs in PLAN_SEMAINES
    )

    sources = "".join(
        f'<li><a href="{url}" target="_blank" rel="noopener">{nom}</a></li>'
        for nom, url in SOURCES_LYCEE
    )

    header = page_header(
        depth=0,
        breadcrumb=[("Accueil", "../../index.html"), ("Lycée Saint-Priest", None)],
        icon="🎓", color="or",
        title="Lycée Saint-Priest (69) → psychologie",
        subtitle="Ce qu'on y fait vraiment, comment ça prépare les quatre branches de L1, et tout ce qu'il faut ajouter pour ces études",
        chips=["📍 Condorcet · Forest · CIO", "🧭 4 branches L1", "✅ Liste complète", "🤖 Assistant IA"],
    )

    toc = """<aside class="toc-side"><h4>Sommaire</h4>
      <a href="#analyse">Ce qu'ils font au lycée</a>
      <a href="#specialites">Spécialités → psycho</a>
      <a href="#calendrier">2de → L1 Lyon 2</a>
      <a href="#branches">Quatre branches</a>
      <a href="#liste">Liste complète à maîtriser</a>
      <a href="#dissertation">Dissertation &amp; Grand oral</a>
      <a href="#plan">Six semaines</a>
      <a href="#sources">Sources</a>
    </aside>"""

    body = f"""{header}
<div class="wrap with-toc">
  {toc}
  <div class="content" style="max-width:none">

  <div class="note-box">
    <strong>Il n'existe pas de « spécialité Psychologie » au lycée.</strong> À Saint-Priest, le projet se
    construit au <a href="#condorcet">lycée Condorcet</a> (voie générale, STI2D, STMG), avec le
    <a href="#cio">CIO</a> et les psychologues de l'Éducation nationale, puis à
    <strong>Lyon 2</strong> (Institut de psychologie) : clinique, sociale, développement, cognitive,
    plus statistiques et psychobiologie. Cette page analyse le parcours réel et relie chaque matière
    du lycée à une fiche du site.
  </div>

  <h2 id="analyse">Ce qu'ils font — les établissements</h2>
  <div class="lycee-grid">{etab}</div>

  <h2 id="specialites">De chaque matière du lycée à une branche</h2>
  <p>Le ministère rappelle qu'aucune combinaison n'est obligatoire pour une licence. En pratique, les
  attendus de L1 (démarche scientifique, données, rédaction) rendent certaines spécialités plus
  confortables. Condorcet offre justement HLP, SES, HGGSP, SVT et maths.</p>
  <div style="overflow-x:auto">
    <table class="lycee-table">
      <thead><tr><th>Matière</th><th>Ce qu'on y fait</th><th>Ce que ça prépare en psycho</th><th></th></tr></thead>
      <tbody>{specs}</tbody>
    </table>
  </div>

  <h2 id="calendrier">De la 2de à la L1 Lyon 2</h2>
  <div class="method-timeline">{tronc}</div>
  <h3>Attendus utiles (sans mythologie Parcoursup)</h3>
  <ul>{attendus}</ul>
  <p>Plans B depuis Condorcet : BTS sur place, CPGE ECT, licences de socio / éducation / sciences
  cognitives, métiers du soin si ST2S ailleurs dans l'agglomération. La licence de psychologie n'est
  pas le seul débouché d'un intérêt pour l'humain.</p>

  <h2 id="branches">Les quatre branches de L1</h2>
  <p>Lyon 2 les enseigne dès le premier semestre. Chaque carte ouvre un parcours complet : objet,
  ponts lycée, notions, auteurs, expériences, éthique, checklist et quiz.</p>
  <div class="hub-grid">{branches}</div>
  <p style="margin-top:1rem"><a class="btn btn-secondary" href="branches/index.html">Comparer les quatre branches →</a></p>

  <h2 id="liste">Liste complète de ce qu'il faut pour ces études</h2>
  <p>Tout ce qu'un élève de Saint-Priest devrait trouver ici pour tenir le lycée <em>et</em> le premier
  semestre de L1. « Ajouté ici » = construit pour ce parcours. « Déjà sur le site » = relié, pas
  réécrit.</p>
  <div class="lycee-list">{liste}</div>

  <h2 id="dissertation">Dissertation HLP / philo appliquée à une étude</h2>
  <p>Le geste de L1 ressemble au Grand oral et à la dissertation : définir, problématiser, citer une
  expérience <em>avec sa limite</em>.</p>
  <div class="method-timeline">{diss}</div>
  <h3>Dix sujets de Grand oral déjà branchés sur le site</h3>
  <div class="grid-2">{oraux}</div>

  <h2 id="plan">Six semaines pour tout couvrir</h2>
  <div class="method-timeline">{plan}</div>

  <div class="cta-row">
    <a class="btn btn-primary" href="assistant.html">🤖 Demander à l'assistant</a>
    <a class="btn btn-secondary" href="quiz/quiz.html?id=lycee-orientation">🎮 Quiz lycée</a>
    <a class="btn btn-secondary" href="metiers.html">💼 Métiers et titre</a>
    <a class="btn btn-secondary" href="emploi-du-temps.html">🎓 Cours de 50 min</a>
  </div>

  <h2 id="sources">Sources</h2>
  <ul>{sources}</ul>
  <p class="muted">Les maquettes universitaires et les spécialités d'un lycée évoluent.
  Vérifiez Onisep, le site de l'établissement et Lyon 2 avant un choix définitif.</p>
  </div>
</div>
"""
    _write("lycee.html", page_shell(
        "Lycée Saint-Priest et psychologie", body, depth=0, active="Lycée",
        description="Parcours psychologie pour le lycée Condorcet de Saint-Priest (69) : spécialités, CIO, quatre branches de L1 Lyon 2, liste complète et Grand oral."))


def render_branches_index():
    rows = ""
    labels = ["", "Clinique", "Sociale", "Développement", "Cognitive"]
    for crit, c, s, d, cog in COMPARAISON:
        rows += f"""<tr>
          <th>{crit}</th>
          <td>{c}</td><td>{s}</td><td>{d}</td><td>{cog}</td>
        </tr>"""

    cards = "".join(
        f"""<a class="hub-card {b['color']}" href="{b['id']}.html">
          <span class="hub-ico">{b['icon']}</span>
          <h3>{b['title']}</h3>
          <p>{b['objet'][:180]}…</p>
          <span class="hub-n">Ouvrir le parcours</span>
        </a>"""
        for b in BRANCHES
    )

    header = page_header(
        depth=1,
        breadcrumb=[("Accueil", "../../../index.html"),
                    ("Lycée", "../lycee.html"),
                    ("Quatre branches", None)],
        icon="🧭", color="vert",
        title="Clinique · sociale · développement · cognitive",
        subtitle="Le socle que Lyon 2 enseigne dès la L1, mis en regard et relié au lycée de Saint-Priest",
        chips=["4 objets", "4 méthodes", "4 pièges lycéens"],
    )
    body = f"""{header}
<div class="section">
  <div class="hub-grid">{cards}</div>
  <h2>Tableau comparatif — pour une copie claire</h2>
  <p>En L1, une question fréquente est : <em>à quelle branche appartient ce problème, et pourquoi ?</em>
  Ce tableau donne la réponse en une ligne, puis chaque parcours développe.</p>
  <div style="overflow-x:auto">
    <table class="lycee-table lycee-table-wide">
      <thead><tr>{''.join(f'<th>{l}</th>' for l in labels)}</tr></thead>
      <tbody>{rows}</tbody>
    </table>
  </div>
  <div class="cta-row">
    <a class="btn btn-primary" href="../lycee.html">🎓 Retour au parcours lycée</a>
    <a class="btn btn-secondary" href="../quiz/quiz.html?id=branches-l1">🎮 Quiz des quatre branches</a>
    <a class="btn btn-secondary" href="../assistant.html">🤖 Poser une question</a>
  </div>
</div>
"""
    _write("branches/index.html", page_shell(
        "Quatre branches de psychologie", body, depth=1, active="Lycée",
        description="Comparer psychologie clinique, sociale, du développement et cognitive — socle L1 Lyon 2."))


def render_branche(b):
    ponts = "".join(f"<li><strong>{m}</strong> — {t}</li>" for m, t in b["lycee_ponts"])
    notions = "".join(
        f'<div class="fiche-def"><b>{n}</b> — {d}</div>' for n, d in b["notions"]
    )
    auteurs = "".join(
        f'<li><a href="../{href}">{nom}</a> — {apport}</li>' for nom, apport, href in b["auteurs"]
    )
    exps = "".join(
        f'<li><a href="../{href}"><strong>{nom}</strong></a> — {idee}</li>'
        for nom, idee, href in b["experiences"]
    )
    meth = "".join(f"<li>{m}</li>" for m in b["methodes"])
    metiers = "".join(f"<li>{m}</li>" for m in b["metiers"])
    mythes = "".join(
        f"""<div class="myth-card">
          <div class="myth-false"><span class="tag">❌</span><span>{faux}</span></div>
          <div class="myth-true"><span class="tag">✅</span><span>{vrai}</span></div>
        </div>"""
        for faux, vrai in b["mythes"]
    )
    modules = "".join(
        f'<h2 id="{slugify(t)}">{t}</h2>{html}' for t, html in b["modules"]
    )
    check = "".join(f"<li>{c}</li>" for c in b["checklist"])
    flash = "".join(
        f"""<div class="flashcard" data-card>
          <div class="flash-q">{q}</div>
          <div class="flash-a">{a}</div>
        </div>"""
        for q, a in b["flashcards"]
    )
    liens = "".join(
        f'<a class="path-step" href="../{href}"><span class="path-step-n">→</span>'
        f'<span class="path-step-title">{label}</span><span class="path-step-kind">{kind}</span></a>'
        for label, href, kind in b["liens"]
    )
    toc_mods = "".join(
        f'<a href="#{slugify(t)}">{t}</a>' for t, _ in b["modules"]
    )
    others = "".join(
        f'<a class="btn btn-secondary" href="{o["id"]}.html">{o["icon"]} {o["title"]}</a>'
        for o in BRANCHES if o["id"] != b["id"]
    )

    header = page_header(
        depth=1,
        breadcrumb=[("Accueil", "../../../index.html"),
                    ("Lycée", "../lycee.html"),
                    ("Branches", "index.html"),
                    (b["title"], None)],
        icon=b["icon"], color=b["color"],
        title=b["title"],
        subtitle=b["subtitle"],
        chips=["Lycée → L1", "Checklist", "Quiz"],
    )

    body = f"""{header}
<div class="wrap with-toc">
  <aside class="toc-side"><h4>Sommaire</h4>
    <a href="#objet">Objet</a>
    <a href="#lycee">Ponts lycée</a>
    <a href="#l1">Lyon 2</a>
    <a href="#notions">Notions</a>
    {toc_mods}
    <a href="#checklist">Checklist</a>
    <a href="#flashcards">Flashcards</a>
  </aside>
  <div class="content" style="max-width:none">
    <h2 id="objet">L'objet de la branche</h2>
    <p>{b['objet']}</p>
    <div class="fun-box">❓ <strong>Question directrice :</strong> {b['question']}</div>

    <h2 id="lycee">Ce que le lycée de Saint-Priest prépare déjà</h2>
    <ul>{ponts}</ul>

    <h2 id="l1">Ce que Lyon 2 en fait en L1</h2>
    <p>{b['l1']}</p>

    <h2 id="notions">Notions à savoir dire en une phrase</h2>
    <div class="fiche-defs">{notions}</div>

    {modules}

    <h2>Auteurs à citer</h2>
    <ul>{auteurs}</ul>
    <h2>Expériences et preuves</h2>
    <ul>{exps}</ul>
    <h2>Méthodes</h2>
    <ul>{meth}</ul>
    <h2>Métiers dans le prolongement</h2>
    <ul>{metiers}</ul>

    <h2>Idées reçues</h2>
    <div class="myth-grid">{mythes}</div>

    <h2 id="checklist">Checklist avant un DS ou un oral</h2>
    <ul class="lycee-check">{check}</ul>

    <h2 id="flashcards">Flashcards</h2>
    <div class="flash-grid">{flash}</div>

    <h2>Continuer sur le site</h2>
    <div class="path-steps">{liens}</div>

    <div class="warn-box">
      <strong>Pédagogie seulement.</strong> Rien ici ne diagnostique, ne soigne, ni ne remplace un
      professionnel. En détresse : <a href="../aide.html">page Aide</a>, 3114, 15.
    </div>

    <div class="cta-row">
      <a class="btn btn-primary" href="../quiz/quiz.html?id={b['quiz_id']}">🎮 Quiz de la branche</a>
      <a class="btn btn-secondary" href="../assistant.html?q={b['title']}">🤖 Question à l'IA</a>
      {others}
    </div>
  </div>
</div>
"""
    _write(f"branches/{b['id']}.html", page_shell(
        b["title"] + " — parcours lycée / L1", body, depth=1, active="Lycée",
        description=b["subtitle"]))


def render_all():
    render_hub()
    render_branches_index()
    for b in BRANCHES:
        render_branche(b)
    return 2 + len(BRANCHES)
