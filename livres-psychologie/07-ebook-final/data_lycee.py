# -*- coding: utf-8 -*-
"""Du lycée à la licence : spécialités, quatre branches L1, Grand oral.

Sources publiques : Onisep, ministère, fiches licence de psychologie,
attendus Parcoursup. Le schéma est le même dans tous les lycées français.
Les règles d'orientation évoluent : vérifier les pages officielles.
"""

# --------------------------------------------------------------------------
# Ce que font réellement les lycées français (schéma national)
# --------------------------------------------------------------------------

ETABLISSEMENTS = [
    {
        "id": "general",
        "nom": "Lycée général et technologique",
        "type": "Voie principale vers une L1 de psychologie",
        "ville": "Toute la France",
        "academie": "toutes académies",
        "adresse": "Offre variable selon l'établissement (Onisep)",
        "role": "Bac général (spécialités) ou technologique (STMG, STI2D, ST2S). C'est le parcours le plus direct vers une licence.",
        "fait": [
            "Voie générale : 2de, 1re, Terminale, avec 3 puis 2 spécialités.",
            "Spécialités fréquentes pour la psycho : SES, HLP, SVT, mathématiques, HGGSP.",
            "Voie techno STMG (ressources humaines, mercatique) : pont vers la psychologie du travail.",
            "Voie techno ST2S (santé et social, selon les lycées) : pont vers clinique et santé.",
            "Voie techno STI2D : moins directe, mais la méthode scientifique reste utile.",
            "Les PsyEN du CIO interviennent dans l'établissement pour l'orientation et l'écoute.",
        ],
        "lien": "https://www.education.gouv.fr/reussir-au-lycee/choisir-ses-enseignements-de-specialite-au-lycee-pour-preparer-ses-etudes-superieures-325475",
    },
    {
        "id": "pro",
        "nom": "Lycée professionnel",
        "type": "Voie professionnelle",
        "ville": "Toute la France",
        "academie": "toutes académies",
        "adresse": "Bac pro, mention complémentaire, BTS",
        "role": "Un projet psychologie y passe plutôt par le CIO, un bac pro relation/soin, puis une remise à niveau ou une L1 sur dossier.",
        "fait": [
            "Le titre de psychologue reste un cursus licence + master.",
            "Un bac pro n'interdit pas la L1, mais les attendus (rédaction, sciences, stats) demandent un rattrapage ciblé.",
            "Les bacs pro accompagnement, soin et services à la personne sont les plus proches.",
        ],
        "lien": "https://www.onisep.fr/formation/apres-le-bac-les-etudes-superieures",
    },
    {
        "id": "cio",
        "nom": "CIO et PsyEN",
        "type": "Orientation et écoute",
        "ville": "Toute la France",
        "academie": "toutes académies",
        "adresse": "Un CIO par bassin, des PsyEN dans les établissements",
        "role": "Lieu où travaillent les psychologues de l'Éducation nationale : orientation, écoute, Parcoursup.",
        "fait": [
            "Accueil élèves, familles et adultes.",
            "Les PsyEN interviennent dans les collèges et lycées publics.",
            "Partenaire naturel pour un Grand oral ou un dossier Parcoursup « psychologie ».",
        ],
        "lien": "https://www.education.gouv.fr/les-centres-d-information-et-d-orientation-cio-11488",
    },
]

SPECIALITES = [
    ("SES", "Sciences économiques et sociales",
     "Socialisation, normes, groupes, institutions, inégalités, méthodes d'enquête.",
     "Psychologie sociale, politique, du travail, interculturelle.",
     "04-sociale"),
    ("HLP", "Humanités, littérature et philosophie",
     "Sujet, conscience, langage, autonomie, argumenter un texte, lire une œuvre.",
     "Clinique (entretien, récit), cognitive (langage, pensée), épistémologie.",
     "09-psychopathologie"),
    ("SVT", "Sciences de la vie et de la Terre",
     "Cerveau, hormones, génétique, homéostasie, démarche expérimentale.",
     "Cognitive, neurosciences, psychobiologie de L1, développement.",
     "08-neurosciences"),
    ("Mathématiques", "Mathématiques",
     "Fonctions, probabilités, lecture de graphiques, raisonnement.",
     "Statistiques descriptives et inférentielles de L1 — premier motif d'échec.",
     "19-psychometrie"),
    ("HGGSP", "Histoire-géo, géopolitique et sciences politiques",
     "Pouvoir, identités collectives, médias, conflictualité.",
     "Psychologie sociale et politique, stéréotypes, polarisation.",
     "26-politique"),
    ("Physique-chimie", "Physique-chimie",
     "Mesure, incertitude, modèle, expérimentation.",
     "Méthode scientifique, psychophysique, lecture d'une étude.",
     "01-fondamentaux"),
    ("Philo Tle", "Philosophie (tronc commun Terminale)",
     "Conscience, inconscient, liberté, autrui, vérité, bonheur.",
     "Toute la L1 : distinguer concept philosophique et résultat empirique.",
     "02-histoire"),
    ("EMC", "Enseignement moral et civique",
     "Dignité, préjugés, débat, engagement.",
     "Identité sociale, conformisme, éthique de la recherche.",
     "04-sociale"),
    ("Français", "Français (1re + épreuve anticipée)",
     "Lire, résumer, argumenter, oral.",
     "Compte rendu d'expérience, dissertation, Grand oral, mémoire plus tard.",
     "18-langage"),
    ("Grand oral", "Grand oral de Terminale",
     "Question, plan, sources, tenue de l'échange.",
     "Présenter une étude, ses limites, et répondre sans bluffer.",
     "01-fondamentaux"),
    ("STMG RH", "STMG ressources humaines",
     "Organisation, communication, gestion des personnes.",
     "Psychologie du travail, recrutement, risques psychosociaux.",
     "12-travail"),
    ("ST2S", "Sciences et technologies de la santé et du social",
     "Santé, protection sociale, biologie humaine — proposée dans de nombreux lycées technologiques.",
     "Clinique, santé, développement, métiers du soin. Accès L1 psychologie possible.",
     "14-sante"),
]

TRONC = [
    ("2de", "Explorer sans se fermer",
     "Prendre SES, SVT et HLP si elles sont offertes en enseignements d'exploration / options. "
     "S'exercer à rédiger et à lire un graphique. Rencontrer le CIO."),
    ("1re", "Trois spécialités, dont une scientifique si possible",
     "Combinaisons cohérentes pour la psycho : SES + HLP + SVT ; SES + SVT + maths ; "
     "HLP + SVT + maths. Aucune combinaison n'est obligatoire sur Parcoursup, mais les stats de L1 punissent l'absence de raisonnement quantitatif."),
    ("Tle", "Deux spécialités + philo + Grand oral",
     "Garder de préférence SES ou HLP et une science (SVT ou maths). Préparer un Grand oral sur une étude, un métier ou un débat (obéissance, mémoire, attachement). "
     "Renseigner Parcoursup : plusieurs licences de psychologie, et un vœu de secours."),
    ("L1", "Les quatre branches + stats + psychobiologie",
     "Semestre 1, dans la plupart des licences : introduction clinique, sociale, développement, cognitive, méthodes, parfois une mineure (sciences cognitives, sociologie, anthropologie ou sciences de l'éducation). "
     "Semestre 2 : approfondissement + statistiques descriptives. La licence seule ne donne pas le titre de psychologue."),
]

ATTENDUS_L1 = [
    "Appétence pour une approche scientifique, pas seulement pour « aider les autres ».",
    "Rigueur de lycée en mathématiques, SVT ou SES : démarche expérimentale, lecture de données.",
    "Capacité à rédiger clairement et à argumenter (français, HLP, philo).",
    "Autonomie : la L1 punit le bachotage de la veille et récompense le travail hebdomadaire.",
    "Curiosité pour le comportement ET pour les stats, la biologie, l'épistémologie.",
    "Comprendre dès maintenant : bac+5 (master) pour le titre ; L1 n'est qu'un socle.",
]

# --------------------------------------------------------------------------
# Liste complète de ce qu'il faut ajouter / maîtriser pour ces études
# --------------------------------------------------------------------------

LISTE_COMPLETE = [
    ("Du lycée français à la L1", [
        ("Carte des spécialités du bac vers les quatre branches", "fait"),
        ("Voie générale, techno (STMG, ST2S, STI2D) et voie pro", "fait"),
        ("Rôle du CIO et des PsyEN", "fait"),
        ("Ponts matière par matière vers les quatre branches", "fait"),
        ("Calendrier 2de → 1re → Tle → L1", "fait"),
        ("Attendus Parcoursup et idées de Grand oral", "fait"),
    ]),
    ("Psychologie clinique", [
        ("Objet : souffrance, entretien, cadre, éthique — sans diagnostic amateur", "fait"),
        ("Différences psychologue / psychiatre / psychothérapeute / PsyEN", "fait"),
        ("Modèles : psychodynamique, cognitivo-comportemental, humaniste, systémique", "site"),
        ("Psychopathologie descriptive (signes, pas étiquettes sur soi)", "site"),
        ("Cas historiques (Gage, Anna O., H.M.) et leurs limites", "site"),
        ("Tests cliniques : ce qu'ils mesurent, ce qu'ils ne mesurent pas", "site"),
        ("Alliance thérapeutique et facteurs communs", "site"),
        ("Numéros d'aide et parcours de soin (CMP, libéral)", "site"),
        ("Quiz et flashcards niveau L1", "fait"),
    ]),
    ("Psychologie sociale", [
        ("Objet : influence, groupes, normes, attitudes, identités", "fait"),
        ("Asch, Milgram, Tajfel, Festinger, Sherif — protocole et critiques éthiques", "site"),
        ("Attribution, stéréotypes, préjugés, contact intergroupe", "site"),
        ("Dissonance, persuasion, normes descriptives", "site"),
        ("Pont SES / EMC / HGGSP : socialisation, pouvoir, médias", "fait"),
        ("Laboratoire : ancrage, conformité (lecture)", "site"),
        ("Quiz et flashcards niveau L1", "fait"),
    ]),
    ("Psychologie du développement", [
        ("Objet : changements de la conception à la vieillesse", "fait"),
        ("Piaget, Vygotski, Bowlby, Erikson — idées, preuves, limites", "site"),
        ("Attachement, théorie de l'esprit, langage, adolescence", "site"),
        ("Plasticité, puberté cérébrale, vieillissement (fiche 24)", "site"),
        ("Pont SVT / EMC : maturation, hormones, relations", "fait"),
        ("Méthodes : longitudinal vs transversal, violation d'attente", "site"),
        ("Quiz et flashcards niveau L1", "fait"),
    ]),
    ("Psychologie cognitive", [
        ("Objet : perception, attention, mémoire, langage, décision", "fait"),
        ("Mémoire de travail, oubli, reconstructive (Loftus)", "site"),
        ("Attention sélective, double tâche, charge cognitive", "site"),
        ("Biais et heuristiques (Kahneman)", "site"),
        ("Labs jouables : Stroop, empan, temps de réaction, Müller-Lyer", "site"),
        ("Pont SVT / maths / philo : cerveau, probabilités, esprit", "fait"),
        ("Quiz et flashcards niveau L1", "fait"),
    ]),
    ("Méthode, stats et esprit scientifique", [
        ("Expérience, observation, étude de cas, enquête", "site"),
        ("Variable indépendante / dépendante, contrôle, éthique", "site"),
        ("Moyenne, médiane, écart-type, corrélation ≠ causalité", "site"),
        ("p-value, taille d'effet, réplication — sans formules intimidantes", "site"),
        ("Lire un article et un graphique de lycée / L1", "site"),
        ("Crise de la réplication et préenregistrement", "site"),
    ]),
    ("Outils d'apprentissage", [
        ("Parcours guidé lycée → L1", "fait"),
        ("Assistant IA ancré dans tout le site", "fait"),
        ("Fiches imprimables des 27 catégories", "site"),
        ("Révision espacée et flashcards", "site"),
        ("Cours magistraux de 50 minutes", "site"),
        ("Emploi du temps et rappels", "site"),
        ("Quiz notés + examen final", "site"),
        ("Méthode de dissertation / commentaire HLP-philo appliquée à une étude", "fait"),
        ("Banque de sujets de Grand oral", "fait"),
    ]),
    ("Orientation et métiers", [
        ("Licence, master, titre protégé, ADELI / RPPS", "site"),
        ("Métiers : clinicien, PsyEN, neuropsy, travail, recherche, UX", "site"),
        ("L1, mineures, double licence sciences cognitives", "fait"),
        ("Plan B : PASS/LAS, STAPS, éducation, socio, BTS, CPGE", "fait"),
    ]),
]

GRAND_ORAL = [
    ("L'obéissance à l'autorité est-elle une question de personnalité ?",
     "Milgram, variations, éthique, lien SES / HLP / EMC.", "04-sociale"),
    ("Peut-on faire confiance à un souvenir ?",
     "Loftus, mémoire reconstructive, témoins, philo de la vérité.", "03-cognitive"),
    ("Les écrans « détruisent-ils » l'attention des lycéens ?",
     "Charge cognitive, sommeil, nuances, neuromythes.", "22-numerique"),
    ("Comment un groupe fabrique-t-il un « eux » et un « nous » ?",
     "Tajfel, stéréotypes, contact, HGGSP.", "04-sociale"),
    ("Qu'est-ce qu'un attachement « sécure » — et que n'est-il pas ?",
     "Bowlby, Ainsworth, limites, clinique.", "05-developpement"),
    ("Pourquoi la L1 de psychologie contient-elle autant de statistiques ?",
     "Mesure, réplication, différence avec le coaching.", "01-fondamentaux"),
    ("Un test de personnalité de magazine mesure-t-il quelque chose ?",
     "Fidélité, validité, étalonnage, Big Five.", "19-psychometrie"),
    ("Faut-il enseigner selon le « style » visuel ou auditif ?",
     "Neuromythe, double codage, apprentissage.", "13-education"),
    ("Peut-on « lire » le caractère sur un cerveau ?",
     "Phrénologie, IRMf, limites, science psychologique.", "27-science-psychologique"),
    ("Aider, c'est soigner ? Le titre de psychologue.",
     "Loi de 1985, métier, éthique, CIO.", "metiers"),
]

DISSERTATION = [
    ("Lire le sujet", "Repérer le verbe (distinguer, expliquer, discuter), les notions, le piège d'évidence."),
    ("Définir", "Chaque mot clé : définition de cours + un exemple + une limite."),
    ("Problématique", "Transformer le sujet en tension (ex. « l'influence sociale libère-t-elle ou aliène-t-elle ? »)."),
    ("Plan", "Deux ou trois parties qui avancent, pas un catalogue. Idéal : constat / mécanisme / limites."),
    ("Preuves", "Une expérience ou une étude par argument, avec auteur, année, résultat ET critique."),
    ("Transition", "Une phrase qui montre pourquoi l'argument précédent ne suffit pas."),
    ("Conclusion", "Réponse nette + ouverture (éthique, réplication, application lycée)."),
]

# --------------------------------------------------------------------------
# Quatre branches — contenu L1 lisible dès le lycée
# --------------------------------------------------------------------------

BRANCHES = [
    {
        "id": "clinique",
        "title": "Psychologie clinique",
        "icon": "🩺",
        "color": "rose",
        "subtitle": "Comprendre une personne souffrante, dans son histoire et son contexte — sans la réduire à un trouble.",
        "objet": (
            "La clinique étudie la souffrance psychique et les ressources d'une personne concrète. "
            "Elle s'appuie sur l'entretien, l'observation, parfois des tests, et sur des modèles "
            "(psychodynamique, TCC, humaniste, systémique). Elle n'est ni de la voyance, ni un "
            "diagnostic en ligne, ni un substitut à un soin."
        ),
        "question": "Comment écouter, formuler des hypothèses et accompagner, sans nuire et sans usurper un titre ?",
        "lycee_ponts": [
            ("HLP", "Sujet, conscience, récit de soi, lecture d'un texte comme on lit un entretien."),
            ("Philo Tle", "Inconscient, liberté, autrui : distinguer concept et donnée clinique."),
            ("SVT", "Stress, hormones, sommeil, cerveau — le corps dans la souffrance."),
            ("EMC", "Dignité, consentement, secret, stigmatisation."),
            ("SES", "Inégalités d'accès aux soins, institutions, protection sociale."),
        ],
        "l1": (
            "Dans la plupart des licences, la clinique et la psychopathologie occupent un cours dès le semestre 1, "
            "puis des CM+TD jusqu'en L3. On y apprend à décrire des signes, à situer un modèle, "
            "pas à poser un diagnostic. Le titre de psychologue clinicien exige le master."
        ),
        "notions": [
            ("Entretien clinique", "Rencontre cadrée dont le but est de comprendre l'expérience du sujet, pas d'obtenir un score."),
            ("Cadre", "Lieu, durée, confidentialité, tarif ou institution : ce qui rend la parole possible."),
            ("Alliance", "Accord sur les buts, les tâches et le lien — meilleur prédicteur du changement."),
            ("Transfert", "Réactivation, dans la relation actuelle, de figures du passé — à travailler, pas à subir."),
            ("Psychopathologie", "Étude descriptive des troubles : signes, cours, facteurs — sans étiqueter un camarade."),
            ("Facteurs communs", "Ce qui soigne dans toute thérapie au-delà de la technique affichée."),
            ("Rétablissement", "Vivre une vie satisfaisante, avec ou sans symptômes résiduels."),
            ("Secret professionnel", "Obligation légale et déontologique : ce qui se dit ne circule pas."),
        ],
        "auteurs": [
            ("Lightner Witmer", "Première clinique psychologique, Pennsylvanie, 1896.", "categories/09-psychopathologie.html"),
            ("Pierre Janet", "Automatisme, dissociation, névroses — livre dans la bibliothèque.", "references/auteurs.html"),
            ("Daniel Lagache", "1949 : la personne totale en situation.", "categories/09-psychopathologie.html"),
            ("Karl Jaspers", "Expliquer par les causes, comprendre le sens.", "categories/09-psychopathologie.html"),
            ("Sigmund Freud", "Inconscient, rêve, transfert — à lire comme document historique et théorique.", "references/auteurs.html"),
            ("Carl Rogers", "Écoute, congruence, regard positif inconditionnel.", "references/auteurs.html"),
            ("Aaron Beck", "Pensées automatiques, thérapie cognitive.", "references/theories.html"),
            ("Philippe Pinel / Esquirol", "Aliénisme, naissance de la clinique moderne.", "references/chronologie.html"),
        ],
        "experiences": [
            ("Études de cas", "Gage, H.M., Anna O. : une personne peut faire basculer une théorie — et la fausser si on généralise trop.", "references/cas.html"),
            ("Essais sur les TCC", "Parmi les approches les mieux évaluées pour anxiété et dépression.", "categories/10-therapies.html"),
        ],
        "methodes": [
            "Entretien (directif, semi-directif, libre)",
            "Observation clinique",
            "Tests et échelles (BDI, MMPI… : pédagogie, pas auto-diagnostic)",
            "Étude de cas unique",
            "Supervision et déontologie",
        ],
        "metiers": [
            "Psychologue clinicien (bac+5, titre protégé)",
            "Psychiatre (médecine + internat)",
            "PsyEN — éducation, développement, orientation (concours)",
            "Psychologue en CMP, hôpital, médico-social, urgence",
        ],
        "mythes": [
            ("Un clinicien lit dans les pensées.", "Il observe, interroge, formule des hypothèses et les met à l'épreuve."),
            ("Faire de la clinique au lycée, c'est déjà être thérapeute.", "Écouter un ami n'est pas un soin. Le titre est protégé."),
            ("Un quiz en ligne pose un diagnostic.", "Aucun questionnaire de site n'a de valeur diagnostique."),
        ],
        "modules": [
            ("Ce que la clinique n'est pas",
             "<p>La clinique n'est pas un test TikTok, ni un forum qui « pose un TDAH », ni une séance improvisée "
             "entre camarades. Elle commence par un <strong>cadre</strong> (qui parle, à qui, pour quoi, sous "
             "quelles règles) et par l'<strong>hypothèse</strong> : ce que je crois comprendre peut être faux.</p>"
             "<p>Au lycée, l'usage juste est pédagogique : reconnaître les signes d'une détresse, savoir orienter "
             "(3114, 15, infirmière scolaire, PsyEN, CMP), et refuser d'étiqueter.</p>"),
            ("L'entretien comme instrument",
             "<p>Trois savoir-faire de L1, déjà entraînables en HLP :</p>"
             "<ol><li><strong>Question ouverte</strong> — « Qu'est-ce qui vous amène ? » plutôt que « Vous êtes déprimé, non ? »</li>"
             "<li><strong>Relance</strong> — répéter un mot, demander un exemple, tolérer le silence.</li>"
             "<li><strong>Reformulation</strong> — vérifier qu'on a compris, pas imposer une interprétation.</li></ol>"
             "<p>Ces gestes servent aussi au Grand oral et à l'entretien Parcoursup.</p>"),
            ("Quatre familles de modèles",
             "<p>Un même symptôme (une angoisse, une compulsion) se lit autrement :</p>"
             "<ul><li><strong>Psychodynamique</strong> — conflit, défense, histoire infantile.</li>"
             "<li><strong>Cognitivo-comportemental</strong> — apprentissage, pensées automatiques, évitement.</li>"
             "<li><strong>Humaniste</strong> — actualisation, congruence, conditions de la croissance.</li>"
             "<li><strong>Systémique</strong> — la souffrance comme nœud dans une famille ou une institution.</li></ul>"
             "<p>L1 demande de les exposer et de les comparer, pas d'en « choisir un pour la vie ».</p>"),
            ("D'où vient le mot clinique",
             "<p>Un cours d'introduction, enregistré puis remis au propre sur la fiche psychopathologie, "
             "tient en quelques repères. <em>Klinike technè</em> : l'art au chevet. Pinel et Esquirol "
             "sortent la folie du seul châtiment. Witmer ouvre en 1896 une clinique pour enfants en "
             "difficulté. Janet demande de penser la maladie, pas seulement de la panser, et de ne pas "
             "confondre une personne avec une moyenne. Jaspers sépare expliquer et comprendre. "
             "Lagache, en 1949, nomme l'objet : la personne totale en situation.</p>"
             "<p>Le psychologue n'est pas médecin : il ne prescrit pas. Le titre est protégé. "
             "Le cours enregistré mélangeait ces idées à du bruit de salle ; la fiche garde les idées "
             "et laisse tomber le bruit.</p>"),
            ("Éthique, dès le lycée",
             "<p>Consentement, secret, compétence limitée, non-nuisance. Un élève qui « diagnostique » un camarade "
             "sort de l'éthique. Un site pédagogique qui propose un quiz clinique doit écrire noir sur blanc : "
             "<em>ceci n'est pas un diagnostic</em>. Psyclopédia le fait partout.</p>"),
        ],
        "checklist": [
            "Définir clinique, psychopathologie, cadre, alliance",
            "Citer quatre modèles et un auteur pour chacun",
            "Distinguer psychologue, psychiatre, psychothérapeute, coach",
            "Nommer 3114 et le rôle d'un CMP",
            "Lire un cas historique en indiquant ce qu'il ne prouve pas",
            "Rédiger une question ouverte et une reformulation",
        ],
        "flashcards": [
            ("Qui peut porter le titre de psychologue en France ?", "Un cursus licence + master de psychologie avec stage et mémoire, puis inscription au répertoire."),
            ("Quel est le meilleur prédicteur du changement en thérapie ?", "L'alliance thérapeutique, plus que la technique affichée."),
            ("Que faire si un camarade va très mal ?", "Écouter sans diagnostiquer, ne pas rester seul, orienter vers un adulte et les numéros d'urgence (3114, 15)."),
        ],
        "liens": [
            ("Fiche psychopathologie", "categories/09-psychopathologie.html", "Fiche"),
            ("Cours remis au propre", "categories/09-psychopathologie.html#la-clinique-une-specialite-dans-la-psychologie", "Cours"),
            ("Clinique à mains nues", "categories/09-psychopathologie.html#mains-nues-et-clinique-armee", "Chapitre"),
            ("Titre protégé", "categories/09-psychopathologie.html#titre-diplome-et-deontologie", "Chapitre"),
            ("Fiche thérapies", "categories/10-therapies.html", "Fiche"),
            ("Troubles (pédagogie)", "references/troubles.html", "Références"),
            ("Cas cliniques", "references/cas.html", "Références"),
            ("Tests", "references/tests.html", "Références"),
            ("Aide et numéros", "aide.html", "Aide"),
            ("Métiers", "metiers.html", "Orientation"),
            ("Quiz clinique L1", "quiz/quiz.html?id=clinique-l1", "Quiz"),
        ],
        "quiz_id": "clinique-l1",
    },
    {
        "id": "sociale",
        "title": "Psychologie sociale",
        "icon": "👥",
        "color": "or",
        "subtitle": "Comment les autres — présents, imaginés ou institutionnels — façonnent jugement, émotion et conduite.",
        "objet": (
            "La psychologie sociale relie l'individu et le groupe. Elle mesure l'influence, les normes, "
            "les attitudes, les préjugés, l'obéissance, l'aide, l'agression. Elle se distingue de la "
            "sociologie par l'échelle (processus psychologiques) et de la clinique par la méthode "
            "(souvent expérimentale)."
        ),
        "question": "Dans quelle mesure mon avis, mon souvenir et mon geste sont-ils déjà des faits sociaux ?",
        "lycee_ponts": [
            ("SES", "Socialisation, groupes, institutions, méthodes d'enquête — le pont le plus direct."),
            ("EMC", "Préjugés, discriminations, débat démocratique."),
            ("HGGSP", "Identités, médias, conflictualité, complotisme."),
            ("HLP", "Autrui, persuasion, rhétorique."),
            ("Grand oral", "Milgram, Asch, stéréotypes : sujets déjà « prêts »."),
        ],
        "l1": (
            "La psychologie sociale est au programme dès le semestre 1, puis en CM+TD jusqu'en L3. "
            "On y apprend à lire une expérience (variable, contrôle, éthique) autant qu'à citer un nom."
        ),
        "notions": [
            ("Norme", "Règle partagée, explicite ou tacite, qui oriente ce qu'on ose faire ou dire."),
            ("Conformité", "Alignement sur le groupe même quand on le sait faux (Asch)."),
            ("Obéissance", "Soumission à une autorité légitime perçue (Milgram) — pas une « personnalité faible »."),
            ("Identité sociale", "Partie du soi qui vient des groupes d'appartenance (Tajfel)."),
            ("Attribution", "Explication qu'on donne d'un acte : interne (la personne) ou externe (la situation)."),
            ("Dissonance", "Tension quand un acte contredit une idée — souvent l'idée qui plie (Festinger)."),
            ("Stéréotype", "Croyance partagée sur un groupe ; le préjugé est l'attitude, la discrimination l'acte."),
            ("Diffusion de responsabilité", "Plus il y a de témoins, moins chacun se sent tenu d'agir."),
        ],
        "auteurs": [
            ("Solomon Asch", "Lignes et conformité.", "references/experiences.html"),
            ("Stanley Milgram", "Obéissance — et le débat éthique qui a changé la recherche.", "references/experiences.html"),
            ("Henri Tajfel", "Groupes minimaux, identité sociale.", "references/theories.html"),
            ("Leon Festinger", "Dissonance cognitive.", "references/theories.html"),
            ("Muzafer Sherif", "Norme autocinétique, grotte des voleurs.", "references/experiences.html"),
        ],
        "experiences": [
            ("Asch (1951)", "Des complices donnent une mauvaise longueur : beaucoup suivent au moins une fois.", "references/experiences.html"),
            ("Milgram (1963)", "65 % vont au voltage maximal dans la version princeps — avec de fortes variations selon le dispositif.", "references/experiences.html"),
            ("Festinger & Carlsmith", "1 $ justifie moins un mensonge que 20 $ : on change d'avis pour réduire la dissonance.", "references/experiences.html"),
        ],
        "methodes": [
            "Expérience de laboratoire (variable isolée)",
            "Expérience de terrain",
            "Enquête et échelles d'attitude",
            "Observation de groupes",
            "Comité d'éthique : plus rien n'est « Stanford 1971 »",
        ],
        "metiers": [
            "Chercheur en psychologie sociale",
            "Sciences comportementales / politiques publiques",
            "Psychologue du travail et des organisations",
            "Prévention des discriminations, éducation",
        ],
        "mythes": [
            ("Les foules sont toujours irrationnelles.", "Les foules suivent des normes et des identités ; elles coopèrent souvent en urgence."),
            ("Milgram prouve que « les gens sont mauvais ».", "Il montre le pouvoir d'un dispositif d'autorité, pas une essence humaine."),
            ("Avoir des préjugés, c'est être un monstre.", "Les biais catégoriels sont banals ; la question est de les reconnaître et de les limiter."),
        ],
        "modules": [
            ("Du cours de SES à l'expérience",
             "<p>En SES, on décrit la socialisation. En psychologie sociale, on <strong>manipule une variable</strong> "
             "pour voir l'effet : un complice, une consigne, une norme affichée. Le lycéen doit apprendre à "
             "écrire : hypothèse, VI, VD, contrôle, résultat, limite éthique.</p>"),
            ("Influence : trois verbes",
             "<ul><li><strong>Se conformer</strong> — le groupe (Asch).</li>"
             "<li><strong>Obéir</strong> — l'autorité (Milgram).</li>"
             "<li><strong>S'identifier</strong> — le « nous » (Tajfel).</li></ul>"
             "<p>Les confondre dans une copie de L1 coûte des points. Un plan de dissertation peut justement "
             "les distinguer.</p>"),
            ("Éthique après Stanford",
             "<p>Consentement, droit de retrait, débriefing, balance bénéfice/risque. On étudie encore "
             "l'obéissance, mais plus en faisant croire qu'on électrocute quelqu'un. Citer une expérience "
             "célèbre sans sa critique éthique est une faute de L1.</p>"),
        ],
        "checklist": [
            "Définir norme, conformité, obéissance, identité sociale",
            "Raconter Asch et Milgram avec un chiffre et une critique",
            "Distinguer stéréotype, préjugé, discrimination",
            "Expliquer dissonance avec un exemple lycée (révisions, amitié)",
            "Écrire VI / VD pour une expérience inventée et éthique",
        ],
        "flashcards": [
            ("Quelle est la différence entre conformité et obéissance ?", "La conformité s'aligne sur des pairs ; l'obéissance s'aligne sur une autorité."),
            ("Que montre l'expérience des groupes minimaux ?", "Une catégorisation arbitraire suffit à produire un favoritisme pour « son » groupe."),
            ("Pourquoi « 65 % » ne suffit pas comme copie ?", "Il faut le dispositif, les variations, l'éthique et ce que le chiffre ne prouve pas."),
        ],
        "liens": [
            ("Fiche psychologie sociale", "categories/04-sociale.html", "Fiche"),
            ("Expériences", "references/experiences.html", "Références"),
            ("Biais", "references/biais.html", "Références"),
            ("Politique et polarisation", "categories/26-politique.html", "Fiche"),
            ("Travail et organisations", "categories/12-travail.html", "Fiche"),
            ("Quiz sociale", "quiz/quiz.html?id=sociale", "Quiz"),
            ("Quiz branches L1", "quiz/quiz.html?id=branches-l1", "Quiz"),
        ],
        "quiz_id": "sociale",
    },
    {
        "id": "developpement",
        "title": "Psychologie du développement",
        "icon": "🌱",
        "color": "vert",
        "subtitle": "Comment un organisme devient une personne — et continue de changer jusqu'à la vieillesse.",
        "objet": (
            "Le développement étudie les transformations cognitives, affectives, sociales et corporelles "
            "tout au long de la vie. Il n'est pas « la psychologie des enfants » : adolescence, âge adulte "
            "et vieillissement en font partie. Il croise génétique, expérience, culture et hasard."
        ),
        "question": "Qu'est-ce qui change avec l'âge, qu'est-ce qui reste, et comment le savoir sans confondre génération et maturation ?",
        "lycee_ponts": [
            ("SVT", "Maturation cérébrale, hormones, puberté, génétique — sans déterminisme plat."),
            ("SES", "Socialisation primaire / secondaire, famille, école."),
            ("HLP", "Enfance, éducation, récit d'apprentissage."),
            ("EMC", "Autonomie progressive, autorité, harcèlement."),
            ("Philo Tle", "Devenir sujet, liberté, habitude."),
        ],
        "l1": (
            "Le développement est enseigné dès le semestre 1, puis en CM+TD. On attend les stades de "
            "Piaget <em>et</em> leurs limites, Vygotski, l'attachement, et la distinction transversal / longitudinal."
        ),
        "notions": [
            ("Stade", "Période qualitativement distincte (Piaget) — utile, trop rigide si on en fait un escalier obligatoire."),
            ("Zone proximale", "Écart entre ce que l'enfant fait seul et ce qu'il fait avec un étayage (Vygotski)."),
            ("Attachement", "Lien durable qui sert de base de sécurité (Bowlby, Ainsworth) — pas un « style de couple » de magazine."),
            ("Théorie de l'esprit", "Comprendre que l'autre a des croyances différentes des miennes."),
            ("Plasticité", "Capacité du système nerveux à se réorganiser selon l'expérience, à tout âge avec des fenêtres."),
            ("Puberté cérébrale", "Le système de récompense mûrit avant le contrôle préfrontal : risque et pairs."),
            ("Cohorte", "Génération partagée ; une étude transversale la confond avec l'âge."),
            ("Étayage", "Aide ajustée qui se retire quand l'enfant peut seul."),
        ],
        "auteurs": [
            ("Jean Piaget", "Stades, équilibration, épreuves — et sous-estimation du bébé.", "references/theories.html"),
            ("Lev Vygotski", "Langage social, ZPD, culture.", "references/theories.html"),
            ("John Bowlby / Mary Ainsworth", "Attachement, situation étrange.", "references/theories.html"),
            ("Erik Erikson", "Huit âges, crises psychosociales.", "references/theories.html"),
            ("Lawrence Kohlberg", "Raisonnement moral — à nuancer (Gilligan, culture).", "references/auteurs.html"),
        ],
        "experiences": [
            ("Conservation (Piaget)", "L'enfant juge la quantité à la forme du verre — jusqu'à un certain âge, et selon la consigne.", "references/experiences.html"),
            ("Situation étrange", "Séparation / réunion : stratégies sécure, évitante, ambivalente, désorganisée.", "references/tests.html"),
            ("Fausse croyance (Sally-Anne)", "Repère classique de la théorie de l'esprit vers 4 ans — avec variants plus précoces.", "references/experiences.html"),
        ],
        "methodes": [
            "Longitudinal (mêmes personnes dans le temps)",
            "Transversal (âges différents le même jour)",
            "Séquentiel (les deux)",
            "Violation d'attente, temps de regard (bébés)",
            "Observation en milieu naturel",
        ],
        "metiers": [
            "Psychologue du développement",
            "PsyEN 1er degré (apprentissages)",
            "CAMSP, PMI, protection de l'enfance",
            "Gérontologie (autre bout de la vie)",
        ],
        "mythes": [
            ("Les trois premières années figent tout.", "Elles comptent ; la plasticité continue. L'adoption tardive montre des récupérations réelles."),
            ("Mozart rend le bébé plus intelligent.", "Effet inexistant sur le QI. La musique reste un plaisir, pas un dopage cognitif."),
            ("L'adolescent est irrationnel.", "Son cerveau pèse autrement récompense et contrôle, surtout devant des pairs."),
        ],
        "modules": [
            ("Piaget, puis après Piaget",
             "<p>Retenir les quatre stades (sensorimoteur, préopératoire, opérations concrètes, formelles) "
             "est le minimum lycée. En L1, on ajoute : le bébé sait plus tôt qu'on ne le mesurait "
             "(permanence de l'objet dès 3-4 mois en violation d'attente), les stades se chevauchent, "
             "et la culture change les âges apparents.</p>"),
            ("Vygotski contre l'escalier solitaire",
             "<p>Ce que je fais aujourd'hui avec une aide, je le ferai seul demain. Le langage, d'abord "
             "social, devient outil intérieur. Pour un lycéen tuteur : expliquer à un 2de, c'est déjà "
             "de la ZPD — et c'est le meilleur entraînement à la L1.</p>"),
            ("Attachement sans romance",
             "<p>Sécure, évitant, ambivalent, désorganisé : catégories de <em>comportement en situation</em>, "
             "pas des essences. Un attachement acquis-sécure existe. Transformer cela en test de couple "
             "est un glissement commercial.</p>"),
        ],
        "checklist": [
            "Réciter les stades de Piaget et une limite moderne",
            "Définir ZPD et étayage avec un exemple de classe",
            "Expliquer l'attachement sans diagnostiquer sa famille",
            "Distinguer étude longitudinale et transversale",
            "Relier adolescence, pairs et cortex préfrontal",
        ],
        "flashcards": [
            ("Qu'est-ce que la zone proximale de développement ?", "L'écart entre ce que l'enfant réussit seul et ce qu'il réussit avec un étayage."),
            ("Pourquoi une étude transversale trompe-t-elle sur le vieillissement ?", "Elle mélange l'âge et la génération (effet de cohorte)."),
            ("À quoi sert l'attachement selon Bowlby ?", "À tenir l'enfant près d'une figure qui protège, et à explorer ensuite depuis cette base."),
        ],
        "liens": [
            ("Fiche développement", "categories/05-developpement.html", "Fiche"),
            ("Étudier un nourrisson", "categories/05-developpement.html#comment-interroger-un-nourrisson", "Chapitre"),
            ("Vie entière", "categories/05-developpement.html#changement-et-continuite-tout-au-long-de-la-vie", "Chapitre"),
            ("Vieillissement", "categories/24-vieillissement.html", "Fiche"),
            ("Éducation", "categories/13-education.html", "Fiche"),
            ("Théories (Piaget, Vygotski…)", "references/theories.html", "Références"),
            ("Quiz développement", "quiz/quiz.html?id=developpement-personnalite", "Quiz"),
        ],
        "quiz_id": "developpement-personnalite",
    },
    {
        "id": "cognitive",
        "title": "Psychologie cognitive",
        "icon": "💭",
        "color": "vert",
        "subtitle": "Comment l'esprit encode, filtre, transforme et décide — comme un système à ressources limitées.",
        "objet": (
            "La cognitive étudie perception, attention, mémoire, langage, raisonnement, décision. "
            "Elle hérite de la révolution des années 1950-60 : l'esprit traite de l'information, "
            "on peut le modéliser et le mesurer (temps de réaction, erreurs, empan)."
        ),
        "question": "Si je me trompe, est-ce mon « intelligence » — ou la façon dont la tâche surcharge un système limité ?",
        "lycee_ponts": [
            ("SVT", "Neurone, synapse, aires, sommeil et consolidation."),
            ("Maths", "Probabilités, courbes, lecture d'un graphique d'oubli."),
            ("Philo Tle", "Esprit, représentation, vérité, illusion."),
            ("HLP", "Langage, interprétation, mémoire d'une œuvre."),
            ("NSI / SI (si présente)", "Algorithme, mémoire, interface — cousinage avec les sciences cognitives."),
        ],
        "l1": (
            "La cognitive ouvre dès le semestre 1 ; certaines universités proposent une mineure ou une double licence "
            "sciences cognitives. Les TD mesurent : empan, Stroop, temps de réaction. "
            "Les labs du site rejouent exactement ces épreuves."
        ),
        "notions": [
            ("Mémoire de travail", "Maintien + manipulation, capacité réelle ≈ 4 unités, pas un disque dur."),
            ("Attention sélective", "Filtrer ; le prix est la cécité à l'inattendu (gorille)."),
            ("Encodage / stockage / récupération", "Trois moments ; on échoue souvent à la récupération, pas à « l'enregistrement »."),
            ("Mémoire reconstructive", "Chaque rappel réécrit ; Loftus et les témoins."),
            ("Charge cognitive", "Apprendre échoue quand la mémoire de travail déborde (Sweller)."),
            ("Heuristique", "Raccourci rapide, souvent utile, parfois biaisé."),
            ("Système 1 / 2", "Rapide-automatique vs lent-contrôlé (Kahneman) — modèle, pas IRM de deux cerveaux."),
            ("Double tâche", "Deux processus qui se gênent révèlent qu'ils partagent une ressource."),
        ],
        "auteurs": [
            ("George Miller / Alan Baddeley", "Empan, modèle de la mémoire de travail.", "references/theories.html"),
            ("Elizabeth Loftus", "Faux souvenirs, suggestibilité.", "references/experiences.html"),
            ("Daniel Kahneman", "Heuristiques, deux systèmes.", "references/theories.html"),
            ("Anne Treisman / Broadbent", "Filtres attentionnels.", "references/auteurs.html"),
            ("John Sweller", "Charge cognitive et pédagogie.", "references/theories.html"),
        ],
        "experiences": [
            ("Stroop", "Le mot « ROUGE » écrit en bleu coûte du temps — interférence.", "laboratoire/stroop.html"),
            ("Empan", "Combien d'items juste après présentation.", "laboratoire/empan.html"),
            ("Gorille invisible", "Attention occupée = événement manqué.", "references/experiences.html"),
            ("Müller-Lyer", "Illusion : la perception n'est pas une photo.", "laboratoire/muller-lyer.html"),
        ],
        "methodes": [
            "Temps de réaction et taux d'erreur",
            "Double tâche",
            "Protocoles d'amorçage",
            "IRMf / EEG (à relier à la fiche science psychologique)",
            "Modélisation (boîtes et flèches, puis computationnelle)",
        ],
        "metiers": [
            "Chercheur en sciences cognitives",
            "Neuropsychologue (master)",
            "Ergonomie / UX research",
            "Ingénierie pédagogique, charge cognitive",
        ],
        "mythes": [
            ("Nous n'utilisons que 10 % du cerveau.", "Faux : l'organe est métaboliquement trop coûteux pour être à 90 % inactif."),
            ("La mémoire est une vidéo.", "Elle reconstruit et se déforme à chaque rappel."),
            ("Multitâche = efficacité.", "Le coût de bascule attentionnelle est massif."),
        ],
        "modules": [
            ("Trois mémoires, une copie",
             "<p>Sensorielle (moins d'une seconde), travail (secondes, ≈ 4 chunks), long terme "
             "(épisodique, sémantique, procédurale). Une question de L1 demande souvent "
             "<em>laquelle</em> est en jeu, pas un roman sur « la mémoire ».</p>"),
            ("Réviser comme un cognitician",
             "<p>Rappel actif, espacement, entrelacement, élaboration : le site Apprendre les "
             "détaille. Un lycéen qui prépare HLP et SES avec ces techniques "
             "arrive en L1 déjà armé — c'est le meilleur avantage, plus qu'une spécialité magique.</p>"),
            ("Du labo du site au TD de licence",
             "<p>Faire Stroop, empan, temps de réaction, flanker, ancrage. Noter son score, "
             "lire l'explication, citer la limite (échantillon = toi). C'est déjà un compte rendu de TD.</p>"),
        ],
        "checklist": [
            "Schéma mémoire sensorielle / travail / long terme",
            "Expliquer Stroop et ce qu'il mesure",
            "Donner un exemple de faux souvenir (sans inventer un trauma)",
            "Définir heuristique et un biais (confirmation, ancrage, disponibilité)",
            "Relier charge cognitive et une fiche de cours trop dense",
        ],
        "flashcards": [
            ("Quelle est la capacité moderne de la mémoire de travail ?", "Environ 4 unités (Cowan), plutôt que 7 ± 2."),
            ("Que montre Loftus ?", "Une information reçue après coup peut modifier le souvenir."),
            ("Pourquoi le multitâche fatigue-t-il ?", "Chaque bascule réinstalle le contexte en mémoire de travail et coûte du temps."),
        ],
        "liens": [
            ("Fiche cognitive", "categories/03-cognitive.html", "Fiche"),
            ("Position sérielle", "categories/03-cognitive.html#le-debut-et-la-fin-dune-liste", "Chapitre"),
            ("Amorçage de Tulving", "categories/03-cognitive.html#une-trace-qui-survit-au-souvenir", "Chapitre"),
            ("Démarche scientifique", "categories/01-fondamentaux.html#trois-criteres-dune-psychologie-scientifique", "Chapitre"),
            ("Neurosciences", "categories/08-neurosciences.html", "Fiche"),
            ("Science psychologique", "categories/27-science-psychologique.html", "Fiche"),
            ("Laboratoire", "laboratoire.html", "Labo"),
            ("Biais", "references/biais.html", "Références"),
            ("Apprendre efficacement", "apprendre.html", "Méthode"),
            ("Quiz cognitive", "quiz/quiz.html?id=cognitive", "Quiz"),
        ],
        "quiz_id": "cognitive",
    },
]

COMPARAISON = [
    ("Question type",
     "Que vit cette personne, et comment l'accompagner ?",
     "Comment le groupe oriente-t-il mon acte ?",
     "Qu'est-ce qui change avec l'âge et l'expérience ?",
     "Comment l'information est-elle traitée ?"),
    ("Unité d'analyse",
     "Le sujet dans son histoire",
     "L'individu-en-situation-sociale",
     "La trajectoire dans le temps",
     "Le système de traitement"),
    ("Méthode star",
     "Entretien, cas, tests cliniques",
     "Expérience sociale, enquête",
     "Longitudinal, observation, épreuves",
     "Temps de réaction, double tâche, labs"),
    ("Piège lycéen",
     "Diagnostiquer un camarade",
     "Moraliser (« les gens sont moutons »)",
     "Croire les stades comme un destin",
     "Croire que mémoire = disque dur"),
    ("Pont lycée",
     "HLP + philo + EMC",
     "SES + EMC + HGGSP",
     "SVT + SES + EMC",
     "SVT + maths + philo"),
    ("Suite master fréquente",
     "Clinique / psychopathologie",
     "Sociale, travail, interculturelle",
     "Développement, éducation, gérontologie",
     "Cognitive, neuropsychologie, UX"),
]

PLAN_SEMAINES = [
    ("Semaine 1", "Socle", "Fondamentaux, histoire, méthodes — et cette page lycée.",
     ["categories/01-fondamentaux.html", "categories/02-histoire.html", "methodes.html"]),
    ("Semaine 2", "Cognitive", "Mémoire, attention, un labo, quiz cognitive.",
     ["categories/03-cognitive.html", "laboratoire.html", "quiz/quiz.html?id=cognitive"]),
    ("Semaine 3", "Sociale", "Asch, Milgram, identité, SES → expérience.",
     ["categories/04-sociale.html", "references/experiences.html", "quiz/quiz.html?id=sociale"]),
    ("Semaine 4", "Développement", "Piaget, Vygotski, attachement.",
     ["categories/05-developpement.html", "references/theories.html", "quiz/quiz.html?id=developpement-personnalite"]),
    ("Semaine 5", "Clinique", "Cadre, modèles, troubles pédagogiques, aide.",
     ["branches/clinique.html", "categories/09-psychopathologie.html", "aide.html"]),
    ("Semaine 6", "Orientation", "Métiers, Grand oral, quiz d'orientation.",
     ["metiers.html", "quiz/quiz.html?id=lycee-orientation", "assistant.html"]),
]

SOURCES_LYCEE = [
    ("Ministère — choisir ses spécialités au lycée",
     "https://www.education.gouv.fr/reussir-au-lycee/choisir-ses-enseignements-de-specialite-au-lycee-pour-preparer-ses-etudes-superieures-325475"),
    ("Onisep — après le bac",
     "https://www.onisep.fr/formation/apres-le-bac-les-etudes-superieures"),
    ("Onisep — licence de psychologie",
     "https://www.onisep.fr/ressources/univers-formation/formations/post-bac/licence-mention-psychologie"),
    ("Éduscol — programmes de spécialité",
     "https://eduscol.education.fr/pid36131/cycle-terminal-de-la-voie-generale.html"),
    ("Ministère — CIO",
     "https://www.education.gouv.fr/les-centres-d-information-et-d-orientation-cio-11488"),
]
