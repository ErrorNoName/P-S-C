# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Emploi du temps, médiathèque et lecteur de cours (50 min)."""

import json
import os

from shell import page_shell, page_header, ebook, asset
from content import CATEGORY_TITLE
from data_cours import ANNEE, PHASES, get_cours, get_intervenants, get_modules

BASE = os.path.dirname(os.path.abspath(__file__))
EB = "livres-psychologie/07-ebook-final/"


def _write(path, html):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full) if os.path.dirname(full) else BASE, exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)


def _css(depth):
    return f'<link rel="stylesheet" href="{asset(depth, "css/cours.css")}">'


def _scripts(depth, extra=""):
    return (
        f'<script src="{asset(depth, "js/cours.js")}"></script>'
        + (extra or "")
    )


def _cat_title(cat_id):
    return CATEGORY_TITLE.get(cat_id, cat_id)


def export_programme(cours):
    payload = {
        "annee": ANNEE,
        "phases": PHASES,
        "cours": cours,
    }
    path = os.path.join(BASE, "cours", "programme.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, separators=(",", ":"))
    return path


def render_emploi(cours):
    n = len(cours)
    header = page_header(
        depth=0,
        breadcrumb=[("Accueil", "../../index.html"), ("Emploi du temps & Cours", None)],
        icon="🎓", color="vert",
        title="Emploi du temps & Cours",
        subtitle=(
            f"Cursus annuel {ANNEE['label']} : {n} séances de 50 minutes, "
            "en direct ou en replay, avec ressources synchronisées."
        ),
        chips=[
            f"📅 {ANNEE['label']}",
            f"⏱️ {n} × 50 min",
            "🟢 Direct ou replay",
            "💾 Progression locale",
        ],
    )

    body = f"""{header}
<div class="section cours-page" data-cours-page="emploi">
  <div class="cours-toolbar">
    <div class="cours-countdown" id="cours-countdown" aria-live="polite">
      <p class="section-eyebrow">Prochain cours planifié</p>
      <h2 id="countdown-title">Chargement du calendrier…</h2>
      <p id="countdown-meta" class="section-desc"></p>
      <div class="countdown-digits" id="countdown-digits">
        <span><b id="cd-j">–</b><small>j</small></span>
        <span><b id="cd-h">–</b><small>h</small></span>
        <span><b id="cd-m">–</b><small>min</small></span>
        <span><b id="cd-s">–</b><small>s</small></span>
      </div>
      <div class="cta-row" id="countdown-actions"></div>
      <div class="emploi-plate-row">
        <div data-emploi-plate></div>
        <div>
          <p class="tiny-note">Active les <a href="rappels.html">rappels</a> pour être prévenu
          une heure avant, quinze minutes avant, et à l'heure du cours — tant qu'un onglet
          du site reste ouvert.</p>
        </div>
      </div>
    </div>
    <div class="cours-progress-card" id="cours-progress-card">
      <p class="section-eyebrow">Ta progression</p>
      <div class="cours-rings">
        <div><strong data-cours-followed>0</strong><span>cours suivis</span></div>
        <div><strong data-cours-attendance>0 %</strong><span>assiduité</span></div>
        <div><strong data-cours-quizavg>—</strong><span>moyenne quiz</span></div>
      </div>
      <p class="tiny-note">Enregistré uniquement dans ce navigateur (localStorage). Rien n'est envoyé.</p>
    </div>
  </div>

  <div class="cours-view-switch" role="tablist">
    <button type="button" class="pill-link active" data-cours-view="semaine">Vue semaine</button>
    <button type="button" class="pill-link" data-cours-view="mois">Vue calendrier</button>
    <button type="button" class="pill-link" data-cours-jump="-1">←</button>
    <button type="button" class="pill-link" data-cours-jump="0">Aujourd'hui</button>
    <button type="button" class="pill-link" data-cours-jump="1">→</button>
    <span class="cours-view-label" id="cours-view-label"></span>
  </div>
  <div id="cours-calendar" class="cours-calendar"></div>

  <div class="section-head" style="margin-top:2.4rem">
    <p class="section-eyebrow">Année {ANNEE['id']}</p>
    <h2 class="section-title" style="font-size:1.45rem">Deux semestres, quatre phases, une heure de cours moins dix minutes</h2>
    <p class="section-desc">Chaque séance tient exactement 50 minutes : exposition, démonstration,
    cas clinique, synthèse et quiz flash. Le lundi à 10 h est réservé au cours magistral ;
    le jeudi à 14 h au travail dirigé. Tu peux entrer en direct pendant la fenêtre, ou
    rouvrir le replay à tout moment — le lecteur resynchronise vidéo et fiches.</p>
  </div>
  <div class="phase-legend">
    <span><i class="ph expo"></i> Exposition 0–18 min</span>
    <span><i class="ph demo"></i> Démonstration 18–32 min</span>
    <span><i class="ph cas"></i> Cas clinique 32–42 min</span>
    <span><i class="ph quiz"></i> Synthèse &amp; quiz 42–50 min</span>
  </div>

  <div class="cta-row" style="margin-top:1.6rem">
    <a class="btn btn-primary" href="cours/index.html">📼 Cours &amp; archives</a>
    <a class="btn btn-secondary" href="parcours.html">🧭 Parcours guidés</a>
    <a class="btn btn-secondary" href="apprendre.html">🎓 Méthodes d'apprentissage</a>
  </div>
</div>
"""
    _write("emploi-du-temps.html", page_shell(
        "Emploi du temps & Cours", body, depth=0, active="Cours",
        description=(
            f"Emploi du temps annuel de Psyclopédia : {n} cours magistraux et TD de 50 minutes, "
            "calendrier interactif, compte à rebours et replays synchronisés."
        ),
        extra_head=_css(0),
        extra_scripts=_scripts(0),
    ))


def render_archives(cours):
    cats = []
    seen = set()
    for c in cours:
        if c["cat"] not in seen:
            seen.add(c["cat"])
            cats.append(c["cat"])
    cat_opts = "".join(
        f'<option value="{cid}">{_cat_title(cid)}</option>' for cid in cats
    )
    mod_opts = "".join(f'<option value="{m}">{m}</option>' for m in get_modules(cours))
    guest_opts = "".join(f'<option value="{g}">{g}</option>' for g in get_intervenants(cours))

    header = page_header(
        depth=1,
        breadcrumb=[
            ("Accueil", "../../../index.html"),
            ("Emploi du temps", "../emploi-du-temps.html"),
            ("Cours & Archives", None),
        ],
        icon="📼", color="or",
        title="Cours & Archives",
        subtitle=(
            f"{len(cours)} séances archivées, classées par catégorie, thème et intervenant. "
            "Chaque replay rouvre le lecteur synchronisé et ton carnet de notes."
        ),
        chips=[f"📼 {len(cours)} replays", f"👤 {len(get_intervenants(cours))} intervenants",
               "📝 Notes exportables"],
    )

    body = f"""{header}
<div class="section cours-page" data-cours-page="archives">
  <div class="cours-filters">
    <label>Catégorie
      <select id="arch-cat"><option value="">Toutes</option>{cat_opts}</select>
    </label>
    <label>Module
      <select id="arch-mod"><option value="">Tous</option>{mod_opts}</select>
    </label>
    <label>Intervenant
      <select id="arch-guest"><option value="">Tous</option>{guest_opts}</select>
    </label>
    <label>Recherche
      <input type="search" id="arch-q" placeholder="Titre, thème, mot-clé…">
    </label>
  </div>
  <p class="tiny-note" id="arch-count"></p>
  <div class="arch-grid" id="arch-grid"></div>
</div>
"""
    _write("cours/index.html", page_shell(
        "Cours & Archives", body, depth=1, active="Cours",
        description=(
            "Médiathèque des cours magistraux et travaux dirigés de Psyclopédia : "
            "replays francophones, filtres et notes locales."
        ),
        extra_head=_css(1),
        extra_scripts=_scripts(1),
    ))


def render_lecteur():
    header = page_header(
        depth=1,
        breadcrumb=[
            ("Accueil", "../../../index.html"),
            ("Emploi du temps", "../emploi-du-temps.html"),
            ("Archives", "index.html"),
            ("Lecteur", None),
        ],
        icon="🎬", color="rose",
        title="Lecteur de cours",
        subtitle="Vidéo francophone, ressources synchronisées, surlignage en direct et carnet de notes.",
        chips=["▶️ YouTube FR", "📄 Fiches live", "🎤 Karaoké", "📝 Notes MD / PDF"],
    )

    phase_bar = "".join(
        f'<div class="phase-seg {p["id"]}" data-phase="{p["id"]}" style="flex:{p["end"]-p["start"]}">'
        f'<span>{p["label"]}</span></div>'
        for p in PHASES
    )

    body = f"""{header}
<div class="section cours-page lecteur-page" data-cours-page="lecteur" id="lecteur-root">
  <div class="lecteur-top">
    <div>
      <p class="section-eyebrow" id="lec-kicker">Séance</p>
      <h2 id="lec-title" class="section-title" style="font-size:1.55rem">Chargement…</h2>
      <p id="lec-meta" class="section-desc"></p>
    </div>
    <div class="lecteur-actions">
      <button type="button" class="btn btn-secondary" id="btn-cinema">🎬 Mode cinéma</button>
      <button type="button" class="btn btn-secondary" id="btn-start">▶️ Commencer la séance</button>
      <a class="btn btn-secondary" href="../emploi-du-temps.html">📅 Emploi du temps</a>
    </div>
  </div>

  <div class="phase-track" id="phase-track" aria-hidden="false">
    <div class="phase-segs">{phase_bar}</div>
    <div class="phase-needle" id="phase-needle"></div>
  </div>
  <p class="phase-now" id="phase-now">Exposition · 00:00 / 50:00</p>

  <div class="lecteur-grid" id="lecteur-grid">
    <div class="lecteur-col video-col">
      <div class="yt-stage" id="yt-stage">
        <div id="yt-player"></div>
        <button type="button" class="yt-fallback" id="yt-fallback" hidden>
          La lecture automatique a été bloquée. Clique pour lancer la vidéo.
        </button>
      </div>
      <p class="tiny-note" id="yt-credit"></p>
      <div class="notes-box">
        <div class="notes-head">
          <h3>Notes de séance</h3>
          <div>
            <button type="button" class="pill-link" id="btn-md">Exporter Markdown</button>
            <button type="button" class="pill-link" id="btn-pdf">Exporter PDF</button>
          </div>
        </div>
        <textarea id="cours-notes" rows="7" placeholder="Écris ici pendant la vidéo. Sauvegarde automatique sur cet appareil."></textarea>
      </div>
    </div>
    <aside class="lecteur-col res-col" id="res-col">
      <div class="sync-card current" id="sync-current">
        <p class="section-eyebrow">En ce moment</p>
        <h3 id="sync-title">Les fiches s'afficheront avec la vidéo</h3>
        <p id="sync-body"></p>
        <p class="karaoke" id="sync-karaoke"></p>
      </div>
      <div data-cours-plate class="cours-plate-host"></div>
      <div id="res-list" class="res-list"></div>
      <div class="quiz-box" id="quiz-box">
        <h3>Quiz flash</h3>
        <p class="tiny-note">Quatre questions de contrôle, notées localement. Pas un examen officiel.</p>
        <div id="quiz-mount"></div>
      </div>
    </aside>
  </div>

  <div class="lec-links" id="lec-links"></div>
  <p class="tiny-note" style="margin-top:1.2rem">⚠️ Contenu pédagogique. Une séance ne diagnostique rien,
  ne remplace pas un professionnel, et les vidéos YouTube restent la propriété de leurs auteurs.
  Si les sous-titres YouTube sont inaccessibles, le lecteur bascule sur la timeline JSON du cours.</p>
</div>
<script src="https://www.youtube.com/iframe_api"></script>
"""
    _write("cours/lecteur.html", page_shell(
        "Lecteur de cours", body, depth=1, active="Cours",
        description=(
            "Lecteur synchronisé de Psyclopédia : conférence francophone, fiches en direct, "
            "surlignage des notions et carnet de notes exportable."
        ),
        extra_head=_css(1),
        extra_scripts=_scripts(1),
        wide=True,
        body_attrs='class="has-lecteur"',
    ))


def render_all():
    cours = get_cours()
    export_programme(cours)
    render_emploi(cours)
    render_archives(cours)
    render_lecteur()
    return len(cours)
