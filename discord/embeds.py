# -*- coding: utf-8 -*-
"""Embeds officiels du serveur Discord Psyclopédia.

Tous les grands messages d'accueil, de règles, de guide et d'orientation.
Couleurs : charte du site (--vert #50A67E, --or #E3AE33, --rose #C7395D, --gris #575E5B).
"""

from __future__ import annotations

from blueprint import APP, COLOR_GRIS, COLOR_OR, COLOR_ROSE, COLOR_VERT, LINKS, SITE

FOOTER = "Psyclopédia — Encyclopédie vivante de la psychologie"
SEP = "━━━━━━━━━━━━━━━━━━━━━━━━━━━━"


def _embed(title, description, color=COLOR_VERT, fields=None, url=None):
    payload = {
        "title": title,
        "description": description,
        "color": color,
        "footer": {"text": FOOTER},
    }
    if url:
        payload["url"] = url
    if fields:
        payload["fields"] = [
            {"name": name, "value": value, "inline": inline}
            for name, value, inline in fields
        ]
    return payload


def _link(label, key):
    return f"[{label}]({LINKS[key]})"


# --------------------------------------------------------------------------
# Accueil
# --------------------------------------------------------------------------

BIENVENUE = [
    _embed(
        "👋 Bienvenue sur Psyclopédia",
        "\n".join([
            f"{SEP}",
            "Vous entrez dans la **communauté francophone** qui prolonge le site",
            f"**[{SITE.replace('https://', '')}]({SITE})**.",
            "",
            "Ici, on apprend la psychologie comme une **science empirique**,",
            "une **clinique prudente** et une **culture** — pas comme un oracle,",
            "ni comme un cabinet.",
            "",
            "**Trois gestes pour arriver :**",
            "1️⃣ Lire <#REGLES> — cinq minutes, non négociables.",
            "2️⃣ Parcourir <#ORIENTATION> — la carte complète du serveur.",
            "3️⃣ Se présenter dans <#PRESENTATIONS> si vous en avez envie.",
            "",
            "Ensuite seulement : les cours, les fiches, les forums.",
            f"{SEP}",
        ]),
        COLOR_VERT,
        fields=[
            ("🎓 Cursus 50 min", _link("Emploi du temps", "cours"), True),
            ("📚 Encyclopédie", _link("Ouvrir le site", "accueil"), True),
            ("🤍 Aide", _link("Numéros et orientation", "aide"), True),
        ],
        url=SITE,
    ),
    _embed(
        "🌱 Premiers pas",
        "\n".join([
            "Le serveur est **découpé en catégories emoji**. Chaque salon a un rôle.",
            "",
            "📌 **Accueil** — règles, annonces, guide, liens.",
            "🎓 **Cours** — séances de 50 min synchronisées avec le site.",
            "📚 **Fiches** — synthèses, citations, livres du domaine public.",
            "💬 **Forums thématiques** — un forum par grand champ, avec tags.",
            "🤝 **Communauté** — agora, études, soutien, hors-sujet.",
            "🎤 **Vocaux** — amphi, révision, bibliothèque silencieuse, café.",
            "",
            "Les salons 📌 sont **en lecture seule** : ce sont des murs d'orientation,",
            "pas des chats. Pour parler, descendez vers 🎓, 💬 ou 🤝.",
            "",
            "Commandes utiles : `/guide` · `/regles` · `/planning` · `/site` · `/aide` · `/roles`",
        ]),
        COLOR_OR,
    ),
]


REGLES = [
    _embed(
        "📜 Règles du serveur",
        "\n".join([
            f"{SEP}",
            "Ces règles protègent **la qualité de l'apprentissage** et **la sécurité**",
            "des personnes. Les ignorer, c'est quitter le cadre.",
            f"{SEP}",
        ]),
        COLOR_ROSE,
        fields=[
            (
                "1 · Bienveillance réelle",
                "Critiquez des **idées**, jamais des personnes. Pas de moquerie sur "
                "la souffrance, le niveau d'études ou l'origine. L'ironie qui blesse "
                "n'est pas de l'esprit.",
                False,
            ),
            (
                "2 · Ici on n'est pas un soin",
                "Interdit de poser un **diagnostic**, de prescrire, de déconseiller "
                "un traitement ou de jouer au thérapeute. On parle de concepts, de "
                "cas **historiques** et de lectures. En détresse : **15 / 112**, "
                "suicide **3114**, violences **3919**, enfance **119**. Page "
                + _link("Aide", "aide") + ".",
                False,
            ),
            (
                "3 · Sourcer, ou taire",
                "Une affirmation psychologique s'appuie sur un **auteur**, une "
                "**étude**, une **fiche** du site ou un **livre du domaine public**. "
                "Les anecdotes ne valent pas une revue. Les instruments "
                "psychométriques propriétaires ne se recopient pas ici.",
                False,
            ),
            (
                "4 · Vie privée et consentement",
                "Ne publiez pas de données personnelles, de dossiers cliniques "
                "réels, ni l'histoire d'un proche « pour exemple ». Anonymisez. "
                "Pas de sollicitation sentimentale ou commerciale en message privé.",
                False,
            ),
            (
                "5 · Droit d'auteur et domaine public",
                "On partage ce qui est **libre** (domaine public, licences ouvertes, "
                "courtes citations sourcées) ou ce qui appartient au site. Pas de "
                "PDF pirates, pas de manuels scannés, pas de tests copyrightés.",
                False,
            ),
            (
                "6 · Hors-sujet cadré",
                "Le café existe : <#HORS_SUJET>. Le reste du serveur reste **dédié "
                "à la psychologie et à l'apprentissage**. Pas de spam, pas de pubs, "
                "pas de recrutements occultes.",
                False,
            ),
            (
                "7 · Modération",
                "L'équipe peut avertir, rendre muet, expulser. Contester calmement "
                "en privé auprès de 🛡️ Modération. Les récidives de diagnostic "
                "sauvage ou de harcèlement ferment la porte.",
                False,
            ),
        ],
    ),
]


ANNONCES = [
    _embed(
        "📢 Annonces officielles",
        "\n".join([
            "Ce salon est un **fil d'actualité**, pas une discussion.",
            "",
            "Vous y trouverez :",
            "• les **ouvertures de modules** et les événements communautaires ;",
            "• les **mises à jour du site** (fiches, lecteur, recherche) ;",
            "• les **décisions de cadre** (règles, rôles, structure).",
            "",
            "Cliquez sur **Suivre** (Follow) pour recevoir ces messages dans votre "
            "propre serveur, si vous en avez un.",
            "",
            f"Le planning des séances se lit aussi dans {_link('l’emploi du temps', 'cours')} "
            "et dans <#PLANNING>.",
        ]),
        COLOR_OR,
        url=SITE,
    ),
]


ROLES = [
    _embed(
        "🎭 Rôles et accès",
        "\n".join([
            f"{SEP}",
            "Les rôles **ne ferment presque rien** : le savoir est public.",
            "Ils servent à **se reconnaître**, à filtrer les mentions et à aider",
            "la modération à voir qui encadre.",
            f"{SEP}",
        ]),
        COLOR_VERT,
        fields=[
            (
                "Parcours",
                "🌱 **Nouveau** — attribué à l'arrivée.\n"
                "🎓 **Apprenant** — vous suivez le cursus ou le site.\n"
                "📗 **Licence** / 📘 **Master** — niveau d'études déclaré.\n"
                "🧑‍🏫 **Tuteur** — aide régulière, validée par l'équipe.",
                False,
            ),
            (
                "Intérêts (via `/roles`)",
                "🧩 Cognitive · 👥 Sociale · 🧠 Neurosciences · "
                "🩺 Psychopathologie · 📜 Histoire · 💬 Clinique",
                False,
            ),
            (
                "Équipe",
                "🏛️ **Équipe** — édition du site et du serveur.\n"
                "🛡️ **Modération** — cadre, signalements, salons verrouillés.",
                False,
            ),
            (
                "Comment les prendre",
                "Tapez **`/roles`** puis choisissez niveau + intérêts.\n"
                "Les rôles 🏛️ et 🛡️ ne s'auto-attribuent pas.",
                False,
            ),
        ],
    ),
]


GUIDE_SERVEUR = [
    _embed(
        "🗺️ Guide du serveur — la carte",
        "\n".join([
            f"{SEP}",
            "Liste **exacte et ordonnée** des catégories et des salons.",
            "Les salons 🔒 sont en lecture seule. Les forums s'ouvrent par **fils**.",
            f"{SEP}",
        ]),
        COLOR_VERT,
        fields=[
            (
                "📌 Accueil & Informations",
                "👋-bienvenue · 📜-regles · 📢-annonces · 🎭-roles-et-acces\n"
                "🗺️-guide-du-serveur · 🧭-guide-et-orientation\n"
                "🔗-liens-psyclopedia · 🛠️-journal-equipe *(équipe)*",
                False,
            ),
            (
                "🎓 Cours & Apprentissage",
                "📣-annonces-cours · 🗓️-planning-50min · 💬-apres-cours\n"
                "📎-ressources-de-seance · 📝-forum-revision · 🆘-entraide-niveaux",
                False,
            ),
            (
                "📚 Fiches & Ressources",
                "🗂️-fiches-synthese · 💬-citations · 📕-livres-domaine-public\n"
                "🩺-fiches-cliniques · 🔖-glossaire-et-notions",
                False,
            ),
            (
                "💬 Forums thématiques",
                "🧩-socle-et-histoire · 💭-esprit-et-cerveau\n"
                "👥-individu-et-societe · 🩺-clinique-et-sante · 🛠️-champs-appliques",
                False,
            ),
            (
                "🤝 Entraide & Communauté",
                "🎉-presentations · 💬-agora · 📰-articles-et-etudes\n"
                "📖-entraide-etudes · 🤍-soutien-mutuel · ☕-hors-sujet",
                False,
            ),
            (
                "🎤 Vocaux",
                "🎤-amphi · 📚-salle-de-revision · 🤫-bibliotheque · ☕-cafe",
                False,
            ),
        ],
    ),
]


# --------------------------------------------------------------------------
# Guide & Orientation — messages longs, structurés
# --------------------------------------------------------------------------

ORIENTATION_1 = [
    _embed(
        "🧭 Guide & Orientation — 1/7 · À quoi sert ce serveur",
        "\n".join([
            f"{SEP}",
            "Psyclopédia n'est **pas** un réseau social de plus. C'est la **salle",
            "commune** d'une encyclopédie : on s'y oriente, on y révise, on s'y",
            "tient compagnie — et on y reste honnêtes sur ce qu'on ne sait pas.",
            "",
            "**Le site reste la source.** Le Discord **prolonge** :",
            "• il **annonce** les séances de 50 minutes ;",
            "• il **discute** ce que le lecteur et les fiches viennent d'exposer ;",
            "• il **archive** les questions trop vivantes pour une page statique ;",
            "• il **oriente** vers l'aide réelle quand la page ne suffit plus.",
            "",
            f"Porte d'entrée du site : **{_link('errornoname.github.io/P-S-C', 'accueil')}**",
            f"{SEP}",
            "",
            "**Comment s'y retrouver en 30 secondes**",
            "```",
            "1. 📌  lire   (règles, guide, liens)",
            "2. 🎓  suivre (planning → séance → après-cours)",
            "3. 📚  ranger (fiches, livres, citations)",
            "4. 💬  creuser (forums par champ + tags emoji)",
            "5. 🤝  parler (agora, études, soutien)",
            "```",
            "",
            "Si vous ne savez plus où poster : **ouvrez un fil** dans le forum du",
            "champ, ou demandez dans <#AGORA>. Mieux un fil mal tagué qu'un pavé",
            "perdu dans le café.",
        ]),
        COLOR_VERT,
        url=SITE,
    ),
]

ORIENTATION_2 = [
    _embed(
        "🧭 Guide & Orientation — 2/7 · Lire les salons d'accueil",
        "\n".join([
            f"{SEP}",
            "La catégorie **📌・Accueil & Informations** est un **vestibule**.",
            "On n'y débat pas : on s'aligne.",
            f"{SEP}",
        ]),
        COLOR_OR,
        fields=[
            (
                "👋-bienvenue",
                "Le seuil. Rappel du projet et des trois premiers gestes.",
                False,
            ),
            (
                "📜-regles",
                "Le contrat. Surtout : **pas de diagnostic**, **sources**, "
                "**domaine public**, **vie privée**.",
                False,
            ),
            (
                "📢-annonces",
                "Le journal de la communauté. Activez **Suivre** si vous voulez "
                "les échos ailleurs.",
                False,
            ),
            (
                "🎭-roles-et-acces",
                "La légende des couleurs. `/roles` pour niveau et intérêts.",
                False,
            ),
            (
                "🗺️-guide-du-serveur",
                "L'inventaire : **chaque** catégorie, **chaque** salon, dans l'ordre.",
                False,
            ),
            (
                "🧭-guide-et-orientation",
                "**Vous êtes ici.** Mode d'emploi narratif, section par section.",
                False,
            ),
            (
                "🔗-liens-psyclopedia",
                "Le plan du site : cours, fiches, bibliothèque, aide, laboratoire.",
                False,
            ),
        ],
    ),
]

ORIENTATION_3 = [
    _embed(
        "🧭 Guide & Orientation — 3/7 · Suivre les cours de 50 minutes",
        "\n".join([
            f"{SEP}",
            "Le cursus **2026-2027** compte **60 séances** de **50 minutes**,",
            "découpées en quatre temps, identiques sur le site et ici :",
            "",
            "▶️ **0–18 min** — Exposition (définitions, auteurs, cadre)",
            "🔬 **18–32 min** — Démonstration (protocoles, figures)",
            "🩺 **32–42 min** — Cas clinique ou expérience fondatrice",
            "✨ **42–50 min** — Synthèse et quiz flash",
            "",
            "**Calendrier (Europe/Paris)**",
            "• **CM** — lundi **10:00**",
            "• **TD** — jeudi **14:00**",
            "• Semestre 1 dès le **7 septembre 2026** — Fondations",
            "• Semestre 2 dès le **4 janvier 2027** — Applications et clinique",
            f"{SEP}",
        ]),
        COLOR_VERT,
        fields=[
            (
                "Où ça se passe ici",
                "📣-annonces-cours — l'ouverture de séance\n"
                "🗓️-planning-50min — la carte de l'année\n"
                "💬-apres-cours — les questions **après** avoir suivi\n"
                "📎-ressources-de-seance — pages, extraits, timestamps\n"
                "📝-forum-revision — un fil par notion\n"
                "🆘-entraide-niveaux — un fil par difficulté de niveau",
                False,
            ),
            (
                "Où ça se passe sur le site",
                f"{_link('Emploi du temps', 'cours')} · "
                f"{_link('Archives', 'archives')} · "
                f"{_link('Lecteur', 'lecteur')}\n"
                "Le lecteur synchronise la vidéo francophone, la timeline et le "
                "panneau de ressources. Si YouTube refuse les sous-titres, la "
                "timeline JSON prend le relais.",
                False,
            ),
            (
                "Bon usage",
                "On ne spoile pas le quiz du jour **pendant** la séance.\n"
                "On relie chaque question à une **fiche** ou à un **timestamp**.\n"
                "On ne demande pas « le corrigé complet » : on montre où l'on bloque.",
                False,
            ),
        ],
        url=LINKS["cours"],
    ),
]

ORIENTATION_4 = [
    _embed(
        "🧭 Guide & Orientation — 4/7 · Fiches, livres et glossaire",
        "\n".join([
            f"{SEP}",
            "La catégorie **📚・Fiches & Ressources** est une **salle d'archives",
            "vivante**. Chaque forum attend **un fil = un objet** (une fiche,",
            "une citation, un livre, un cas, une notion).",
            f"{SEP}",
        ]),
        COLOR_OR,
        fields=[
            (
                "🗂️-fiches-synthese",
                f"Prolongez {_link('l’index des fiches', 'fiches')}. "
                "Titre du fil = titre de la fiche. Tag du champ obligatoire.",
                False,
            ),
            (
                "💬-citations",
                "Toujours : **auteur, œuvre, année**. Courte citation. "
                "Domaine public bienvenu ; pas de chapitres entiers sous droit.",
                False,
            ),
            (
                "📕-livres-domaine-public",
                f"Club de lecture de la {_link('bibliothèque', 'bibliotheque')} : "
                "James, Janet, Ribot et les autres textes libres, lisibles en ligne.",
                False,
            ),
            (
                "🩺-fiches-cliniques",
                "Cas **historiques** et grilles **pédagogiques**. "
                "Le tag **Pas un diagnostic** n'est pas décoratif.",
                False,
            ),
            (
                "🔖-glossaire-et-notions",
                f"Nuances de vocabulaire, ponts {_link('dictionnaire', 'dictionnaire')} "
                "et équivalents anglais-français.",
                False,
            ),
        ],
    ),
]

ORIENTATION_5 = [
    _embed(
        "🧭 Guide & Orientation — 5/7 · Forums thématiques et tags emoji",
        "\n".join([
            f"{SEP}",
            "Les **forums Discord** remplacent le grand bazar d'un salon unique.",
            "Chaque grand champ de la psychologie a **son forum**. Chaque fil",
            "porte **un ou deux tags emoji** pour filtrer.",
            "",
            "**Carte des forums**",
            "🧩-socle-et-histoire — fondamentaux, histoire, auteurs, courants",
            "💭-esprit-et-cerveau — cognitive, neurosciences, langage, émotions",
            "👥-individu-et-societe — sociale, développement, personnalité",
            "🩺-clinique-et-sante — psychopathologie, thérapies, éthique",
            "🛠️-champs-appliques — travail, éducation, légale, sport, numérique",
            f"{SEP}",
            "",
            "**Comment ouvrir un bon fil**",
            "1. Titre clair : *« Effet de simple exposition — limite de Zajonc »*",
            "2. Tag de champ + tag de type (`❓ Question`, `🔬 Expérience`…)",
            "3. Deux phrases de contexte + **lien** vers la fiche ou l'étude",
            "4. Votre question **précise** (pas « explique-moi tout Freud »)",
            "",
            "Les tags sont la **table des matières**. Sans tag, le fil se noie.",
        ]),
        COLOR_VERT,
        fields=[
            (
                "Clinique : cadre serré",
                "Dans 🩺-clinique-et-sante, on parle de **concepts** et de "
                "**cas publiés**. On n'analyse pas un camarade, un parent, un "
                "patient. La page " + _link("Aide", "aide") + " reste le bon réflexe.",
                False,
            ),
        ],
    ),
]

ORIENTATION_6 = [
    _embed(
        "🧭 Guide & Orientation — 6/7 · Entraide, soutien et numéros",
        "\n".join([
            f"{SEP}",
            "Apprendre ensemble n'autorise pas à **soigner** ensemble.",
            "Cette distinction est le **cœur** de la catégorie 🤝.",
            f"{SEP}",
        ]),
        COLOR_ROSE,
        fields=[
            (
                "🎉-presentations",
                "Un prénom ou un pseudo, un niveau, une curiosité. Rien de médical, "
                "rien d'obligatoire.",
                False,
            ),
            (
                "💬-agora",
                "Le salon général : questions transversales, vie du site, "
                "orientation « où poster ? ».",
                False,
            ),
            (
                "📰-articles-et-etudes",
                "Un fil par texte. Titre, auteurs, année, lien, **deux lignes** "
                "de lecture (méthode, limite, intérêt).",
                False,
            ),
            (
                "📖-entraide-etudes",
                "Méthodes, planning, oraux, orientation. On aide à **structurer**, "
                "on ne rédige pas le devoir d'autrui.",
                False,
            ),
            (
                "🤍-soutien-mutuel",
                "Écoute entre pairs, lenteur, pas de conseils cliniques. "
                "Un ralentissement anti-emballement est actif.",
                False,
            ),
            (
                "☕-hors-sujet",
                "Le reste de la vie, sans envahir les salons de travail.",
                False,
            ),
            (
                "Numéros — France et voisinage",
                "**Urgence vitale** : 15 ou 112\n"
                "**Prévention du suicide** : 3114 (24 h/24, gratuit)\n"
                "**Violences femmes** : 3919 — **Enfance en danger** : 119\n"
                "**SOS Amitié** : 09 72 39 40 50 — **Suicide Écoute** : 01 45 39 40 00\n"
                "**Belgique** 0800 32 123 / 107 · **Suisse** 143 / 147 · **Canada** 988\n"
                f"Liste commentée : {_link('page Aide', 'aide')}",
                False,
            ),
        ],
        url=LINKS["aide"],
    ),
]

ORIENTATION_7 = [
    _embed(
        "🧭 Guide & Orientation — 7/7 · Vocaux, commandes, et la suite",
        "\n".join([
            f"{SEP}",
            "**Vocaux**",
            "🎤-amphi — séances commentées, oraux blancs",
            "📚-salle-de-revision — questions à voix haute",
            "🤫-bibliotheque — présence silencieuse, micros coupés",
            "☕-cafe — parole libre, toujours courtoise",
            "",
            "**Commandes slash**",
            "`/guide` — ce mode d'emploi, version courte",
            "`/regles` — le contrat",
            "`/planning` — horaires et lien de l'année",
            "`/cours` — emploi du temps, lecteur, archives",
            "`/site` — plan du site",
            "`/aide` — numéros et cadre",
            "`/roles` — niveau + intérêts",
            f"{SEP}",
            "",
            "**Si le bot est hors ligne**",
            "Les murs d'orientation restent. Relisez ce salon, 🗺️-guide-du-serveur",
            "et le site. Rien d'essentiel n'est enfermé dans une commande.",
            "",
            "**Ce que Psyclopédia ne sera jamais**",
            "Un lieu de diagnostic sauvage, un revendeur de tests, un cabinet,",
            "une salle de piratage de manuels. Une encyclopédie a le droit d'être",
            "**exigeante** et **chaleureuse** en même temps.",
            "",
            f"À très vite sur {_link('le site', 'accueil')} — et dans 💬-apres-cours.",
        ]),
        COLOR_VERT,
        url=SITE,
    ),
]


LIENS = [
    _embed(
        "🔗 Le site Psyclopédia",
        "\n".join([
            f"**Portail :** {_link('errornoname.github.io/P-S-C', 'accueil')}",
            "",
            "Tout ce qui s'enseigne ici **pointe** vers une page. Bookmarkez.",
        ]),
        COLOR_VERT,
        url=SITE,
        fields=[
            ("Cours", f"{_link('Emploi du temps', 'cours')}\n{_link('Archives', 'archives')}\n{_link('Lecteur', 'lecteur')}", True),
            ("Savoir", f"{_link('Catégories', 'categories')}\n{_link('Fiches', 'fiches')}\n{_link('Références', 'references')}", True),
            ("Outils", f"{_link('Dictionnaire', 'dictionnaire')}\n{_link('Méthodes', 'methodes')}\n{_link('Quiz', 'quiz')}", True),
            ("Apprendre", f"{_link('Parcours', 'parcours')}\n{_link('Révision SM-2', 'revision')}\n{_link('Apprendre', 'apprendre')}", True),
            ("Pratique", f"{_link('Laboratoire', 'labo')}\n{_link('Métiers', 'metiers')}\n{_link('Pratique', 'pratique')}", True),
            ("Cadre", f"{_link('Aide', 'aide')}\n{_link('FAQ', 'faq')}\n{_link('Bibliothèque', 'bibliotheque')}", True),
        ],
    ),
]


JOURNAL = [
    _embed(
        "🛠️ Journal d'équipe",
        "Salon **staff** : notes de déploiement, alertes Community de Discord, "
        "brouillons. Rien de public ici. Le bac à sable 🧪-sandbox sert aux essais d'embeds.",
        COLOR_GRIS,
    ),
]


# --------------------------------------------------------------------------
# Cours
# --------------------------------------------------------------------------

ANNONCES_COURS = [
    _embed(
        "📣 Annonces de cours — 50 minutes",
        "\n".join([
            "Chaque séance officielle est **annoncée ici** : titre, semaine, CM ou TD,",
            "lien du lecteur, pages associées.",
            "",
            "Format type d'une annonce :",
            "```",
            "S07 · CM · La mémoire de travail",
            "Lundi 10:00 Europe/Paris · 50 min",
            "Lecteur + timeline + ressources",
            "```",
            "",
            f"Calendrier maître : {_link('emploi-du-temps.html', 'cours')}",
            "Les questions se posent **après** dans <#APRES_COURS>, pas ici.",
        ]),
        COLOR_VERT,
        url=LINKS["cours"],
    ),
]

PLANNING = [
    _embed(
        "🗓️ Planning des séances de 50 minutes",
        "\n".join([
            f"**Année universitaire 2026-2027** — 60 séances.",
            "",
            "**Semestre 1 — Fondations** à partir du 7 septembre 2026",
            "**Semestre 2 — Applications et clinique** à partir du 4 janvier 2027",
            "",
            "• Cours magistral : **lundi 10:00** (Europe/Paris)",
            "• Travaux dirigés : **jeudi 14:00** (Europe/Paris)",
            "• Durée invariable : **50 minutes**",
            "",
            "Phases internes : Exposition → Démonstration → Cas → Synthèse & quiz.",
            "",
            f"Source unique et à jour : {_link('consulter l’emploi du temps', 'cours')}",
            f"Archives et replay : {_link('cours / index', 'archives')}",
        ]),
        COLOR_OR,
        url=LINKS["cours"],
        fields=[
            ("Modules S1", "Socle, histoire, cognitive, sociale, développement, personnalité, émotions, neurosciences, psychopathologie, méthodes…", False),
            ("Modules S2", "Travail, éducation, santé, légale, interculturel, langage, psychométrie, débats, clôture.", False),
        ],
    ),
]

APRES_COURS = [
    _embed(
        "💬 Après le cours",
        "\n".join([
            "Salon **chaud** : on y arrive **après** avoir suivi la séance (site ou amphi).",
            "",
            "• Une question = un message clair, avec le **timestamp** si possible.",
            "• Reliez à une fiche, un auteur, un item de quiz.",
            "• Pas de correction complète demandée « pour gagner du temps ».",
            "• Pas de récit clinique personnel : 🤍-soutien-mutuel ou la "
            + _link("page Aide", "aide") + ".",
        ]),
        COLOR_VERT,
    ),
]

RESSOURCES_SEANCE = [
    _embed(
        "📎 Ressources de séance",
        "\n".join([
            "L'équipe et les tuteurs y déposent, **après** chaque CM/TD :",
            "• le lien du **lecteur** ;",
            "• les **pages** du site (catégorie, théorie, cas) ;",
            "• les **mots-clés** de la timeline ;",
            "• le quiz flash (sans spoiler avant la fin de séance).",
            "",
            "Les membres peuvent ajouter une ressource **sourcée**. "
            "Pas de fichiers sous droit d'auteur.",
        ]),
        COLOR_OR,
        url=LINKS["archives"],
    ),
]

FORUM_REVISION = [
    _embed(
        "📝 Forum de révision",
        "Un fil = **une notion**. Tags : niveau (Licence, Master, Autodidacte) + type "
        "(Fiche, Quiz, Question, Synthèse). Marquez **Résolu** quand c'est éclairci.\n\n"
        f"Cartes SM-2 du site : {_link('revision.html', 'revision')}",
        COLOR_VERT,
        url=LINKS["revision"],
    ),
]

ENTRAIDE_NIVEAUX = [
    _embed(
        "🆘 Entraide par niveaux",
        "Un fil = **une difficulté**. Taguez L1–M2 ou Autodidacte, plus Urgent ou Posé.\n\n"
        "Montrez ce que vous avez **déjà lu**. On ne fait pas le partiel à votre place.",
        COLOR_OR,
    ),
]


# --------------------------------------------------------------------------
# Fiches
# --------------------------------------------------------------------------

FICHES_SYNTHESE = [
    _embed(
        "🗂️ Fiches de synthèse",
        f"Archive commentée des fiches. Index : {_link('fiches / index', 'fiches')}\n\n"
        "Titre du fil = titre de la fiche. Premier message : 5 lignes max + lien + tag de champ.",
        COLOR_VERT,
        url=LINKS["fiches"],
    ),
]

CITATIONS = [
    _embed(
        "💬 Citations",
        "Une citation **sourcée** par fil : auteur, œuvre, année, traducteur si besoin.\n"
        "Courte. Discutez le **contexte**, pas le gourou.",
        COLOR_OR,
    ),
]

LIVRES_DP = [
    _embed(
        "📕 Livres du domaine public",
        f"Lisez d'abord dans la {_link('bibliothèque', 'bibliotheque')} du site "
        "(lecteur + modernisation du français).\n\n"
        "Un fil par ouvrage. Tags : À lire / Lu / Discussion + auteur.",
        COLOR_VERT,
        url=LINKS["bibliotheque"],
    ),
]

FICHES_CLINIQUES = [
    _embed(
        "🩺 Fiches cliniques — cadre pédagogique",
        "\n".join([
            "**Ce forum n'est pas une consultation.**",
            "",
            "On y range des **cas historiques** (Tan, Phineas Gage, Rosenhan…),",
            "des grilles de lecture, des mises en garde éthiques.",
            "",
            "Interdit : diagnostiquer un membre, un proche, une célébrité vivante.",
            "En souffrance : **15 / 112 / 3114** — " + _link("page Aide", "aide") + ".",
        ]),
        COLOR_ROSE,
        url=LINKS["aide"],
    ),
]

GLOSSAIRE = [
    _embed(
        "🔖 Glossaire et notions",
        f"Un fil = un terme. Vérifiez d'abord le {_link('dictionnaire', 'dictionnaire')}.\n"
        "Utile : nuances (émotion / affect / humeur), faux-amis EN-FR, mots de cours.",
        COLOR_VERT,
        url=LINKS["dictionnaire"],
    ),
]


# --------------------------------------------------------------------------
# Thématiques
# --------------------------------------------------------------------------

SOCLE = [
    _embed(
        "🧩 Socle et histoire",
        "Wundt, James, les courants, la naissance du laboratoire, les querelles de méthodes.\n"
        f"Pages : {_link('catégories', 'categories')} · {_link('références', 'references')}",
        COLOR_GRIS,
    ),
]

ESPRIT = [
    _embed(
        "💭 Esprit et cerveau",
        "Attention, mémoire, langage, émotions, plasticité, mythes neurologiques.\n"
        "Taguez **Cognitive**, **Neurosciences**, **Langage** ou **Émotions**.",
        COLOR_VERT,
    ),
]

SOCIETE = [
    _embed(
        "👥 Individu et société",
        "Normes, groupes, développement, traits, cultures. Méfiez-vous des « types » de magazine.\n"
        "Une expérience classique = un fil (Asch, Milgram, Harlow…), toujours **contextualisée**.",
        COLOR_OR,
    ),
]

CLINIQUE = [
    _embed(
        "🩺 Clinique et santé",
        "Concepts, histoires de classifications, facteurs communs des thérapies, éthique.\n"
        "**Pas un cabinet.** Urgences : 15 / 112 / 3114 — " + _link("Aide", "aide") + ".",
        COLOR_ROSE,
        url=LINKS["aide"],
    ),
]

APPLIQUE = [
    _embed(
        "🛠️ Champs appliqués",
        "Travail, école, justice, sport, écrans. Reliez toujours au **modèle** "
        f"(Karasek, charge cognitive, etc.) et aux {_link('métiers', 'metiers')}.",
        COLOR_VERT,
        url=LINKS["metiers"],
    ),
]


# --------------------------------------------------------------------------
# Communauté
# --------------------------------------------------------------------------

PRESENTATIONS = [
    _embed(
        "🎉 Présentations",
        "\n".join([
            "Un message suffit. Modèle libre :",
            "",
            "• **À appeler** — prénom ou pseudo",
            "• **Niveau** — L1, M2, reconversion, simple curiosité…",
            "• **Boussole** — un champ qui vous attire",
            "• **Promesse** — ce que vous ne ferez *pas* ici (diagnostiquer, par exemple)",
            "",
            "Pas de dossier intime. Ensuite : `/roles` et <#ORIENTATION>.",
        ]),
        COLOR_OR,
    ),
]

AGORA = [
    _embed(
        "💬 Agora",
        "Salon transversal. Si le sujet **dure** ou **mérite un tag**, "
        "ouvrez plutôt un fil dans le forum du champ.\n\n"
        "Les annonces officielles restent dans 📢 et 📣.",
        COLOR_VERT,
    ),
]

ARTICLES = [
    _embed(
        "📰 Articles et études",
        "Un fil par texte. **Titre · auteurs · année · lien · deux phrases critiques.**\n"
        "Préférez HAL, OpenEdition, PubMed Central, rapports publics. "
        "Dites la **limite** (échantillon, WEIRD, conflit d'intérêts).",
        COLOR_OR,
    ),
]

ENTRAIDE_ETUDES = [
    _embed(
        "📖 Entraide aux études",
        "Méthodes, charge de travail, oraux, orientation, lectures.\n"
        f"Boîte à outils site : {_link('apprendre', 'apprendre')} · {_link('méthodes', 'methodes')} · {_link('métiers', 'metiers')}\n\n"
        "On n'écrit pas vos copies. On vous aide à **construire** les vôtres.",
        COLOR_VERT,
    ),
]

SOUTIEN = [
    _embed(
        "🤍 Soutien mutuel — lire avant d'écrire",
        "\n".join([
            f"{SEP}",
            "Ce salon est une **salle d'attente humaine**, pas un service de soin.",
            "On peut dire que c'est lourd. On ne s'improvise pas clinicien.",
            f"{SEP}",
            "",
            "**Ici, on peut :** écouter, reformuler, rappeler qu'une page d'aide existe,",
            "proposer de l'air (un vocal 🤫, une pause).",
            "",
            "**Ici, on ne peut pas :** diagnostiquer, prescrire, déconseiller un",
            "traitement, extraire le récit traumatique de quelqu'un, donner des",
            "« techniques » présentées comme thérapeutiques.",
            "",
            "Si vous êtes en danger **immédiat** : **15** ou **112**.",
            "Si des idées suicidaires sont là : **3114** (24 h/24, gratuit, soignants formés).",
            "Violences faites aux femmes : **3919**. Enfant en danger : **119**.",
            "SOS Amitié : **09 72 39 40 50**. Suicide Écoute : **01 45 39 40 00**.",
            "Belgique 0800 32 123 · Suisse 143 · Canada 988.",
            "",
            f"Page complète et à jour : {_link('Aide Psyclopédia', 'aide')}",
        ]),
        COLOR_ROSE,
        url=LINKS["aide"],
    ),
]

HORS_SUJET = [
    _embed(
        "☕ Hors-sujet",
        "Livres hors psy, fatigue de semestre, playlists de révision — "
        "tant que 📜-regles restent debout. Le spam et la pub non.",
        COLOR_GRIS,
    ),
]

MODERATION = [
    _embed(
        "📋 Modération",
        "Signalements, décisions, historique court. Jamais de dossier clinique réel.\n"
        "Critères : règles 1–7, surtout diagnostic sauvage, harcèlement, droit d'auteur.",
        COLOR_GRIS,
    ),
]


# --------------------------------------------------------------------------
# Commandes slash (versions courtes)
# --------------------------------------------------------------------------

CMD_GUIDE = _embed(
    "🧭 Mode d'emploi express",
    "\n".join([
        "1️⃣ <#REGLES> puis <#ORIENTATION>",
        "2️⃣ Cursus : <#PLANNING> et " + _link("l’emploi du temps", "cours"),
        "3️⃣ Questions de séance → <#APRES_COURS>",
        "4️⃣ Questions de champ → forums 💬 (avec tags)",
        "5️⃣ Mal-être → <#SOUTIEN> ou " + _link("Aide", "aide") + " — urgences **15 / 112 / 3114**",
        "",
        "Carte complète : <#GUIDE_SERVEUR>",
    ]),
    COLOR_VERT,
)

CMD_PLANNING = PLANNING[0]
CMD_SITE = LIENS[0]
CMD_AIDE = SOUTIEN[0]
CMD_COURS = _embed(
    "🎓 Cursus Psyclopédia",
    "\n".join([
        "60 séances × 50 min · CM lundi 10:00 · TD jeudi 14:00 · Europe/Paris",
        f"{_link('Emploi du temps', 'cours')} · {_link('Archives', 'archives')} · {_link('Lecteur', 'lecteur')}",
        "Annonces : <#ANNONCES_COURS> · discussion : <#APRES_COURS>",
    ]),
    COLOR_VERT,
    url=LINKS["cours"],
)
CMD_REGLES = REGLES[0]


EMBEDS = {
    "bienvenue": BIENVENUE,
    "regles": REGLES,
    "annonces": ANNONCES,
    "roles": ROLES,
    "guide_serveur": GUIDE_SERVEUR,
    "orientation_1": ORIENTATION_1,
    "orientation_2": ORIENTATION_2,
    "orientation_3": ORIENTATION_3,
    "orientation_4": ORIENTATION_4,
    "orientation_5": ORIENTATION_5,
    "orientation_6": ORIENTATION_6,
    "orientation_7": ORIENTATION_7,
    "liens": LIENS,
    "journal": JOURNAL,
    "annonces_cours": ANNONCES_COURS,
    "planning": PLANNING,
    "apres_cours": APRES_COURS,
    "ressources_seance": RESSOURCES_SEANCE,
    "forum_revision": FORUM_REVISION,
    "entraide_niveaux": ENTRAIDE_NIVEAUX,
    "fiches_synthese": FICHES_SYNTHESE,
    "citations": CITATIONS,
    "livres_dp": LIVRES_DP,
    "fiches_cliniques": FICHES_CLINIQUES,
    "glossaire": GLOSSAIRE,
    "socle": SOCLE,
    "esprit": ESPRIT,
    "societe": SOCIETE,
    "clinique": CLINIQUE,
    "applique": APPLIQUE,
    "presentations": PRESENTATIONS,
    "agora": AGORA,
    "articles": ARTICLES,
    "entraide_etudes": ENTRAIDE_ETUDES,
    "soutien": SOUTIEN,
    "hors_sujet": HORS_SUJET,
    "moderation": MODERATION,
}

COMMAND_EMBEDS = {
    "guide": CMD_GUIDE,
    "regles": CMD_REGLES,
    "planning": CMD_PLANNING,
    "site": CMD_SITE,
    "aide": CMD_AIDE,
    "cours": CMD_COURS,
}


def validate_embeds():
    """Contrôles Discord : titres ≤ 256, descriptions ≤ 4096, fields ≤ 25 × 1024."""
    errors = []
    for key, bundle in EMBEDS.items():
        for index, embed in enumerate(bundle):
            title = embed.get("title") or ""
            desc = embed.get("description") or ""
            fields = embed.get("fields") or []
            loc = f"{key}[{index}]"
            if len(title) > 256:
                errors.append(f"{loc} title {len(title)} > 256")
            if len(desc) > 4096:
                errors.append(f"{loc} description {len(desc)} > 4096")
            if len(fields) > 25:
                errors.append(f"{loc} fields {len(fields)} > 25")
            for field in fields:
                if len(field["name"]) > 256:
                    errors.append(f"{loc} field name {field['name'][:40]!r}")
                if len(field["value"]) > 1024:
                    errors.append(
                        f"{loc} field {field['name']!r} value {len(field['value'])} > 1024"
                    )
    return errors


def mentionize(embed, ids):
    """Remplace <#CLE> par de vrais mentions de salons."""
    import copy

    mapping = {
        "REGLES": ids.get("regles"),
        "ORIENTATION": ids.get("guide_orientation"),
        "PRESENTATIONS": ids.get("presentations"),
        "PLANNING": ids.get("planning"),
        "APRES_COURS": ids.get("apres_cours"),
        "AGORA": ids.get("agora"),
        "HORS_SUJET": ids.get("hors_sujet"),
        "GUIDE_SERVEUR": ids.get("guide_serveur"),
        "SOUTIEN": ids.get("soutien"),
        "ANNONCES_COURS": ids.get("annonces_cours"),
    }

    def repl(text):
        if not text:
            return text
        for key, channel_id in mapping.items():
            token = f"<#{key}>"
            if channel_id:
                text = text.replace(token, f"<#{channel_id}>")
            else:
                text = text.replace(token, f"#{key.lower().replace('_', '-')}")
        return text

    out = copy.deepcopy(embed)
    out["description"] = repl(out.get("description"))
    for field in out.get("fields") or []:
        field["value"] = repl(field.get("value"))
    return out
