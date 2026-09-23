# -*- coding: utf-8 -*-
"""Synthèse pédagogique des quatre UE de psychologie d'une L1.

Textes rédigés pour Psyclopédia à partir des plans et des lectures
(démarche scientifique, clinique, développement, corpus cognitif).
Ce n'est pas un polycopié universitaire : les articles et manuels
restent chez leurs auteurs. Aucun diagnostic, aucun conseil de soin.
"""

L1_QUIZ = {
    "id": "l1-psychologie",
    "icon": "🎓",
    "color": "vert",
    "title": "Psychologie de licence",
    "desc": "Démarche scientifique, clinique, développement et lectures cognitives.",
    "difficulty": "Moyen",
    "questions": [
        {"q": "Une démarche est scientifique si elle est à la fois…",
         "a": ["intuitive, rapide et secrète",
               "systématique, précise et communicable",
               "uniquement quantitative",
               "réservée aux laboratoires de biologie"],
         "correct": 1,
         "explain": "Sans organisation, sans procédure réplicable, ou sans discussion par d'autres chercheurs, on n'est plus dans une science."},
        {"q": "Dans une expérience, la variable dépendante est…",
         "a": ["le paramètre que l'on manipule",
               "la mesure qui sert à observer l'effet",
               "le consentement du participant",
               "le nom de la théorie"],
         "correct": 1,
         "explain": "La variable indépendante est manipulée. La variable dépendante est ce que l'on mesure."},
        {"q": "La « clinique à mains nues » désigne surtout…",
         "a": ["l'IRM et les tests projectifs",
               "l'observation et l'entretien",
               "la prescription de médicaments",
               "l'expérience en double aveugle"],
         "correct": 1,
         "explain": "Juliette Favez-Boutonnier opposait cette clinique, armée de l'observation et de l'entretien, à la clinique « armée » de tests (Lagache)."},
        {"q": "La psychologie du développement étudie…",
         "a": ["seulement l'enfant jusqu'à 6 ans",
               "les changements et les continuités tout au long de la vie",
               "uniquement les troubles",
               "le QI comme seul indicateur"],
         "correct": 1,
         "explain": "La perspective « tout au long de la vie » regarde le changement et ce qui demeure, de la conception au grand âge."},
        {"q": "Le paradigme d'habituation sert à étudier le nourrisson parce que…",
         "a": ["le bébé parle déjà",
               "il regarde moins ce qui est devenu familier, puis réagit à la nouveauté",
               "il passe le test de Binet",
               "il choisit une réponse au clavier"],
         "correct": 1,
         "explain": "On présente un stimulus jusqu'à ce que le regard baisse, puis un stimulus nouveau : la reprise du regard indique une discrimination."},
        {"q": "L'expérience de Tolman, Ritchie et Kalish (1946) montre que le rat…",
         "a": ["n'apprend qu'une chaîne de muscles",
               "peut prendre un raccourci, comme s'il avait une carte des lieux",
               "oublie dès qu'on retire la récompense",
               "ne distingue pas les directions"],
         "correct": 1,
         "explain": "Le raccourci vers le but, sans avoir pratiqué ce chemin, plaide pour une attente spatiale, pas pour une simple réponse motrice."},
        {"q": "Chez Tulving, Schacter et Stark (1982), l'amorçage sur des fragments de mots…",
         "a": ["disparaît en même temps que la reconnaissance",
               "reste stable alors que la reconnaissance chute en une semaine",
               "n'existe pas chez l'humain",
               "mesure le quotient intellectuel"],
         "correct": 1,
         "explain": "Compléter A _ _ A _ IN est facilité par une lecture antérieure, même quand on ne reconnaît plus le mot. Deux systèmes de mémoire ne se confondent pas."},
        {"q": "L'effet Google (Sparrow et al., 2011) décrit le fait que…",
         "a": ["on mémorise mieux une information si l'on sait où la retrouver",
               "Internet supprime toute mémoire",
               "les moteurs de recherche créent des faux souvenirs visuels",
               "on retient mieux ce qu'on a effacé"],
         "correct": 0,
         "explain": "On encode moins le contenu lui-même quand on s'attend à pouvoir le rechercher, et davantage l'endroit où le chercher."},
    ],
}

L1_GLOSSAIRE = [
    ("Variable indépendante",
     "Paramètre que l'expérimentateur manipule. Ses modalités doivent rester comparables, sur une même dimension psychologique.",
     "01-fondamentaux"),
    ("Variable dépendante",
     "Mesure recueillie pour observer l'effet de la manipulation. Ce n'est pas la cause que l'on fait varier.",
     "01-fondamentaux"),
    ("Standardisation",
     "Identité de la situation pour tous les participants : consignes, matériel, durée, environnement. Elle rend les données comparables et la réplication possible.",
     "01-fondamentaux"),
    ("Modèle biopsychosocial",
     "Façon d'expliquer une expérience humaine par l'entrecroisement de facteurs biologiques, psychologiques et sociaux (Engel, 1977), plutôt que par une seule cause.",
     "01-fondamentaux"),
    ("Méthode clinique",
     "Démarche qui cherche à comprendre une personne singulière dans son histoire et ses liens, du fonctionnement ordinaire à la souffrance. Ce n'est pas un diagnostic posé sur Internet.",
     "09-psychopathologie"),
    ("Clinique à mains nues",
     "Observation et entretien, sans test, selon la formule de Juliette Favez-Boutonnier. La clinique « armée » (Lagache) y ajoute des épreuves et des médiations.",
     "09-psychopathologie"),
    ("Ontogenèse",
     "Développement d'un individu, de la conception à la mort. À distinguer de la phylogenèse (l'espèce) et de la microgenèse (l'apprentissage d'une compétence, sur des jours ou des mois).",
     "05-developpement"),
    ("Habituation",
     "Baisse de l'intérêt quand un stimulus se répète. Chez le nourrisson, la reprise du regard face à un stimulus nouveau sert à montrer qu'il discrimine.",
     "05-developpement"),
    ("Transgression des attentes",
     "Paradigme où l'on montre au bébé un événement possible et un événement impossible. Un regard plus long vers l'impossible suggère une attente sur le monde physique ou social.",
     "05-developpement"),
    ("Hospitalisme",
     "Tableau décrit par René Spitz chez des nourrissons privés de relation stable : retrait, ralentissement du développement. Il a montré que le soin n'est pas qu'alimentaire.",
     "05-developpement"),
    ("Métacognition",
     "Connaissance et pilotage de ses propres processus mentaux : savoir ce que l'on sait, choisir une stratégie, surveiller une mémorisation (Flavell).",
     "03-cognitive"),
    ("Mémoire transactive",
     "Répartition du savoir dans un couple ou un groupe : chacun retient une partie, et sait à qui demander le reste (Wegner).",
     "03-cognitive"),
    ("Pédagogie naturelle",
     "Hypothèse de Csibra et Gergely : les humains sont préparés à transmettre et à recevoir des savoirs généraux, via des signaux ostensifs (regard, pointage, adresse).",
     "03-cognitive"),
    ("Oubli dirigé",
     "Consigne d'oublier un matériel qui réduit ensuite son interférence sur ce qu'il faut retenir (Bjork). Oublier peut être une fonction, pas seulement une panne.",
     "03-cognitive"),
]

L1_CHRONO = [
    ("1946", "Le raccourci de Tolman",
     "Tolman, Ritchie et Kalish montrent qu'un rat peut rejoindre un but par un chemin nouveau : l'apprentissage spatial n'est pas qu'une chaîne de réponses.",
     "cognitive"),
    ("1953", "L'écoute dichotique de Cherry",
     "Colin Cherry fait répéter un message à une oreille pendant qu'un autre arrive à l'autre oreille : on suit une voix, et l'on rate presque tout le reste.",
     "cognitive"),
    ("1969", "Mémoire dépendante de l'état",
     "Goodwin et ses collègues observent que ce qui a été appris sous alcool se rappelle mieux dans le même état. Le contexte interne fait partie de l'indice de récupération.",
     "cognitive"),
    ("1979", "La métacognition selon Flavell",
     "Flavell nomme la connaissance que l'on a de sa propre cognition, et le contrôle que l'on exerce pendant une tâche de mémoire.",
     "cognitive"),
    ("1982", "L'amorçage sans reconnaissance",
     "Tulving, Schacter et Stark : compléter un fragment de mot reste facilité une semaine plus tard, alors que reconnaître le mot a chuté.",
     "cognitive"),
    ("1998", "Mémoire de type épisodique chez le geai",
     "Clayton et Dickinson montrent que des geais retrouvent une cache en tenant compte de quoi, où et quand la nourriture a été cachée.",
     "cognitive"),
    ("2009", "La pédagogie naturelle",
     "Csibra et Gergely proposent que la communication humaine sert d'abord à transmettre des connaissances générales, et que le nourrisson est prêt à les recevoir.",
     "cognitive"),
    ("2011", "L'effet Google",
     "Sparrow, Liu et Wegner : savoir qu'une information sera retrouvable en ligne change ce que l'on encode — le chemin plus que le contenu.",
     "cognitive"),
]

L1_EXPERIENCES = [
    ("raccourci-tolman", "Le raccourci et la carte cognitive", "Edward Tolman, Ritchie & Kalish", "1946", "03-cognitive",
     "Le rat n'apprend pas seulement à tourner : il se construit une attente sur la disposition des lieux.",
     "Des rats s'entraînent dans un labyrinthe en croix à trouver de la nourriture toujours au même endroit. On les fait ensuite partir d'un bras nouveau.",
     "Beaucoup prennent le chemin le plus direct vers le but, un raccourci qu'ils n'ont pas pratiqué comme réponse musculaire.",
     "Argument classique contre un behaviorisme qui ne verrait que des stimulus et des réponses. La « carte cognitive » devient un concept de la psychologie spatiale.",
     "Les protocoles de l'époque ne mesurent pas le cerveau ; d'autres lectures, plus tard, discuteront ce que le rat encode vraiment."),
    ("oubli-dirige-bjork", "L'oubli dirigé", "Robert Bjork", "1968", "03-cognitive",
     "On peut consigner un matériel à l'oubli, et ainsi alléger la mémoire de travail de ce qui n'est plus utile.",
     "On présente un premier item verbal, puis la consigne de l'oublier ou de le retenir, puis un second item à rappeler.",
     "La consigne d'oublier réduit l'interférence du premier item sur le second. L'oubli n'est pas seulement une défaillance.",
     "Éclaire la mise à jour de la mémoire : réviser, changer de tâche, laisser tomber une information devenue inutile.",
     "« Oublier sur commande » n'efface pas toujours la trace ; une reconnaissance ultérieure peut encore la retrouver."),
    ("memoire-etat-goodwin", "La mémoire dépendante de l'état", "Donald Goodwin et collègues", "1969", "03-cognitive",
     "Le contexte interne — ici l'alcool — peut servir d'indice pour retrouver ce que l'on a appris.",
     "Des volontaires apprennent sous alcool ou sobres, puis sont testés dans le même état ou dans l'état inverse.",
     "Le rappel est meilleur quand l'état d'apprentissage et l'état de test coïncident.",
     "Montre que la récupération dépend des indices, y compris internes. Ce n'est pas une permission de boire pour réviser.",
     "Effet réel mais modeste, et dangereux à mal raconter : l'alcool détériore d'abord l'encodage."),
    ("metacognition-flavell", "Apprendre à savoir que l'on sait", "John Flavell", "1970-1979", "05-developpement",
     "Les enfants ne naissent pas avec une bonne estimation de leur mémoire : la métacognition se construit.",
     "On demande à des enfants d'étudier jusqu'à être sûrs de pouvoir rappeler, ou d'anticiper combien d'images ils retiendront.",
     "Les plus jeunes surestiment leur rappel et étudient peu. Avec l'âge, l'estimation et les stratégies (répétition, organisation) s'ajustent.",
     "Distingue « avoir une mémoire » et « savoir s'en servir ». Utile pour comprendre les méthodes d'étude, sans juger un élève.",
     "La métacognition ne se résume pas à un score : le contexte de la tâche change beaucoup les jugements."),
    ("amorcage-fragments-tulving", "L'amorçage des fragments de mots", "Endel Tulving, Daniel Schacter & Heather Stark", "1982", "03-cognitive",
     "Une lecture laisse une facilitation durable, même quand on ne reconnaît plus avoir vu le mot.",
     "Les participants voient une liste. Une heure puis sept jours plus tard, ils essaient de reconnaître les mots et de compléter des fragments (par exemple A _ _ A _ IN).",
     "La reconnaissance chute sur la semaine. La facilitation du fragment, elle, reste. Elle est aussi forte pour les mots jugés « nouveaux ».",
     "Argument pour séparer une mémoire épisodique (l'épisode « je l'ai vu ») et une mémoire qui agit sans ce souvenir.",
     "Le fragment graphique n'est pas toute la mémoire implicite. D'autres épreuves (amorçage sémantique, procédures) ne se recouvrent pas entièrement."),
    ("interdependance-wegner", "L'interdépendance cognitive du couple", "Daniel Wegner, Giuliano & Hertel", "1985", "04-sociale",
     "Dans une relation proche, la mémoire est en partie collective : chacun spécialise ce qu'il retient.",
     "On compare la façon dont des couples qui se connaissent bien se répartissent des informations, face à des duos de circonstance.",
     "Les proches se complètent : moins de doublons, plus de savoir « qui sait quoi ». C'est la mémoire transactive.",
     "Explique pourquoi un groupe soudé peut savoir plus que la somme de ses membres — et pourquoi une séparation désorganise des souvenirs pratiques.",
     "Le laboratoire ne capture pas toute une vie de couple. La spécialisation peut aussi créer une dépendance."),
    ("geai-clayton", "Le geai qui se souvient de ses caches", "Nicola Clayton & Anthony Dickinson", "1998", "16-comparee",
     "Un oiseau qui cache de la nourriture peut retrouver quoi, où, et depuis combien de temps.",
     "Des geais buissonniers cachent des vers (périssables) et des cacahuètes (durables) dans des sites distincts. On les laisse chercher après un délai court ou long.",
     "Après un délai court ils cherchent les vers ; après un délai long, quand les vers seraient gâtés, ils vont aux cacahuètes — s'ils ont vu les vers se dégrader.",
     "Mémoire de type épisodique hors de l'espèce humaine : quoi, où, quand. Elle nourrit le débat sur la continuité des mémoires animales.",
     "« De type épisodique » ne veut pas dire que l'oiseau se raconte l'épisode comme un humain. Le critère est comportemental."),
    ("outils-futur-mulcahy", "Le bonobo qui garde un outil", "Nicholas Mulcahy & Josep Call", "2006", "16-comparee",
     "Certains grands singes transportent un outil dont ils n'auront besoin que plus tard.",
     "Un bonobo ou un orang-outan doit choisir un outil, attendre, puis l'utiliser dans une autre pièce pour obtenir une récompense.",
     "Ils sélectionnent et conservent l'outil utile, au-delà de l'attrait immédiat.",
     "Suggère une forme de planification, pas seulement une réaction au présent. À rapprocher des caches du geai.",
     "Les effectifs sont petits. Planifier n'est pas encore voyager mentalement dans le temps comme le décrit Tulving chez l'humain."),
    ("intelligence-culturelle-herrmann", "L'hypothèse de l'intelligence culturelle", "Esther Herrmann et collègues", "2007", "16-comparee",
     "Les enfants humains et les grands singes se ressemblent sur certains problèmes physiques, et divergent sur les problèmes sociaux.",
     "On compare de jeunes enfants, des chimpanzés et des orangs-outans sur des batteries d'espace, de quantités, de causalité, puis de communication, de théorie de l'esprit et d'apprentissage social.",
     "Les performances physiques sont proches. Les enfants distancent les singes sur le social.",
     "Propose que la cognition humaine soit spécialisée pour apprendre des autres, pas seulement pour raisonner sur les objets.",
     "Une batterie ne résume pas une espèce. L'élevage des enfants et celui des singes de sanctuaire ne sont pas équivalents."),
    ("pedagogie-naturelle", "La pédagogie naturelle", "Gergely Csibra & György Gergely", "2009", "05-developpement",
     "La communication humaine serait faite pour transmettre des savoirs généraux, pas seulement des épisodes.",
     "Synthèse théorique : les signaux ostensifs (contact visuel, voix adressée, pointage) préparent le nourrisson à prendre l'information comme valable pour le genre d'objet, pas pour cet exemplaire seulement.",
     "Les bébés généralisent davantage après un enseignement ostensif qu'après une simple observation.",
     "Relie développement, apprentissage culturel et attention. Éclaire pourquoi montrer et nommer n'est pas la même chose que laisser explorer.",
     "C'est un cadre, pas une expérience unique. Tous les savoirs culturels ne passent pas par ce canal."),
    ("effet-google-sparrow", "L'effet Google", "Betsy Sparrow, Jenny Liu & Daniel Wegner", "2011", "22-numerique",
     "Quand on pense qu'une information restera disponible en ligne, on mémorise le chemin d'accès plus que le fait.",
     "On fait apprendre des énoncés, en disant ou non qu'ils seront effacés ou retrouvables sur un ordinateur. On teste ensuite le contenu et l'emplacement.",
     "L'attente d'un accès futur diminue le rappel du contenu et augmente le souvenir de l'endroit où chercher.",
     "La mémoire s'externalise vers les machines, dans la lignée de la mémoire transactive. Ce n'est pas la disparition de toute mémoire.",
     "Les interfaces de 2011 ne sont pas les nôtres. L'effet décrit une stratégie, pas une lésion."),
    ("metamemoire-lockl", "Théorie de l'esprit et métamémoire", "Kathrin Lockl & Wolfgang Schneider", "2007", "05-developpement",
     "Comprendre que les autres ont des croyances aide, plus tard, à comprendre sa propre mémoire.",
     "Suivi longitudinal : des épreuves de théorie de l'esprit chez le jeune enfant, puis des jugements métamnésiques (est-ce que je vais me souvenir ?).",
     "La théorie de l'esprit précoce prédit une partie de la métamémoire ultérieure, au-delà du seul niveau de langage.",
     "Relie deux cours souvent séparés : le social (fausses croyances) et le cognitif (surveiller sa mémoire).",
     "Prédiction n'est pas destin. Beaucoup d'autres facteurs (école, stratégies enseignées) pèsent sur la métamémoire."),
]

# Sections ajoutées aux catégories existantes. Le dossier complet est la page l1-psychologie.html.
L1_EXTRA = {
    "01-fondamentaux": {
        "sections": [
            ("Ce qui rend une psychologie scientifique",
             "<p>Une psychologie de comptoir donne des causes à tout, sans dire comment on pourrait la contredire. "
             "Une psychologie scientifique s'oblige à trois critères : elle est <strong>systématique</strong> "
             "(une procédure organisée, pas une intuition isolée), <strong>précise</strong> "
             "(assez détaillée pour qu'une autre équipe la refasse) et <strong>communicable</strong> "
             "(colloque, article, critique). S'il en manque un, on a quitté la science.</p>"
             "<p>Le modèle <strong>biopsychosocial</strong> (Engel, 1977) rappelle qu'une conduite se tient "
             "au croisement du corps, de l'histoire personnelle et du milieu. Les courants ne s'opposent pas "
             "comme des camps qui auraient « raison » : ils choisissent quoi expliquer, quelles données compter, "
             "et quel type de cause privilégier. La question utile est : que voit cette approche, et que laisse-t-elle dans l'ombre ?</p>"
             "<p>Le cycle d'une recherche enchaîne une observation, des hypothèses "
             "(théorique, puis opérationnelle, puis statistique), une vérification, un traitement des données "
             "et une discussion. La <strong>variable indépendante</strong> est ce que l'on manipule ; "
             "la <strong>variable dépendante</strong> est ce que l'on mesure. La <strong>standardisation</strong> "
             "— mêmes consignes, même matériel, même durée — rend les comparaisons possibles.</p>"
             "<p>Ce cadre a des limites connues : l'éthique (on ne refait pas Milgram pour « voir »), "
             "l'artificialité du laboratoire, la difficulté de généraliser, le fait qu'un comportement a plusieurs causes. "
             "La recherche est aussi une pratique sociale : l'observateur a une histoire et des biais. "
             "Les analyses peuvent être quantitatives ou qualitatives selon la question, pas selon une mode.</p>"
             "<p>Le dossier <a href=\"../l1-psychologie.html\">Psychologie de licence</a> reprend ce cycle, "
             "la clinique, le développement et les lectures cognitives.</p>"),
        ],
        "flashcards": [
            ("Quels sont les trois critères d'une méthode scientifique ?",
             "Systématique, précise (réplicable), communicable et discutable."),
            ("Quelle est la différence entre VI et VD ?",
             "La variable indépendante est manipulée ; la variable dépendante est mesurée."),
        ],
    },
    "09-psychopathologie": {
        "sections": [
            ("La psychologie clinique : une personne, pas une étiquette",
             "<p>La psychologie clinique a pour objet la <strong>subjectivité</strong> : une personne singulière, "
             "ses liens, son histoire infantile et familiale, sa vie affective — du fonctionnement ordinaire "
             "jusqu'à la souffrance. « Du normal au pathologique » veut dire un continuum à comprendre, "
             "pas une case à cocher depuis un article.</p>"
             "<p>La <strong>méthode clinique</strong> vise à saisir cette singularité. Ses outils se répartissent "
             "entre la <strong>clinique à mains nues</strong> (observation, entretien semi-directif ; "
             "Favez-Boutonnier) et la <strong>clinique armée</strong> (tests, médiations ; Lagache). "
             "Aucun des deux ne remplace une formation, un diplôme et le code de déontologie. "
             "En France, le titre de psychologue est protégé. Ce site ne fait pas ce métier.</p>"
             "<p>Les lieux d'exercice sont nombreux : soin, psychiatrie, justice, éducation spécialisée, "
             "petite enfance, prévention, gérontologie, travail social. Un référentiel théorique fréquent "
             "en licence, celui de la métapsychologie, regarde le psychisme sous plusieurs angles : "
             "un appareil (les topiques), des conflits et des défenses, une vie pulsionnelle "
             "(source, poussée, but, objet) réglée par des principes, et une construction au fil du développement. "
             "D'autres modèles existent. Un seul angle, pris seul, appauvrit.</p>"),
        ],
        "flashcards": [
            ("Que distingue la clinique « à mains nues » de la clinique « armée » ?",
             "Observation et entretien, d'un côté ; tests et médiations, de l'autre."),
        ],
    },
    "05-developpement": {
        "sections": [
            ("Tout au long de la vie, à trois vitesses",
             "<p>La psychologie du développement répond à une question : <strong>comment devient-on qui l'on est</strong>, "
             "et qu'est-ce qui demeure malgré le changement. Elle ne s'arrête pas à l'enfance. "
             "Chaque âge a sa forme d'adaptation, pas une montée unique vers un sommet adulte puis une chute.</p>"
             "<p>Trois temporalités s'emboîtent. La <strong>phylogenèse</strong> est celle de l'espèce. "
             "L'<strong>ontogenèse</strong> est celle d'une vie. La <strong>microgenèse</strong> est celle "
             "d'un apprentissage précis (la marche, un mot, une stratégie), sur des jours ou des mois. "
             "Le cours ordinaire porte sur l'ontogenèse, éclairée parfois par les deux autres.</p>"
             "<p>Le mythe de l'enfant sauvage (Victor de l'Aveyron, élevé par Itard) a fait croire qu'un humain "
             "pourrait se construire hors de toute relation. Les observations d'<strong>hospitalisme</strong> "
             "(Spitz) montrent l'inverse : un nourrisson nourri mais privé d'un lien stable se retire et son "
             "développement se grippe. Le soin n'est pas qu'une ration.</p>"),
            ("Comment étudier un bébé qui ne parle pas",
             "<p>On ne fait pas passer un questionnaire à un nourrisson. On lit son regard, sa succion, "
             "son rythme cardiaque, son orientation. Quatre paradigmes reviennent.</p>"
             "<ul>"
             "<li><strong>Préférence visuelle</strong> : il regarde plus longtemps l'un des deux stimuli.</li>"
             "<li><strong>Habituation</strong> : le regard baisse quand la scène se répète ; il remonte si la scène change. Il a discriminé.</li>"
             "<li><strong>Transgression des attentes</strong> : il regarde plus longtemps un événement « impossible » s'il avait une attente.</li>"
             "<li><strong>Conditionnement</strong> : une réponse motrice (succion, tête tournée) est renforcée, puis sert de réponse oui/non.</li>"
             "</ul>"
             "<p>Ces mesures disent une discrimination ou une attente. Elles ne disent pas ce que le bébé « pense » en mots d'adulte.</p>"
             "<p>Deux héritages éthologiques éclairent le début de la vie sociale. L'<strong>empreinte</strong> de Lorenz "
             "et les singes de Harlow (le contact compte plus que le lait) montrent un besoin de lien. "
             "Le couple <strong>CONSPEC / CONLERN</strong> (Johnson et Morton) propose un biais précoce vers "
             "une configuration de visage, puis un apprentissage des visages réels. "
             "La <a href=\"../l1-psychologie.html#lectures\">page des lectures</a> poursuit avec la pédagogie naturelle, "
             "la théorie de l'esprit et la métamémoire.</p>"),
        ],
        "flashcards": [
            ("Quelle est la différence entre ontogenèse et microgenèse ?",
             "L'ontogenèse est le temps d'une vie ; la microgenèse est le temps d'un apprentissage précis."),
            ("À quoi sert l'habituation chez le nourrisson ?",
             "À montrer qu'il distingue un stimulus nouveau d'un stimulus devenu familier, via le regard."),
        ],
    },
    "03-cognitive": {
        "sections": [
            ("Un corpus de lectures : de la carte cognitive à l'effet Google",
             "<p>Un semestre de psychologie cognitive s'appuie souvent sur des articles qui ont changé la question, "
             "pas sur une liste de « lois ». En voici le fil, rédigé ici sans remplacer la lecture.</p>"
             "<ul>"
             "<li><strong>Tolman, 1946.</strong> Le rat qui prend un raccourci a une attente spatiale, pas seulement un virage appris.</li>"
             "<li><strong>Cherry, 1953.</strong> À une fête, on suit une voix et l'on perd l'autre : l'attention sélectionne.</li>"
             "<li><strong>Murdock, 1962.</strong> En rappel libre, le début et la fin d'une liste ressortent (position sérielle).</li>"
             "<li><strong>Bjork, 1968.</strong> Consigne d'oublier : l'oubli peut protéger ce qu'il faut retenir.</li>"
             "<li><strong>Goodwin, 1969.</strong> On retrouve mieux un souvenir dans l'état où on l'a encodé.</li>"
             "<li><strong>Flavell, 1970 et 1979.</strong> Les enfants apprennent à estimer et à conduire leur mémoire.</li>"
             "<li><strong>Tulving, Schacter et Stark, 1982.</strong> L'amorçage d'un fragment survit à l'oubli de l'épisode.</li>"
             "<li><strong>Baron-Cohen, Leslie et Frith, 1985.</strong> La fausse croyance (Sally et Anne) comme épreuve de théorie de l'esprit.</li>"
             "<li><strong>Wegner, 1985.</strong> Dans un couple, la mémoire se répartit.</li>"
             "<li><strong>Clayton et Dickinson, 1998.</strong> Le geai retrouve quoi, où, quand.</li>"
             "<li><strong>Mulcahy et Call, 2006.</strong> Un grand singe garde un outil pour plus tard.</li>"
             "<li><strong>Herrmann et al., 2007.</strong> L'enfant se distingue du singe surtout sur le social.</li>"
             "<li><strong>Lockl et Schneider, 2007.</strong> La théorie de l'esprit précoce annonce une partie de la métamémoire.</li>"
             "<li><strong>Csibra et Gergely, 2009.</strong> Montrer, c'est transmettre un savoir général.</li>"
             "<li><strong>Sparrow, Liu et Wegner, 2011.</strong> On retient où chercher quand le Web garde le fait.</li>"
             "</ul>"
             "<p>Chaque étude est détaillée dans les <a href=\"../references/experiences.html\">expériences</a> "
             "et réunie dans le <a href=\"../l1-psychologie.html\">dossier de licence</a>.</p>"),
        ],
        "flashcards": [
            ("Que reste-t-il quand la reconnaissance a chuté, dans l'étude de Tulving (1982) ?",
             "L'amorçage : on complète mieux un fragment de mot déjà vu, sans le reconnaître."),
            ("Que montre le raccourci de Tolman ?",
             "Un apprentissage spatial de type carte, pas seulement une chaîne de réponses."),
        ],
    },
}
