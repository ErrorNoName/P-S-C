# -*- coding: utf-8 -*-
"""Architecture exhaustive du serveur Discord Psyclopédia.

Source unique : catégories, salons, forums, tags, rôles et permissions.
Aucun secret ici — le jeton se lit uniquement depuis l'environnement.
"""

from __future__ import annotations

# --------------------------------------------------------------------------
# Identifiants publics (non secrets)
# --------------------------------------------------------------------------

GUILD_ID_DEFAULT = "1550870849140166697"
SITE = "https://errornoname.github.io/P-S-C"
APP = f"{SITE}/livres-psychologie/07-ebook-final"

LINKS = {
    "accueil": f"{SITE}/",
    "cours": f"{APP}/emploi-du-temps.html",
    "archives": f"{APP}/cours/index.html",
    "lecteur": f"{APP}/cours/lecteur.html",
    "aide": f"{APP}/aide.html",
    "fiches": f"{APP}/fiches/index.html",
    "bibliotheque": f"{APP}/bibliotheque.html",
    "dictionnaire": f"{APP}/dictionnaire.html",
    "methodes": f"{APP}/methodes.html",
    "apprendre": f"{APP}/apprendre.html",
    "parcours": f"{APP}/parcours.html",
    "revision": f"{APP}/revision.html",
    "quiz": f"{APP}/quiz/index.html",
    "labo": f"{APP}/laboratoire.html",
    "metiers": f"{APP}/metiers.html",
    "pratique": f"{APP}/pratique.html",
    "faq": f"{APP}/faq.html",
    "references": f"{APP}/references/index.html",
    "categories": f"{APP}/index.html",
}

# Charte (assets-ebook/css/style.css)
COLOR_VERT = 0x50A67E
COLOR_OR = 0xE3AE33
COLOR_ROSE = 0xC7395D
COLOR_GRIS = 0x575E5B

# Types Discord
T_TEXT = 0
T_VOICE = 2
T_CATEGORY = 4
T_NEWS = 5
T_FORUM = 15

# Bits de permission utiles
P_VIEW = 1 << 10
P_SEND = 1 << 11
P_EMBED = 1 << 14
P_ATTACH = 1 << 15
P_HISTORY = 1 << 16
P_CONNECT = 1 << 20
P_SPEAK = 1 << 21
P_APP_COMMANDS = 1 << 31
P_PUBLIC_THREAD = 1 << 35
P_PRIVATE_THREAD = 1 << 36
P_SEND_THREAD = 1 << 38

LOCK_SEND = P_SEND | P_PUBLIC_THREAD | P_PRIVATE_THREAD | P_SEND_THREAD

# Salons Discord d'origine à supprimer après bascule
LEGACY_CHANNEL_NAMES = {
    "informations",
    "salons-textuels",
    "salons-vocaux",
    "bienvenue-et-règles",
    "bienvenue-et-regles",
    "annonces",
    "ressources",
    "général",
    "general",
    "réunions-planifiées",
    "reunions-planifiees",
    "hors-sujet",
    "lounge",
    "salle-de-réunion",
    "salle-de-reunion",
}

GUILD_PATCH = {
    "name": "Psyclopédia",
    "preferred_locale": "fr",
    "description": (
        "Communauté francophone d'apprentissage de la psychologie : "
        "cours de 50 min, fiches et entraide."
    ),
    "verification_level": 1,
    "explicit_content_filter": 2,
    "default_message_notifications": 1,
}


# --------------------------------------------------------------------------
# Rôles
# --------------------------------------------------------------------------

ROLES = [
    {
        "key": "equipe",
        "name": "🏛️ Équipe",
        "color": COLOR_VERT,
        "hoist": True,
        "mentionable": True,
        "permissions": str(8),  # Administrateur — comptes fondateurs
    },
    {
        "key": "moderation",
        "name": "🛡️ Modération",
        "color": COLOR_ROSE,
        "hoist": True,
        "mentionable": True,
        "permissions": str(
            (1 << 1) | (1 << 2) | (1 << 13) | (1 << 28) | (1 << 40) | P_VIEW | P_SEND
        ),
    },
    {
        "key": "tuteur",
        "name": "🧑‍🏫 Tuteur",
        "color": COLOR_OR,
        "hoist": True,
        "mentionable": True,
        "permissions": "0",
    },
    {
        "key": "master",
        "name": "📘 Master",
        "color": 0x3D6B8C,
        "hoist": False,
        "mentionable": False,
        "permissions": "0",
    },
    {
        "key": "licence",
        "name": "📗 Licence",
        "color": COLOR_VERT,
        "hoist": False,
        "mentionable": False,
        "permissions": "0",
    },
    {
        "key": "apprenant",
        "name": "🎓 Apprenant",
        "color": COLOR_OR,
        "hoist": False,
        "mentionable": False,
        "permissions": "0",
    },
    {
        "key": "nouveau",
        "name": "🌱 Nouveau",
        "color": 0x8F9A96,
        "hoist": False,
        "mentionable": False,
        "permissions": "0",
    },
    # Rôles d'intérêt (auto-attribuables via /roles)
    {
        "key": "int_cognitive",
        "name": "🧩 Cognitive",
        "color": 0x6BA3A7,
        "hoist": False,
        "mentionable": False,
        "permissions": "0",
        "interest": True,
    },
    {
        "key": "int_sociale",
        "name": "👥 Sociale",
        "color": 0xC47B4A,
        "hoist": False,
        "mentionable": False,
        "permissions": "0",
        "interest": True,
    },
    {
        "key": "int_neuro",
        "name": "🧠 Neurosciences",
        "color": 0x7A6BA7,
        "hoist": False,
        "mentionable": False,
        "permissions": "0",
        "interest": True,
    },
    {
        "key": "int_patho",
        "name": "🩺 Psychopathologie",
        "color": COLOR_ROSE,
        "hoist": False,
        "mentionable": False,
        "permissions": "0",
        "interest": True,
    },
    {
        "key": "int_histoire",
        "name": "📜 Histoire",
        "color": COLOR_GRIS,
        "hoist": False,
        "mentionable": False,
        "permissions": "0",
        "interest": True,
    },
    {
        "key": "int_clinique",
        "name": "💬 Clinique",
        "color": 0xA75A6B,
        "hoist": False,
        "mentionable": False,
        "permissions": "0",
        "interest": True,
    },
]


# --------------------------------------------------------------------------
# Tags de forums (nom ≤ 20 caractères)
# --------------------------------------------------------------------------

def _tags(*pairs):
    """pairs: (emoji, name) — name sans emoji, emoji séparé."""
    return [{"name": name, "emoji_name": emoji, "moderated": False} for emoji, name in pairs]


TAGS_REVISION = _tags(
    ("📗", "Licence"),
    ("📘", "Master"),
    ("🌱", "Autodidacte"),
    ("📝", "Fiche"),
    ("🎯", "Quiz"),
    ("❓", "Question"),
    ("📌", "Synthèse"),
    ("✅", "Résolu"),
)

TAGS_NIVEAUX = _tags(
    ("1️⃣", "L1"),
    ("2️⃣", "L2"),
    ("3️⃣", "L3"),
    ("4️⃣", "M1"),
    ("5️⃣", "M2"),
    ("🌱", "Autodidacte"),
    ("⏰", "Urgent"),
    ("🧘", "Posé"),
    ("✅", "Résolu"),
)

TAGS_FICHES = _tags(
    ("🧩", "Cognitive"),
    ("👥", "Sociale"),
    ("🧠", "Neurosciences"),
    ("🩺", "Psychopatho"),
    ("📜", "Histoire"),
    ("📐", "Méthodes"),
    ("💚", "Santé"),
    ("🏢", "Appliquée"),
)

TAGS_CITATIONS = _tags(
    ("🏛️", "Classique"),
    ("✨", "Contemporain"),
    ("🌞", "Citation du jour"),
    ("💬", "Discussion"),
    ("🔍", "Source"),
)

TAGS_LIVRES = _tags(
    ("📕", "À lire"),
    ("📗", "Lu"),
    ("💬", "Discussion"),
    ("✒️", "James"),
    ("🪞", "Janet"),
    ("🧠", "Ribot"),
    ("📜", "Domaine public"),
)

TAGS_CLINIQUES = _tags(
    ("⚠️", "Pédagogique"),
    ("📖", "Cas historique"),
    ("🧭", "Repères"),
    ("⚖️", "Éthique"),
    ("🚫", "Pas un diagnostic"),
)

TAGS_GLOSSAIRE = _tags(
    ("🔤", "Définition"),
    ("🔄", "Nuance"),
    ("🇬🇧", "EN-FR"),
    ("❓", "Question"),
    ("📌", "À retenir"),
)

TAGS_SOCLE = _tags(
    ("📜", "Histoire"),
    ("🧭", "Fondamentaux"),
    ("👤", "Auteur"),
    ("🌊", "Courant"),
    ("📚", "Lecture"),
    ("❓", "Question"),
)

TAGS_ESPRIT = _tags(
    ("🧩", "Cognitive"),
    ("🧠", "Neurosciences"),
    ("💬", "Langage"),
    ("😊", "Émotions"),
    ("🔬", "Expérience"),
    ("❓", "Question"),
)

TAGS_SOCIETE = _tags(
    ("👥", "Sociale"),
    ("🌱", "Développement"),
    ("🎭", "Personnalité"),
    ("🌍", "Interculturelle"),
    ("🔬", "Expérience"),
    ("❓", "Question"),
)

TAGS_CLINIQUE_FORUM = _tags(
    ("🩺", "Psychopatho"),
    ("💊", "Thérapies"),
    ("💚", "Santé"),
    ("⚖️", "Éthique"),
    ("📖", "Cas historique"),
    ("⚠️", "Pédagogique"),
    ("❓", "Question"),
)

TAGS_APPLIQUE = _tags(
    ("🏢", "Travail"),
    ("🏫", "Éducation"),
    ("⚖️", "Légale"),
    ("🏅", "Sport"),
    ("📱", "Numérique"),
    ("❓", "Question"),
)

TAGS_ARTICLES = _tags(
    ("📰", "Article"),
    ("🧪", "Étude"),
    ("🗣️", "Vulgarisation"),
    ("⚖️", "Lecture critique"),
    ("🇫🇷", "Francophone"),
)


# --------------------------------------------------------------------------
# Catégories et salons — ordre d'affichage = ordre de cette liste
# --------------------------------------------------------------------------

CATEGORIES = [
    {
        "key": "accueil",
        "name": "📌・Accueil & Informations",
        "channels": [
            {
                "key": "bienvenue",
                "name": "👋-bienvenue",
                "type": T_TEXT,
                "topic": (
                    "Premier pas sur Psyclopédia. Lisez 📜-regles puis 🧭-guide-et-orientation. "
                    f"Site : {SITE}"
                ),
                "locked": True,
                "system": True,
                "embeds": ["bienvenue"],
            },
            {
                "key": "regles",
                "name": "📜-regles",
                "type": T_TEXT,
                "topic": "Règles communautaires de Psyclopédia — lecture obligatoire.",
                "locked": True,
                "rules": True,
                "embeds": ["regles"],
            },
            {
                "key": "annonces",
                "name": "📢-annonces",
                "type": T_NEWS,
                "topic": "Annonces officielles de la communauté et du site Psyclopédia.",
                "locked": True,
                "embeds": ["annonces"],
            },
            {
                "key": "roles",
                "name": "🎭-roles-et-acces",
                "type": T_TEXT,
                "topic": "Carte des rôles : niveaux, intérêts, équipe. Commande /roles.",
                "locked": True,
                "embeds": ["roles"],
            },
            {
                "key": "guide_serveur",
                "name": "🗺️-guide-du-serveur",
                "type": T_TEXT,
                "topic": "Carte compacte de toutes les catégories et de tous les salons.",
                "locked": True,
                "embeds": ["guide_serveur"],
            },
            {
                "key": "guide_orientation",
                "name": "🧭-guide-et-orientation",
                "type": T_TEXT,
                "topic": (
                    "Mode d'emploi complet : s'orienter, suivre les cours, utiliser les forums, "
                    "trouver de l'aide."
                ),
                "locked": True,
                "embeds": [
                    "orientation_1",
                    "orientation_2",
                    "orientation_3",
                    "orientation_4",
                    "orientation_5",
                    "orientation_6",
                    "orientation_7",
                ],
            },
            {
                "key": "liens",
                "name": "🔗-liens-psyclopedia",
                "type": T_TEXT,
                "topic": f"Tous les accès vers le site {SITE}",
                "locked": True,
                "embeds": ["liens"],
            },
            {
                "key": "journal",
                "name": "🛠️-journal-equipe",
                "type": T_TEXT,
                "topic": "Journal interne et mises à jour Community de Discord.",
                "staff_only": True,
                "public_updates": True,
                "embeds": ["journal"],
            },
        ],
    },
    {
        "key": "cours",
        "name": "🎓・Cours & Apprentissage",
        "channels": [
            {
                "key": "annonces_cours",
                "name": "📣-annonces-cours",
                "type": T_NEWS,
                "topic": (
                    "Annonces des séances de 50 minutes (CM le lundi 10:00, TD le jeudi 14:00, "
                    "Europe/Paris). Cursus 2026-2027."
                ),
                "locked": True,
                "embeds": ["annonces_cours"],
            },
            {
                "key": "planning",
                "name": "🗓️-planning-50min",
                "type": T_TEXT,
                "topic": (
                    "Rappels du planning annuel. Source : "
                    f"{LINKS['cours']}"
                ),
                "locked": True,
                "embeds": ["planning"],
            },
            {
                "key": "apres_cours",
                "name": "💬-apres-cours",
                "type": T_TEXT,
                "topic": (
                    "Discussion post-séance : questions, doutes, liens avec les fiches. "
                    "Pas de diagnostic personnel."
                ),
                "embeds": ["apres_cours"],
            },
            {
                "key": "ressources_seance",
                "name": "📎-ressources-de-seance",
                "type": T_TEXT,
                "topic": (
                    "Ressources partagées après chaque CM/TD : pages du site, timestamps, quiz."
                ),
                "embeds": ["ressources_seance"],
            },
            {
                "key": "forum_revision",
                "name": "📝-forum-revision",
                "type": T_FORUM,
                "topic": (
                    "Un fil = une notion, une fiche ou un quiz. Choisissez un tag de niveau "
                    "et un tag de type. Reliez vos questions aux pages du site."
                ),
                "tags": TAGS_REVISION,
                "default_reaction": "📌",
                "embeds": ["forum_revision"],
            },
            {
                "key": "entraide_niveaux",
                "name": "🆘-entraide-niveaux",
                "type": T_FORUM,
                "topic": (
                    "Entraide par niveau (L1 à M2, autodidacte). Un fil = une question. "
                    "Taguez le niveau et l'urgence. Pas de devoirs copiés-collés."
                ),
                "tags": TAGS_NIVEAUX,
                "default_reaction": "🆘",
                "embeds": ["entraide_niveaux"],
            },
        ],
    },
    {
        "key": "fiches",
        "name": "📚・Fiches & Ressources",
        "channels": [
            {
                "key": "fiches_synthese",
                "name": "🗂️-fiches-synthese",
                "type": T_FORUM,
                "topic": (
                    "Archivage et discussion des fiches de synthèse. "
                    f"Index : {LINKS['fiches']}"
                ),
                "tags": TAGS_FICHES,
                "default_reaction": "🗂️",
                "embeds": ["fiches_synthese"],
            },
            {
                "key": "citations",
                "name": "💬-citations",
                "type": T_FORUM,
                "topic": (
                    "Citations sourcées (auteur, œuvre, année, domaine public ou courte citation). "
                    "Toujours indiquer la référence."
                ),
                "tags": TAGS_CITATIONS,
                "default_reaction": "💬",
                "embeds": ["citations"],
            },
            {
                "key": "livres_dp",
                "name": "📕-livres-domaine-public",
                "type": T_FORUM,
                "topic": (
                    "Livres du domaine public lisibles sur le site. "
                    f"Bibliothèque : {LINKS['bibliotheque']}"
                ),
                "tags": TAGS_LIVRES,
                "default_reaction": "📕",
                "embeds": ["livres_dp"],
            },
            {
                "key": "fiches_cliniques",
                "name": "🩺-fiches-cliniques",
                "type": T_FORUM,
                "topic": (
                    "Fiches cliniques pédagogiques et cas historiques. "
                    "Ce n'est ni un diagnostic ni un traitement. En détresse : 15 / 112 / 3114."
                ),
                "tags": TAGS_CLINIQUES,
                "default_reaction": "🩺",
                "embeds": ["fiches_cliniques"],
            },
            {
                "key": "glossaire",
                "name": "🔖-glossaire-et-notions",
                "type": T_FORUM,
                "topic": (
                    "Notions, nuances de vocabulaire, équivalents EN-FR. "
                    f"Dictionnaire : {LINKS['dictionnaire']}"
                ),
                "tags": TAGS_GLOSSAIRE,
                "default_reaction": "🔖",
                "embeds": ["glossaire"],
            },
        ],
    },
    {
        "key": "thematiques",
        "name": "💬・Forums & Discussions Thématiques",
        "channels": [
            {
                "key": "socle",
                "name": "🧩-socle-et-histoire",
                "type": T_FORUM,
                "topic": (
                    "Fondamentaux, histoire de la psychologie, auteurs et courants. "
                    "Filtrez par tag emoji."
                ),
                "tags": TAGS_SOCLE,
                "default_reaction": "🧩",
                "embeds": ["socle"],
            },
            {
                "key": "esprit",
                "name": "💭-esprit-et-cerveau",
                "type": T_FORUM,
                "topic": (
                    "Psychologie cognitive, neurosciences, langage, émotions. "
                    "Filtrez par tag emoji."
                ),
                "tags": TAGS_ESPRIT,
                "default_reaction": "💭",
                "embeds": ["esprit"],
            },
            {
                "key": "societe",
                "name": "👥-individu-et-societe",
                "type": T_FORUM,
                "topic": (
                    "Psychologie sociale, développement, personnalité, interculturel. "
                    "Filtrez par tag emoji."
                ),
                "tags": TAGS_SOCIETE,
                "default_reaction": "👥",
                "embeds": ["societe"],
            },
            {
                "key": "clinique",
                "name": "🩺-clinique-et-sante",
                "type": T_FORUM,
                "topic": (
                    "Psychopathologie, thérapies, santé, éthique — cadre pédagogique uniquement. "
                    "Pas de diagnostic. Urgence : 15 / 112 / 3114."
                ),
                "tags": TAGS_CLINIQUE_FORUM,
                "default_reaction": "🩺",
                "embeds": ["clinique"],
            },
            {
                "key": "applique",
                "name": "🛠️-champs-appliques",
                "type": T_FORUM,
                "topic": (
                    "Travail, éducation, légale, sport, numérique et autres champs appliqués."
                ),
                "tags": TAGS_APPLIQUE,
                "default_reaction": "🛠️",
                "embeds": ["applique"],
            },
        ],
    },
    {
        "key": "entraide",
        "name": "🤝・Entraide, Partage & Communauté",
        "channels": [
            {
                "key": "presentations",
                "name": "🎉-presentations",
                "type": T_TEXT,
                "topic": (
                    "Présentez-vous : prénom ou pseudo, niveau, ce que vous venez chercher. "
                    "Aucune obligation de dévoiler sa vie personnelle."
                ),
                "embeds": ["presentations"],
            },
            {
                "key": "agora",
                "name": "💬-agora",
                "type": T_TEXT,
                "topic": "Salon d'échange général autour de la psychologie et du site.",
                "embeds": ["agora"],
            },
            {
                "key": "articles",
                "name": "📰-articles-et-etudes",
                "type": T_FORUM,
                "topic": (
                    "Partage d'articles et d'études : titre, auteurs, année, lien, deux lignes "
                    "de lecture critique. Privilégiez les sources ouvertes."
                ),
                "tags": TAGS_ARTICLES,
                "default_reaction": "📰",
                "embeds": ["articles"],
            },
            {
                "key": "entraide_etudes",
                "name": "📖-entraide-etudes",
                "type": T_TEXT,
                "topic": (
                    "Méthodes de travail, oraux, mémoires, orientation. "
                    "Pas de demande de rédaction à votre place."
                ),
                "embeds": ["entraide_etudes"],
            },
            {
                "key": "soutien",
                "name": "🤍-soutien-mutuel",
                "type": T_TEXT,
                "topic": (
                    "Écoute bienveillante entre pairs. Ce salon n'est pas un soin. "
                    "Urgence France : 15 / 112 — suicide : 3114 — violences : 3919 — enfance : 119."
                ),
                "slowmode": 15,
                "embeds": ["soutien"],
            },
            {
                "key": "hors_sujet",
                "name": "☕-hors-sujet",
                "type": T_TEXT,
                "topic": "Tout le reste, dans le respect des règles. Un peu d'air, sans débordement.",
                "embeds": ["hors_sujet"],
            },
        ],
    },
    {
        "key": "vocaux",
        "name": "🎤・Salons vocaux",
        "channels": [
            {
                "key": "amphi",
                "name": "🎤-amphi",
                "type": T_VOICE,
                "topic": "Amphithéâtre : séances commentées et mises en situation pédagogiques.",
            },
            {
                "key": "revision_voc",
                "name": "📚-salle-de-revision",
                "type": T_VOICE,
                "topic": "Révision à voix haute, questions croisées, binômes.",
            },
            {
                "key": "biblio_voc",
                "name": "🤫-bibliotheque",
                "type": T_VOICE,
                "topic": "Présence silencieuse : travail en parallèle, micro coupé par défaut.",
            },
            {
                "key": "cafe_voc",
                "name": "☕-cafe",
                "type": T_VOICE,
                "topic": "Café vocal — discussions libres, toujours courtoises.",
            },
        ],
    },
    {
        "key": "equipe_cat",
        "name": "🔒・Équipe",
        "staff_only": True,
        "channels": [
            {
                "key": "moderation",
                "name": "📋-moderation",
                "type": T_TEXT,
                "topic": "Coordination de la modération.",
                "staff_only": True,
                "embeds": ["moderation"],
            },
            {
                "key": "sandbox",
                "name": "🧪-sandbox",
                "type": T_TEXT,
                "topic": "Bac à sable pour tester embeds, commandes et messages.",
                "staff_only": True,
            },
        ],
    },
]


SLASH_COMMANDS = [
    {
        "name": "guide",
        "description": "Afficher le mode d'emploi du serveur Psyclopédia",
        "type": 1,
    },
    {
        "name": "regles",
        "description": "Rappeler les règles communautaires",
        "type": 1,
    },
    {
        "name": "planning",
        "description": "Rappeler le planning des cours de 50 minutes",
        "type": 1,
    },
    {
        "name": "site",
        "description": "Obtenir les liens officiels du site Psyclopédia",
        "type": 1,
    },
    {
        "name": "aide",
        "description": "Afficher les numéros d'aide et le cadre de bienveillance",
        "type": 1,
    },
    {
        "name": "cours",
        "description": "Pointer vers le cursus, le lecteur et les archives",
        "type": 1,
    },
    {
        "name": "roles",
        "description": "Choisir ses rôles de niveau et d'intérêt",
        "type": 1,
    },
]


def iter_channels():
    for category in CATEGORIES:
        for channel in category["channels"]:
            yield category, channel


def all_channel_names():
    return [ch["name"] for _, ch in iter_channels()]


def all_category_names():
    return [cat["name"] for cat in CATEGORIES]


def channel_by_key(key):
    for category, channel in iter_channels():
        if channel["key"] == key:
            return category, channel
    raise KeyError(key)


def flatten_structure():
    """Liste ordonnée destinée à la documentation et aux tests."""
    rows = []
    for index, category in enumerate(CATEGORIES, start=1):
        rows.append({
            "kind": "category",
            "order": index,
            "key": category["key"],
            "name": category["name"],
            "staff_only": bool(category.get("staff_only")),
        })
        for c_index, channel in enumerate(category["channels"], start=1):
            rows.append({
                "kind": {T_TEXT: "text", T_VOICE: "voice", T_NEWS: "news", T_FORUM: "forum"}[channel["type"]],
                "order": f"{index}.{c_index}",
                "key": channel["key"],
                "name": channel["name"],
                "category": category["name"],
                "locked": bool(channel.get("locked")),
                "staff_only": bool(channel.get("staff_only") or category.get("staff_only")),
                "tags": [t["name"] for t in channel.get("tags", [])],
            })
    return rows
