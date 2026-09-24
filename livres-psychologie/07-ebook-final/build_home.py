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
    ("🎓", "Psychologie de licence", "Méthode, clinique, développement et lectures cognitives"),
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
    ("l1-psychologie.html", "vert", "🎓", "Psychologie de licence",
     "Démarche scientifique, clinique, développement du nourrisson à la vie entière, "
     "et les lectures cognitives (Tolman, Cherry, Tulving, Sparrow).",
     "Méthode · lectures"),
    ("compte.html", "or", "👤", "Compte étudiant",
     "Connexion e-mail/mot de passe ou Google. Progression, notes, scores et photo conservés sur le serveur.",
     "Compte · serveur"),
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

    def pic(name):
        return f'<img src="assets-ebook/collage/{name}" alt="">'

    doors = [
        (f"{EB}parcours.html", "livre.png", "Parcours", "Un itinéraire, pas toute la bibliothèque d'un coup."),
        (f"{EB}index.html", "cerveau-petit.png", "Catégories", f"Les {len(CATEGORIES)} domaines, rangés par questions."),
        (f"{EB}emploi-du-temps.html", "horloge.png", "Cours", "Le calendrier et les séances."),
        (f"{EB}cahier.html", "machine.png", "Cahier", "Écrire, dicter, garder une note."),
    ]
    door_html = "".join(
        f'<a class="door" href="{h}">{pic(i)}<strong>{t}</strong><span>{d}</span></a>'
        for h, i, t, d in doors
    )
    shorts = [
        ("03-cognitive", "memoire.png", "Cognitive"),
        ("04-sociale", "lien.png", "Sociale"),
        ("08-neurosciences", "cerveau-petit.png", "Neurosciences"),
        ("09-psychopathologie", "pince.png", "Clinique"),
        ("07-emotions", "coeur.png", "Émotions"),
        ("27-science-psychologique", "oeil.png", "Science"),
    ]
    short_html = "".join(
        f'<a class="cat" href="{EB}categories/{slug}.html">{pic(img)}<div><strong>{label}</strong></div></a>'
        for slug, img, label in shorts
    )
    tools = [
        (f"{EB}references/courants.html", "time.png", "Courants", "Chaque école naît d'une objection."),
        (f"{EB}references/mythes.html", "oeil.png", "Idées reçues", "Ce que les données disent vraiment."),
        (f"{EB}faq.html", "parole.png", "Questions", "Des réponses qui disent aussi l'inconnu."),
        (f"{EB}laboratoire.html", "camera.png", "Laboratoire", "Expériences à faire dans le navigateur."),
        (f"{EB}bibliotheque.html", "livres.png", "Bibliothèque", "Livres du domaine public."),
        (f"{EB}aide.html", "mains.png", "Aide", "Où s'adresser, sans se substituer à un soin."),
    ]
    tool_html = "".join(
        f'<a href="{h}">{pic(i)}<div><strong>{t}</strong><br><small>{d}</small></div></a>'
        for h, i, t, d in tools
    )
    body = f"""
<main class="wrap">
<section class="hero">
  <div>
    <p class="kicker">Encyclopédie de psychologie</p>
    <h1>Lire l'esprit sans se perdre dans les tiroirs.</h1>
    <p class="lede">{len(CATEGORIES)} domaines, {n_sections} chapitres, {n_flash} flashcards,
    {n_refs} fiches de référence, {len(BOOKS)} livres et {n_questions} questions corrigées.
    Le collage montre le sujet. Le texte reste au premier plan.</p>
    <div class="actions">
      <a class="btn-main" href="{EB}index.html">{pic("cerveau-petit.png")}Voir les catégories</a>
      <a class="btn-ghost" href="{EB}parcours.html">{pic("livre.png")}Commencer un parcours</a>
      <a class="btn-ghost" href="{EB}cahier.html">{pic("machine.png")}Ouvrir le cahier</a>
    </div>
  </div>
  <div class="stage" aria-hidden="true">
    <img class="s-eye" src="assets-ebook/collage/oeil.png" alt="">
    <img class="s-heart" src="assets-ebook/collage/coeur.png" alt="">
    <img class="s-brain" src="assets-ebook/collage/cerveau.png" alt="">
    <img class="s-sun" src="assets-ebook/collage/soleil.png" alt="">
    <img class="s-moon" src="assets-ebook/collage/lune.png" alt="">
  </div>
</section>
<div class="doors">{door_html}</div>
<div class="block">{pic("lien.png")}<div><h2>Domaines proches</h2><p>Six portes, pas vingt-sept d'un coup.</p></div></div>
<div class="cats">{short_html}</div>
<div class="block">{pic("livres.png")}<div><h2>Le cabinet</h2><p>Autour des chapitres : histoire, doutes, expériences, livres.</p></div></div>
<div class="cabinet">{tool_html}</div>
<div class="block">{pic("horloge.png")}<div><h2>Les autres salles</h2><p>Recherche, cours, compte, quiz et le reste du site.</p></div></div>
<div class="hub-grid">{_outils_cards()}</div>
</main>
"""
    html = page_shell(
        "Psyclopédia — L'encyclopédie vivante de la psychologie", body, depth=-2, active="Accueil",
        description=(f"Psyclopédia : encyclopédie illustrée de la psychologie en français. "
                     f"{len(CATEGORIES)} catégories, {n_sections} chapitres, {len(BOOKS)} livres du domaine public, "
                     f"{len(QUIZZES)} quiz notés."),
    )
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
