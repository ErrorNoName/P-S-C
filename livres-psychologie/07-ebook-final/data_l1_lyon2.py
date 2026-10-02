# -*- coding: utf-8 -*-
"""L1 Sciences de l'éducation + mineure Psychologie — Université Lumière Lyon 2 (ISPEF)."""

PROGRAMME = {
    "id": "1paf02",
    "titre": "Licence 1 — Majeure Sciences de l'éducation et mineure Psychologie",
    "annee": "2026-2027",
    "campus": "Porte des Alpes (Bron)",
    "composante": "ISPEF — Institut des Sciences et Pratiques d'Éducation et de Formation",
    "compensable": True,
    "intro": (
        "Le couple majeure SDE et mineure psychologie (parcours 1PAF02) structure le premier semestre "
        "autour de trois blocs : introduction aux sciences de l'éducation, découverte des spécialités "
        "ISPEF, et initiation aux méthodes et branches fondamentales de la psychologie. "
        "Le campus Porte des Alpes accueille simultanément l'ISPEF et l'Institut de psychologie."
    ),
}

OFFICIAL_SOURCES = [
    ("Page MCCC ISPEF 2026-2027", "https://www.univ-lyon2.fr/formation/mccc-2025-2026-ispef"),
    (
        "MCCC PDF 1PAF02 (SDE + Psychologie)",
        "https://www.univ-lyon2.fr/medias/fichier/mccc-1paf02-licence-1-majeure-sciences-de-l-education-et-mineure-psychologie_1784278932988-pdf?ID_FICHE=19010&INLINE=FALSE",
    ),
    (
        "MCCC Psycho majeure + SDE mineure (miroir 1NAF02)",
        "https://psycho.univ-lyon2.fr/medias/fichier/mccc-1naf02-licence-1-majeure-psychologie-et-mineure-sciences-de-l-education-et-de-la-formation_1755510031904-pdf?ID_FICHE=16471&INLINE=FALSE",
    ),
    ("Licence SDE — présentation ISPEF", "https://ispef.univ-lyon2.fr/formation/en-presentiel/licences-sciences-de-leducation"),
    ("FAQ vie étudiante ISPEF", "https://ispef.univ-lyon2.fr/vie-etudiante/foire-aux-questions"),
    ("Fiche Parcoursup SDE Lyon 2", "https://dossier.parcoursup.fr/Candidats/public/fiches/afficherFicheFormation?g_ta_cod=35314"),
]

SEMESTRE2_APERCU = [
    ("Anthropologie de l'éducation", "12PAAA01 CM + 12PAAA02 TD"),
    ("Psychologie de l'éducation", "12PAAB03 CM + 12PAAB04 TD"),
    ("Sociologie de l'éducation", "12PAAC01 CM + 12PAAC02 TD"),
    ("Mineure psychologie S2", "Méthode expérimentale, cognitive, sociale"),
]

# Chaque module : code UE, examen, résumé encyclopédique, séances probables, liens internes.
MODULES = [
    {
        "id": "education-comparee",
        "code": "11PAAA01",
        "titre": "Éducation comparée",
        "format": "CM",
        "bloc": "Introduction aux sciences de l'éducation (6 ECTS)",
        "coeff": 1,
        "exam": "Contrôle terminal : QCM 30 min (seconde chance : QCM 30 min)",
        "resume": (
            "Premier grand cours d'introduction aux sciences de l'éducation. L'éducation comparée "
            "étudie les systèmes scolaires en les mettant en perspective internationale, en évitant "
            "l'ethnocentrisme éducatif — la tendance à croire que « notre » école est la meilleure. "
            "La discipline naît au XIXe siècle (Jullien de Paris, 1817) et croise histoire, "
            "anthropologie et politiques publiques. Elle interroge la mondialisation de l'école "
            "et le rôle des organisations internationales."
        ),
        "seances": [
            ("Introduction : ethnocentrisme et buts de la discipline", [
                "Vision internationale de l'éducation ; naissance au XIXe siècle.",
                "Ethnocentrisme éducatif : croire que l'éducation de son groupe est supérieure.",
                "L'école comme institution qui rattache l'individu à la société.",
                "Objectif : comparer avec méthode, pas idéaliser l'ailleurs.",
            ]),
            ("Perspectives historiques", [
                "Des récits de voyage aux sciences humaines.",
                "Évolution des objets et méthodes de comparaison.",
            ]),
            ("Jullien de Paris et naissance de la discipline", [
                "L'Esquisse et vingt et un questions (1817).",
                "Première formalisation d'une méthode comparative.",
            ]),
            ("Disciplines voisines", [
                "Didactique comparée, anthropologie, politique comparée.",
                "Frontières et complémentarités.",
            ]),
            ("Organisations internationales", [
                "UNESCO, OCDE, critiques du XXe siècle.",
                "Indicateurs et classements internationaux.",
            ]),
            ("Mondialisation et cas d'étude", [
                "Convergence et diversité des systèmes.",
                "Études de cas régionaux.",
            ]),
        ],
        "psyclo": [
            ("Psychologie comparée", "categories/16-comparee.html"),
            ("Psychologie interculturelle", "categories/17-interculturelle.html"),
            ("Psychologie de l'éducation", "categories/13-education.html"),
        ],
    },
    {
        "id": "evaluation-politiques",
        "code": "11PAAA03",
        "titre": "Évaluation des politiques éducatives",
        "format": "CM",
        "bloc": "Introduction aux sciences de l'éducation (6 ECTS)",
        "coeff": 1,
        "exam": "Contrôle terminal : QCM 30 min (seconde chance : QCM 30 min)",
        "resume": (
            "Ce cours distingue l'évaluation des politiques publiques en éducation de la simple "
            "notation scolaire. Une politique publique mobilise institutions, lois et acteurs "
            "sur la durée. L'évaluation en éducation croise acteurs nationaux (ministère, DEPP) "
            "et internationaux (OCDE/PISA, Union européenne, Banque mondiale, CONFEMEN). "
            "Elle interroge gouvernance, démocratie d'opinion et effets des réformes."
        ),
        "seances": [
            ("Qu'est-ce qu'une politique publique ?", [
                "Domaine public, institutions, lois, administration.",
                "Projection dans le temps : « gouverner c'est prévoir ».",
            ]),
            ("Évaluer une politique en éducation", [
                "Indicateurs, effets attendus et effets pervers.",
                "Distinction évaluation formative / sommative des politiques.",
            ]),
            ("Acteurs internationaux", [
                "OCDE (PISA), Union européenne, Banque mondiale, CONFEMEN/CPS.",
                "Circulation des réformes et benchmarking.",
            ]),
            ("Le cas français", [
                "Évaluations des politiques publiques en France.",
                "Gouvernance des systèmes éducatifs.",
            ]),
            ("Synthèse et préparation QCM", [
                "Notions transversales : démocratie d'opinion, gouvernance.",
                "Lecture critique des rapports officiels.",
            ]),
        ],
        "psyclo": [
            ("Psychologie politique", "categories/26-politique.html"),
            ("Psychologie de l'éducation", "categories/13-education.html"),
            ("Méthodes et statistiques", "methodes.html"),
        ],
    },
    {
        "id": "idees-pedagogiques",
        "code": "11PAAA04",
        "titre": "École(s), éducation(s) et idées pédagogiques",
        "format": "TD",
        "bloc": "Introduction aux sciences de l'éducation (6 ECTS)",
        "coeff": 1,
        "exam": "Contrôle continu : écrit 1 h + dossier (seconde chance : écrit 1 h 30, dossier si dispense)",
        "resume": (
            "Travaux dirigés d'introduction historique et conceptuelle aux sciences de l'éducation. "
            "Qu'est-ce qu'une « idée pédagogique » ? Comment l'école s'est construite dans le temps ? "
            "Quel lien entre projet politique et système éducatif ? Les sciences de l'éducation, "
            "discipline reconnue depuis les années 1960 (Mialaret), offrent un regard "
            "interdisciplinaire sur ces questions."
        ),
        "seances": [
            ("Sciences de l'éducation et idées pédagogiques", [
                "Objet et méthodes de la discipline (Mialaret).",
                "Idée pédagogique vs pratique quotidienne.",
            ]),
            ("Longue durée : Antiquité aux Temps modernes", [
                "Confucius, humanisme, Lumières.",
                "Institutionnalisation progressive de l'école.",
            ]),
            ("Forme scolaire et institutions", [
                "Rythmes, programmes, autorité pédagogique.",
                "Lien école / État / société.",
            ]),
            ("Courants pédagogiques", [
                "Montessori, Freinet, Dewey, éducation nouvelle.",
                "Continuités et ruptures.",
            ]),
            ("Éducation et politique", [
                "Réformes, enjeux de citoyenneté, laïcité.",
                "Tensions entre égalité et différenciation.",
            ]),
            ("Préparation dossier et écrit", [
                "Méthodologie du dossier TD.",
                "Entraînement à l'écrit de contrôle continu.",
            ]),
        ],
        "psyclo": [
            ("Psychologie de l'éducation", "categories/13-education.html"),
            ("Histoire de la psychologie", "categories/02-histoire.html"),
            ("Psychologie du développement", "branches/developpement.html"),
        ],
    },
    {
        "id": "referent-handicap",
        "code": "11PAAB02",
        "titre": "Introduction aux spécialités — Référent handicap",
        "format": "CM",
        "bloc": "Spécialisations en éducation (6 ECTS)",
        "coeff": 1,
        "exam": "Contrôle terminal : QCM 30 min",
        "resume": (
            "Introduction à la spécialité « référent handicap » dans le champ des sciences "
            "de l'éducation. Définir le handicap (loi de 2005, CIF/OMS), comprendre l'inclusion "
            "et la société inclusive, connaître les dispositifs MDPH/CDAPH, AESH et PPS. "
            "Le modèle évolue du médical vers le social et la participation (PPH)."
        ),
        "seances": [
            ("Représentations du handicap", [
                "Diversité, altérité, brainstorming visible/invisible.",
                "Handicap moteur, sensoriel, psychique, cognitif.",
            ]),
            ("Types et définition légale", [
                "Loi du 11 février 2005 pour l'égalité des droits.",
                "Limitation d'activité et restriction de participation.",
            ]),
            ("Modèles et chiffres", [
                "Modèle médical → modèle social / PPH.",
                "Statistiques et représentations médiatiques.",
            ]),
            ("MDPH, droits, scolarisation inclusive", [
                "MDPH, CDAPH, prestations.",
                "AESH, PPS, aménagements raisonnables.",
            ]),
            ("Société inclusive et bilan", [
                "Pédagogues de l'éducation spécialisée.",
                "Préparation au QCM terminal.",
            ]),
        ],
        "psyclo": [
            ("Psychopathologie descriptive", "categories/09-psychopathologie.html"),
            ("Psychologie de l'éducation", "categories/13-education.html"),
            ("Psychologie du développement", "branches/developpement.html"),
        ],
        "externe": [
            ("MDPH — fiche Vie publique", "https://www.vie-publique.fr/fiches/262479-quest-ce-quune-maison-departementale-des-personnes-handicapees-mdph"),
            ("AESH et école inclusive (Éducation nationale)", "https://www.education.gouv.fr/"),
        ],
    },
    {
        "id": "formation-adultes",
        "code": "11PAAB04",
        "titre": "Formation des adultes et éducation populaire",
        "format": "CM",
        "bloc": "Spécialisations en éducation (6 ECTS)",
        "coeff": 1,
        "exam": "Contrôle terminal : QCM 30 min",
        "resume": (
            "Présentation d'une spécialité des sciences de l'éducation : qui forme les adultes, "
            "dans quels secteurs (alphabétisation, formation professionnelle, entreprise, "
            "syndical, éducation populaire) ? Quelles théories de l'apprentissage chez l'adulte ? "
            "Quel métier de formateur, distinct de l'enseignant scolaire ?"
        ),
        "seances": [
            ("Champ et identité du formateur", [
                "Effectifs, secteurs, statuts professionnels.",
                "Formateur vs enseignant vs animateur.",
            ]),
            ("Approche par secteurs", [
                "Historique de la formation professionnelle.",
                "Éducation populaire et mouvements associatifs.",
            ]),
            ("Théories de l'apprentissage adulte", [
                "Behaviorisme, cognitivisme, constructivisme, andragogie.",
                "Connectivisme et formation numérique.",
            ]),
            ("Compétences et métiers", [
                "Référentiels de compétences du formateur.",
                "Parcours professionnels types.",
            ]),
            ("Bilan et QCM", [
                "Synthèse transversale des secteurs.",
                "Préparation au contrôle terminal.",
            ]),
        ],
        "psyclo": [
            ("Psychologie du travail", "categories/12-travail.html"),
            ("Psychologie de l'éducation", "categories/13-education.html"),
            ("Psychologie cognitive", "branches/cognitive.html"),
        ],
    },
    {
        "id": "demarche-scientifique",
        "code": "11NAAA04",
        "titre": "Méthodologie disciplinaire : démarche scientifique",
        "format": "CM",
        "bloc": "Mineure psychologie — semestre 1 (6 ECTS)",
        "coeff": None,
        "exam": "Noté dans l'UE mineure psychologie (contrôle terminal écrit selon MCCC Psycho)",
        "resume": (
            "Premier cours de méthodologie en psychologie. Objectif : comprendre ce qui rend "
            "la psychologie une science (observation rigoureuse, théories réfutables, éthique), "
            "comment se construit une recherche (observation → théorie → hypothèses → vérification) "
            "et quels outils empiriques existent (observation, entretien, questionnaire, tests)."
        ),
        "seances": [
            ("La psychologie parmi les sciences (1/2)", [
                "Définitions : étude de l'esprit et du comportement (APA, Collins & Rateau).",
                "Place de la psychologie dans le paysage scientifique.",
                "Représentations sociales de la psychologie.",
            ]),
            ("La psychologie comme science (2/2)", [
                "Scientificité, débats épistémologiques.",
                "Distinction science / pseudoscience (Lilienfeld).",
            ]),
            ("Le cycle de la recherche (1/2)", [
                "Démarche hypothético-déductive.",
                "Revue de littérature, théories réfutables.",
            ]),
            ("Le cycle de la recherche (2/2)", [
                "Hypothèses théorique, opérationnelle, statistique.",
                "Devis transversal, longitudinal, séquentiel.",
                "Diffusion et reproductibilité.",
            ]),
            ("Démarche processuelle (1/2)", [
                "Recherche qualitative et approches mixtes.",
                "Analyse de données non expérimentales.",
            ]),
            ("Démarche processuelle (2/2) + révisions", [
                "Synthèse des méthodes quantitatives et qualitatives.",
                "Préparation à l'évaluation terminale.",
            ]),
        ],
        "psyclo": [
            ("Fondamentaux & méthodes", "categories/01-fondamentaux.html"),
            ("Méthodes scientifiques", "methodes.html"),
            ("Science psychologique", "categories/27-science-psychologique.html"),
            ("Biais cognitifs", "references/biais.html"),
        ],
    },
    {
        "id": "psycho-clinique",
        "code": "11NAAA05",
        "titre": "Psychologie clinique",
        "format": "CM",
        "bloc": "Mineure psychologie — semestre 1 (6 ECTS)",
        "coeff": None,
        "exam": "Noté dans l'UE mineure psychologie",
        "resume": (
            "Introduction à la psychologie clinique : étude de la souffrance psychique, "
            "du cadre thérapeutique, de l'entretien clinique et de l'éthique professionnelle. "
            "Présentation des grands modèles (psychodynamique, cognitivo-comportemental, "
            "humaniste, systémique) sans confondre connaissance académique et diagnostic."
        ),
        "seances": [
            ("Objet et histoire de la clinique", [
                "De la cure freudienne aux approches contemporaines.",
                "Distinction psychologie clinique / psychiatrie.",
            ]),
            ("Cadre, alliance et éthique", [
                "Cadre thérapeutique, secret professionnel, limites.",
                "Alliance thérapeutique et facteurs communs.",
            ]),
            ("Modèles et outils", [
                "Entretien, observation, tests projectifs et psychométriques.",
                "Ce que mesurent — et ne mesurent pas — les outils cliniques.",
            ]),
            ("Psychopathologie descriptive", [
                "Signes, syndromes, nosographies (DSM, CIM).",
                "Prudence diagnostique en contexte universitaire.",
            ]),
            ("Cas et débats", [
                "Études de cas historiques (Gage, Anna O., H.M.) et leurs limites.",
                "Critiques des modèles uniques.",
            ]),
            ("Synthèse semestre 1", [
                "Articulation clinique / recherche.",
                "Préparation aux évaluations.",
            ]),
        ],
        "psyclo": [
            ("Psychologie clinique — branche L1", "branches/clinique.html"),
            ("Psychopathologie", "categories/09-psychopathologie.html"),
            ("Thérapies", "categories/10-therapies.html"),
            ("Cas cliniques historiques", "references/cas.html"),
        ],
    },
    {
        "id": "psycho-developpement",
        "code": "11NAAA06",
        "titre": "Psychologie du développement",
        "format": "CM",
        "bloc": "Mineure psychologie — semestre 1 (6 ECTS)",
        "coeff": None,
        "exam": "Noté dans l'UE mineure psychologie",
        "resume": (
            "Étude des changements du comportement et des processus mentaux de la conception "
            "à la vieillesse. Grands auteurs (Piaget, Vygotski, Bowlby, Erikson), méthodes "
            "longitudinales et transversales, thèmes de l'attachement, du langage, "
            "de l'adolescence et du vieillissement."
        ),
        "seances": [
            ("Objet et méthodes du développement", [
                "Longitudinal vs transversal, violation d'attente.",
                "Nature vs nurture, plasticité.",
            ]),
            ("Développement cognitif", [
                "Piaget : stades, assimilation, accommodation.",
                "Vygotski : zone proximale de développement.",
            ]),
            ("Attachement et relations précoces", [
                "Bowlby, Ainsworth, styles d'attachement.",
                "Expériences de Harlow (limites éthiques).",
            ]),
            ("Langage et théorie de l'esprit", [
                "Acquisition du langage, métacognition (Flavell).",
                "Développement social et émotionnel.",
            ]),
            ("Adolescence et adulte", [
                "Puberté cérébrale, identité (Erikson).",
                "Transitions de vie.",
            ]),
            ("Vieillissement", [
                "Plasticité cognitive tardive.",
                "Théories du vieillissement réussi.",
            ]),
        ],
        "psyclo": [
            ("Psychologie du développement — branche L1", "branches/developpement.html"),
            ("Fiche développement", "categories/05-developpement.html"),
            ("Vieillissement", "categories/24-vieillissement.html"),
        ],
    },
    {
        "id": "accompagnement",
        "code": "11PAAF01",
        "titre": "Accompagnement",
        "format": "TD",
        "bloc": "Accompagnement (3 ECTS)",
        "coeff": 1,
        "exam": "Contrôle continu : oral 10 min + dossier",
        "resume": (
            "Travaux dirigés d'accompagnement à la réussite et à l'insertion dans le parcours L1 SDE : "
            "méthode universitaire, orientation, découverte des spécialités, construction d'un dossier "
            "et entraînement à l'oral."
        ),
        "seances": [
            ("Prise de contact et critères d'évaluation", [
                "Règles du TD, attentes pour le dossier et l'oral.",
                "Calendrier du semestre.",
            ]),
            ("Méthode universitaire", [
                "Prises de notes, lecture académique, citations.",
                "Gestion du temps et autonomie.",
            ]),
            ("Orientation et spécialités SDE", [
                "Panorama des parcours L2/L3.",
                "Métiers de l'éducation et de la formation.",
            ]),
            ("Construction du dossier", [
                "Structuration, problématique, bibliographie.",
                "Relecture et critères de qualité.",
            ]),
            ("Entraînement oral", [
                "Présentation 10 minutes, gestion du stress.",
                "Questions du jury.",
            ]),
            ("Soutenances", [
                "Oral de contrôle continu.",
                "Retours et bilan du semestre.",
            ]),
        ],
        "psyclo": [
            ("Du lycée à la licence", "lycee.html"),
            ("Métiers de la psychologie", "metiers.html"),
            ("Comment apprendre", "apprendre.html"),
        ],
    },
]

# Modules semestre 2 (aperçu MCCC — contenu détaillé sur Psyclopédia)
MODULES_S2 = [
    {
        "id": "methode-experimentale",
        "code": "11NAAB04",
        "titre": "Méthodologie disciplinaire : méthode expérimentale",
        "format": "CM",
        "bloc": "Mineure psychologie — semestre 2",
        "resume": (
            "Approfondissement méthodologique : conception expérimentale, variables, "
            "validité interne et externe, plans intra- et inter-sujets."
        ),
        "psyclo": [
            ("Méthodes", "methodes.html"),
            ("Expériences historiques", "references/experiences.html"),
            ("Laboratoire jouable", "laboratoire.html"),
        ],
    },
    {
        "id": "psycho-cognitive",
        "code": "11NAAB05",
        "titre": "Psychologie cognitive",
        "format": "CM",
        "bloc": "Mineure psychologie — semestre 2",
        "resume": (
            "Perception, attention, mémoire, langage, raisonnement et décision. "
            "Méthodes expérimentales et modèles informationnels."
        ),
        "psyclo": [
            ("Branche cognitive L1", "branches/cognitive.html"),
            ("Psychologie cognitive", "categories/03-cognitive.html"),
            ("Laboratoire Stroop, empan…", "laboratoire/stroop.html"),
        ],
    },
    {
        "id": "psycho-sociale",
        "code": "11NAAB06",
        "titre": "Psychologie sociale",
        "format": "CM",
        "bloc": "Mineure psychologie — semestre 2",
        "resume": (
            "Influence, conformité, attitudes, stéréotypes, identités sociales et dynamiques de groupe."
        ),
        "psyclo": [
            ("Branche sociale L1", "branches/sociale.html"),
            ("Psychologie sociale", "categories/04-sociale.html"),
            ("Expériences Asch, Milgram", "references/experiences.html"),
        ],
    },
]
