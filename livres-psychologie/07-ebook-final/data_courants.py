# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Les grands courants de la psychologie.

Chaque courant est décrit par : (id, nom, periode, figures, postulat, methode,
apport, critique, heritage). Le texte est rédigé pour être lu d'une traite : on
cherche à faire comprendre *pourquoi* chaque école est née en réaction à la
précédente, plutôt qu'à empiler des étiquettes.
"""

COURANTS = [
    (
        "structuralisme",
        "Le structuralisme",
        "1879-1920",
        "Wilhelm Wundt, Edward Titchener",
        "L'esprit est composé d'éléments simples — sensations, images, sentiments — qui se combinent "
        "comme les atomes d'une molécule. La tâche de la psychologie est d'en dresser le catalogue et "
        "d'établir les lois de leur combinaison.",
        "L'introspection expérimentale : un observateur entraîné pendant des mois décrit, dans un "
        "vocabulaire strictement codifié, le contenu de sa conscience pendant qu'on lui présente un "
        "stimulus calibré. Le laboratoire de Leipzig, ouvert en 1879, mesure surtout des temps de "
        "réaction et des seuils sensoriels.",
        "Le structuralisme invente le laboratoire de psychologie. Avant lui, l'esprit appartenait à la "
        "philosophie ; après lui, il devient un objet qu'on mesure avec un chronoscope. La première "
        "génération de psychologues du monde entier — y compris ses futurs adversaires — s'y est formée.",
        "L'introspection ne permet pas l'arbitrage : quand deux laboratoires bien entraînés rapportent "
        "des contenus de conscience incompatibles, aucune expérience ne peut les départager. On ne peut "
        "pas non plus interroger un bébé, un animal ou une personne délirante. Le programme s'est éteint "
        "faute de pouvoir trancher ses propres désaccords.",
        "L'exigence de mesure, la psychophysique et l'idée qu'un phénomène mental a une durée mesurable "
        "sont restées. La chronométrie mentale de la psychologie cognitive moderne descend en ligne "
        "directe des temps de réaction de Leipzig.",
    ),
    (
        "fonctionnalisme",
        "Le fonctionnalisme",
        "1890-1930",
        "William James, John Dewey, James Angell",
        "La bonne question n'est pas « de quoi la conscience est-elle faite ? » mais « à quoi sert-elle ? ». "
        "L'esprit est un organe façonné par l'évolution pour permettre à l'organisme de s'adapter à un "
        "milieu changeant.",
        "Une méthode délibérément plurielle : introspection, observation naturelle, comparaison entre "
        "espèces, étude des enfants et des personnes atypiques, tout ce qui éclaire la fonction d'un "
        "processus mental.",
        "Le fonctionnalisme ouvre la psychologie à tout ce que le structuralisme excluait : l'animal, "
        "l'enfant, l'habitude, l'émotion, la différence individuelle, l'application pratique. La "
        "psychologie appliquée — scolaire, industrielle, clinique — naît de ce courant.",
        "Sa force est aussi sa faiblesse : en acceptant toutes les méthodes, il n'a jamais produit de "
        "programme de recherche unifié ni de critère clair pour départager deux explications "
        "fonctionnelles rivales.",
        "Il a gagné en disparaissant : sa perspective adaptative imprègne aujourd'hui la psychologie du "
        "développement, la psychologie évolutionniste et les sciences cognitives.",
    ),
    (
        "behaviorisme",
        "Le behaviorisme",
        "1913-1960",
        "John B. Watson, Ivan Pavlov, Edward Thorndike, B. F. Skinner",
        "Une science ne peut porter que sur ce qui est observable publiquement. Or la conscience ne "
        "l'est pas ; le comportement, si. La psychologie doit donc étudier les relations entre les "
        "stimulus du milieu et les réponses de l'organisme, sans postuler ce qui se passe entre les deux.",
        "L'expérimentation contrôlée en laboratoire, souvent sur l'animal, avec manipulation "
        "systématique des conditions et enregistrement objectif des réponses. Skinner ajoute l'analyse "
        "des <em>contingences de renforcement</em> : on modifie ce qui suit le comportement et on observe "
        "l'effet sur sa fréquence.",
        "Le behaviorisme a doté la psychologie d'une méthode reproductible et de lois d'apprentissage "
        "toujours valides : conditionnement classique, renforcement, extinction, généralisation, "
        "programmes de renforcement. Les thérapies comportementales, l'analyse appliquée du comportement "
        "et une part de la pédagogie en sont issues.",
        "En traitant l'organisme comme une boîte noire, il a buté sur le langage : un enfant produit des "
        "phrases qu'il n'a jamais entendues ni été renforcé à produire. La critique de Chomsky en 1959 a "
        "montré qu'un modèle purement associatif ne peut rendre compte de la créativité linguistique.",
        "Ses lois restent exactes dans leur domaine et ses techniques thérapeutiques sont parmi les "
        "mieux validées. Le behaviorisme n'a pas été réfuté : il a été englobé dans un cadre plus large "
        "qui réintroduit les représentations.",
    ),
    (
        "gestalt",
        "La Gestalt",
        "1912-1950",
        "Max Wertheimer, Wolfgang Köhler, Kurt Koffka, Kurt Lewin",
        "Le tout est autre chose que la somme de ses parties. Une mélodie transposée reste la même "
        "mélodie bien qu'aucune note ne soit identique : c'est la structure, la <em>forme</em>, qui est "
        "l'unité psychologique élémentaire, pas la sensation isolée.",
        "L'expérience perceptive rigoureuse, souvent avec des figures ambiguës, des illusions et le "
        "mouvement apparent, complétée par l'observation de la résolution de problèmes chez le singe et "
        "l'humain.",
        "Les lois d'organisation perceptive — proximité, similitude, clôture, continuité, destin commun — "
        "sont vérifiées quotidiennement et fondent aujourd'hui le design d'interface. La Gestalt introduit "
        "aussi l'<em>insight</em>, cette réorganisation soudaine du problème qui contredit l'apprentissage "
        "par essais et erreurs.",
        "Les explications gestaltistes décrivent admirablement les phénomènes mais les expliquent peu : "
        "dire qu'une forme s'impose parce qu'elle est « bonne » ne dit pas quel mécanisme la produit. "
        "L'appel à des champs de forces cérébraux n'a jamais été confirmé.",
        "La psychologie de la perception, l'ergonomie visuelle, le design d'interaction et une partie de "
        "la psychologie sociale (via Lewin et la théorie du champ) reposent sur son héritage.",
    ),
    (
        "psychanalyse",
        "La psychanalyse",
        "1900-aujourd'hui",
        "Sigmund Freud, Carl Jung, Alfred Adler, Mélanie Klein, Jacques Lacan",
        "L'essentiel de la vie mentale est inconscient. Les symptômes, les rêves, les lapsus et les choix "
        "apparemment libres sont les compromis visibles d'un conflit entre des désirs inacceptables et "
        "les exigences de la réalité et de la morale intériorisée.",
        "La cure par la parole : association libre, analyse des rêves, attention portée au transfert. La "
        "preuve est recherchée dans la cohérence de l'interprétation et dans l'évolution du patient, non "
        "dans l'expérimentation contrôlée.",
        "La psychanalyse impose l'idée que le comportement a des causes non conscientes, que l'enfance "
        "façonne l'adulte et qu'écouter longuement un patient est en soi un acte thérapeutique. Elle a "
        "profondément marqué la clinique, la littérature, l'anthropologie et le sens commun.",
        "Ses propositions centrales sont difficiles à mettre en défaut : une interprétation peut "
        "expliquer un fait et son contraire. Les études d'efficacité restent plus rares et plus faibles "
        "que celles des thérapies structurées, et plusieurs constructions théoriques n'ont reçu aucune "
        "confirmation expérimentale.",
        "L'inconscient a été reformulé par la psychologie cognitive sous la forme des traitements "
        "automatiques, non intentionnels et inaccessibles à l'introspection. Les thérapies "
        "psychodynamiques contemporaines, plus brèves et évaluées, prolongent la pratique en la soumettant "
        "à la mesure.",
    ),
    (
        "humanisme",
        "La psychologie humaniste",
        "1950-1980",
        "Carl Rogers, Abraham Maslow, Rollo May",
        "Ni machine à réflexes ni champ de bataille pulsionnel : la personne est un sujet orienté vers la "
        "croissance, capable de choisir, et dont l'expérience subjective est une donnée légitime. On "
        "l'appelle la « troisième force » face au behaviorisme et à la psychanalyse.",
        "L'entretien non directif centré sur la personne, l'étude de l'expérience vécue et l'analyse de "
        "ce qui distingue les personnes qui s'épanouissent plutôt que celles qui souffrent.",
        "Rogers a identifié et mesuré trois attitudes du thérapeute — empathie, congruence, regard "
        "positif inconditionnel — dont l'effet sur l'alliance thérapeutique est aujourd'hui l'un des "
        "résultats les mieux établis de toute la recherche en psychothérapie, quelle que soit l'approche.",
        "Les concepts d'auto-actualisation et de hiérarchie des besoins sont mal définis et peu "
        "testables ; la pyramide de Maslow, notamment, n'a jamais reçu de confirmation empirique sérieuse "
        "de son ordre strict. Le courant a aussi nourri un optimisme sans preuves.",
        "La relation thérapeutique comme facteur actif, l'entretien motivationnel, la psychologie "
        "positive et une grande part de la formation des soignants à l'écoute viennent de là.",
    ),
    (
        "cognitivisme",
        "Le cognitivisme",
        "1956-aujourd'hui",
        "George Miller, Ulric Neisser, Herbert Simon, Noam Chomsky, Donald Broadbent",
        "Entre le stimulus et la réponse, il y a un traitement de l'information : l'esprit code, stocke, "
        "transforme et récupère des représentations, comme un système de calcul dont on peut décrire "
        "l'architecture fonctionnelle.",
        "L'expérimentation chronométrique : on infère les étapes invisibles du traitement à partir des "
        "temps de réaction, des taux d'erreur et des interférences entre tâches. La modélisation "
        "informatique permet ensuite de tester si l'architecture proposée produit bien le comportement "
        "observé.",
        "Le cognitivisme a rendu mesurables des objets qu'on croyait inaccessibles : capacité de la "
        "mémoire de travail, coût du changement de tâche, profondeur de l'encodage, organisation du "
        "lexique mental. Il fournit le vocabulaire commun de la psychologie contemporaine.",
        "La métaphore de l'ordinateur minimise le corps, l'émotion, la culture et le contexte social. "
        "Longtemps, les modèles ont décrit un esprit désincarné résolvant des problèmes en laboratoire, "
        "loin des conditions réelles de la cognition.",
        "Il reste le cadre dominant, élargi par les neurosciences cognitives, la cognition incarnée et "
        "les modèles bayésiens qui décrivent le cerveau comme une machine à prédire plutôt qu'à calculer.",
    ),
    (
        "neurosciences-cognitives",
        "Les neurosciences cognitives",
        "1980-aujourd'hui",
        "Michael Gazzaniga, Brenda Milner, Antonio Damasio, Stanislas Dehaene",
        "Les fonctions mentales sont réalisées par des réseaux cérébraux identifiables ; comprendre "
        "l'esprit suppose d'articuler le niveau psychologique et le niveau biologique plutôt que de les "
        "opposer.",
        "L'imagerie fonctionnelle (IRMf, TEP), l'électrophysiologie (EEG, MEG), la stimulation magnétique "
        "transcrânienne et surtout l'étude des patients cérébrolésés, qui reste la seule méthode "
        "réellement causale chez l'humain.",
        "Elles ont montré que des fonctions qu'on croyait unitaires sont dissociables : on peut perdre la "
        "mémoire des faits en conservant celle des gestes, reconnaître un visage sans éprouver sa "
        "familiarité, décider correctement sans pouvoir justifier son choix.",
        "Le risque du raisonnement inverse : constater qu'une zone s'active ne permet pas d'en déduire "
        "quelle opération mentale a eu lieu. La faiblesse des effectifs et la souplesse des analyses ont "
        "produit une littérature en partie non reproductible, et une image cérébrale reste un argument "
        "rhétoriquement surpuissant.",
        "Ce courant est devenu le socle méthodologique commun de la psychopathologie, de la psychologie "
        "du développement et de la psychologie cognitive.",
    ),
    (
        "constructivisme",
        "Le constructivisme",
        "1920-aujourd'hui",
        "Jean Piaget, Lev Vygotski, Jerome Bruner",
        "La connaissance n'est ni copiée du réel ni innée : elle est construite par le sujet à travers "
        "son activité. L'enfant n'est pas un adulte ignorant mais un penseur cohérent dont la logique "
        "diffère de la nôtre.",
        "L'observation clinique de l'enfant en train de raisonner, avec des situations-problèmes conçues "
        "pour rendre visible sa logique — conservation des quantités, inclusion des classes, permanence "
        "de l'objet. Vygotski y ajoute l'analyse de ce que l'enfant réussit avec l'aide d'autrui.",
        "Le constructivisme a établi que les erreurs des enfants sont informatives et systématiques, et "
        "il a fourni à la pédagogie l'idée que l'on apprend en agissant sur le monde plutôt qu'en "
        "recevant des informations.",
        "Piaget a sous-estimé les compétences précoces du nourrisson : avec des méthodes fondées sur le "
        "regard plutôt que sur l'action manuelle, on observe des acquisitions bien plus tôt que ses "
        "stades ne le prévoient. Le développement est aussi moins uniforme d'un domaine à l'autre.",
        "La pédagogie active, la notion de zone proximale de développement et les didactiques "
        "disciplinaires en découlent directement.",
    ),
    (
        "systemique",
        "L'approche systémique",
        "1950-aujourd'hui",
        "Gregory Bateson, Paul Watzlawick, Salvador Minuchin, Mara Selvini Palazzoli",
        "Un symptôme n'appartient pas à un individu mais à un système de relations. Il remplit une "
        "fonction dans l'équilibre du groupe — souvent la famille — et se maintient par les tentatives "
        "mêmes qu'on fait pour le supprimer.",
        "L'observation de la communication en séance, avec toute la famille présente, et l'intervention "
        "sur les règles implicites du système plutôt que sur le psychisme d'un membre.",
        "Elle a introduit deux idées durables : on ne peut pas ne pas communiquer, et la « solution » "
        "répétée est souvent devenue le problème. Elle a aussi déplacé la culpabilité de l'individu "
        "désigné vers l'organisation collective.",
        "Certaines hypothèses fortes des débuts, comme l'idée qu'une communication familiale "
        "contradictoire provoquerait la schizophrénie, se sont révélées fausses et ont longtemps "
        "culpabilisé les familles.",
        "La thérapie familiale, la médiation, l'analyse des organisations et une partie du travail social "
        "raisonnent aujourd'hui en termes systémiques.",
    ),
    (
        "tcc",
        "Les thérapies cognitivo-comportementales",
        "1960-aujourd'hui",
        "Aaron Beck, Albert Ellis, Marsha Linehan, Steven Hayes",
        "Ce n'est pas l'événement qui détermine l'émotion, mais l'interprétation qu'on en fait. Modifier "
        "les pensées automatiques et les comportements d'évitement qui entretiennent le trouble modifie "
        "la souffrance.",
        "Un protocole structuré, limité dans le temps, avec objectifs mesurables, exercices entre les "
        "séances, exposition graduée et évaluation chiffrée avant/après. L'efficacité est testée par "
        "essais contrôlés randomisés.",
        "Les TCC constituent le corpus thérapeutique le mieux évalué : efficacité solide sur les troubles "
        "anxieux, la dépression, les troubles obsessionnels compulsionnels et l'insomnie, avec des tailles "
        "d'effet reproduites dans de nombreux pays.",
        "Leur format standardisé se prête mal aux situations complexes et intriquées, et leur évaluation "
        "privilégie ce qui se mesure facilement sur quelques mois. La question du maintien à long terme "
        "reste en partie ouverte.",
        "La troisième vague — pleine conscience, thérapie d'acceptation et d'engagement, thérapie "
        "comportementale dialectique — élargit le modèle en travaillant le rapport aux pensées plutôt que "
        "leur contenu.",
    ),
    (
        "evolutionniste",
        "La psychologie évolutionniste",
        "1990-aujourd'hui",
        "Leda Cosmides, John Tooby, David Buss",
        "Le cerveau humain a été façonné par la sélection naturelle pour résoudre les problèmes récurrents "
        "de nos ancêtres : trouver de la nourriture, éviter les prédateurs, coopérer, choisir un "
        "partenaire. Nos biais actuels sont souvent d'anciennes solutions devenues inadaptées.",
        "La méthode comparative entre espèces et entre cultures, la recherche d'universaux, et la "
        "dérivation d'hypothèses précises à partir d'un raisonnement adaptatif, ensuite testées "
        "expérimentalement.",
        "Elle explique pourquoi certains apprentissages sont plus faciles que d'autres — on apprend à "
        "craindre un serpent en un essai, une prise électrique jamais — et pourquoi certains "
        "raisonnements deviennent soudain faciles quand on les reformule en termes de tricherie sociale.",
        "Le risque du récit rétrospectif : il est toujours possible d'inventer une histoire adaptative "
        "plausible après coup. Les hypothèses vraiment réfutables sont plus rares que les explications "
        "séduisantes, et le contexte ancestral reste largement reconstruit.",
        "Elle a durablement enrichi l'étude des émotions, de la coopération, du dégoût, de la peur et des "
        "relations, en fournissant une raison fonctionnelle à des mécanismes qu'on décrivait sans les "
        "expliquer.",
    ),
    (
        "culturelle",
        "La psychologie culturelle",
        "1990-aujourd'hui",
        "Richard Shweder, Hazel Markus, Shinobu Kitayama, Richard Nisbett",
        "L'esprit et la culture se constituent mutuellement. Il n'existe pas de psychologie humaine "
        "générale qu'on pourrait établir en étudiant des étudiants occidentaux : les processus eux-mêmes "
        "varient avec le monde social qui les façonne.",
        "La comparaison expérimentale systématique entre populations, l'analyse des pratiques "
        "quotidiennes et l'étude des personnes biculturelles qu'on peut amorcer alternativement dans "
        "l'un ou l'autre cadre.",
        "Elle a montré que des résultats tenus pour universels — le biais d'attribution, la préférence "
        "pour la distinctivité, la façon même de regarder une scène — varient fortement selon les "
        "sociétés, et que les échantillons occidentaux, éduqués, industrialisés, riches et démocratiques "
        "sont des cas particuliers.",
        "Le risque est d'essentialiser les cultures en deux blocs opposés, alors que la variation "
        "intérieure à chaque société est souvent plus grande que la différence entre sociétés.",
        "Toute revendication d'universalité en psychologie doit désormais préciser sur quelles "
        "populations elle repose : c'est un acquis méthodologique définitif.",
    ),
    (
        "positive",
        "La psychologie positive",
        "1998-aujourd'hui",
        "Martin Seligman, Mihály Csíkszentmihályi, Barbara Fredrickson",
        "La psychologie a passé un siècle à étudier la souffrance et presque rien à comprendre ce qui "
        "rend une vie bonne. Le bien-être, les forces de caractère et l'engagement méritent le même "
        "traitement scientifique que les troubles.",
        "Les échelles de bien-être validées, les études longitudinales sur de grandes cohortes et les "
        "essais contrôlés d'interventions brèves comme l'expression de la gratitude ou l'usage délibéré "
        "de ses forces.",
        "Elle a rendu mesurables des objets jusque-là abandonnés à l'essai philosophique, et montré que "
        "certaines interventions simples produisent des effets réels, quoique modestes, sur l'humeur et "
        "la satisfaction de vie.",
        "Plusieurs résultats spectaculaires des débuts, dont le fameux ratio d'émotions positives, se "
        "sont effondrés à l'examen. Le courant s'expose aussi à un usage idéologique qui rend l'individu "
        "responsable de son bonheur en ignorant ses conditions matérielles.",
        "Une version assagie subsiste : des interventions modestes mais reproductibles, et une attention "
        "renouvelée aux ressources plutôt qu'aux seuls déficits, y compris en clinique.",
    ),
]
