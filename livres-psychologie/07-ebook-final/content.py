# -*- coding: utf-8 -*-
"""
PSYCLOPÉDIA — Fusion des sources de données.

Rassemble en structures canoniques les 27 catégories (16 fondatrices enrichies
+ 11 nouvelles), le dictionnaire complet, les quiz et les bases de références.
Aucune génération HTML ici : uniquement de la donnée prête à l'emploi.
"""

from data_categories import CATEGORIES as _CATS_BASE, DICTIONNAIRE as _DICT_BASE
from data_categories_plus import CATEGORIES_PLUS as _CATS_PLUS
from data_enrichissement import EXTRA as _EXTRA
from data_glossaire import GLOSSAIRE_PLUS as _DICT_PLUS
from data_quiz import QUIZZES as _QUIZ_BASE
from data_quiz_plus import QUIZZES_PLUS as _QUIZ_PLUS
from data_quiz_lycee import QUIZZES_LYCEE as _QUIZ_LYCEE
from data_experiences import EXPERIENCES
from data_auteurs import AUTEURS
from data_troubles import TROUBLES
from data_biais import BIAIS
from data_tests import TESTS, CHRONOLOGIE
from data_theories import THEORIES
from data_cas import CAS
from data_debats import DEBATS
from data_methodes import CHAPITRES as METHODES_CHAPITRES, NOTIONS as METHODES_NOTIONS
from data_bilingue import LEXIQUE_EN, FAUX_AMIS
from data_pratique import PRATIQUES
from data_metiers import METIERS, PARCOURS_ETUDES

# --------------------------------------------------------------------------
# Catégories : fusion + enrichissement
# --------------------------------------------------------------------------


def _merge_category(cat):
    """Applique l'enrichissement (sections, mythes, chiffres, flashcards) à une catégorie."""
    extra = _EXTRA.get(cat["id"])
    merged = dict(cat)
    merged.setdefault("mythes", [])
    merged.setdefault("chiffres", [])
    if not extra:
        return merged
    merged["sections"] = list(cat["sections"]) + list(extra.get("sections", []))
    merged["mythes"] = list(extra.get("mythes", []))
    merged["chiffres"] = list(extra.get("chiffres", []))
    merged["flashcards"] = list(cat.get("flashcards", [])) + list(extra.get("flashcards", []))
    return merged


CATEGORIES = [_merge_category(c) for c in _CATS_BASE] + [_merge_category(c) for c in _CATS_PLUS]

CATEGORY_BY_ID = {c["id"]: c for c in CATEGORIES}
CATEGORY_TITLE = {c["id"]: c["title"] for c in CATEGORIES}

# --------------------------------------------------------------------------
# Dictionnaire : fusion sans doublon (la première définition rencontrée gagne)
# --------------------------------------------------------------------------


def _merge_dictionnaire():
    seen = {}
    ordered = []
    for term, definition, cat_id in list(_DICT_BASE) + list(_DICT_PLUS):
        key = term.strip().lower()
        if key in seen:
            continue
        seen[key] = True
        ordered.append((term.strip(), definition, cat_id))
    return sorted(ordered, key=lambda x: _sort_key(x[0]))


def _sort_key(term):
    import unicodedata
    txt = unicodedata.normalize("NFD", term.lower())
    return "".join(c for c in txt if unicodedata.category(c) != "Mn")


DICTIONNAIRE = _merge_dictionnaire()

# --------------------------------------------------------------------------
# Quiz
# --------------------------------------------------------------------------

QUIZZES = list(_QUIZ_BASE) + list(_QUIZ_PLUS) + list(_QUIZ_LYCEE)
QUIZ_IDS = {q["id"] for q in QUIZZES}

# Quiz recommandé au bas de chaque fiche de catégorie.
QUIZ_FOR_CATEGORY = {
    "01-fondamentaux": "fondamentaux-histoire",
    "02-histoire": "fondamentaux-histoire",
    "03-cognitive": "cognitive",
    "04-sociale": "sociale",
    "05-developpement": "developpement-personnalite",
    "06-personnalite": "developpement-personnalite",
    "07-emotions": "emotions-motivation",
    "08-neurosciences": "neurosciences",
    "09-psychopathologie": "psychopathologie",
    "10-therapies": "therapies",
    "11-positive": "vie-quotidienne",
    "12-travail": "vie-quotidienne",
    "13-education": "vie-quotidienne",
    "14-sante": "vie-quotidienne",
    "15-legale": "legale-comparee",
    "16-comparee": "legale-comparee",
    "17-interculturelle": "interculturelle",
    "18-langage": "langage",
    "19-psychometrie": "psychometrie",
    "20-sport": "sport",
    "21-consommation": "consommation",
    "22-numerique": "numerique",
    "23-evolutionniste": "evolutionniste",
    "24-vieillissement": "vieillissement",
    "25-environnementale": "environnementale",
    "26-politique": "politique",
    "27-science-psychologique": "science-psychologique",
}

# --------------------------------------------------------------------------
# Chronologie : découpage en grandes périodes à partir de l'année
# --------------------------------------------------------------------------

PERIODES = [
    ("antiquite", "Antiquité et Moyen Âge", "Des humeurs d'Hippocrate aux premiers hôpitaux psychiatriques", -10000, 1500),
    ("classique", "Époque classique (1500-1850)", "Le dualisme, l'empirisme et la naissance de l'aliénisme", 1500, 1850),
    ("fondation", "Fondation scientifique (1850-1920)", "Laboratoires, psychophysique, psychanalyse et premiers tests", 1850, 1920),
    ("essor", "Grands courants (1920-1970)", "Behaviorisme, Gestalt, développement, humanisme, révolution cognitive", 1920, 1970),
    ("moderne", "Époque contemporaine (1970-2000)", "Neurosciences, biais cognitifs, thérapies validées", 1970, 2000),
    ("contemporain", "Psychologie d'aujourd'hui (depuis 2000)", "Imagerie, psychologie positive, crise de la réplication, numérique", 2000, 3000),
]


def periode_of(annee_str):
    """Retourne l'identifiant de période d'une date de la chronologie."""
    try:
        year = int(str(annee_str).split("-")[0] if not str(annee_str).startswith("-") else str(annee_str))
    except ValueError:
        digits = "".join(c for c in str(annee_str) if c.isdigit())
        year = int(digits) if digits else 1900
    for pid, _label, _desc, start, end in PERIODES:
        if start <= year < end:
            return pid
    return "contemporain"


CHRONOLOGIE_TRIEE = sorted(
    CHRONOLOGIE,
    key=lambda c: int("".join(ch for ch in str(c[0]) if ch.isdigit() or ch == "-").split("-")[0] or 0)
    * (-1 if str(c[0]).startswith("-") else 1),
)

# --------------------------------------------------------------------------
# Bibliothèque : ouvrages du domaine public hébergés dans le dépôt
# --------------------------------------------------------------------------

BOOKS = [
    {"title": "Précis de psychologie", "author": "William James", "year": "1909", "pages": "≈ 500 p.",
     "cat": "Fondamentaux", "color": "vert", "icon": "🧩", "texte": True,
     "desc": "Le texte fondateur du fonctionnalisme, traduit en français : perception, habitude, conscience, émotion.",
     "path": "psychologie-generale/james-precis-de-psychologie-1909.pdf"},
    {"title": "De l'intelligence", "author": "Hippolyte Taine", "year": "1870", "pages": "512 p.",
     "cat": "Histoire", "color": "gris", "icon": "📜", "texte": True,
     "desc": "Une somme philosophique majeure du XIXe siècle sur la connaissance et l'intelligence humaine.",
     "path": "histoire-psychologie/taine-de-lintelligence-1870.pdf"},
    {"title": "La Suggestibilité", "author": "Alfred Binet", "year": "1900", "pages": "≈ 200 p.",
     "cat": "Cognitive", "color": "vert", "icon": "💭", "texte": True,
     "desc": "L'étude pionnière sur l'influence et la suggestion, aux racines de la psychologie cognitive moderne.",
     "path": "psychologie-generale/binet-suggestibilite.html"},
    {"title": "Psychologie des foules", "author": "Gustave Le Bon", "year": "1895", "pages": "204 p.",
     "cat": "Sociale", "color": "or", "icon": "👥", "texte": True,
     "desc": "L'ouvrage fondateur sur la psychologie collective et l'influence de masse.",
     "path": "psychologie-sociale/le-bon-psychologie-des-foules-1895-complet.pdf"},
    {"title": "Le Suicide : étude de sociologie", "author": "Émile Durkheim", "year": "1897", "pages": "≈ 460 p.",
     "cat": "Sociale", "color": "or", "icon": "👥", "texte": True,
     "desc": "L'étude classique démontrant l'influence des structures sociales sur les comportements individuels.",
     "path": "psychologie-sociale/durkheim-le-suicide-1897.pdf"},
    {"title": "Les maladies de la volonté", "author": "Théodule Ribot", "year": "1883", "pages": "≈ 170 p.",
     "cat": "Personnalité", "color": "rose", "icon": "🎭", "texte": True,
     "desc": "L'étude pionnière sur les troubles de la volonté, aux racines de la psychologie de la personnalité.",
     "path": "psychopathologie/ribot-maladies-volonte-1883.pdf"},
    {"title": "Les maladies de la mémoire", "author": "Théodule Ribot", "year": "1898", "pages": "188 p.",
     "cat": "Psychopathologie", "color": "rose", "icon": "🩺", "texte": True,
     "desc": "L'étude fondatrice sur les troubles de la mémoire et la célèbre « loi de régression ».",
     "path": "psychopathologie/ribot-maladies-memoire-1898.pdf"},
    {"title": "Les névroses", "author": "Pierre Janet", "year": "1909", "pages": "397 p.",
     "cat": "Psychopathologie", "color": "rose", "icon": "🩺", "texte": True,
     "desc": "Référence historique majeure sur l'hystérie, l'automatisme psychologique et les troubles dissociatifs.",
     "path": "psychopathologie/janet-les-nevroses-1909.pdf"},
    {"title": "Leçons sur les maladies du système nerveux", "author": "Jean-Martin Charcot", "year": "1884", "pages": "568 p.",
     "cat": "Neurosciences", "color": "vert", "icon": "🧠", "texte": True,
     "desc": "L'œuvre fondatrice de la neurologie clinique moderne, observée à la Salpêtrière.",
     "path": "psychopathologie/charcot-lecons-systeme-nerveux-1884.pdf"},
    {"title": "L'interprétation des rêves", "author": "Sigmund Freud", "year": "1900", "pages": "≈ 500 p.",
     "cat": "Thérapies", "color": "or", "icon": "🛋️", "texte": True,
     "desc": "Le texte fondateur de la psychanalyse, en intégralité (format HTML).",
     "path": "psychologie-clinique/freud-interpretation-reves-1900.html"},
    {"title": "Psychologie de l'éducation", "author": "Gustave Le Bon", "year": "≈ 1910", "pages": "≈ 300 p.",
     "cat": "Éducation", "color": "vert", "icon": "🎓", "texte": True,
     "desc": "Un plaidoyer historique pour une pédagogie active, à lire avec regard critique.",
     "path": "psychologie-generale/le-bon-psychologie-education.html"},
    {"title": "L'homme criminel", "author": "Cesare Lombroso", "year": "1887", "pages": "682 p.",
     "cat": "Légale", "color": "gris", "icon": "⚖️", "texte": True,
     "desc": "Document historique sur la naissance (controversée) de la criminologie — à lire avec recul critique.",
     "path": "psychologie-legale/lombroso-homme-criminel-1887.pdf"},
    {"title": "L'expression des émotions chez l'homme et les animaux", "author": "Charles Darwin",
     "year": "1877 (trad.)", "pages": "≈ 400 p.", "cat": "Comparée / Émotions", "color": "or", "icon": "🐾",
     "texte": True,
     "desc": "L'ouvrage fondateur, richement illustré, sur les racines évolutives de nos émotions.",
     "path": "psychologie-comparative/darwin-expression-emotions-1877.pdf"},
]

PDF_BOOKS = [b for b in BOOKS if b["path"].endswith(".pdf")]
