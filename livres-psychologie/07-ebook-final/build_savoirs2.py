# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Pages v4 : courants, idées reçues, questions fréquentes et aide."""

import os

from shell import DISCORD_INVITE, page_shell, page_header, strip_html
from data_courants import COURANTS
from data_mythes import MYTHES
from data_faq import FAQ
from data_aide import URGENCES, ECOUTE, PARCOURS_SOIN, RESSOURCES_LIBRES

BASE = os.path.dirname(os.path.abspath(__file__))
COLORS = ["vert", "or", "rose", "gris"]

VERDICT_LABEL = {
    "faux": ("✗ Faux", "faux"),
    "exagere": ("~ Très exagéré", "exagere"),
    "partiel": ("≈ En partie vrai", "partiel"),
}


def _write(path, html_content):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html_content)


def _toolbar(placeholder, familles, count, mot="fiches"):
    chips = '<button class="search-filter active" data-famille="all">Toutes</button>'
    chips += "".join(
        f'<button class="search-filter" data-famille="{f}">{f}</button>' for f in familles
    )
    return f"""
<div class="ref-toolbar" data-ref-filter>
  <input type="search" placeholder="{placeholder}" aria-label="Filtrer la liste">
  <span class="ref-count">{count} {mot}</span>
</div>
<div class="search-filters" data-ref-filter style="padding:0 0 1.2rem;border:none">{chips}</div>"""


# --------------------------------------------------------------------------
# Les grands courants
# --------------------------------------------------------------------------

def render_courants():
    cards = ""
    for i, (cid, nom, periode, figures, postulat, methode, apport, critique, heritage) in enumerate(COURANTS, 1):
        color = COLORS[i % len(COLORS)]
        cards += f"""<div class="ref-card {color}" data-ref-id="{cid}" data-famille="{periode.split('-')[0][:4]}" data-search="{nom} {figures} {periode} {strip_html(postulat)}">
          <div class="ref-card-head">
            <span class="ref-n">{i:02d}</span>
            <div class="ref-h"><h3>{nom}</h3><p class="ref-sub">{periode} · {figures}</p></div>
            <span class="ref-chev">▾</span>
          </div>
          <div class="ref-card-body">
            <div class="ref-field"><h5>Le postulat de départ</h5><p>{postulat}</p></div>
            <div class="ref-field"><h5>Comment on y travaille</h5><p>{methode}</p></div>
            <div class="ref-field"><h5>Ce que le courant a apporté</h5><p>{apport}</p></div>
            <div class="ref-field"><h5>Pourquoi on en est revenu</h5><p>{critique}</p></div>
            <div class="ref-field"><h5>Ce qu'il en reste aujourd'hui</h5><p>{heritage}</p></div>
            <div class="ref-tags"><span>{periode}</span><span>{figures.split(',')[0]}</span></div>
          </div>
        </div>"""

    periodes = sorted(set(c[2].split("-")[0][:4] for c in COURANTS))

    header = page_header(
        depth=1,
        breadcrumb=[("Accueil", "../../../index.html"), ("Références", "index.html"), ("Courants", None)],
        icon="🏛️", color="or",
        title="Les grands courants de la psychologie",
        subtitle="Quatorze écoles, et surtout les raisons pour lesquelles chacune est née contre la précédente",
        chips=[f"🏛️ {len(COURANTS)} courants", "🕰️ De 1879 à aujourd'hui", "⚖️ Apports et critiques"],
    )

    body = f"""{header}
<div class="section">
  <p class="section-desc" style="max-width:760px">L'histoire de la psychologie ne s'empile pas, elle rebondit.
  Chaque école est d'abord une objection : le behaviorisme naît du reproche fait à l'introspection de ne rien
  pouvoir trancher, le cognitivisme du constat que le behaviorisme ne peut expliquer le langage, la psychologie
  culturelle de la découverte que les résultats « universels » venaient tous des mêmes campus. Lire ces fiches
  dans l'ordre, c'est suivre une conversation de cent cinquante ans.</p>

  {_toolbar("Filtrer par courant, auteur, période…", periodes, len(COURANTS), "courants")}
  {cards}

  <div class="note-box">
    <strong>Aucun de ces courants n'est mort.</strong> Le conditionnement de Pavlov reste vrai, les lois de la
    Gestalt structurent les interfaces que vous utilisez aujourd'hui, et l'écoute rogérienne est le facteur
    commun de toutes les psychothérapies efficaces. Ce qui a disparu, ce sont leurs prétentions à tout
    expliquer seuls.
  </div>
</div>
"""
    _write("references/courants.html", page_shell(
        "Les grands courants", body, depth=1, active="Références",
        description="Les 14 grands courants de la psychologie expliqués en français : postulat, méthode, apports, critiques et héritage, du structuralisme aux neurosciences cognitives."))


# --------------------------------------------------------------------------
# Idées reçues
# --------------------------------------------------------------------------

def render_mythes():
    familles = sorted(set(m[2] for m in MYTHES))

    cards = ""
    for i, (mid, affirmation, famille, verdict, savoir, origine, nuance) in enumerate(MYTHES, 1):
        label, cls = VERDICT_LABEL[verdict]
        cards += f"""<div class="mythe-card {cls}" data-ref-id="{mid}" data-famille="{famille}" data-search="{strip_html(affirmation)} {famille} {strip_html(savoir)}">
          <div class="ref-card-head">
            <span class="ref-n">{i:02d}</span>
            <div class="ref-h"><h3>{affirmation}</h3><p class="ref-sub">{famille}</p></div>
            <span class="verdict {cls}">{label}</span>
            <span class="ref-chev">▾</span>
          </div>
          <div class="ref-card-body">
            <div class="ref-field"><h5>Ce que montrent les données</h5><p>{savoir}</p></div>
            <div class="ref-field"><h5>D'où vient la croyance</h5><p>{origine}</p></div>
            <div class="ref-field"><h5>La part de vérité</h5><p>{nuance}</p></div>
          </div>
        </div>"""

    n_faux = sum(1 for m in MYTHES if m[3] == "faux")

    header = page_header(
        depth=1,
        breadcrumb=[("Accueil", "../../../index.html"), ("Références", "index.html"), ("Idées reçues", None)],
        icon="🧹", color="rose",
        title="Idées reçues et neuromythes",
        subtitle=f"{len(MYTHES)} affirmations très répandues, passées au crible des données disponibles",
        chips=[f"🧹 {len(MYTHES)} idées examinées", f"✗ {n_faux} clairement fausses", "🔍 Origine retracée"],
    )

    body = f"""{header}
<div class="section">
  <p class="section-desc" style="max-width:760px">Chaque fiche suit le même plan : ce que disent réellement les
  données, d'où vient la croyance, et la part de vérité qu'elle contient presque toujours. Cette dernière rubrique
  est la plus importante : une idée reçue survit parce qu'elle s'appuie sur quelque chose de réel qu'elle
  déforme. Comprendre ce noyau vaut mieux que retenir un simple « c'est faux ».</p>

  {_toolbar("Filtrer par affirmation, domaine…", familles, len(MYTHES), "idées reçues")}
  {cards}

  <div class="note-box">
    <strong>Pourquoi ces croyances résistent.</strong> Corriger une information fausse en la répétant la rend
    parfois plus familière, donc plus crédible. La stratégie qui fonctionne est de fournir une explication de
    remplacement complète : le cerveau n'abandonne pas volontiers une explication, il l'échange contre une
    meilleure. C'est la raison pour laquelle chaque fiche dit ce qui est vrai, et pas seulement ce qui est faux.
  </div>
</div>
"""
    _write("references/mythes.html", page_shell(
        "Idées reçues et neuromythes", body, depth=1, active="Références",
        description=f"{len(MYTHES)} idées reçues sur le cerveau et la psychologie examinées en français : ce que disent les données, l'origine de la croyance et sa part de vérité."))


# --------------------------------------------------------------------------
# Questions fréquentes
# --------------------------------------------------------------------------

def render_faq():
    familles = []
    for _fid, _q, famille, _r in FAQ:
        if famille not in familles:
            familles.append(famille)

    sommaire = "".join(f'<a class="pill-link" href="#{f.replace(" ", "-").lower()}">{f}</a>' for f in familles)

    blocks = ""
    for famille in familles:
        entrees = [e for e in FAQ if e[2] == famille]
        items = "".join(
            f"""<details class="faq-item" id="{fid}">
              <summary>{question}</summary>
              <div class="faq-answer">{reponse}</div>
            </details>"""
            for fid, question, _f, reponse in entrees
        )
        blocks += f"""
<div class="faq-block" id="{famille.replace(' ', '-').lower()}">
  <h2 class="faq-famille">{famille} <span>{len(entrees)} questions</span></h2>
  {items}
</div>"""

    header = page_header(
        depth=0,
        breadcrumb=[("Accueil", "../../index.html"), ("Questions fréquentes", None)],
        icon="❓", color="vert",
        title="Questions fréquentes",
        subtitle=f"{len(FAQ)} questions que tout le monde se pose, avec des réponses qui disent aussi ce qu'on ignore",
        chips=[f"❓ {len(FAQ)} questions", f"🗂️ {len(familles)} thèmes", "📖 Réponses développées"],
    )

    body = f"""{header}
<div class="section">
  <p class="section-desc" style="max-width:760px">Les réponses privilégient l'exactitude sur la concision. Quand
  un point est réellement débattu, c'est dit ; quand un résultat populaire s'est effondré à la réplication,
  c'est dit aussi. Cliquez sur une question pour déplier la réponse.</p>
  <div class="pill-row">{sommaire}</div>
  {blocks}

  <div class="warn-box">
    <strong>Une question personnelle ?</strong> Ces réponses sont générales et pédagogiques. Si votre question
    porte sur votre situation ou celle d'un proche, la page <a href="aide.html">aide et ressources</a> indique
    à qui s'adresser concrètement.
  </div>
</div>
"""
    _write("faq.html", page_shell(
        "Questions fréquentes", body, depth=0, active="Apprendre",
        description=f"{len(FAQ)} questions fréquentes sur la psychologie, le cerveau, l'apprentissage, la santé mentale et la méthode scientifique, répondues en français."))


# --------------------------------------------------------------------------
# Aide et ressources
# --------------------------------------------------------------------------

def render_aide():
    zones = []
    for zone, *_ in URGENCES:
        if zone not in zones:
            zones.append(zone)

    urgences_html = ""
    for zone in zones:
        lignes = "".join(
            f"""<div class="aide-ligne">
              <div class="aide-num">{numero}</div>
              <div class="aide-info">
                <h4>{nom}</h4>
                <p class="aide-horaire">{horaires}</p>
                <p>{description}</p>
              </div>
            </div>"""
            for z, nom, numero, horaires, description in URGENCES if z == zone
        )
        urgences_html += f'<div class="aide-zone"><h3>{zone}</h3>{lignes}</div>'

    ecoute_html = "".join(
        f"""<div class="aide-ligne secondaire">
          <div class="aide-num petit">{numero}</div>
          <div class="aide-info"><h4>{nom}</h4><p>{description}</p></div>
        </div>"""
        for nom, numero, description in ECOUTE
    )

    parcours_html = "".join(
        f'<div class="aide-bloc" id="{pid}"><h3>{titre}</h3>{contenu}</div>'
        for pid, titre, contenu in PARCOURS_SOIN
    )

    ressources_html = "".join(
        f'<li><b>{nom}</b>{f" — <a href=\"{url}\" target=\"_blank\" rel=\"noopener\">{url}</a>" if url else ""}'
        f"<br>{description}</li>"
        for nom, url, description in RESSOURCES_LIBRES
    )

    header = page_header(
        depth=0,
        breadcrumb=[("Accueil", "../../index.html"), ("Aide et ressources", None)],
        icon="🤝", color="rose",
        title="Aide, orientation et ressources",
        subtitle="Où s'adresser quand on ne va pas bien, ou quand on s'inquiète pour quelqu'un",
        chips=[f"☎️ {len(URGENCES)} lignes d'urgence", f"👂 {len(ECOUTE)} lignes d'écoute", "🏥 Parcours de soin"],
    )

    body = f"""{header}
<div class="section">
  <div class="note-box">
    <strong>Communauté Discord.</strong> Le serveur
    <a href="{DISCORD_INVITE}" target="_blank" rel="noopener">Psyclopédia</a>
    prolonge le site : annonces des cours de 50 minutes, forums par champ, fiches et entraide.
    Ce n'est <em>pas</em> un lieu de soin ni de diagnostic. En détresse, utilisez d'abord les
    numéros ci-dessous.
  </div>

  <div class="urgence-box">
    <h2>En cas d'urgence</h2>
    <p>Si vous ou quelqu'un d'autre êtes en danger immédiat, appelez le <b>15</b> ou le <b>112</b>, ou rendez-vous
    aux urgences les plus proches. En France, le <b>3114</b> est joignable gratuitement à toute heure pour toute
    situation de souffrance suicidaire, y compris si vous appelez pour quelqu'un d'autre.</p>
  </div>

  <h2 class="section-title" style="margin-top:2.5rem">Lignes d'urgence et de crise</h2>
  <p class="section-desc" style="max-width:760px">Ces dispositifs sont publics ou associatifs, gratuits sauf
  mention contraire, et tenus par des personnes formées. Appeler n'engage à rien et ne déclenche aucune démarche
  automatique.</p>
  {urgences_html}

  <h2 class="section-title" style="margin-top:2.5rem">Écoute, addictions et situations particulières</h2>
  <div class="aide-zone">{ecoute_html}</div>

  <h2 class="section-title" style="margin-top:2.5rem">Trouver de l'aide et s'y retrouver</h2>
  {parcours_html}

  <h2 class="section-title" style="margin-top:2.5rem">Pour aller plus loin par soi-même</h2>
  <p class="section-desc" style="max-width:760px">Ressources francophones en accès libre, utiles pour vérifier
  une information ou lire directement la recherche plutôt que son résumé de presse.</p>
  <ul class="ressource-list">{ressources_html}</ul>

  <div class="warn-box" style="margin-top:2rem">
    <strong>Vérifiez avant d'appeler.</strong> Les numéros, horaires et conditions de prise en charge évoluent.
    Ceux indiqués ici sont des dispositifs nationaux stables, mais en cas de doute, la source faisant foi reste
    le site officiel de l'organisme concerné ou celui de l'Assurance maladie.
  </div>

  <div class="note-box">
    <strong>Ce site ne soigne pas.</strong> Psyclopédia explique des mécanismes et décrit des troubles à des fins
    pédagogiques. Il ne pose pas de diagnostic, ne remplace aucune consultation, et la reconnaissance de soi dans
    une description n'a aucune valeur diagnostique.
  </div>
</div>
"""
    _write("aide.html", page_shell(
        "Aide et ressources", body, depth=0, active="Apprendre",
        description="Où trouver de l'aide psychologique : numéros d'urgence et d'écoute en France, Belgique, Suisse et Canada, parcours de soin, remboursement et ressources en accès libre."))


def render_all():
    render_courants()
    render_mythes()
    render_faq()
    render_aide()
