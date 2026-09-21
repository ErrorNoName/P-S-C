# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Génération de la page d'accueil, à la racine du dépôt."""

import os

from shell import DISCORD_INVITE, page_shell
from content import (
    CATEGORIES, DICTIONNAIRE, QUIZZES, BOOKS,
    EXPERIENCES, AUTEURS, TROUBLES, BIAIS, TESTS, CHRONOLOGIE_TRIEE,
    THEORIES, CAS, DEBATS, METHODES_NOTIONS, LEXIQUE_EN, PRATIQUES, METIERS,
)
from data_laboratoire import EXPERIENCES_LAB
from data_courants import COURANTS
from data_mythes import MYTHES
from data_faq import FAQ
from data_autoeval import EVALUATIONS

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
EB = "livres-psychologie/07-ebook-final/"

# Catégories mises en avant dans la barre d'accès rapide.
RACCOURCIS = [
    ("03-cognitive", "vert", "💭", "Cognitive"),
    ("04-sociale", "or", "👥", "Sociale"),
    ("09-psychopathologie", "rose", "🩺", "Psychopathologie"),
    ("08-neurosciences", "gris", "🧠", "Neurosciences"),
    ("27-science-psychologique", "vert", "🔬", "Science psycho."),
    ("07-emotions", "rose", "❤️", "Émotions"),
    ("22-numerique", "or", "📱", "Numérique"),
]

NOUVEAUTES = [
    ("🏛️", f"{len(COURANTS)} grands courants", "Pourquoi chaque école est née contre la précédente"),
    ("🧹", f"{len(MYTHES)} idées reçues démontées", "Les 10 % du cerveau, les styles d'apprentissage, l'effet Mozart…"),
    ("❓", f"{len(FAQ)} questions fréquentes", "Des réponses qui disent aussi ce qu'on ignore encore"),
    ("🤝", "Aide et ressources", "Numéros d'urgence, parcours de soin, remboursement, où consulter"),
    ("📋", f"{len(EVALUATIONS)} auto-évaluations", "Comprendre la psychométrie en la pratiquant sur soi"),
    ("🧩", f"{len(THEORIES)} théories et modèles", "L'idée, le mécanisme, les usages et les limites"),
    ("🗃️", f"{len(CAS)} cas cliniques historiques", "Phineas Gage, H.M., Genie, Anna O., les jumeaux séparés…"),
    ("⚖️", f"{len(DEBATS)} débats argumentés", "Inné/acquis, psychanalyse, écrans, libre arbitre, QI…"),
    ("🔬", "Méthodes et statistiques", f"12 chapitres et {len(METHODES_NOTIONS)} notions pour lire une étude"),
    ("🧰", f"{len(PRATIQUES)} fiches pratiques", "Apprendre, dormir, décider, communiquer, gérer le stress"),
    ("💼", f"{len(METIERS)} métiers et parcours d'études", "Clinicien, neuropsychologue, ergonome, UX, psychiatre…"),
    ("🧪", f"Laboratoire : {len(EXPERIENCES_LAB)} expériences jouables", "Stroop, empan, temps de réaction, Müller-Lyer, ancrage"),
    ("🔁", "Révision espacée", "Un algorithme te représente chaque notion au bon moment"),
    ("🎓", "Cours magistraux de 50 min", "Cursus annuel, calendrier, replays YouTube francophones et fiches en direct"),
    ("💬", "Serveur Discord", "Cours, fiches, forums thématiques et entraide — le site reste la source"),
    ("🔔", "Rappels et planches", "Pensées du jour, notifications de cours, cabinet de gravures géométriques"),
    ("🔭", "Zone de découverte", "Planches d'expériences, vraies images du cerveau, projets ouverts, cave des mythes"),
    ("🧭", "Quatre branches de la psychologie", "Clinique, sociale, développement, cognitive — le socle de toute licence"),
    ("🤖", "Assistant du site", "Questions en français, réponses sourcées dans tout le corpus"),
    ("👤", "Compte étudiant", "E-mail ou Google, notes de cours et scores enregistrés"),
]

# (href, classe couleur, icône, titre, description, compteur)
OUTILS_V3 = [
    ("references/courants.html", "or", "🏛️", "Les grands courants",
     "L'histoire de la discipline lue comme une conversation : chaque école naît d'une objection faite "
     "à la précédente.", f"{len(COURANTS)} écoles"),
    ("references/mythes.html", "rose", "🧹", "Idées reçues et neuromythes",
     "Ce que disent réellement les données, d'où vient la croyance, et la part de vérité qu'elle déforme "
     "presque toujours.", f"{len(MYTHES)} idées"),
    ("faq.html", "vert", "❓", "Questions fréquentes",
     "Les questions que tout le monde se pose, avec des réponses qui précisent aussi ce qu'on ignore "
     "encore.", f"{len(FAQ)} réponses"),
    ("auto-evaluations.html", "gris", "📋", "Auto-évaluations",
     "Cinq questionnaires écrits pour le site, qui font comprendre de l'intérieur comment se construit "
     "une mesure en psychologie.", f"{len(EVALUATIONS)} questionnaires"),
    ("aide.html", "rose", "🤝", "Aide et ressources",
     "Où s'adresser quand on ne va pas bien : urgences, lignes d'écoute, parcours de soin, "
     "remboursement, ressources en accès libre.", "France · Belgique · Suisse · Canada"),
    ("references/theories.html", "", "🧩", "Théories et modèles",
     "Le cœur conceptuel de la discipline : ce que chaque modèle affirme, comment il fonctionne, "
     "à quoi il sert et là où il échoue.", f"{len(THEORIES)} fiches"),
    ("references/cas.html", "rose", "🗃️", "Cas cliniques célèbres",
     "Les patients singuliers qui ont fait basculer la théorie, de la barre à mine de Phineas Gage "
     "à l'amnésie de H.M.", f"{len(CAS)} histoires"),
    ("references/debats.html", "or", "⚖️", "Débats et controverses",
     "Chaque camp présenté au meilleur de ses arguments, puis l'état réel des données disponibles.",
     f"{len(DEBATS)} dossiers"),
    ("methodes.html", "gris", "🔬", "Méthodes et statistiques",
     "Comment on prouve quelque chose en psychologie : plans d'expérience, p-value, taille d'effet, "
     "biais, éthique et crise de la réplication.", f"12 chapitres · {len(METHODES_NOTIONS)} notions"),
    ("pratique.html", "vert", "🧰", "Psychologie appliquée",
     "Ce que la recherche permet vraiment de faire dans la vie quotidienne, en protocoles pas à pas.",
     f"{len(PRATIQUES)} fiches"),
    ("metiers.html", "or", "💼", "Métiers et études",
     "Vingt métiers décrits de l'intérieur — mission, formation, quotidien, réalités du terrain — "
     "et les quatre étapes du cursus français.", f"{len(METIERS)} métiers"),
    ("laboratoire.html", "rose", "🧪", "Le laboratoire",
     "Des expériences classiques rejouées directement dans le navigateur, avec tes propres résultats "
     "chiffrés et leur explication.", f"{len(EXPERIENCES_LAB)} expériences"),
    ("revision.html", "", "🔁", "Révision espacée",
     "Toutes les notions du site transformées en cartes, représentées au moment où tu es sur le point "
     "de les oublier.", "1 000 cartes"),
    ("lexique.html", "gris", "🌍", "Lexique anglais-français",
     "Le vocabulaire des articles scientifiques, avec les faux amis qui piègent les lecteurs francophones.",
     f"{len(LEXIQUE_EN)} termes"),
    ("fiches/index.html", "vert", "🗂️", "Fiches imprimables",
     "L'essentiel de chaque domaine condensé sur une page, mis en forme pour l'impression et la révision "
     "hors écran.", f"{len(CATEGORIES)} fiches"),
    ("plan.html", "or", "🗺️", "Plan du site et index A-Z",
     "Toutes les pages du site et un index alphabétique de chaque notion, expérience, auteur et trouble.",
     "800+ entrées"),
    ("lecteur.html", "rose", "📖", "Le lecteur de livres",
     "Les ouvrages originaux lus page par page, avec reconnaissance du texte scanné et modernisation "
     "du français ancien.", f"{len(BOOKS)} ouvrages"),
    ("emploi-du-temps.html", "vert", "🎓", "Emploi du temps & cours",
     "Un cursus annuel de cours magistraux et de TD de 50 minutes, avec compte à rebours, "
     "replays francophones et ressources synchronisées.", "60 séances · 2 semestres"),
    (DISCORD_INVITE, "or", "💬", "Communauté Discord",
     "Annonces de cours, forums par champ, fiches et entraide. Ce n'est pas un soin : "
     "en détresse, ouvrez d'abord la page Aide.", "Rejoindre"),
    ("rappels.html", "or", "🔔", "Rappels & planches",
     "Citations et questions dans la journée, rappels avant chaque cours de 50 minutes, "
     "et un cabinet de planches de psychologie géométrique.", "Pensées · gravures"),
    ("decouverte.html", "vert", "🔭", "Zone de découverte",
     "Planches d'expériences sur le cerveau, galerie d'images libres, techniques, "
     "projets ouverts (Connectome, OpenNeuro, Allen, BigBrain) et cave des mythes.", "Images · sources"),
    ("metiers.html", "or", "🎓", "Métiers et études",
     "Du lycée à la licence, le titre de psychologue, et les quatre branches de L1 "
     "reliées aux fiches du site.", "Parcours"),
    ("assistant.html", "vert", "🤖", "Assistant",
     "Une question, une réponse complète tirée uniquement des pages du site, avec les sources.",
     "Ctrl + J"),
    ("compte.html", "or", "👤", "Compte étudiant",
     "Connexion e-mail/mot de passe ou Google. Progression, notes de cours et scores conservés.",
     "SQLite · IndexedDB"),
]


def _cat_cards():
    cards = ""
    for c in CATEGORIES:
        cards += f"""<a href="{EB}categories/{c['id']}.html" class="cat-card" data-cat-id="{c['id']}">
          <span class="cat-check">✅</span>
          <div class="cat-card-icon" style="background:var(--{c['color']}-light)">{c['icon']}</div>
          <h3>{c['num']} · {c['title']}</h3>
          <p>{c['subtitle']}</p>
          <div class="cat-progress-track"><div class="cat-progress-fill" data-cat-key="{c['id']}"></div></div>
        </a>"""
    return cards


def _sparkline():
    return "".join(
        f'<i data-spark-key="{c["id"]}" style="height:{18 + (i * 7) % 34}px"></i>'
        for i, c in enumerate(CATEGORIES)
    )


def _quiz_preview():
    cards = ""
    for q in QUIZZES[:3] + [next(x for x in QUIZZES if x["id"] == "examen-final")]:
        cards += f"""<a href="{EB}quiz/quiz.html?id={q['id']}" class="quiz-card" data-quiz-id="{q['id']}">
          <div class="quiz-card-top"><span class="quiz-icon">{q['icon']}</span>
          <span class="quiz-best" style="display:none">Meilleur score</span></div>
          <h3>{q['title']}</h3><p>{q['desc']}</p>
          <div class="quiz-meta"><span>❓ {len(q['questions'])} questions</span><span>📊 {q['difficulty']}</span><span>📝 /20</span></div>
        </a>"""
    return cards


def _books_list():
    items = ""
    for b in BOOKS[-6:]:
        is_pdf = b["path"].endswith(".pdf")
        href = (f"{EB}lecteur.html?livre=../06-pdf-domaine-public/{b['path']}") if is_pdf \
            else f"livres-psychologie/06-pdf-domaine-public/{b['path']}"
        items += f"""<li class="tx-item"><div class="tx-icon">{b['icon']}</div>
          <div class="tx-info"><div class="tx-name"><a href="{href}" style="text-decoration:none">{b['title']}</a></div>
          <div class="tx-date">{b['author']} · {b['cat']}</div></div>
          <span class="tx-amount plus">Lire</span></li>"""
    return items


def _hub_href(href):
    if href.startswith("http"):
        return href, ' target="_blank" rel="noopener"'
    return EB + href, ""


def _outils_cards():
    cards = []
    for href, cls, ico, titre, desc, compteur in OUTILS_V3:
        url, extra = _hub_href(href)
        cards.append(
            f'<a class="hub-card{(" " + cls) if cls else ""}" href="{url}"{extra}>'
            f'<span class="hub-ico">{ico}</span><h3>{titre}</h3><p>{desc}</p>'
            f'<span class="hub-n">{compteur}</span></a>'
        )
    return "".join(cards)


def _nouveautes():
    return "".join(
        f'<li class="tx-item"><div class="tx-icon">{ico}</div>'
        f'<div class="tx-info"><div class="tx-name">{titre}</div><div class="tx-date">{desc}</div></div>'
        f'<span class="tx-amount plus">Nouveau</span></li>'
        for ico, titre, desc in NOUVEAUTES
    )


def render_home():
    n_sections = sum(len(c["sections"]) for c in CATEGORIES)
    n_flash = sum(len(c.get("flashcards", [])) for c in CATEGORIES)
    n_questions = sum(len(q["questions"]) for q in QUIZZES)
    n_refs = len(EXPERIENCES) + len(AUTEURS) + len(TROUBLES) + len(BIAIS) + len(TESTS) + len(CHRONOLOGIE_TRIEE)
    n_savoirs = (len(THEORIES) + len(CAS) + len(DEBATS) + len(METHODES_NOTIONS)
                 + len(LEXIQUE_EN) + len(PRATIQUES) + len(METIERS)
                 + len(COURANTS) + len(MYTHES) + len(FAQ))
    n_fiches = n_refs + n_savoirs + len(DICTIONNAIRE) + n_sections

    raccourcis = "".join(
        f'<a class="quick-avatar" style="background:var(--{color})" href="{EB}categories/{cid}.html" title="{label}">{ico}</a>'
        for cid, color, ico, label in RACCOURCIS
    ) + f'<a class="quick-avatar add" href="{EB}index.html" title="Tout voir">+</a>'

    body = f"""
<div class="wrap" style="margin-top:1rem">
  <div style="text-align:center;padding:2.5rem 1rem 1rem">
    <p class="section-eyebrow">L'encyclopédie vivante et illustrée de la psychologie</p>
    <h1 style="font-family:var(--serif);font-weight:700;font-size:clamp(2.2rem,6vw,3.4rem);line-height:1.1;max-width:820px;margin:0 auto 1rem">
      Comprendre l'esprit humain, <span style="color:var(--vert)">une notion</span> à la fois
    </h1>
    <p style="color:var(--gris);max-width:680px;margin:0 auto 1.75rem;font-size:1.05rem">
      {len(CATEGORIES)} domaines, {n_sections} chapitres, {n_fiches} fiches consultables, {len(THEORIES)} théories,
      {len(CAS)} cas cliniques, {len(DEBATS)} débats, {len(BOOKS)} livres du domaine public lisibles en ligne,
      {len(EXPERIENCES_LAB)} expériences jouables et {n_questions} questions corrigées — tout, entièrement en français.
    </p>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary" href="{EB}parcours.html">🧭 Commencer un parcours</a>
      <a class="btn btn-secondary" href="{EB}emploi-du-temps.html">🎓 Emploi du temps</a>
      <a class="btn btn-secondary" href="{DISCORD_INVITE}" target="_blank" rel="noopener">💬 Rejoindre le Discord</a>
      <a class="btn btn-secondary" href="{EB}compte.html">👤 Compte étudiant</a>
      <button class="btn btn-secondary" data-search-open="">🔍 Rechercher (Ctrl + K)</button>
    </div>
  </div>
</div>

<div class="hero-card">
  <div class="hero-top">
    <div class="hero-stat">
      <div class="hero-stat-row">
        <div class="hero-icon vert">📖</div>
        <div><div class="hero-stat-num" data-visited-count>0</div>
        <div class="hero-stat-label">Catégories explorées / <span data-cat-total>26</span></div></div>
      </div>
      <div class="hero-stat-row">
        <div class="hero-icon or">🎯</div>
        <div><div class="hero-stat-num" data-quiz-count>0</div>
        <div class="hero-stat-label">Quiz complétés / <span data-quiz-total>26</span></div></div>
      </div>
    </div>
    <div>
      <div class="hero-center-label">Ton score de maîtrise global</div>
      <div class="hero-balance" data-mastery-pct>0%</div>
      <div class="hero-pill-change">Chaque fiche lue et chaque quiz réussi font monter ce score 🚀</div>
    </div>
    <div class="hero-stat">
      <div class="hero-stat-row">
        <div class="hero-icon vert">🏆</div>
        <div><div class="hero-stat-num" data-best-quiz-pct>—</div><div class="hero-stat-label">Meilleur score de quiz</div></div>
      </div>
      <div class="hero-stat-row">
        <div class="hero-icon or">📚</div>
        <div><div class="hero-stat-num">{len(BOOKS)}</div><div class="hero-stat-label">Livres complets inclus</div></div>
      </div>
    </div>
  </div>
  <div class="hero-sparkline" id="hero-sparkline">{_sparkline()}</div>
</div>

<div class="pensee-band" data-pensee-home>
  <figure class="geo-plate cream">
    <img src="assets-ebook/plates/hero/plate_frontispice_site.png" alt="Planche de représentation">
    <figcaption><span class="geo-fig">Fig. A.</span><strong>Planche du jour</strong>
    <em>Une pensée se charge ici selon la date.</em></figcaption>
  </figure>
  <div class="pensee-copy">
    <p class="section-eyebrow">Planche du jour</p>
    <blockquote>Une citation, un rappel de cours ou une question qui fait réfléchir — chaque jour une gravure différente.</blockquote>
    <cite>Psyclopédia</cite>
    <div class="cta-row">
      <a class="btn btn-secondary" href="{EB}rappels.html">Ouvrir les rappels</a>
    </div>
  </div>
</div>

<div class="section" style="padding-top:0">
  <div class="stat-strip">
    <div class="stat-cell"><div class="val">{len(CATEGORIES)}</div><div class="lbl">catégories complètes</div></div>
    <div class="stat-cell"><div class="val">{n_sections}</div><div class="lbl">chapitres rédigés</div></div>
    <div class="stat-cell"><div class="val">{len(DICTIONNAIRE)}</div><div class="lbl">notions au dictionnaire</div></div>
    <div class="stat-cell"><div class="val">{len(THEORIES)}</div><div class="lbl">théories et modèles</div></div>
    <div class="stat-cell"><div class="val">{len(COURANTS)}</div><div class="lbl">courants de pensée</div></div>
    <div class="stat-cell"><div class="val">{len(MYTHES)}</div><div class="lbl">idées reçues démontées</div></div>
    <div class="stat-cell"><div class="val">{len(FAQ)}</div><div class="lbl">questions fréquentes</div></div>
    <div class="stat-cell"><div class="val">{len(EXPERIENCES)}</div><div class="lbl">expériences détaillées</div></div>
    <div class="stat-cell"><div class="val">{len(AUTEURS)}</div><div class="lbl">grandes figures</div></div>
    <div class="stat-cell"><div class="val">{len(TROUBLES)}</div><div class="lbl">troubles expliqués</div></div>
    <div class="stat-cell"><div class="val">{len(BIAIS)}</div><div class="lbl">biais cognitifs</div></div>
    <div class="stat-cell"><div class="val">{len(TESTS)}</div><div class="lbl">tests psychométriques</div></div>
    <div class="stat-cell"><div class="val">{len(CAS)}</div><div class="lbl">cas cliniques</div></div>
    <div class="stat-cell"><div class="val">{len(DEBATS)}</div><div class="lbl">débats argumentés</div></div>
    <div class="stat-cell"><div class="val">{len(METHODES_NOTIONS)}</div><div class="lbl">notions de méthode</div></div>
    <div class="stat-cell"><div class="val">{len(PRATIQUES)}</div><div class="lbl">fiches pratiques</div></div>
    <div class="stat-cell"><div class="val">{len(METIERS)}</div><div class="lbl">métiers décrits</div></div>
    <div class="stat-cell"><div class="val">{len(LEXIQUE_EN)}</div><div class="lbl">termes anglais traduits</div></div>
    <div class="stat-cell"><div class="val">{len(CHRONOLOGIE_TRIEE)}</div><div class="lbl">dates de chronologie</div></div>
    <div class="stat-cell"><div class="val">{n_flash}</div><div class="lbl">flashcards de révision</div></div>
    <div class="stat-cell"><div class="val">{n_questions}</div><div class="lbl">questions corrigées</div></div>
    <div class="stat-cell"><div class="val">{len(BOOKS)}</div><div class="lbl">ouvrages en ligne</div></div>
  </div>
</div>

<div class="section" style="padding-top:0">
  <div class="section-head">
    <p class="section-eyebrow">Les fondations</p>
    <h2 class="section-title">Par où entrer dans le site</h2>
    <p class="section-desc">Psyclopédia n'est pas seulement une suite d'articles : c'est un environnement
    d'apprentissage avec une recherche globale, une bibliothèque lisible en ligne, une base de références
    filtrable, des parcours balisés et des quiz notés.</p>
  </div>
  <div class="hub-grid">
    <a class="hub-card" href="{EB}index.html"><span class="hub-ico">📂</span><h3>Les catégories</h3>
      <p>Des fiches longues et illustrées, avec sommaire, chiffres clés, idées reçues et flashcards.</p>
      <span class="hub-n">{len(CATEGORIES)} domaines</span></a>
    <a class="hub-card or" href="{EB}references/index.html"><span class="hub-ico">🗂️</span><h3>La base de références</h3>
      <p>Tout ce qu'on cherche vite : expériences, auteurs, troubles, biais, tests, chronologie.</p>
      <span class="hub-n">{n_refs} fiches</span></a>
    <a class="hub-card rose" href="{EB}lecteur.html"><span class="hub-ico">📖</span><h3>Le lecteur de livres</h3>
      <p>Lire les originaux page par page, avec reconnaissance du texte scanné et français modernisé.</p>
      <span class="hub-n">{len(BOOKS)} ouvrages</span></a>
    <a class="hub-card gris" href="{EB}parcours.html"><span class="hub-ico">🧭</span><h3>Les parcours guidés</h3>
      <p>Débutant, introspection, clinique, révision d'examen, travail, sujets avancés.</p>
      <span class="hub-n">6 itinéraires</span></a>
    <a class="hub-card" href="{EB}quiz/index.html"><span class="hub-ico">🎮</span><h3>Les quiz notés</h3>
      <p>Un quiz par domaine, corrigé et expliqué question par question, noté sur 20.</p>
      <span class="hub-n">{len(QUIZZES)} quiz</span></a>
    <a class="hub-card or" href="{EB}dictionnaire.html"><span class="hub-ico">📖</span><h3>Le dictionnaire</h3>
      <p>Chaque notion définie en une phrase claire, reliée à la catégorie qui l'approfondit.</p>
      <span class="hub-n">{len(DICTIONNAIRE)} entrées</span></a>
    <a class="hub-card" href="{EB}emploi-du-temps.html"><span class="hub-ico">🎓</span><h3>Les cours de 50 minutes</h3>
      <p>Cursus annuel, calendrier, compte à rebours, replays YouTube francophones et fiches en direct.</p>
      <span class="hub-n">60 séances</span></a>
    <a class="hub-card or" href="{DISCORD_INVITE}" target="_blank" rel="noopener"><span class="hub-ico">💬</span><h3>Le serveur Discord</h3>
      <p>Prolonger le site : annonces de séance, forums thématiques, fiches et entraide bienveillante.</p>
      <span class="hub-n">Rejoindre</span></a>
    <a class="hub-card" href="{EB}decouverte.html"><span class="hub-ico">🔭</span><h3>La zone de découverte</h3>
      <p>Planches d'expériences, vraies images du cerveau, projets ouverts et cave des mythes — avec les sources.</p>
      <span class="hub-n">Galerie · planches</span></a>
    <a class="hub-card or" href="{EB}metiers.html"><span class="hub-ico">🎓</span><h3>Métiers et études</h3>
      <p>Du lycée à la licence : spécialités, quatre branches, titre de psychologue — dans le même site.</p>
      <span class="hub-n">Parcours</span></a>
    <a class="hub-card" href="{EB}assistant.html"><span class="hub-ico">🤖</span><h3>L'assistant du site</h3>
      <p>Réponses complètes et sourcées : une question, les pages qui y répondent, sans invention.</p>
      <span class="hub-n">Ctrl + J</span></a>
    <a class="hub-card or" href="{EB}compte.html"><span class="hub-ico">👤</span><h3>Compte étudiant</h3>
      <p>E-mail et mot de passe, ou Google. Cours suivis, notes de séance et scores de quiz enregistrés.</p>
      <span class="hub-n">Connexion</span></a>
  </div>
</div>

<div class="section" style="padding-top:0">
  <div class="section-head">
    <p class="section-eyebrow">{n_savoirs} fiches supplémentaires</p>
    <h2 class="section-title">Les {len(OUTILS_V3)} salles de la bibliothèque</h2>
    <p class="section-desc">Au-delà des catégories, le site ouvre des espaces spécialisés : les écoles de
    pensée et les cas qui les ont construites, les idées reçues démontées, les controverses non tranchées,
    la méthode scientifique elle-même, les applications quotidiennes, les métiers, un laboratoire jouable,
    des auto-évaluations, un système de révision, et de quoi trouver de l'aide quand on en a besoin.</p>
  </div>
  <div class="hub-grid">{_outils_cards()}</div>
</div>

<div class="dash-grid">
  <div class="panel">
    <div class="panel-head"><h3>⚡ Accès rapide</h3><a href="{EB}index.html">Tout voir</a></div>
    <div class="quick-row">{raccourcis}</div>

    <div class="panel-head"><h3>🧭 Par où commencer ?</h3></div>
    <div class="path-steps" style="padding:0">
      <a class="path-step" href="{EB}parcours.html#decouverte"><span class="path-step-n">1</span>
        <span class="path-step-title">Je pars de zéro</span><span class="path-step-kind">≈ 2 h</span></a>
      <a class="path-step" href="{EB}parcours.html#mieux-se-comprendre"><span class="path-step-n">2</span>
        <span class="path-step-title">Mieux me comprendre</span><span class="path-step-kind">≈ 3 h</span></a>
      <a class="path-step" href="{EB}parcours.html#clinique"><span class="path-step-n">3</span>
        <span class="path-step-title">Comprendre la souffrance psychique</span><span class="path-step-kind">≈ 3 h 30</span></a>
      <a class="path-step" href="{EB}parcours.html#etudiant"><span class="path-step-n">4</span>
        <span class="path-step-title">Réviser pour un examen</span><span class="path-step-kind">≈ 6 h</span></a>
    </div>

    <div class="reader-card">
      <div class="reader-card-top"><span>CARTE D'APPRENANT</span><span class="reader-card-badge">PSYCLOPÉDIA</span></div>
      <div class="reader-card-score">🧠 Prêt à apprendre</div>
      <div class="reader-card-actions">
        <a class="rc-btn" href="{EB}categories/01-fondamentaux.html" title="Commencer">▶</a>
        <a class="rc-btn" href="#" id="btn-random-cat" data-cats="{','.join(c['id'] for c in CATEGORIES)}" title="Catégorie au hasard">🎲</a>
        <a class="rc-btn" href="{EB}quiz/index.html" title="Quiz">🎮</a>
      </div>
    </div>
  </div>

  <div class="panel">
    <div class="panel-head"><h3>🆕 Nouveautés de cette version</h3></div>
    <ul class="tx-list">{_nouveautes()}</ul>

    <div class="panel-head"><h3>📚 Dans la bibliothèque</h3><a href="{EB}bibliotheque.html">Tout voir</a></div>
    <ul class="tx-list">{_books_list()}</ul>
  </div>

  <div class="panel">
    <div class="panel-head"><h3>🗂️ Base de références</h3><a href="{EB}references/index.html">Explorer</a></div>
    <ul class="tx-list">
      <li class="tx-item"><div class="tx-icon">🔬</div><div class="tx-info"><div class="tx-name"><a href="{EB}references/experiences.html" style="text-decoration:none">Expériences célèbres</a></div><div class="tx-date">Protocole, résultat, critiques</div></div><span class="tx-amount plus">{len(EXPERIENCES)}</span></li>
      <li class="tx-item"><div class="tx-icon">👤</div><div class="tx-info"><div class="tx-name"><a href="{EB}references/auteurs.html" style="text-decoration:none">Grandes figures</a></div><div class="tx-date">Biographies et apports</div></div><span class="tx-amount plus">{len(AUTEURS)}</span></li>
      <li class="tx-item"><div class="tx-icon">🩺</div><div class="tx-info"><div class="tx-name"><a href="{EB}references/troubles.html" style="text-decoration:none">Troubles psychiques</a></div><div class="tx-date">Signes et prises en charge</div></div><span class="tx-amount plus">{len(TROUBLES)}</span></li>
      <li class="tx-item"><div class="tx-icon">🌀</div><div class="tx-info"><div class="tx-name"><a href="{EB}references/biais.html" style="text-decoration:none">Biais cognitifs</a></div><div class="tx-date">Définition, exemple, parade</div></div><span class="tx-amount plus">{len(BIAIS)}</span></li>
      <li class="tx-item"><div class="tx-icon">📊</div><div class="tx-info"><div class="tx-name"><a href="{EB}references/tests.html" style="text-decoration:none">Tests psychométriques</a></div><div class="tx-date">Mesure, passation, limites</div></div><span class="tx-amount plus">{len(TESTS)}</span></li>
      <li class="tx-item"><div class="tx-icon">🗓️</div><div class="tx-info"><div class="tx-name"><a href="{EB}references/chronologie.html" style="text-decoration:none">Chronologie</a></div><div class="tx-date">Six grandes périodes</div></div><span class="tx-amount plus">{len(CHRONOLOGIE_TRIEE)}</span></li>
    </ul>

    <div class="mastery-box">
      <div class="mastery-head"><span style="font-size:0.85rem;color:var(--gris)">Niveau de maîtrise</span>
      <span class="mastery-badge" data-mastery-badge>Débutant</span></div>
      <div class="mastery-track"><div class="mastery-marker" data-mastery-marker style="left:0%"></div></div>
      <div class="mastery-pct" data-mastery-pct>0%</div>
    </div>
  </div>
</div>

<div class="section" id="categories">
  <div class="section-head">
    <p class="section-eyebrow">{len(CATEGORIES)} domaines complets</p>
    <h2 class="section-title">Toutes les catégories de la psychologie</h2>
    <p class="section-desc">Des fondamentaux méthodologiques à la psychologie politique, en passant par les
    neurosciences, la clinique, le sport, le numérique et l'environnement : une couverture complète, pensée
    pour tous les niveaux.</p>
  </div>
  <div class="cat-grid">{_cat_cards()}</div>
  <div class="cta-row">
    <a class="btn btn-secondary" href="{EB}dictionnaire.html">📖 Dictionnaire A-Z ({len(DICTIONNAIRE)} notions)</a>
    <a class="btn btn-secondary" href="{EB}references/index.html">🗂️ Base de références</a>
  </div>
</div>

<div class="section">
  <div class="section-head">
    <p class="section-eyebrow">{len(QUIZZES)} quiz · {n_questions} questions</p>
    <h2 class="section-title">🎮 Teste tes connaissances</h2>
    <p class="section-desc">Chaque quiz est noté sur 20, avec un corrigé complet et l'explication du raisonnement
    pour chaque question — y compris celles que tu as réussies.</p>
  </div>
  <div class="grid-3">{_quiz_preview()}</div>
  <div class="cta-row"><a class="btn btn-secondary" href="{EB}quiz/index.html">Voir les {len(QUIZZES)} quiz</a></div>
</div>

<div class="section">
  <div class="section-head">
    <p class="section-eyebrow">Apprentissage</p>
    <h2 class="section-title">🧠 Conçu pour que ça reste</h2>
    <p class="section-desc">Rappel actif, répétition espacée, entrelacement, élaboration et double codage : les
    cinq techniques les mieux établies de la science cognitive sont intégrées à la structure même du site.</p>
  </div>
  <div class="vark-grid">
    <div class="vark-card" style="border-top-color:var(--vert)"><span class="emoji">🔄</span><h3>Rappel actif</h3>
      <p>{n_flash} flashcards et {n_questions} questions pour te tester plutôt que relire.</p></div>
    <div class="vark-card" style="border-top-color:var(--or)"><span class="emoji">📅</span><h3>Répétition espacée</h3>
      <p>Un millier de cartes te sont représentées juste avant l'oubli, selon tes propres réponses.</p></div>
    <div class="vark-card" style="border-top-color:var(--rose)"><span class="emoji">🔀</span><h3>Entrelacement</h3>
      <p>Les parcours alternent fiches, références, livres et quiz plutôt que d'enchaîner le même format.</p></div>
    <div class="vark-card" style="border-top-color:var(--gris)"><span class="emoji">🖼️</span><h3>Double codage</h3>
      <p>Portraits, schémas et chiffres clés doublent le texte par une voie visuelle.</p></div>
    <div class="vark-card" style="border-top-color:var(--vert)"><span class="emoji">🧪</span><h3>Apprentissage par l'expérience</h3>
      <p>Le laboratoire te fait vivre l'effet Stroop ou l'illusion de Müller-Lyer avant de l'expliquer.</p></div>
  </div>
  <div class="cta-row">
    <a class="btn btn-primary" href="{EB}revision.html">🔁 Lancer une session de révision</a>
    <a class="btn btn-secondary" href="{EB}laboratoire.html">🧪 Entrer dans le laboratoire</a>
    <a class="btn btn-secondary" href="{EB}auto-evaluations.html">📋 Les auto-évaluations</a>
    <a class="btn btn-secondary" href="{EB}apprendre.html">📚 Le guide des méthodes</a>
  </div>
</div>
"""
    html = page_shell(
        "Psyclopédia — L'encyclopédie vivante de la psychologie", body, depth=-2, active="Accueil",
        description=(f"Psyclopédia : encyclopédie illustrée et interactive de la psychologie en français. "
                     f"{len(CATEGORIES)} catégories, {n_fiches} fiches consultables, {len(THEORIES)} théories, "
                     f"{len(BOOKS)} livres du domaine public lisibles en ligne, {len(QUIZZES)} quiz notés, "
                     f"laboratoire jouable et révision espacée."),
    )
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
