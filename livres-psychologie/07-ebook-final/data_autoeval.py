# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Auto-évaluations pédagogiques.

Ces questionnaires sont rédigés pour ce site. Ils illustrent la façon dont on
construit une mesure en psychologie — items équilibrés, items inversés, échelle
de Likert, score par dimension — sans reproduire aucun instrument publié et sans
aucune valeur diagnostique. Le but est de faire comprendre la psychométrie de
l'intérieur, pas de classer qui que ce soit.

Format d'une évaluation :
    id, titre, icone, couleur, duree, accroche, intro_html,
    echelle    : liste de libellés du plus bas au plus haut
    items      : liste de (texte, dimension, inverse)
    dimensions : liste de (cle, nom, couleur, description, bas, haut)
    note_html  : mise au point finale affichée sous les résultats
"""

_ECHELLE_ACCORD = [
    "Pas du tout d'accord",
    "Plutôt pas d'accord",
    "Ni d'accord ni pas d'accord",
    "Plutôt d'accord",
    "Tout à fait d'accord",
]

_ECHELLE_FREQ = [
    "Jamais",
    "Rarement",
    "Parfois",
    "Souvent",
    "Presque toujours",
]

EVALUATIONS = [
    # ------------------------------------------------------------------ Big Five
    {
        "id": "cinq-facteurs",
        "titre": "Les cinq grands facteurs",
        "icone": "🧭",
        "couleur": "vert",
        "duree": "5 minutes",
        "accroche": "Le modèle de personnalité le mieux validé, illustré sur vous-même en 25 affirmations.",
        "intro_html":
            "<p>Depuis les années 1980, l'analyse statistique de milliers de descriptions de personnalité "
            "fait émerger cinq dimensions relativement indépendantes, retrouvées dans de très nombreuses "
            "langues. Ce ne sont pas des types : ce sont des axes continus sur lesquels chacun se situe "
            "quelque part, le plus souvent près du milieu.</p>"
            "<p>Vous remarquerez que certains items sont formulés à l'envers. C'est volontaire : un "
            "questionnaire dont tous les items vont dans le même sens mesure autant la tendance à "
            "acquiescer que le trait lui-même.</p>",
        "echelle": _ECHELLE_ACCORD,
        "items": [
            ("J'engage facilement la conversation avec des inconnus.", "extraversion", False),
            ("Après une soirée animée, j'ai besoin de longs moments seul pour récupérer.", "extraversion", True),
            ("On me décrit souvent comme quelqu'un d'énergique.", "extraversion", False),
            ("Je préfère rester en retrait dans un groupe.", "extraversion", True),
            ("J'aime être au centre de l'attention.", "extraversion", False),

            ("Je prends le temps d'écouter quelqu'un qui va mal, même si cela me retarde.", "agreabilite", False),
            ("Je dis ce que je pense même si cela blesse.", "agreabilite", True),
            ("Je pars du principe que les gens sont honnêtes jusqu'à preuve du contraire.", "agreabilite", False),
            ("Dans une négociation, obtenir ce que je veux compte plus que préserver la relation.", "agreabilite", True),
            ("Je rends service sans qu'on me le demande.", "agreabilite", False),

            ("Je termine ce que j'ai commencé, même quand cela devient ennuyeux.", "conscience", False),
            ("Je remets souvent au lendemain des tâches que je pourrais faire tout de suite.", "conscience", True),
            ("Mes affaires et mes fichiers sont rangés d'une manière que je retrouve facilement.", "conscience", False),
            ("Je m'écarte facilement de mon plan quand quelque chose de plus amusant se présente.", "conscience", True),
            ("Je prépare mes rendez-vous importants à l'avance.", "conscience", False),

            ("Je m'inquiète pour des choses qui ont peu de chances d'arriver.", "stabilite", True),
            ("Je reste calme quand la situation dérape.", "stabilite", False),
            ("Une critique, même mesurée, me préoccupe longtemps.", "stabilite", True),
            ("Mon humeur change plusieurs fois dans la même journée.", "stabilite", True),
            ("Je récupère vite après une contrariété.", "stabilite", False),

            ("Les idées abstraites m'intéressent pour elles-mêmes.", "ouverture", False),
            ("Je préfère ce que je connais déjà aux nouveautés.", "ouverture", True),
            ("Je remarque des détails esthétiques que d'autres ne voient pas.", "ouverture", False),
            ("Les discussions philosophiques me paraissent une perte de temps.", "ouverture", True),
            ("J'aime changer mes habitudes juste pour voir ce que ça donne.", "ouverture", False),
        ],
        "dimensions": [
            ("extraversion", "Extraversion", "or",
             "La recherche de stimulation sociale et l'énergie tirée des interactions.",
             "Vous puisez votre énergie dans le calme et les échanges restreints. Ce n'est pas de la timidité : "
             "c'est un seuil de stimulation différent.",
             "Les interactions vous rechargent plutôt qu'elles ne vous vident. L'extraversion prédit la "
             "satisfaction dans les métiers de contact, pas la compétence sociale."),
            ("agreabilite", "Agréabilité", "vert",
             "La tendance à coopérer, à faire confiance et à privilégier l'harmonie.",
             "Vous tranchez et vous exprimez les désaccords. Cette position est associée à de meilleures "
             "négociations salariales et à des conflits plus fréquents.",
             "Vous privilégiez la relation et la coopération. C'est un atout relationnel réel, avec un risque "
             "identifié : accepter trop souvent ce qui vous coûte."),
            ("conscience", "Conscienciosité", "gris",
             "L'organisation, la persévérance et le contrôle des impulsions.",
             "Vous fonctionnez par impulsions et par échéances proches. La souplesse y gagne, la régularité y "
             "perd — et c'est le trait qui se travaille le plus efficacement par l'environnement.",
             "C'est la dimension qui prédit le mieux la réussite scolaire et professionnelle, et même la "
             "longévité. Son revers est la difficulté à lâcher un plan devenu inadapté."),
            ("stabilite", "Stabilité émotionnelle", "rose",
             "L'inverse du névrosisme : la résistance aux émotions négatives et la vitesse de récupération.",
             "Vous réagissez fortement et vous récupérez lentement. C'est la dimension la plus liée au risque "
             "de troubles anxieux et dépressifs — et celle sur laquelle la psychothérapie agit le plus.",
             "Vous encaissez et vous rebondissez vite. Attention à l'angle mort qui accompagne souvent ce "
             "profil : sous-estimer la détresse d'autrui."),
            ("ouverture", "Ouverture à l'expérience", "vert",
             "L'appétit pour la nouveauté, l'abstraction, l'art et les idées.",
             "Vous préférez le concret, l'éprouvé et l'utile. C'est un profil efficace dans les environnements "
             "stables et exigeants en fiabilité.",
             "Vous cherchez la nouveauté et l'abstraction. C'est la dimension la plus liée à la créativité "
             "mesurée, et la moins liée à la réussite scolaire classique."),
        ],
        "note_html":
            "<p>Un score élevé n'est jamais « mieux ». Chaque extrémité a un coût et un bénéfice selon le "
            "contexte, et la plupart des gens se situent dans la zone moyenne, qui est la plus fréquente et "
            "la plus souple.</p>"
            "<p>Ces cinq dimensions sont assez stables à l'âge adulte, mais elles évoluent : la "
            "conscienciosité et l'agréabilité augmentent en moyenne avec l'âge, le névrosisme diminue. "
            "Ce n'est donc pas une signature définitive.</p>"
            "<p><b>Une vérification à faire vous-même.</b> Refaites le questionnaire en répondant « tout à "
            "fait d'accord » partout : vos cinq scores resteront proches de la moyenne au lieu de monter à "
            "100. C'est exactement le rôle des items inversés — ils annulent la tendance à acquiescer. Un "
            "questionnaire qui ne fait pas cela mesure en partie votre docilité.</p>",
    },

    # ------------------------------------------------------------------ Chronotype
    {
        "id": "chronotype",
        "titre": "Votre chronotype",
        "icone": "🌙",
        "couleur": "gris",
        "duree": "2 minutes",
        "accroche": "Êtes-vous du matin ou du soir ? Une préférence réelle, en partie génétique, qu'on ne choisit pas.",
        "intro_html":
            "<p>Le chronotype décrit le décalage de votre horloge interne par rapport à l'horloge sociale. "
            "Il a une composante génétique documentée, varie fortement avec l'âge — il se décale vers le soir "
            "à l'adolescence, vers le matin après cinquante ans — et il ne relève pas de la volonté.</p>"
            "<p>Ce questionnaire porte sur vos préférences les jours où vous êtes entièrement libre de votre "
            "emploi du temps, pas sur ce que vos horaires vous imposent.</p>",
        "echelle": _ECHELLE_ACCORD,
        "items": [
            ("Un jour sans contrainte, je me réveille spontanément tôt.", "matin", False),
            ("Je suis parfaitement opérationnel dans la première heure après mon réveil.", "matin", False),
            ("Je fais mon travail le plus exigeant en fin de soirée.", "matin", True),
            ("Me lever avant sept heures me demande un effort considérable.", "matin", True),
            ("Le week-end, je me couche nettement plus tard qu'en semaine.", "matin", True),
            ("Je me sens fatigué en début de soirée.", "matin", False),
            ("Mes meilleures idées me viennent tard dans la nuit.", "matin", True),
            ("Sans réveil, je dormirais jusqu'en milieu de matinée.", "matin", True),
            ("Un rendez-vous important à huit heures ne me pose aucun problème.", "matin", False),
            ("Je prends mon petit-déjeuner avec appétit dès le réveil.", "matin", False),
        ],
        "dimensions": [
            ("matin", "Tendance matinale", "or",
             "La position de votre horloge interne sur l'axe matin-soir.",
             "Vous êtes plutôt du soir. Votre difficulté n'est généralement pas le sommeil lui-même mais le "
             "décalage entre votre horloge et les horaires imposés — ce qu'on appelle le décalage social. "
             "Les leviers utiles : lumière vive dès le lever, obscurité le soir, et heure de lever constante.",
             "Vous êtes plutôt du matin. Votre performance chute tôt dans la soirée : planifiez les tâches "
             "exigeantes avant midi et méfiez-vous des décisions importantes prises tard."),
        ],
        "note_html":
            "<p>Aucun chronotype n'est supérieur. Les personnes du soir obtiennent des scores légèrement "
            "supérieurs à certains tests cognitifs, les personnes du matin de meilleurs résultats scolaires — "
            "les deux s'expliquent largement par l'heure à laquelle on les mesure et par les horaires "
            "scolaires.</p>"
            "<p>Ce qui améliore réellement le sommeil est indépendant du chronotype : une heure de lever "
            "régulière sept jours sur sept, de la lumière le matin, et un lit réservé au sommeil.</p>",
    },

    # ------------------------------------------------------------------ Méthodes d'étude
    {
        "id": "methodes-etude",
        "titre": "Vos méthodes d'apprentissage",
        "icone": "📚",
        "couleur": "vert",
        "duree": "3 minutes",
        "accroche": "Confrontez vos habitudes de révision à ce que les comparaisons expérimentales ont établi.",
        "intro_html":
            "<p>Ce questionnaire ne mesure pas un trait de personnalité : il compare vos habitudes aux "
            "techniques dont l'efficacité a été comparée directement en laboratoire et en classe. Les deux "
            "premières dimensions rassemblent ce qui fonctionne, la troisième ce qui donne surtout une "
            "impression de travail.</p>"
            "<p>Répondez sur vos habitudes réelles, pas sur vos intentions.</p>",
        "echelle": _ECHELLE_FREQ,
        "items": [
            ("Je ferme mon cours et j'essaie de restituer de mémoire ce que je viens de lire.", "actif", False),
            ("Je me fabrique des questions et j'y réponds sans regarder.", "actif", False),
            ("Je m'entraîne sur des exercices avant d'avoir relu la totalité du chapitre.", "actif", False),
            ("J'explique la notion à voix haute comme si j'enseignais à quelqu'un.", "actif", False),
            ("Je vérifie mes réponses après coup et je note précisément ce que j'ai raté.", "actif", False),

            ("Je reviens sur une notion plusieurs jours après l'avoir apprise.", "espace", False),
            ("Je mélange plusieurs types d'exercices dans une même séance.", "espace", False),
            ("Je révise l'essentiel de la matière la veille de l'examen.", "espace", True),
            ("Je planifie des rappels courts et répétés plutôt qu'une longue session.", "espace", False),
            ("Je travaille un seul chapitre jusqu'à le maîtriser avant de passer au suivant.", "espace", True),

            ("Je relis mes notes plusieurs fois jusqu'à ce qu'elles me paraissent familières.", "passif", False),
            ("Je surligne abondamment en lisant.", "passif", False),
            ("Je recopie mes cours au propre.", "passif", False),
            ("Je considère qu'une notion est acquise dès qu'elle me semble évidente à la lecture.", "passif", False),
            ("Je révise en écoutant le cours en fond pendant que je fais autre chose.", "passif", False),
        ],
        "dimensions": [
            ("actif", "Rappel actif", "vert",
             "Se tester de mémoire plutôt que relire. C'est la technique la plus efficace mesurée.",
             "Vous utilisez peu le rappel actif. C'est le changement qui produit le gain le plus important "
             "par heure investie : commencez par fermer le document et écrire ce dont vous vous souvenez "
             "avant toute relecture.",
             "Vous pratiquez déjà l'essentiel. Le raffinement suivant consiste à espacer les rappels et à "
             "cibler délibérément ce que vous ratez plutôt que ce que vous maîtrisez."),
            ("espace", "Répartition et entrelacement", "or",
             "Répartir les sessions dans le temps et mélanger les types de problèmes.",
             "Votre travail est concentré et cloisonné. Répartir le même temps total sur plusieurs jours "
             "améliore nettement la rétention à long terme, sans travailler davantage.",
             "Vous répartissez bien votre travail. C'est l'habitude qui distingue le plus nettement une "
             "révision efficace d'une révision de dernière minute."),
            ("passif", "Techniques peu rentables", "rose",
             "Relecture, surlignage, recopiage : des méthodes qui donnent une impression de maîtrise.",
             "Vous y avez peu recours : c'est un bon signe. Le piège de ces techniques est la fluidité "
             "trompeuse qu'elles procurent.",
             "Une large part de votre temps va à des techniques peu rentables. Elles ne sont pas nuisibles "
             "en soi, mais elles remplacent du temps de rappel actif — et elles créent le sentiment de "
             "savoir, qui est la principale cause de mauvaise surprise le jour de l'examen."),
        ],
        "note_html":
            "<p>Une découverte contre-intuitive explique la persistance des mauvaises méthodes : les "
            "techniques efficaces donnent, pendant l'apprentissage, une impression de difficulté et "
            "d'inefficacité, alors que la relecture procure une sensation de fluidité. On appelle cela une "
            "difficulté désirable, et il faut accepter de se sentir moins performant sur le moment.</p>",
    },

    # ------------------------------------------------------------------ Régulation émotionnelle
    {
        "id": "regulation-emotionnelle",
        "titre": "Votre régulation émotionnelle",
        "icone": "🌊",
        "couleur": "rose",
        "duree": "3 minutes",
        "accroche": "Deux stratégies très inégales : réévaluer la situation, ou masquer ce qu'on ressent.",
        "intro_html":
            "<p>La recherche distingue deux grandes familles de stratégies. La <em>réévaluation</em> "
            "intervient tôt : on modifie la lecture qu'on fait de la situation avant que l'émotion ne "
            "culmine. La <em>suppression expressive</em> intervient tard : l'émotion est là, on masque son "
            "expression.</p>"
            "<p>Les deux marchent à court terme. Une seule est associée à un meilleur bien-être, à des "
            "relations de meilleure qualité et à un moindre coût attentionnel.</p>",
        "echelle": _ECHELLE_FREQ,
        "items": [
            ("Face à une contrariété, je cherche d'abord une autre lecture possible de la situation.", "reevaluation", False),
            ("Je me demande ce que l'événement changera vraiment dans un mois.", "reevaluation", False),
            ("Quand je suis tendu, je réfléchis à ce qui, précisément, me met en tension.", "reevaluation", False),
            ("Devant une critique, j'essaie d'identifier ce qui est utile dedans.", "reevaluation", False),
            ("Je sais me raconter une situation difficile d'une manière qui la rend supportable.", "reevaluation", False),

            ("Je garde un visage neutre alors que je ressens quelque chose de fort.", "suppression", False),
            ("Je préfère qu'on ne devine pas ce que j'éprouve.", "suppression", False),
            ("Je retiens mes émotions pour ne pas gêner les autres.", "suppression", False),
            ("En réunion, je ne laisse rien paraître même quand je suis contrarié.", "suppression", False),
            ("Je considère que montrer ses émotions est une forme de faiblesse.", "suppression", False),

            ("Quand je vais mal, j'en parle à quelqu'un en qui j'ai confiance.", "soutien", False),
            ("Je demande de l'aide avant d'être complètement débordé.", "soutien", False),
            ("Je sais dire à mes proches ce dont j'ai besoin.", "soutien", False),
            ("Je préfère régler mes difficultés entièrement seul.", "soutien", True),
            ("Après une journée difficile, je cherche la compagnie plutôt que l'isolement.", "soutien", False),
        ],
        "dimensions": [
            ("reevaluation", "Réévaluation cognitive", "vert",
             "Modifier l'interprétation de la situation avant que l'émotion ne s'installe.",
             "Vous utilisez peu cette stratégie. C'est celle qui se travaille le mieux : la question "
             "« quelle autre lecture est possible ? », posée tôt, est le cœur de la thérapie cognitive.",
             "Vous réévaluez spontanément. C'est la stratégie la plus systématiquement associée à un "
             "meilleur bien-être. Sa limite : elle ne doit pas servir à minimiser des situations qui "
             "demandent d'agir plutôt que de reconsidérer."),
            ("suppression", "Suppression expressive", "rose",
             "Masquer l'expression d'une émotion déjà présente.",
             "Vous y avez peu recours, ce qui est plutôt favorable.",
             "Vous masquez souvent ce que vous ressentez. Les études montrent que cela ne réduit pas le "
             "vécu émotionnel, augmente l'activation physiologique, mobilise des ressources attentionnelles "
             "et dégrade la qualité perçue des interactions. L'alternative n'est pas de tout exprimer, "
             "c'est d'intervenir plus tôt sur l'interprétation."),
            ("soutien", "Recours au soutien social", "or",
             "La capacité à s'appuyer sur autrui, qui est un facteur de protection majeur.",
             "Vous affrontez les difficultés seul. C'est possible, mais l'isolement au moment du stress est "
             "l'un des facteurs de risque les mieux documentés pour la santé mentale.",
             "Vous vous appuyez sur votre entourage. La qualité du soutien perçu est l'un des meilleurs "
             "prédicteurs de la récupération après un événement difficile."),
        ],
        "note_html":
            "<p>Aucune stratégie n'est bonne en toutes circonstances. Masquer une émotion pendant dix "
            "minutes pour terminer une réunion est raisonnable ; en faire son mode de fonctionnement "
            "permanent a un coût mesurable. De même, réévaluer une injustice réelle peut servir à ne pas "
            "agir alors qu'il faudrait.</p>",
    },

    # ------------------------------------------------------------------ Procrastination
    {
        "id": "procrastination",
        "titre": "Procrastination et rapport à la tâche",
        "icone": "⏳",
        "couleur": "or",
        "duree": "3 minutes",
        "accroche": "Repérer le mécanisme précis qui vous fait repousser — ils ne se traitent pas de la même façon.",
        "intro_html":
            "<p>La procrastination n'est pas un problème de gestion du temps mais de régulation des "
            "émotions : on repousse la tâche qui déclenche de l'ennui, du doute ou la peur de mal faire, et "
            "le soulagement immédiat renforce l'évitement.</p>"
            "<p>Ce questionnaire distingue trois moteurs distincts, parce qu'ils appellent des réponses "
            "différentes.</p>",
        "echelle": _ECHELLE_FREQ,
        "items": [
            ("Je repousse une tâche parce que je crains de ne pas la réussir assez bien.", "perfection", False),
            ("Je préfère ne pas commencer plutôt que de produire quelque chose de moyen.", "perfection", False),
            ("Je passe un temps excessif sur les détails de la première partie.", "perfection", False),
            ("Je recommence depuis le début parce que ce que j'ai fait ne me convient pas.", "perfection", False),
            ("L'idée d'être jugé sur ce travail m'empêche de m'y mettre.", "perfection", False),

            ("Je repousse les tâches qui m'ennuient, même faciles.", "aversion", False),
            ("Je m'occupe de dix petites choses pour éviter la tâche principale.", "aversion", False),
            ("Je m'y mets seulement quand l'échéance devient menaçante.", "aversion", False),
            ("Je trouve toujours quelque chose de plus urgent à faire.", "aversion", False),
            ("Une tâche longue et sans retour immédiat me décourage d'emblée.", "aversion", False),

            ("Je ne sais pas par quelle étape commencer.", "structure", False),
            ("Mes objectifs sont formulés de façon vague.", "structure", False),
            ("Je n'ai pas de moment fixe dans la semaine pour ce type de travail.", "structure", False),
            ("Je m'installe pour travailler sans avoir décidé ce que je vais faire exactement.", "structure", False),
            ("Mon environnement de travail contient de nombreuses sources de distraction.", "structure", False),
        ],
        "dimensions": [
            ("perfection", "Évitement par crainte de l'échec", "rose",
             "Repousser pour ne pas produire quelque chose d'imparfait, ou pour ne pas être évalué.",
             "Ce mécanisme joue peu chez vous.",
             "C'est votre moteur principal. La parade n'est pas de viser plus haut mais plus bas : "
             "s'autoriser explicitement une première version mauvaise, se fixer un temps maximum plutôt "
             "qu'un niveau de qualité, et séparer le moment de produire de celui de corriger. "
             "L'auto-indulgence après un épisode de procrastination réduit la procrastination suivante."),
            ("aversion", "Fuite de l'inconfort immédiat", "or",
             "Repousser ce qui est ennuyeux ou pénible au profit d'une gratification immédiate.",
             "Ce mécanisme joue peu chez vous.",
             "C'est votre moteur principal. Il répond bien aux techniques qui réduisent le coût d'entrée : "
             "s'engager sur deux minutes seulement, associer la tâche à quelque chose d'agréable, rendre "
             "l'alternative distrayante moins accessible plutôt que compter sur la volonté."),
            ("structure", "Manque de structure", "gris",
             "Repousser parce que la tâche n'est pas découpée, datée ni située.",
             "Vos tâches sont bien structurées.",
             "C'est votre moteur principal, et c'est le plus facile à corriger. Une intention de mise en "
             "œuvre — « quand telle situation se produit, je fais telle action précise » — a un effet "
             "démontré. Découpez jusqu'à obtenir une première action qui tient en une phrase et qui ne "
             "demande aucune décision."),
        ],
        "note_html":
            "<p>Un point souvent négligé : se reprocher d'avoir procrastiné augmente la probabilité de "
            "recommencer, parce que la culpabilité rend la tâche encore plus aversive. Les travaux sur "
            "l'auto-compassion montrent que se pardonner un épisode réduit la procrastination lors de "
            "l'échéance suivante.</p>",
    },
]
