# -*- coding: utf-8 -*-
"""Données complètes des 17 catégories de la Psyclopédie."""

IMG = "../../05-larousse-illustre-complet/illustrations/wikimedia"
PDF = "../../06-pdf-domaine-public"

CATEGORIES = [
    {
        "id": "01-fondamentaux",
        "icon": "🧩", "color": "vert", "num": "01",
        "title": "Fondamentaux & Méthodes",
        "subtitle": "Qu'est-ce que la psychologie et comment la étudie-t-on ?",
        "read_time": "12 min",
        "objectives": [
            "Définir la psychologie et distinguer ses grandes branches",
            "Comprendre les méthodes scientifiques utilisées (expérimentation, observation, étude de cas)",
            "Connaître les règles éthiques de la recherche en psychologie",
            "Identifier les 6 grandes écoles de pensée qui structurent la discipline",
        ],
        "sections": [
            ("Qu'est-ce que la psychologie ?",
             "<p>La psychologie est la <strong>science du comportement et des processus mentaux</strong>. "
             "Elle étudie comment les êtres humains (et parfois les animaux) perçoivent, pensent, ressentent, "
             "apprennent et agissent, seuls ou en interaction avec les autres.</p>"
             "<p>Contrairement à une idée reçue, la psychologie n'est pas qu'une discipline d'introspection : "
             "c'est une <strong>science empirique</strong> qui formule des hypothèses, les teste par l'expérimentation "
             "et les remet en question à la lumière des résultats.</p>"),
            ("Les grandes branches de la psychologie",
             "<p>La psychologie se divise en de nombreuses spécialités, que ce guide explore une à une : "
             "cognitive, sociale, du développement, clinique, biologique, du travail, positive… "
             "Chacune apporte un éclairage complémentaire sur l'esprit humain.</p>"
             "<ul><li><strong>Recherche fondamentale</strong> : comprendre les mécanismes (mémoire, perception…)</li>"
             "<li><strong>Psychologie appliquée</strong> : intervenir concrètement (clinique, travail, éducation…)</li></ul>"),
            ("Les méthodes scientifiques",
             "<p>Pour étudier l'esprit humain de façon rigoureuse, les psychologues utilisent plusieurs outils :</p>"
             "<ul><li><strong>L'expérimentation</strong> : manipuler une variable pour observer son effet (méthode reine pour établir la causalité)</li>"
             "<li><strong>L'observation</strong> : décrire un comportement dans son contexte naturel, sans intervenir</li>"
             "<li><strong>L'étude de cas</strong> : analyse approfondie d'un individu ou d'un groupe (ex. patients avec lésions cérébrales)</li>"
             "<li><strong>L'enquête et le questionnaire</strong> : recueillir des données déclaratives sur de grands échantillons</li>"
             "<li><strong>La neuroimagerie</strong> : observer l'activité cérébrale (IRMf, EEG) pendant une tâche</li></ul>"),
            ("Éthique de la recherche",
             "<p>Depuis les dérives de certaines expériences historiques (obéissance de Milgram, prison de Stanford), "
             "la recherche en psychologie est encadrée par des principes stricts :</p>"
             "<ul><li><strong>Consentement éclairé</strong> : le participant sait à quoi il s'engage</li>"
             "<li><strong>Droit de retrait</strong> : il peut arrêter à tout moment</li>"
             "<li><strong>Confidentialité</strong> des données recueillies</li>"
             "<li><strong>Débriefing</strong> : expliquer l'expérience après coup, en cas de déception nécessaire</li>"
             "<li><strong>Balance bénéfice/risque</strong> validée par un comité d'éthique</li></ul>"),
            ("Les 6 grandes écoles de pensée",
             "<p>Chaque courant a proposé une manière différente de comprendre l'esprit :</p>"
             "<ul><li><strong>Structuralisme</strong> (Wundt, 1879) : décomposer la conscience en éléments de base par introspection</li>"
             "<li><strong>Fonctionnalisme</strong> (James, 1890) : comprendre à quoi « sert » chaque fonction mentale pour l'adaptation</li>"
             "<li><strong>Psychanalyse</strong> (Freud, 1900) : l'inconscient et les conflits internes guident le comportement</li>"
             "<li><strong>Behaviorisme</strong> (Watson, Skinner) : seul le comportement observable est étudié scientifiquement</li>"
             "<li><strong>Cognitivisme</strong> (années 1960) : l'esprit traite l'information comme un ordinateur</li>"
             "<li><strong>Humanisme</strong> (Rogers, Maslow) : l'humain a un potentiel de croissance et d'épanouissement</li></ul>"),
        ],
        "figures": ["portrait-wundt.jpg:Wilhelm Wundt", "portrait-james.jpg:William James"],
        "pdfs": [
            {"title": "Précis de psychologie", "author": "William James (1909)", "path": f"{PDF}/psychologie-generale/james-precis-de-psychologie-1909.pdf",
             "desc": "L'ouvrage fondateur du fonctionnalisme, traduit en français : une porte d'entrée complète vers la discipline."},
        ],
        "fun_fact": "Le mot « psychologie » vient du grec ancien <em>psukhê</em> (âme, esprit) et <em>logos</em> (étude, discours) — littéralement « l'étude de l'âme ».",
        "flashcards": [
            ("Que signifie « psychologie » étymologiquement ?", "Étude (logos) de l'âme/l'esprit (psukhê), du grec ancien."),
            ("Quelle est la méthode la plus fiable pour établir une causalité ?", "L'expérimentation, car elle permet de manipuler une variable et d'isoler son effet."),
            ("Qui a fondé le premier laboratoire de psychologie expérimentale ?", "Wilhelm Wundt, à Leipzig en 1879."),
            ("Quel principe éthique garantit qu'un participant peut arrêter une étude ?", "Le droit de retrait."),
            ("Quelle école pense que l'esprit fonctionne comme un ordinateur ?", "Le cognitivisme."),
        ],
    },
    {
        "id": "02-histoire",
        "icon": "📜", "color": "gris", "num": "02",
        "title": "Histoire & Grands Courants",
        "subtitle": "De la philosophie antique à la science moderne de l'esprit",
        "read_time": "14 min",
        "objectives": [
            "Retracer les grandes étapes historiques de la psychologie",
            "Comprendre le passage de la philosophie à la science expérimentale",
            "Situer les figures majeures dans leur contexte historique",
            "Percevoir les ruptures et continuités entre les courants",
        ],
        "sections": [
            ("Avant la science : les racines philosophiques",
             "<p>Bien avant d'être une science, la psychologie était une branche de la <strong>philosophie</strong>. "
             "Platon et Aristote s'interrogeaient déjà sur l'âme (psukhê), la perception et la mémoire. "
             "Descartes (XVIIe siècle) pose le dualisme corps-esprit qui influencera des siècles de débat.</p>"),
            ("1879 : la naissance de la psychologie scientifique",
             "<p><strong>Wilhelm Wundt</strong> fonde à Leipzig le premier laboratoire consacré exclusivement à "
             "l'étude expérimentale de l'esprit. Il mesure les temps de réaction, étudie la perception sensorielle : "
             "la psychologie devient une science à part entière, séparée de la philosophie.</p>"),
            ("La psychologie française : Ribot, Binet, Janet",
             "<p>En France, une tradition clinique et expérimentale se développe en parallèle :</p>"
             "<ul><li><strong>Théodule Ribot</strong> (1839-1916) étudie les « maladies » de la mémoire, de la volonté et "
             "de la personnalité — une approche par la pathologie pour comprendre le normal</li>"
             "<li><strong>Alfred Binet</strong> (1857-1911) invente le premier test d'intelligence utilisable (1905) "
             "et explore la suggestibilité</li>"
             "<li><strong>Pierre Janet</strong> (1859-1947) développe des concepts clés sur les névroses et "
             "l'automatisme psychologique, précurseur de la psychotraumatologie</li></ul>"),
            ("1900 : la révolution de l'inconscient",
             "<p><strong>Sigmund Freud</strong> publie <em>L'interprétation des rêves</em> et fonde la psychanalyse : "
             "l'essentiel de notre psychisme serait inconscient, gouverné par des pulsions et des conflits refoulés "
             "depuis l'enfance. Cette théorie, très controversée scientifiquement, aura une influence culturelle immense.</p>"),
            ("1913-1950 : la révolution behavioriste",
             "<p><strong>John Watson</strong> puis <strong>B.F. Skinner</strong> rejettent l'introspection : "
             "seul le comportement observable et mesurable doit être étudié. Le conditionnement (Pavlov, Skinner) "
             "devient le paradigme dominant pendant 40 ans dans le monde anglo-saxon.</p>"),
            ("1956 : la révolution cognitive",
             "<p>Avec l'essor de l'informatique, les chercheurs (Miller, Neisser) reviennent à l'étude des "
             "processus mentaux internes — mais avec une rigueur scientifique nouvelle, en modélisant l'esprit "
             "comme un système de traitement de l'information. Les neurosciences viendront ensuite ancrer ces "
             "modèles dans le cerveau biologique.</p>"),
        ],
        "figures": ["portrait-wundt.jpg:Wilhelm Wundt", "portrait-ribot.jpg:Théodule Ribot",
                    "portrait-binet.jpg:Alfred Binet", "portrait-janet.jpg:Pierre Janet",
                    "portrait-freud.jpg:Sigmund Freud", "portrait-pavlov.jpg:Ivan Pavlov",
                    "portrait-thorndike.jpg:Edward Thorndike"],
        "pdfs": [
            {"title": "De l'intelligence", "author": "Hippolyte Taine (1870)", "path": f"{PDF}/histoire-psychologie/taine-de-lintelligence-1870.pdf",
             "desc": "Une somme philosophique et psychologique majeure du XIXe siècle sur la connaissance et l'intelligence humaine (512 pages)."},
        ],
        "fun_fact": "Wilhelm Wundt a formé plus de 180 doctorants venus du monde entier — beaucoup sont ensuite rentrés fonder leur propre laboratoire, essaimant la discipline sur tous les continents.",
        "flashcards": [
            ("En quelle année Wundt fonde-t-il son laboratoire ?", "1879, à Leipzig."),
            ("Qui a inventé le premier test d'intelligence utilisable ?", "Alfred Binet, en 1905."),
            ("Quel livre de Freud marque la naissance de la psychanalyse ?", "L'interprétation des rêves (1900)."),
            ("Quel courant a dominé la psychologie anglo-saxonne de 1913 à 1950 ?", "Le behaviorisme."),
            ("Qu'est-ce qui a déclenché la révolution cognitive des années 1950 ?", "L'essor de l'informatique et la modélisation de l'esprit comme système de traitement de l'information."),
        ],
    },
    {
        "id": "03-cognitive",
        "icon": "💭", "color": "vert", "num": "03",
        "title": "Psychologie Cognitive",
        "subtitle": "Comment le cerveau perçoit, mémorise et raisonne",
        "read_time": "15 min",
        "objectives": [
            "Comprendre les grands systèmes de mémoire",
            "Expliquer pourquoi notre perception peut nous tromper",
            "Identifier les principaux biais cognitifs et heuristiques",
            "Comprendre les limites de l'attention humaine",
        ],
        "sections": [
            ("La perception : une construction active",
             "<p>Voir, entendre ou toucher n'est pas un enregistrement passif du monde : c'est une "
             "<strong>construction active</strong> du cerveau à partir d'indices incomplets. Les illusions "
             "visuelles (vase de Rubin, illusion de Müller-Lyer) démontrent que percevoir ≠ enregistrer fidèlement.</p>"
             "<div class='learn-tip-box'><span class='emoji'>👁️</span><p><strong>Pour les apprenants visuels</strong> : "
             "recherchez des illusions d'optique en ligne et observez comment votre cerveau « complète » l'image.</p></div>"),
            ("Les systèmes de mémoire",
             "<p>La mémoire n'est pas un bloc unique mais un ensemble de systèmes coordonnés :</p>"
             "<table style='width:100%;border-collapse:collapse;margin:1rem 0;font-size:0.9rem'>"
             "<tr style='background:var(--gris-light)'><th style='padding:0.5rem;text-align:left'>Système</th><th style='padding:0.5rem;text-align:left'>Durée</th><th style='padding:0.5rem;text-align:left'>Exemple</th></tr>"
             "<tr><td style='padding:0.5rem;border-bottom:1px solid var(--border)'>Sensorielle</td><td style='padding:0.5rem;border-bottom:1px solid var(--border)'>&lt; 1 sec</td><td style='padding:0.5rem;border-bottom:1px solid var(--border)'>Persistance rétinienne</td></tr>"
             "<tr><td style='padding:0.5rem;border-bottom:1px solid var(--border)'>Court terme</td><td style='padding:0.5rem;border-bottom:1px solid var(--border)'>15-30 sec</td><td style='padding:0.5rem;border-bottom:1px solid var(--border)'>Retenir un numéro</td></tr>"
             "<tr><td style='padding:0.5rem;border-bottom:1px solid var(--border)'>Travail</td><td style='padding:0.5rem;border-bottom:1px solid var(--border)'>Active</td><td style='padding:0.5rem;border-bottom:1px solid var(--border)'>Calcul mental</td></tr>"
             "<tr><td style='padding:0.5rem'>Long terme</td><td style='padding:0.5rem'>Illimitée</td><td style='padding:0.5rem'>Souvenirs d'enfance</td></tr></table>"
             "<p>Miller (1956) a montré que la mémoire à court terme retient environ <strong>7 ± 2 éléments</strong> — "
             "d'où l'usage des numéros de téléphone découpés en petits groupes.</p>"),
            ("Une mémoire reconstructive, pas une vidéo",
             "<p>Les travaux d'<strong>Elizabeth Loftus</strong> montrent que la mémoire est <strong>suggestible</strong> : "
             "une information reçue après un événement peut modifier le souvenir original (« effet de désinformation »). "
             "Cela a des conséquences majeures pour la fiabilité des témoignages judiciaires.</p>"),
            ("Attention sélective et charge cognitive",
             "<p>Notre attention est une ressource limitée. L'expérience du <strong>« gorille invisible »</strong> "
             "(Simons & Chabris, 1999) montre que des observateurs concentrés sur une tâche ne remarquent pas "
             "un événement inattendu pourtant très visible, se déroulant sous leurs yeux.</p>"),
            ("Biais cognitifs et heuristiques",
             "<p>Pour décider vite, le cerveau utilise des raccourcis mentaux (heuristiques) — utiles, mais "
             "sources d'erreurs systématiques :</p>"
             "<ul><li><strong>Heuristique de disponibilité</strong> : juger la fréquence d'un événement par la facilité "
             "à s'en souvenir (peur de l'avion vs. de la voiture)</li>"
             "<li><strong>Biais de confirmation</strong> : privilégier les informations qui confirment nos croyances</li>"
             "<li><strong>Effet d'ancrage</strong> : la première information reçue influence tout le jugement suivant</li>"
             "<li><strong>Biais rétrospectif</strong> : croire, après coup, qu'un événement était prévisible</li></ul>"),
        ],
        "figures": ["portrait-binet.jpg:Alfred Binet", "portrait-james.jpg:William James"],
        "pdfs": [
            {"title": "La Suggestibilité", "author": "Alfred Binet", "path": f"{PDF}/psychologie-generale/binet-suggestibilite.html",
             "desc": "L'étude fondatrice sur la manière dont nos souvenirs et jugements peuvent être influencés — base des travaux modernes sur la mémoire."},
        ],
        "fun_fact": "Dans l'expérience du gorille invisible, environ <strong>50 % des observateurs</strong> ne remarquent pas une personne déguisée en gorille traversant l'écran, tant leur attention est absorbée par le comptage des passes de basket.",
        "flashcards": [
            ("Combien d'éléments la mémoire à court terme retient-elle en moyenne ?", "7 ± 2 éléments (loi de Miller, 1956)."),
            ("Qu'a démontré Elizabeth Loftus sur la mémoire ?", "Qu'elle est reconstructive et suggestible : elle peut être altérée par une information reçue après les faits."),
            ("Qu'est-ce que l'heuristique de disponibilité ?", "Juger la probabilité d'un événement selon la facilité avec laquelle des exemples nous viennent à l'esprit."),
            ("Que montre l'expérience du gorille invisible ?", "Que l'attention sélective nous rend « aveugles » à des événements inattendus, même très visibles."),
            ("Qu'est-ce que l'effet d'ancrage ?", "Le fait que la première information reçue influence disproportionnellement notre jugement final."),
        ],
    },
    {
        "id": "04-sociale",
        "icon": "👥", "color": "or", "num": "04",
        "title": "Psychologie Sociale",
        "subtitle": "Comment le groupe transforme la pensée et l'action",
        "read_time": "14 min",
        "objectives": [
            "Comprendre les mécanismes de conformité et d'obéissance",
            "Expliquer l'effet du témoin et la diffusion de responsabilité",
            "Analyser le fonctionnement des foules et de l'influence de masse",
            "Distinguer préjugé, stéréotype et discrimination",
        ],
        "sections": [
            ("La psychologie des foules selon Le Bon",
             "<p><strong>Gustave Le Bon</strong> publie en 1895 <em>Psychologie des foules</em>, l'un des premiers "
             "textes majeurs de psychologie sociale. Sa thèse : dans une foule, l'individu perd son sens critique "
             "et sa responsabilité individuelle au profit d'une « âme collective » émotionnelle et contagieuse.</p>"
             "<p>Cette analyse, bien que datée et critiquée pour son manque de rigueur empirique, a profondément "
             "influencé la réflexion sur la propagande et les mouvements de masse au XXe siècle — <strong>à lire "
             "avec esprit critique</strong>.</p>"),
            ("Conformité : l'expérience d'Asch",
             "<p><strong>Solomon Asch</strong> (1951) demande à des participants de comparer des lignes, en "
             "présence de complices donnant délibérément une réponse fausse. Résultat : <strong>75 % des "
             "participants</strong> se sont conformés au moins une fois à la réponse erronée du groupe — même "
             "quand elle contredisait leurs propres yeux.</p>"),
            ("Obéissance : l'expérience de Milgram",
             "<p><strong>Stanley Milgram</strong> (1963) étudie jusqu'où des personnes ordinaires obéissent à "
             "une autorité légitime, même quand cela implique de faire du mal à autrui. Résultat frappant : "
             "<strong>65 % des participants</strong> ont administré ce qu'ils croyaient être des chocs électriques "
             "potentiellement mortels, simplement parce qu'un expérimentateur en blouse blanche le leur demandait.</p>"),
            ("L'effet du témoin",
             "<p>Suite au meurtre de Kitty Genovese (1964, New York), Darley et Latané étudient pourquoi de "
             "nombreux témoins n'interviennent pas en cas d'urgence. Explication : la <strong>diffusion de "
             "responsabilité</strong> — plus il y a de témoins, moins chacun se sent individuellement responsable "
             "d'agir.</p>"),
            ("Le suicide comme fait social (Durkheim)",
             "<p><strong>Émile Durkheim</strong> (1897) démontre dans <em>Le Suicide</em> que même l'acte le plus "
             "intime obéit à des <strong>régularités sociales</strong>. Il distingue le suicide égoïste (manque "
             "d'intégration sociale), altruiste (excès d'intégration), anomique (dérégulation sociale) et fataliste. "
             "Ce travail fonde la sociologie moderne tout en éclairant la psychologie sociale du désespoir.</p>"),
            ("Stéréotypes, préjugés et discrimination",
             "<p>Trois notions à ne pas confondre :</p>"
             "<ul><li><strong>Stéréotype</strong> : croyance généralisée (souvent fausse) sur un groupe</li>"
             "<li><strong>Préjugé</strong> : attitude négative (émotionnelle) envers un groupe</li>"
             "<li><strong>Discrimination</strong> : comportement défavorable envers un groupe</li></ul>"
             "<p>La <strong>théorie de l'identité sociale</strong> (Tajfel, 1979) explique que nous favorisons "
             "automatiquement notre groupe (endogroupe) au détriment des autres (exogroupe), même pour des "
             "catégorisations arbitraires.</p>"),
        ],
        "figures": ["portrait-le-bon.jpg:Gustave Le Bon", "portrait-durkheim.jpg:Émile Durkheim"],
        "pdfs": [
            {"title": "Psychologie des foules", "author": "Gustave Le Bon (1895)", "path": f"{PDF}/psychologie-sociale/le-bon-psychologie-des-foules-1895-complet.pdf",
             "desc": "L'ouvrage fondateur — 204 pages — sur la psychologie des mouvements de masse et de l'influence collective."},
            {"title": "Le Suicide : étude de sociologie", "author": "Émile Durkheim (1897)", "path": f"{PDF}/psychologie-sociale/durkheim-le-suicide-1897.pdf",
             "desc": "L'étude classique démontrant l'influence des structures sociales sur les comportements les plus individuels."},
        ],
        "fun_fact": "Dans l'expérience de Milgram, avant l'étude, des psychiatres avaient prédit que moins de 1 % des participants iraient jusqu'au bout — la réalité (65 %) a stupéfié la communauté scientifique.",
        "flashcards": [
            ("Que démontre l'expérience d'Asch ?", "Que la pression du groupe peut nous faire donner une réponse fausse que l'on sait pourtant erronée (conformité)."),
            ("Quel pourcentage de participants a obéi jusqu'au bout dans l'expérience de Milgram ?", "65 %."),
            ("Qu'est-ce que la diffusion de responsabilité ?", "Le phénomène par lequel plus il y a de témoins à une urgence, moins chacun se sent responsable d'intervenir."),
            ("Quels sont les 4 types de suicide selon Durkheim ?", "Égoïste, altruiste, anomique et fataliste."),
            ("Quelle est la différence entre préjugé et discrimination ?", "Le préjugé est une attitude (émotion négative), la discrimination est un comportement (action défavorable)."),
        ],
    },
    {
        "id": "05-developpement",
        "icon": "🌱", "color": "vert", "num": "05",
        "title": "Psychologie du Développement",
        "subtitle": "De la petite enfance au grand âge : une vie de transformations",
        "read_time": "13 min",
        "objectives": [
            "Décrire les 4 stades du développement cognitif de Piaget",
            "Comprendre les styles d'attachement et leurs conséquences",
            "Expliquer les 8 stades psychosociaux d'Erikson",
            "Situer la théorie de l'esprit dans le développement social de l'enfant",
        ],
        "sections": [
            ("Les stades de Piaget",
             "<p><strong>Jean Piaget</strong> décrit 4 grandes étapes du développement cognitif de l'enfant, "
             "chacune restructurant sa compréhension du monde :</p>"
             "<ul><li><strong>Sensorimoteur</strong> (0-2 ans) : découverte du monde par les sens et l'action ; "
             "acquisition de la « permanence de l'objet »</li>"
             "<li><strong>Préopératoire</strong> (2-7 ans) : pensée symbolique (jeu de « faire semblant ») mais "
             "encore égocentrique</li>"
             "<li><strong>Opératoire concret</strong> (7-11 ans) : logique sur des objets concrets, maîtrise de "
             "la conservation (quantité, volume)</li>"
             "<li><strong>Opératoire formel</strong> (11 ans et +) : raisonnement abstrait et hypothétique</li></ul>"),
            ("L'attachement : un besoin fondamental",
             "<p><strong>John Bowlby</strong> et <strong>Mary Ainsworth</strong> montrent que le lien affectif "
             "précoce avec la figure de soin façonne la sécurité relationnelle future. La « situation étrange » "
             "d'Ainsworth identifie 4 styles d'attachement :</p>"
             "<ul><li><strong>Sûr</strong> (~65 %) : explore avec confiance, se rassure vite au retour du parent</li>"
             "<li><strong>Anxieux-ambivalent</strong> : détresse intense, difficile à apaiser</li>"
             "<li><strong>Évitant</strong> : semble indifférent, évite le contact émotionnel</li>"
             "<li><strong>Désorganisé</strong> : comportements contradictoires, souvent lié à un contexte de soin imprévisible</li></ul>"),
            ("Les 8 âges de la vie selon Erikson",
             "<p><strong>Erik Erikson</strong> étend le développement à toute la vie, en 8 crises psychosociales : "
             "confiance vs méfiance (nourrisson), autonomie vs honte (2-3 ans), initiative vs culpabilité "
             "(3-6 ans), compétence vs infériorité (6-12 ans), <strong>identité vs confusion</strong> (adolescence), "
             "intimité vs isolement (jeune adulte), générativité vs stagnation (âge mûr), intégrité vs désespoir "
             "(vieillesse).</p>"),
            ("La théorie de l'esprit",
             "<p>Vers 4 ans, l'enfant acquiert la capacité à comprendre que <strong>les autres ont des croyances, "
             "désirs et intentions différents des siens</strong>. Le test classique des « fausses croyances » "
             "(Sally-Anne) permet de mesurer cette étape clé du développement social et de l'empathie.</p>"),
            ("Vygotsky et l'apprentissage social",
             "<p>Pour <strong>Lev Vygotsky</strong>, le développement cognitif est indissociable du contexte "
             "social et culturel. Sa <strong>« zone proximale de développement »</strong> désigne l'écart entre "
             "ce qu'un enfant peut faire seul et ce qu'il peut réaliser avec l'aide d'un adulte ou d'un pair plus "
             "avancé — un concept fondateur de la pédagogie moderne.</p>"),
            ("Le vieillissement cognitif",
             "<p>Le développement ne s'arrête pas à l'âge adulte : la <strong>plasticité cérébrale</strong> "
             "persiste toute la vie. Si certaines fonctions (vitesse de traitement) déclinent avec l'âge, d'autres "
             "(vocabulaire, sagesse pratique, régulation émotionnelle) continuent souvent de progresser.</p>"),
        ],
        "figures": ["portrait-piaget.jpg:Jean Piaget"],
        "pdfs": [],
        "fun_fact": "Un nourrisson de quelques minutes préfère déjà regarder un visage humain schématique plutôt qu'un motif aléatoire de complexité équivalente — preuve d'une prédisposition sociale innée.",
        "flashcards": [
            ("Quels sont les 4 stades du développement cognitif de Piaget ?", "Sensorimoteur, préopératoire, opératoire concret, opératoire formel."),
            ("Quel est le style d'attachement le plus fréquent ?", "L'attachement sûr (environ 65 % des enfants)."),
            ("Quelle crise psychosociale caractérise l'adolescence selon Erikson ?", "Identité vs confusion des rôles."),
            ("À quel âge la théorie de l'esprit apparaît-elle généralement ?", "Vers 4 ans."),
            ("Qu'est-ce que la zone proximale de développement de Vygotsky ?", "L'écart entre ce qu'un enfant sait faire seul et ce qu'il peut faire avec l'aide d'autrui."),
        ],
    },
    {
        "id": "06-personnalite",
        "icon": "🎭", "color": "rose", "num": "06",
        "title": "Personnalité & Différences individuelles",
        "subtitle": "Ce qui nous rend uniques : traits, intelligence, volonté",
        "read_time": "13 min",
        "objectives": [
            "Connaître le modèle des Big Five (OCEAN)",
            "Comprendre les théories pluralistes de l'intelligence",
            "Découvrir les travaux historiques de Ribot sur la volonté",
            "Distinguer traits stables et états passagers",
        ],
        "sections": [
            ("Le modèle des Big Five (OCEAN)",
             "<p>Le modèle le plus validé scientifiquement décrit la personnalité selon 5 grands traits, "
             "chacun étant un continuum (et non une catégorie fixe) :</p>"
             "<ul><li><strong>O</strong>uverture — curiosité intellectuelle, créativité, goût de la nouveauté</li>"
             "<li><strong>C</strong>onscienciosité — organisation, discipline, fiabilité</li>"
             "<li><strong>E</strong>xtraversion — sociabilité, énergie, recherche de stimulation</li>"
             "<li><strong>A</strong>gréabilité — coopération, confiance envers autrui, empathie</li>"
             "<li><strong>N</strong>évrosisme — tendance à l'instabilité émotionnelle, à l'anxiété (l'inverse "
             "étant la stabilité émotionnelle)</li></ul>"
             "<div class='learn-tip-box'><span class='emoji'>✍️</span><p><strong>Pour les apprenants « lecture-écriture »</strong> : "
             "essayez de vous noter de 1 à 10 sur chacun des 5 traits, avec un exemple concret pour chaque score.</p></div>"),
            ("Combien y a-t-il d'intelligences ?",
             "<p>Le modèle traditionnel du <strong>facteur g</strong> (intelligence générale) prédit bien les "
             "performances scolaires et professionnelles. Mais <strong>Howard Gardner</strong> propose une théorie "
             "des <strong>intelligences multiples</strong> : linguistique, logico-mathématique, spatiale, musicale, "
             "kinesthésique, interpersonnelle, intrapersonnelle et naturaliste. Très populaire en pédagogie, "
             "cette théorie reste débattue sur le plan scientifique (manque de preuves empiriques solides).</p>"),
            ("Ribot et les maladies de la volonté",
             "<p><strong>Théodule Ribot</strong> étudie au XIXe siècle les troubles de la volonté (aboulie, "
             "impulsivité pathologique) pour mieux comprendre son fonctionnement normal — une méthode originale : "
             "<strong>étudier le pathologique pour éclairer le normal</strong>. Il identifie deux grandes formes "
             "de dysfonctionnement : l'insuffisance d'impulsion (incapacité à agir) et l'excès d'impulsion "
             "(actes irrésistibles).</p>"),
            ("Traits stables vs états passagers",
             "<p>Un <strong>trait de personnalité</strong> est une disposition stable dans le temps et les "
             "situations (ex. être globalement sociable). Un <strong>état</strong> est temporaire et lié au "
             "contexte (ex. être anxieux avant un examen). Confondre les deux est une erreur fréquente : une "
             "personne « timide » n'est pas nécessairement anxieuse dans toutes les situations.</p>"),
            ("Estime de soi et locus de contrôle",
             "<p>Le <strong>locus de contrôle</strong> (Rotter) désigne la tendance à attribuer les événements "
             "de sa vie à des causes internes (ses propres actions) ou externes (chance, autrui, destin). Un "
             "locus interne est généralement associé à une meilleure résilience et à une plus grande motivation.</p>"),
        ],
        "figures": ["portrait-ribot.jpg:Théodule Ribot"],
        "pdfs": [
            {"title": "Les maladies de la volonté", "author": "Théodule Ribot (1883)", "path": f"{PDF}/psychopathologie/ribot-maladies-volonte-1883.pdf",
             "desc": "L'étude pionnière sur les troubles de la volonté — un classique pour comprendre les racines de la psychologie de la personnalité."},
        ],
        "fun_fact": "Les traits de personnalité sont relativement stables dès l'âge de 30 ans, mais restent malléables : la conscienciosité et l'agréabilité tendent à augmenter naturellement avec l'âge (« maturation de la personnalité »).",
        "flashcards": [
            ("Que signifie l'acronyme OCEAN ?", "Ouverture, Conscienciosité, Extraversion, Agréabilité, Névrosisme — les Big Five."),
            ("Combien d'intelligences Gardner propose-t-il ?", "8 (linguistique, logico-mathématique, spatiale, musicale, kinesthésique, interpersonnelle, intrapersonnelle, naturaliste)."),
            ("Quelle est la méthode originale de Ribot pour étudier la volonté ?", "Étudier ses pathologies (aboulie, impulsivité) pour comprendre son fonctionnement normal."),
            ("Quelle est la différence entre un trait et un état ?", "Le trait est stable dans le temps ; l'état est temporaire et dépend du contexte."),
            ("Qu'est-ce que le locus de contrôle interne ?", "La tendance à attribuer les événements de sa vie à ses propres actions plutôt qu'à des causes externes."),
        ],
    },
    {
        "id": "07-emotions",
        "icon": "❤️", "color": "rose", "num": "07",
        "title": "Émotions & Motivation",
        "subtitle": "Ce qui nous fait ressentir, désirer et agir",
        "read_time": "12 min",
        "objectives": [
            "Comparer les grandes théories de l'émotion",
            "Comprendre l'universalité (ou non) des expressions émotionnelles",
            "Distinguer motivation intrinsèque et extrinsèque",
            "Découvrir l'apport de Darwin à l'étude des émotions",
        ],
        "sections": [
            ("Darwin et l'universalité des émotions",
             "<p>Dans <em>L'expression des émotions chez l'homme et les animaux</em> (1872), <strong>Charles "
             "Darwin</strong> avance une thèse audacieuse pour l'époque : les expressions émotionnelles "
             "(sourire, colère, dégoût) seraient <strong>innées et universelles</strong>, héritées de nos "
             "ancêtres animaux, et non purement culturelles. Cette idée sera confirmée un siècle plus tard par "
             "les travaux de Paul Ekman sur les 6 émotions de base reconnues dans toutes les cultures étudiées "
             "(joie, tristesse, colère, peur, dégoût, surprise).</p>"),
            ("Les grandes théories de l'émotion",
             "<p>Comment naît une émotion ? Trois théories historiques s'opposent :</p>"
             "<ul><li><strong>Théorie de James-Lange</strong> : l'émotion résulte de la perception des "
             "changements corporels (« je cours, donc j'ai peur », et non l'inverse)</li>"
             "<li><strong>Théorie de Cannon-Bard</strong> : l'émotion et la réaction corporelle surviennent "
             "simultanément, sans lien causal direct</li>"
             "<li><strong>Théorie de Schachter-Singer (bifactorielle)</strong> : l'émotion résulte de "
             "l'activation physiologique <strong>+</strong> de son interprétation cognitive selon le contexte</li></ul>"),
            ("Universel ou culturel ?",
             "<p>Si les 6 émotions de base semblent universelles dans leur <strong>expression faciale</strong>, "
             "leur <strong>régulation</strong> varie fortement selon les cultures (« règles d'affichage » ou "
             "display rules) : certaines cultures valorisent l'expressivité, d'autres la retenue émotionnelle.</p>"),
            ("Motivation intrinsèque et extrinsèque",
             "<p>La <strong>théorie de l'autodétermination</strong> (Deci & Ryan) distingue :</p>"
             "<ul><li><strong>Motivation intrinsèque</strong> : agir pour le plaisir de l'activité elle-même "
             "(curiosité, satisfaction personnelle)</li>"
             "<li><strong>Motivation extrinsèque</strong> : agir pour une récompense ou éviter une punition "
             "externe</li></ul>"
             "<p>Trois besoins psychologiques fondamentaux nourrissent la motivation intrinsèque : "
             "<strong>autonomie</strong>, <strong>compétence</strong> et <strong>relation sociale</strong>.</p>"),
            ("Régulation émotionnelle",
             "<p>Face à une émotion intense, plusieurs stratégies existent, avec des effets très différents : "
             "la <strong>suppression</strong> (cacher l'émotion) est coûteuse cognitivement et peu efficace à "
             "long terme, tandis que le <strong>recadrage cognitif</strong> (réinterpréter la situation) est "
             "associé à un meilleur bien-être psychologique.</p>"),
        ],
        "figures": ["portrait-darwin.jpg:Charles Darwin"],
        "pdfs": [
            {"title": "L'expression des émotions chez l'homme et les animaux", "author": "Charles Darwin (trad. 1877)", "path": f"{PDF}/psychologie-comparative/darwin-expression-emotions-1877.pdf",
             "desc": "L'ouvrage fondateur sur les racines biologiques et évolutives de nos émotions, richement illustré."},
        ],
        "fun_fact": "Le sourire dit « de Duchenne » (authentique, avec plissement des yeux) active des muscles quasi impossibles à contrôler volontairement — ce qui permet souvent de distinguer un vrai sourire d'un sourire de politesse.",
        "flashcards": [
            ("Selon Darwin, les expressions émotionnelles sont-elles culturelles ou innées ?", "Innées et universelles, héritées de l'évolution — thèse confirmée plus tard par Paul Ekman."),
            ("Que dit la théorie de James-Lange ?", "Que l'émotion résulte de la perception des changements corporels (pas l'inverse)."),
            ("Quels sont les 6 émotions de base selon Ekman ?", "Joie, tristesse, colère, peur, dégoût, surprise."),
            ("Quels sont les 3 besoins de la théorie de l'autodétermination ?", "Autonomie, compétence, relation sociale."),
            ("Quelle stratégie de régulation émotionnelle est la plus efficace à long terme ?", "Le recadrage cognitif, plus efficace que la suppression émotionnelle."),
        ],
    },
    {
        "id": "08-neurosciences",
        "icon": "🧠", "color": "vert", "num": "08",
        "title": "Neurosciences & Psychologie biologique",
        "subtitle": "Le cerveau : 86 milliards de neurones au service de l'esprit",
        "read_time": "14 min",
        "objectives": [
            "Situer les grandes fonctions des lobes cérébraux",
            "Comprendre le rôle des principaux neurotransmetteurs",
            "Expliquer la neuroplasticité",
            "Découvrir les apports historiques de Charcot à la neurologie",
        ],
        "sections": [
            ("Charcot et la naissance de la neurologie moderne",
             "<p><strong>Jean-Martin Charcot</strong>, à la Salpêtrière (Paris), fonde la neurologie clinique "
             "moderne en observant méthodiquement les patients atteints de troubles neurologiques (sclérose en "
             "plaques, maladie de Parkinson, hystérie). Ses <em>Leçons sur les maladies du système nerveux</em> "
             "influenceront directement le jeune Freud, qui assista à ses cours.</p>"),
            ("Les grandes régions du cerveau",
             "<p>Le cortex cérébral se divise en 4 lobes principaux, chacun spécialisé :</p>"
             "<ul><li><strong>Lobe frontal</strong> : planification, décision, contrôle des impulsions, "
             "personnalité</li>"
             "<li><strong>Lobe pariétal</strong> : intégration sensorielle, perception spatiale</li>"
             "<li><strong>Lobe temporal</strong> : audition, langage, mémoire (hippocampe)</li>"
             "<li><strong>Lobe occipital</strong> : traitement visuel</li></ul>"
             "<p>Sous le cortex, des structures clés : l'<strong>amygdale</strong> (traitement de la peur), "
             "l'<strong>hippocampe</strong> (formation des souvenirs) et le <strong>cervelet</strong> "
             "(coordination motrice, mais aussi cognition fine).</p>"),
            ("Les neurotransmetteurs : les messagers chimiques",
             "<p>L'information circule entre neurones grâce à des molécules chimiques :</p>"
             "<ul><li><strong>Dopamine</strong> : motivation, récompense, mouvement (impliquée dans l'addiction "
             "et la maladie de Parkinson)</li>"
             "<li><strong>Sérotonine</strong> : humeur, sommeil, appétit (cible des antidépresseurs ISRS)</li>"
             "<li><strong>GABA</strong> : principal neurotransmetteur inhibiteur, effet calmant (cible de "
             "l'alcool et des benzodiazépines)</li>"
             "<li><strong>Glutamate</strong> : principal neurotransmetteur excitateur, essentiel à "
             "l'apprentissage</li>"
             "<li><strong>Noradrénaline</strong> : vigilance, réaction de stress (« attaque ou fuite »)</li></ul>"),
            ("La neuroplasticité : un cerveau qui se réorganise",
             "<p>Contrairement à une idée longtemps répandue, le cerveau adulte reste capable de créer de "
             "nouvelles connexions synaptiques toute la vie, en fonction de l'expérience — c'est la "
             "<strong>neuroplasticité</strong>. Elle explique la récupération partielle après une lésion "
             "cérébrale et l'apprentissage de nouvelles compétences à tout âge.</p>"),
            ("Voir le cerveau en action",
             "<p>Les techniques de <strong>neuroimagerie</strong> permettent d'observer l'activité cérébrale : "
             "l'<strong>IRMf</strong> mesure les variations du flux sanguin liées à l'activité neuronale (bonne "
             "résolution spatiale), l'<strong>EEG</strong> mesure l'activité électrique (excellente résolution "
             "temporelle), le <strong>TEP</strong> traque des marqueurs métaboliques ou chimiques.</p>"),
        ],
        "figures": ["portrait-charcot.jpg:Jean-Martin Charcot"],
        "pdfs": [
            {"title": "Leçons sur les maladies du système nerveux", "author": "Jean-Martin Charcot (1884)", "path": f"{PDF}/psychopathologie/charcot-lecons-systeme-nerveux-1884.pdf",
             "desc": "L'œuvre fondatrice de la neurologie clinique moderne, richement illustrée de cas cliniques observés à la Salpêtrière."},
        ],
        "fun_fact": "Le cerveau ne représente que 2 % du poids corporel mais consomme environ <strong>20 % de l'énergie totale</strong> du corps — un organe extrêmement gourmand en glucose et en oxygène.",
        "flashcards": [
            ("Quel lobe cérébral gère la planification et le contrôle des impulsions ?", "Le lobe frontal."),
            ("Quel neurotransmetteur est lié à la motivation et à la récompense ?", "La dopamine."),
            ("Quelle structure cérébrale est essentielle à la formation des souvenirs ?", "L'hippocampe."),
            ("Qu'est-ce que la neuroplasticité ?", "La capacité du cerveau à créer de nouvelles connexions synaptiques tout au long de la vie."),
            ("Quelle technique de neuroimagerie a la meilleure résolution temporelle ?", "L'EEG (électroencéphalographie)."),
        ],
    },
    {
        "id": "09-psychopathologie",
        "icon": "🩺", "color": "rose", "num": "09",
        "title": "Psychopathologie & Troubles mentaux",
        "subtitle": "Comprendre la souffrance psychique sans stigmatiser",
        "read_time": "16 min",
        "objectives": [
            "Distinguer les grandes familles de troubles mentaux",
            "Comprendre les apports historiques de Ribot, Janet et Charcot",
            "Identifier les principaux troubles anxieux et de l'humeur",
            "Adopter un regard non stigmatisant sur la maladie mentale",
        ],
        "sections": [
            ("Étudier le pathologique pour comprendre le normal",
             "<p>Au XIXe siècle, une idée féconde émerge : observer les <strong>dysfonctionnements</strong> "
             "psychiques permet de mieux comprendre le fonctionnement normal. Ribot l'applique à la mémoire et "
             "à la volonté, Janet aux névroses, Charcot aux troubles neurologiques — une méthode encore utilisée "
             "aujourd'hui en neuropsychologie clinique (étudier des lésions cérébrales pour cartographier les "
             "fonctions cognitives).</p>"),
            ("Ribot et les maladies de la mémoire",
             "<p><strong>Théodule Ribot</strong> formule en 1881 la <strong>« loi de régression »</strong> : "
             "dans l'amnésie, les souvenirs les plus récents et les plus complexes disparaissent en premier, "
             "tandis que les souvenirs anciens et les habitudes automatiques (motrices, émotionnelles) "
             "résistent le plus longtemps. Cette loi reste globalement valide dans la compréhension moderne des "
             "démences.</p>"),
            ("Janet et les névroses",
             "<p><strong>Pierre Janet</strong> étudie l'hystérie et les névroses en développant le concept "
             "d'<strong>automatisme psychologique</strong> : certains comportements et pensées échappent au "
             "contrôle conscient et fonctionnent de manière dissociée. Ses travaux sont aujourd'hui reconnus "
             "comme précurseurs de la compréhension moderne du <strong>psychotraumatisme</strong> et des "
             "troubles dissociatifs.</p>"),
            ("Les grandes familles de troubles",
             "<p>Les classifications actuelles (DSM-5, CIM-11) organisent les troubles mentaux en grandes "
             "catégories :</p>"
             "<ul><li><strong>Troubles anxieux</strong> : anxiété généralisée, phobies spécifiques, "
             "agoraphobie, trouble panique, anxiété sociale</li>"
             "<li><strong>Troubles de l'humeur</strong> : dépression, trouble bipolaire</li>"
             "<li><strong>Troubles obsessionnels-compulsifs</strong> (TOC) : pensées intrusives et rituels "
             "compulsifs</li>"
             "<li><strong>Troubles psychotiques</strong> : schizophrénie (hallucinations, délires, symptômes "
             "négatifs)</li>"
             "<li><strong>Troubles de la personnalité</strong> : schémas rigides et inadaptés de pensée et de "
             "comportement</li>"
             "<li><strong>Troubles du neurodéveloppement</strong> : TSA (autisme), TDAH</li>"
             "<li><strong>Troubles liés au trauma</strong> : état de stress post-traumatique (PTSD)</li></ul>"),
            ("Anxiété et dépression : les troubles les plus fréquents",
             "<p>L'<strong>anxiété</strong> est une réaction à une menace perçue (parfois disproportionnée), "
             "combinant pensées d'inquiétude, tension physique et évitement. La <strong>dépression</strong> "
             "associe tristesse persistante, perte d'intérêt (anhédonie), troubles du sommeil et de l'appétit, "
             "et une vision négative de soi, du monde et de l'avenir (triade cognitive de Beck).</p>"),
            ("Déconstruire la stigmatisation",
             "<p>Un trouble mental n'est ni une faiblesse de caractère, ni un choix : c'est le résultat "
             "d'interactions complexes entre facteurs biologiques (génétique, neurochimie), psychologiques "
             "(schémas de pensée, histoire personnelle) et sociaux (stress, isolement, conditions de vie) — "
             "le <strong>modèle bio-psycho-social</strong>. La stigmatisation retarde le recours aux soins et "
             "aggrave la souffrance des personnes concernées.</p>"),
        ],
        "figures": ["portrait-ribot.jpg:Théodule Ribot", "portrait-janet.jpg:Pierre Janet", "portrait-charcot.jpg:Jean-Martin Charcot"],
        "pdfs": [
            {"title": "Les maladies de la mémoire", "author": "Théodule Ribot (1898)", "path": f"{PDF}/psychopathologie/ribot-maladies-memoire-1898.pdf",
             "desc": "L'étude fondatrice sur les troubles de la mémoire, avec la célèbre « loi de régression »."},
            {"title": "Les névroses", "author": "Pierre Janet (1909)", "path": f"{PDF}/psychopathologie/janet-les-nevroses-1909.pdf",
             "desc": "Une référence historique majeure sur l'hystérie, l'automatisme psychologique et les troubles dissociatifs."},
        ],
        "fun_fact": "Selon l'Organisation Mondiale de la Santé, <strong>1 personne sur 8</strong> dans le monde vit avec un trouble mental — la dépression et l'anxiété sont les plus répandus.",
        "flashcards": [
            ("Qu'est-ce que la loi de régression de Ribot ?", "Dans l'amnésie, les souvenirs récents et complexes disparaissent avant les souvenirs anciens et automatiques."),
            ("Qu'est-ce que l'automatisme psychologique selon Janet ?", "Des comportements et pensées qui échappent au contrôle conscient, fonctionnant de façon dissociée."),
            ("Quelle est la triade cognitive de Beck dans la dépression ?", "Une vision négative de soi, du monde et de l'avenir."),
            ("Qu'est-ce que le modèle bio-psycho-social ?", "Un modèle expliquant les troubles mentaux par l'interaction de facteurs biologiques, psychologiques et sociaux."),
            ("Quels sont les symptômes typiques d'un trouble anxieux ?", "Pensées d'inquiétude, tension physique et comportements d'évitement."),
        ],
    },
    {
        "id": "10-therapies",
        "icon": "🛋️", "color": "or", "num": "10",
        "title": "Thérapies & Interventions",
        "subtitle": "Les grandes approches pour soigner l'esprit",
        "read_time": "13 min",
        "objectives": [
            "Comparer les principales approches thérapeutiques",
            "Comprendre les fondements de la psychanalyse freudienne",
            "Expliquer le modèle ABC de la thérapie cognitivo-comportementale",
            "Connaître les thérapies plus récentes (EMDR, ACT, pleine conscience)",
        ],
        "sections": [
            ("Freud et la psychanalyse",
             "<p>Dans <em>L'interprétation des rêves</em> (1900), <strong>Freud</strong> pose les bases de la "
             "psychanalyse : les rêves seraient l'expression déguisée de désirs inconscients refoulés. La cure "
             "psychanalytique explore l'inconscient par la libre association, l'analyse du transfert (les "
             "sentiments du patient envers le thérapeute reproduisant des relations passées) et l'interprétation "
             "des résistances.</p>"),
            ("La thérapie cognitivo-comportementale (TCC)",
             "<p>La TCC, développée notamment par <strong>Aaron Beck</strong>, est aujourd'hui l'approche la "
             "plus <strong>validée empiriquement</strong> pour l'anxiété et la dépression. Elle repose sur le "
             "modèle ABC :</p>"
             "<ul><li><strong>A</strong>ctivating event — l'événement déclencheur</li>"
             "<li><strong>B</strong>elief — la pensée automatique / croyance interprétative</li>"
             "<li><strong>C</strong>onsequence — l'émotion et le comportement qui en résultent</li></ul>"
             "<p>Le travail thérapeutique consiste à identifier les <strong>distorsions cognitives</strong> "
             "(pensée tout-ou-rien, catastrophisme, surgénéralisation) et à les remplacer par des pensées plus "
             "réalistes, tout en modifiant les comportements d'évitement par l'exposition progressive.</p>"),
            ("L'approche humaniste",
             "<p><strong>Carl Rogers</strong> développe la <strong>thérapie centrée sur la personne</strong>, "
             "fondée sur trois attitudes du thérapeute : l'<strong>empathie</strong> (comprendre le vécu du "
             "patient sans jugement), la <strong>congruence</strong> (authenticité) et le "
             "<strong>regard positif inconditionnel</strong> (acceptation sans condition). Cette approche a "
             "profondément influencé la relation d'aide dans de nombreux métiers (santé, éducation, travail "
             "social).</p>"),
            ("Thérapies systémiques et familiales",
             "<p>Plutôt que de traiter un individu isolé, les thérapies systémiques considèrent la "
             "<strong>famille comme un système</strong> où chaque comportement a une fonction dans l'équilibre "
             "global. Un symptôme chez un enfant peut ainsi révéler une tension dans le couple parental ou dans "
             "l'organisation familiale.</p>"),
            ("Approches plus récentes : EMDR, ACT, pleine conscience",
             "<p>Trois approches contemporaines complètent l'arsenal thérapeutique :</p>"
             "<ul><li><strong>EMDR</strong> (mouvements oculaires) : retraitement des souvenirs traumatiques, "
             "particulièrement efficace pour le PTSD</li>"
             "<li><strong>ACT</strong> (thérapie d'acceptation et d'engagement) : accepter les pensées et "
             "émotions difficiles plutôt que de lutter contre elles, en se recentrant sur ses valeurs</li>"
             "<li><strong>Mindfulness</strong> (pleine conscience) : porter une attention non-jugeante au "
             "moment présent, avec des bénéfices démontrés sur le stress et la rechute dépressive</li></ul>"),
        ],
        "figures": ["portrait-freud.jpg:Sigmund Freud", "portrait-rogers.jpg:Carl Rogers"],
        "pdfs": [
            {"title": "L'interprétation des rêves", "author": "Sigmund Freud (trad. fr., 1900)", "path": f"{PDF}/psychologie-clinique/freud-interpretation-reves-1900.html",
             "desc": "Le texte fondateur de la psychanalyse, disponible en intégralité au format HTML (source Project Gutenberg)."},
        ],
        "fun_fact": "La thérapie centrée sur la personne de Carl Rogers a inspiré l'écoute active utilisée aujourd'hui dans des domaines très variés : ressources humaines, médiation, négociation, et même certaines formations en intelligence artificielle conversationnelle.",
        "flashcards": [
            ("Que signifie le modèle ABC en TCC ?", "Activating event (déclencheur), Belief (croyance), Consequence (émotion/comportement)."),
            ("Quelles sont les 3 attitudes clés du thérapeute selon Rogers ?", "Empathie, congruence, regard positif inconditionnel."),
            ("Pour quel trouble l'EMDR est-il particulièrement recommandé ?", "Le trouble de stress post-traumatique (PTSD)."),
            ("Qu'est-ce que la thérapie systémique considère comme unité de soin ?", "La famille comme un système, plutôt que l'individu isolé."),
            ("Quel est le principe central de l'ACT ?", "Accepter les pensées et émotions difficiles plutôt que lutter contre elles, en se recentrant sur ses valeurs."),
        ],
    },
    {
        "id": "11-positive",
        "icon": "🌤️", "color": "or", "num": "11",
        "title": "Psychologie Positive & Bien-être",
        "subtitle": "La science du bien vivre, pas seulement de la maladie",
        "read_time": "11 min",
        "objectives": [
            "Comprendre le modèle PERMA du bien-être",
            "Expliquer l'état de flow et ses conditions",
            "Distinguer bonheur hédonique et eudémonique",
            "Connaître les limites et critiques de la psychologie positive",
        ],
        "sections": [
            ("Naissance d'un nouveau champ",
             "<p>En 1998, <strong>Martin Seligman</strong>, alors président de l'Association Américaine de "
             "Psychologie, appelle à ne plus étudier uniquement la maladie mentale, mais aussi ce qui permet "
             "aux êtres humains de <strong>s'épanouir</strong> (flourishing). La psychologie positive est née.</p>"),
            ("Le modèle PERMA",
             "<p>Seligman identifie 5 piliers du bien-être durable, résumés par l'acronyme PERMA :</p>"
             "<ul><li><strong>P</strong>ositive emotions — cultiver des émotions positives fréquentes</li>"
             "<li><strong>E</strong>ngagement — s'absorber dans des activités stimulantes (flow)</li>"
             "<li><strong>R</strong>elationships — entretenir des relations sociales de qualité</li>"
             "<li><strong>M</strong>eaning — donner du sens à sa vie, se sentir utile</li>"
             "<li><strong>A</strong>ccomplishment — poursuivre et atteindre des objectifs valorisants</li></ul>"),
            ("L'état de flow",
             "<p><strong>Mihaly Csikszentmihalyi</strong> décrit le <strong>flow</strong> comme un état "
             "d'absorption totale dans une activité, où l'on perd la notion du temps. Il survient quand le "
             "niveau de <strong>défi</strong> est parfaitement ajusté au niveau de <strong>compétence</strong> : "
             "ni trop facile (ennui), ni trop difficile (anxiété). Le flow nécessite aussi des objectifs clairs "
             "et un retour d'information (feedback) immédiat sur sa performance.</p>"),
            ("Hédonisme vs eudémonisme",
             "<p>Deux conceptions philosophiques du bonheur coexistent en psychologie positive :</p>"
             "<ul><li><strong>Bien-être hédonique</strong> : maximiser le plaisir, minimiser la douleur "
             "(satisfaction de vie, émotions positives)</li>"
             "<li><strong>Bien-être eudémonique</strong> : réaliser son potentiel, vivre selon ses valeurs, "
             "contribuer à quelque chose de plus grand que soi (concept issu d'Aristote)</li></ul>"
             "<p>Les recherches montrent que les deux dimensions sont importantes et se renforcent souvent "
             "mutuellement.</p>"),
            ("Gratitude, résilience et optimisme appris",
             "<p>Plusieurs interventions brèves ont montré un effet positif validé scientifiquement : tenir un "
             "<strong>journal de gratitude</strong> régulier, pratiquer la <strong>savoring</strong> (savourer "
             "consciemment les moments positifs), et développer un <strong>optimisme réaliste</strong> — "
             "expliquer les échecs par des causes spécifiques et temporaires plutôt que globales et permanentes.</p>"),
            ("Les limites et critiques",
             "<p>La psychologie positive a été critiquée pour un risque de <strong>« positivité toxique »</strong> "
             "(minimiser les émotions négatives légitimes), pour des résultats parfois surestimés dans la "
             "vulgarisation médiatique, et pour un possible biais culturel occidental dans sa définition du "
             "bien-être. Un regard critique sur ces travaux reste essentiel.</p>"),
        ],
        "figures": [],
        "pdfs": [],
        "fun_fact": "Écrire 3 choses positives de sa journée pendant seulement 2 semaines suffit, selon plusieurs études, à produire une augmentation mesurable du bien-être ressenti — un effet qui peut persister plusieurs mois.",
        "flashcards": [
            ("Que signifie l'acronyme PERMA ?", "Positive emotions, Engagement, Relationships, Meaning, Accomplishment."),
            ("Quelles sont les deux conditions nécessaires au flow ?", "Un équilibre entre défi et compétence, plus des objectifs clairs et un feedback immédiat."),
            ("Quelle est la différence entre bien-être hédonique et eudémonique ?", "L'hédonique vise le plaisir immédiat ; l'eudémonique vise la réalisation de son potentiel et le sens."),
            ("Qui a fondé la psychologie positive et en quelle année ?", "Martin Seligman, en 1998."),
            ("Quelle est une critique majeure de la psychologie positive ?", "Le risque de « positivité toxique », qui minimise les émotions négatives légitimes."),
        ],
    },
    {
        "id": "12-travail",
        "icon": "💼", "color": "gris", "num": "12",
        "title": "Psychologie du Travail & des Organisations",
        "subtitle": "Motivation, leadership et bien-être en entreprise",
        "read_time": "12 min",
        "objectives": [
            "Comprendre les grandes théories de la motivation au travail",
            "Distinguer les styles de leadership",
            "Identifier les causes et symptômes du burn-out",
            "Comprendre les dynamiques d'équipe et de communication professionnelle",
        ],
        "sections": [
            ("Les théories de la motivation au travail",
             "<p>La <strong>théorie des deux facteurs</strong> de Herzberg distingue les facteurs "
             "d'insatisfaction (salaire, conditions de travail — leur absence démotive, leur présence ne motive "
             "pas vraiment) des facteurs de motivation réels (reconnaissance, accomplissement, responsabilités). "
             "La <strong>théorie de l'autodétermination</strong> (vue au chapitre Émotions) s'applique aussi "
             "parfaitement au contexte professionnel : autonomie, compétence et relations sont clés pour "
             "l'engagement durable.</p>"),
            ("Styles de leadership",
             "<p>Trois grands styles de leadership ont été identifiés historiquement (Lewin) :</p>"
             "<ul><li><strong>Autoritaire</strong> : décisions centralisées, efficace à court terme mais "
             "souvent démotivant</li>"
             "<li><strong>Démocratique</strong> : décisions partagées, favorise l'engagement et la créativité</li>"
             "<li><strong>Laissez-faire</strong> : peu de directives, efficace avec des équipes très autonomes, "
             "risqué sinon</li></ul>"
             "<p>Le <strong>leadership transformationnel</strong> moderne ajoute une dimension inspirationnelle : "
             "donner du sens, incarner une vision, développer les collaborateurs.</p>"),
            ("Le burn-out : anatomie de l'épuisement professionnel",
             "<p>Le burn-out (épuisement professionnel) se caractérise par trois dimensions (Maslach) :</p>"
             "<ul><li><strong>Épuisement émotionnel</strong> : sentiment de vide, fatigue extrême</li>"
             "<li><strong>Dépersonnalisation / cynisme</strong> : distance émotionnelle avec le travail et les "
             "collègues/usagers</li>"
             "<li><strong>Perte d'accomplissement personnel</strong> : sentiment d'inefficacité</li></ul>"
             "<p>Les principaux facteurs de risque : charge de travail excessive, manque de reconnaissance, "
             "manque de contrôle sur ses tâches, conflits de valeurs et isolement social.</p>"),
            ("Dynamiques d'équipe",
             "<p>Le modèle de <strong>Tuckman</strong> décrit 4 phases de développement d'une équipe : "
             "<strong>formation</strong> (politesse, prudence), <strong>tensions</strong> (conflits, "
             "clarification des rôles), <strong>normalisation</strong> (coopération établie), "
             "<strong>performance</strong> (efficacité collective optimale). Une équipe qui traverse ces "
             "étapes développe généralement une meilleure cohésion durable.</p>"),
            ("Justice organisationnelle et engagement",
             "<p>Le sentiment de <strong>justice au travail</strong> — équité des décisions, transparence des "
             "procédures, respect interpersonnel — est un puissant prédicteur de l'engagement des salariés, "
             "souvent plus déterminant que le niveau de rémunération lui-même.</p>"),
        ],
        "figures": [],
        "pdfs": [],
        "fun_fact": "Selon plusieurs études, un salarié qui a un ami proche au travail est significativement plus engagé et productif — la qualité des relations sociales au bureau pèse autant que les conditions matérielles.",
        "flashcards": [
            ("Que distingue la théorie des deux facteurs de Herzberg ?", "Les facteurs d'insatisfaction (hygiène) et les facteurs de motivation réels (accomplissement, reconnaissance)."),
            ("Quels sont les 3 styles de leadership de Lewin ?", "Autoritaire, démocratique, laissez-faire."),
            ("Quelles sont les 3 dimensions du burn-out selon Maslach ?", "Épuisement émotionnel, dépersonnalisation/cynisme, perte d'accomplissement personnel."),
            ("Quelles sont les 4 phases du modèle de Tuckman ?", "Formation, tensions, normalisation, performance."),
            ("Qu'est-ce que la justice organisationnelle ?", "Le sentiment d'équité et de transparence dans les décisions et procédures de l'entreprise."),
        ],
    },
    {
        "id": "13-education",
        "icon": "🎓", "color": "vert", "num": "13",
        "title": "Psychologie de l'Éducation & de l'Apprentissage",
        "subtitle": "Comment on apprend vraiment (et comment mieux enseigner)",
        "read_time": "13 min",
        "objectives": [
            "Comprendre le conditionnement classique et opérant",
            "Découvrir l'apprentissage social de Bandura",
            "Connaître les principes pédagogiques de Le Bon et leur actualité",
            "Identifier les techniques d'apprentissage validées scientifiquement",
        ],
        "sections": [
            ("Le conditionnement classique",
             "<p><strong>Ivan Pavlov</strong> découvre en 1897 que ses chiens salivent au son d'une sonnette "
             "annonçant la nourriture, même en l'absence de nourriture. Un stimulus neutre, associé de façon "
             "répétée à un stimulus qui déclenche naturellement une réponse, devient capable de déclencher "
             "cette réponse seul. Ce mécanisme explique de nombreuses associations émotionnelles (phobies, "
             "aversions alimentaires…).</p>"),
            ("Le conditionnement opérant",
             "<p><strong>B.F. Skinner</strong> montre que le comportement est modelé par ses conséquences :</p>"
             "<ul><li><strong>Renforcement positif</strong> : ajouter une conséquence agréable → le "
             "comportement se répète davantage</li>"
             "<li><strong>Renforcement négatif</strong> : retirer une conséquence désagréable → le comportement "
             "se répète davantage</li>"
             "<li><strong>Punition</strong> : ajouter une conséquence désagréable → le comportement diminue "
             "(mais avec des effets secondaires possibles : peur, évitement, agressivité)</li>"
             "<li><strong>Extinction</strong> : arrêter le renforcement → le comportement disparaît "
             "progressivement</li></ul>"),
            ("L'apprentissage social de Bandura",
             "<p><strong>Albert Bandura</strong> montre, avec la célèbre expérience de la poupée Bobo (1961), "
             "que l'on peut apprendre un comportement simplement en <strong>observant un modèle</strong>, sans "
             "renforcement direct. L'imitation est particulièrement forte quand le modèle est valorisé ou "
             "similaire à l'observateur — un principe fondamental pour comprendre l'influence des pairs et des "
             "figures d'autorité sur les enfants.</p>"),
            ("Le Bon et la « psychologie de l'éducation »",
             "<p><strong>Gustave Le Bon</strong>, dans son ouvrage <em>Psychologie de l'éducation</em>, critique "
             "déjà à son époque un enseignement trop centré sur la mémorisation passive et plaide pour "
             "l'expérimentation active et l'intérêt de l'élève — des idées étonnamment proches de la pédagogie "
             "active moderne, bien qu'exprimées dans un style parfois daté et à lire avec un regard critique sur "
             "certains présupposés de l'auteur.</p>"),
            ("Les techniques d'apprentissage validées par la science",
             "<p>La recherche en psychologie cognitive identifie des méthodes nettement plus efficaces que la "
             "relecture passive :</p>"
             "<ul><li><strong>Rappel actif (testing effect)</strong> : se tester activement plutôt que relire "
             "renforce durablement la mémorisation</li>"
             "<li><strong>Répétition espacée</strong> : réviser à intervalles croissants lutte efficacement "
             "contre la courbe de l'oubli</li>"
             "<li><strong>Entrelacement (interleaving)</strong> : alterner les sujets plutôt que les bloquer "
             "améliore la discrimination et le transfert</li>"
             "<li><strong>Élaboration</strong> : expliquer avec ses propres mots, faire des liens avec ce que "
             "l'on connaît déjà</li></ul>"
             "<p>Ces techniques sont détaillées et mises en pratique sur la page "
             "<a href='../apprendre.html'>Comment apprendre efficacement</a> de ce guide.</p>"),
        ],
        "figures": ["portrait-pavlov.jpg:Ivan Pavlov", "portrait-thorndike.jpg:Edward Thorndike", "portrait-le-bon.jpg:Gustave Le Bon"],
        "pdfs": [
            {"title": "Psychologie de l'éducation", "author": "Gustave Le Bon", "path": f"{PDF}/psychologie-generale/le-bon-psychologie-education.html",
             "desc": "Un plaidoyer historique pour une pédagogie active — à lire avec un regard critique sur son époque."},
        ],
        "fun_fact": "Se tester activement sur un contenu (même en échouant) améliore davantage la mémorisation à long terme que le relire quatre fois de suite — c'est le fameux « testing effect », l'une des découvertes les plus robustes de la psychologie cognitive.",
        "flashcards": [
            ("Quelle est la différence entre renforcement négatif et punition ?", "Le renforcement négatif retire un élément désagréable (augmente le comportement) ; la punition ajoute un élément désagréable (diminue le comportement)."),
            ("Que démontre l'expérience de la poupée Bobo de Bandura ?", "Qu'on peut apprendre un comportement par simple observation d'un modèle, sans renforcement direct."),
            ("Qu'est-ce que le testing effect ?", "Le fait de se tester activement mémorise mieux que de relire passivement."),
            ("Qu'est-ce que la répétition espacée ?", "Réviser à intervalles de temps croissants pour lutter contre l'oubli."),
            ("Qu'est-ce que l'extinction en conditionnement opérant ?", "La disparition progressive d'un comportement quand son renforcement s'arrête."),
        ],
    },
    {
        "id": "14-sante",
        "icon": "🏥", "color": "rose", "num": "14",
        "title": "Psychologie de la Santé",
        "subtitle": "Le corps et l'esprit face à la maladie et au stress",
        "read_time": "11 min",
        "objectives": [
            "Comprendre le mécanisme physiologique du stress",
            "Distinguer les stratégies de coping",
            "Expliquer le lien entre facteurs psychologiques et maladies physiques",
            "Connaître les leviers d'adhésion aux traitements médicaux",
        ],
        "sections": [
            ("Le stress : une réaction adaptative... parfois dépassée",
             "<p>Le <strong>syndrome général d'adaptation</strong> (Hans Selye) décrit 3 phases de la réponse "
             "au stress : <strong>alarme</strong> (mobilisation immédiate, adrénaline), <strong>résistance</strong> "
             "(adaptation prolongée, cortisol), <strong>épuisement</strong> (si le stress persiste trop "
             "longtemps, les ressources s'effondrent). Ce mécanisme, utile face à un danger ponctuel, devient "
             "délétère quand il est activé de façon chronique par des stress modernes (travail, finances, "
             "relations).</p>"),
            ("Les stratégies de coping",
             "<p>Le <strong>coping</strong> désigne l'ensemble des stratégies mises en œuvre pour faire face à "
             "une situation stressante :</p>"
             "<ul><li><strong>Coping centré sur le problème</strong> : agir directement sur la source du "
             "stress (chercher une solution, planifier)</li>"
             "<li><strong>Coping centré sur l'émotion</strong> : réguler sa réaction émotionnelle (relaxation, "
             "recadrage, soutien social)</li>"
             "<li><strong>Coping d'évitement</strong> : fuir ou nier le problème — soulage à court terme mais "
             "aggrave souvent la situation à long terme</li></ul>"),
            ("Psychosomatique : quand l'esprit affecte le corps",
             "<p>De nombreuses recherches établissent des liens robustes entre facteurs psychologiques et santé "
             "physique : le stress chronique affaiblit le système immunitaire, favorise l'inflammation et "
             "augmente le risque de maladies cardiovasculaires. Inversement, le soutien social et l'optimisme "
             "sont associés à une meilleure récupération après une maladie grave.</p>"),
            ("L'adhésion thérapeutique",
             "<p>Près d'un patient sur deux ne suit pas correctement son traitement médical prescrit. Les "
             "leviers psychologiques pour améliorer l'<strong>adhésion thérapeutique</strong> incluent : bien "
             "comprendre l'utilité du traitement, se sentir acteur de sa décision de santé (plutôt que subir), "
             "simplifier les schémas de prise, et bénéficier d'un accompagnement empathique du soignant.</p>"),
            ("Sentiment d'auto-efficacité et santé",
             "<p>Le <strong>sentiment d'auto-efficacité</strong> (Bandura) — la croyance en sa capacité à "
             "réussir une action — prédit fortement l'adoption durable de comportements de santé (arrêt du "
             "tabac, activité physique régulière, gestion du diabète). Il se renforce par l'expérience de "
             "petites réussites progressives.</p>"),
        ],
        "figures": [],
        "pdfs": [],
        "fun_fact": "Des études montrent qu'un simple contact social bref (quelques minutes de conversation chaleureuse) peut mesurablement réduire le taux de cortisol (hormone du stress) — le lien social est un véritable outil de régulation physiologique.",
        "flashcards": [
            ("Quelles sont les 3 phases du syndrome général d'adaptation de Selye ?", "Alarme, résistance, épuisement."),
            ("Quelle différence entre coping centré sur le problème et centré sur l'émotion ?", "Le premier agit sur la source du stress, le second régule la réaction émotionnelle."),
            ("Pourquoi le coping d'évitement est-il risqué à long terme ?", "Il soulage à court terme mais tend à aggraver le problème s'il persiste."),
            ("Qu'est-ce que l'adhésion thérapeutique ?", "Le fait de suivre correctement un traitement médical prescrit."),
            ("Qu'est-ce que le sentiment d'auto-efficacité ?", "La croyance en sa propre capacité à réussir une action, prédicteur clé des comportements de santé."),
        ],
    },
    {
        "id": "15-legale",
        "icon": "⚖️", "color": "gris", "num": "15",
        "title": "Psychologie Légale & Criminologie",
        "subtitle": "Comprendre le crime, le témoignage et l'expertise judiciaire",
        "read_time": "12 min",
        "objectives": [
            "Comprendre l'histoire (et les limites) de la criminologie de Lombroso",
            "Analyser la fiabilité du témoignage oculaire",
            "Découvrir le rôle du psychologue expert en justice",
            "Distinguer profilage scientifique et stéréotype populaire",
        ],
        "sections": [
            ("Lombroso et les débuts (controversés) de la criminologie",
             "<p><strong>Cesare Lombroso</strong> publie en 1876 <em>L'homme criminel</em>, où il défend l'idée "
             "que certains individus seraient des « criminels-nés », identifiables par des traits physiques "
             "particuliers (anthropologie criminelle). Cette théorie est aujourd'hui <strong>totalement "
             "réfutée</strong> scientifiquement et considérée comme dangereuse (elle a nourri des dérives "
             "eugénistes) — mais elle marque historiquement la naissance d'une approche empirique, bien que "
             "profondément erronée, de l'étude du crime.</p>"
             "<div class='learn-tip-box'><span class='emoji'>⚠️</span><p><strong>Regard critique nécessaire</strong> : "
             "ce texte est conservé pour sa valeur historique et documentaire, non comme une vérité scientifique. "
             "La criminologie moderne s'appuie sur des facteurs sociaux, psychologiques et situationnels, pas sur "
             "des traits physiques.</p></div>"),
            ("La fiabilité (limitée) du témoignage oculaire",
             "<p>Les tribunaux accordent traditionnellement une grande confiance aux témoins oculaires — "
             "pourtant, la recherche (notamment d'Elizabeth Loftus, vue au chapitre Cognition) montre que la "
             "mémoire des témoins est <strong>hautement reconstructive</strong> et influençable par : la façon "
             "de poser les questions, le stress au moment des faits, la présence d'une arme (qui capte "
             "l'attention au détriment de l'identification du visage), et le délai avant témoignage.</p>"),
            ("Le psychologue expert judiciaire",
             "<p>Le psychologue légal peut intervenir à plusieurs niveaux :</p>"
             "<ul><li><strong>Expertise de responsabilité pénale</strong> : évaluer le discernement d'un "
             "accusé au moment des faits</li>"
             "<li><strong>Expertise de crédibilité</strong> : évaluer la fiabilité d'un témoignage (notamment "
             "chez l'enfant victime)</li>"
             "<li><strong>Évaluation du risque de récidive</strong> : à l'aide d'outils actuariels validés "
             "scientifiquement</li>"
             "<li><strong>Accompagnement des victimes</strong> : évaluation du psychotraumatisme</li></ul>"),
            ("Profilage criminel : mythe et réalité",
             "<p>Contrairement à l'image médiatique (séries policières), le profilage criminel n'est "
             "<strong>pas une science exacte</strong> permettant de deviner l'apparence d'un suspect à partir "
             "d'indices minimes. Les études contrôlées montrent que les profileurs professionnels ne sont "
             "statistiquement pas plus précis que des policiers expérimentés sans formation spécifique — le "
             "profilage reste un outil d'aide à l'enquête, pas une preuve.</p>"),
            ("Facteurs de risque du comportement délinquant",
             "<p>La recherche identifie des facteurs de risque multiples (et non déterministes) : exposition "
             "précoce à la violence, carences éducatives, troubles du contrôle des impulsions, influence des "
             "pairs délinquants, précarité sociale. Aucun facteur seul n'est prédictif : c'est "
             "<strong>l'accumulation</strong> de plusieurs facteurs de risque, non compensés par des facteurs de "
             "protection, qui augmente la probabilité de comportements délinquants.</p>"),
        ],
        "figures": ["portrait-lombroso.jpg:Cesare Lombroso"],
        "pdfs": [
            {"title": "L'homme criminel", "author": "Cesare Lombroso (1887)", "path": f"{PDF}/psychologie-legale/lombroso-homme-criminel-1887.pdf",
             "desc": "Un document historique majeur (à lire avec recul critique) sur la naissance de la criminologie et ses dérives."},
        ],
        "fun_fact": "Des études d'exonération basées sur les tests ADN aux États-Unis ont montré que le <strong>témoignage oculaire erroné</strong> est la cause la plus fréquente de condamnations injustes — impliqué dans près de 70 % des cas étudiés.",
        "flashcards": [
            ("Que défendait Lombroso avec sa théorie du « criminel-né » ?", "Que certains individus seraient identifiables comme criminels par des traits physiques — théorie aujourd'hui totalement réfutée."),
            ("Quels facteurs influencent la fiabilité d'un témoignage oculaire ?", "La façon de poser les questions, le stress, la présence d'une arme, le délai avant témoignage."),
            ("Le profilage criminel est-il une science exacte ?", "Non : les études montrent qu'il n'est pas plus fiable qu'une enquête policière classique."),
            ("Que fait un psychologue expert en évaluation de risque de récidive ?", "Il utilise des outils actuariels validés scientifiquement pour estimer le risque."),
            ("Comment les facteurs de risque délinquants agissent-ils ?", "Par accumulation : c'est le cumul de plusieurs facteurs non compensés qui augmente le risque, pas un facteur isolé."),
        ],
    },
    {
        "id": "16-comparee",
        "icon": "🐾", "color": "or", "num": "16",
        "title": "Psychologie Comparée & Éthologie",
        "subtitle": "Ce que les animaux nous apprennent sur l'esprit",
        "read_time": "12 min",
        "objectives": [
            "Comprendre l'apport de Darwin à la psychologie comparée",
            "Découvrir les expériences fondatrices de Pavlov",
            "Connaître les grandes découvertes en cognition animale",
            "Comprendre les principes de l'éthologie (Lorenz)",
        ],
        "sections": [
            ("Darwin, précurseur de la psychologie comparée",
             "<p>En affirmant une <strong>continuité</strong> entre les émotions humaines et animales, Darwin "
             "pose les fondations de la psychologie comparée : étudier les animaux n'est pas seulement utile "
             "pour eux-mêmes, mais éclaire aussi la <strong>nature humaine</strong> par ses racines "
             "évolutives communes.</p>"),
            ("Pavlov et les chiens qui salivent",
             "<p>Les expériences de <strong>Pavlov</strong> sur le conditionnement (voir chapitre Éducation) "
             "ont été menées sur des chiens, mais leurs conclusions se sont révélées universelles, s'appliquant "
             "aussi bien aux humains — une découverte majeure de la psychologie comparée : les mécanismes "
             "d'apprentissage de base sont largement <strong>partagés entre espèces</strong>.</p>"),
            ("L'intelligence animale : au-delà de l'instinct",
             "<p>Des recherches modernes révèlent des capacités cognitives insoupçonnées chez de nombreuses "
             "espèces :</p>"
             "<ul><li><strong>Corbeaux et corneilles</strong> : fabrication d'outils, résolution de problèmes "
             "complexes (parfois comparable à un enfant de 5-7 ans)</li>"
             "<li><strong>Grands singes</strong> : reconnaissance de soi au miroir, apprentissage de langages "
             "des signes rudimentaires (Washoe, Koko)</li>"
             "<li><strong>Dauphins</strong> : communication complexe, coopération stratégique</li>"
             "<li><strong>Pieuvres</strong> : résolution de problèmes malgré un système nerveux très différent "
             "du nôtre — preuve que l'intelligence peut émerger par des voies évolutives multiples</li></ul>"),
            ("L'éthologie de Konrad Lorenz",
             "<p><strong>Konrad Lorenz</strong> fonde l'éthologie moderne en étudiant les comportements innés "
             "des animaux dans leur milieu naturel. Sa découverte de l'<strong>empreinte</strong> "
             "(imprinting) — le lien d'attachement immédiat que développent certains oisillons envers la "
             "première figure mobile rencontrée après la naissance — a directement influencé les théories de "
             "l'attachement en psychologie humaine (Bowlby s'en inspirera fortement).</p>"),
            ("Pourquoi étudier les animaux éclaire l'esprit humain",
             "<p>La psychologie comparée permet de :</p>"
             "<ul><li>Isoler des mécanismes fondamentaux (apprentissage, mémoire) sans la complexité du "
             "langage humain</li>"
             "<li>Étudier expérimentalement des questions impossibles à tester chez l'humain pour des raisons "
             "éthiques</li>"
             "<li>Comprendre les racines évolutives de nos propres comportements sociaux et émotionnels</li></ul>"),
        ],
        "figures": ["portrait-darwin.jpg:Charles Darwin", "portrait-pavlov.jpg:Ivan Pavlov", "portrait-lorenz.jpg:Konrad Lorenz"],
        "pdfs": [
            {"title": "L'expression des émotions chez l'homme et les animaux", "author": "Charles Darwin (trad. 1877)", "path": f"{PDF}/psychologie-comparative/darwin-expression-emotions-1877.pdf",
             "desc": "Un ouvrage richement illustré comparant les expressions émotionnelles humaines et animales."},
        ],
        "fun_fact": "Les corbeaux calédoniens peuvent fabriquer des outils <strong>en plusieurs étapes</strong> pour atteindre de la nourriture inaccessible — une prouesse cognitive que l'on croyait autrefois réservée aux grands singes et aux humains.",
        "flashcards": [
            ("Quelle est la thèse centrale de Darwin sur les émotions animales et humaines ?", "Il existe une continuité évolutive entre les émotions humaines et animales."),
            ("Qu'est-ce que l'empreinte (imprinting) découverte par Lorenz ?", "L'attachement immédiat qu'un oisillon développe envers la première figure mobile rencontrée après la naissance."),
            ("Quel animal a démontré une fabrication d'outils en plusieurs étapes ?", "Le corbeau calédonien."),
            ("Pourquoi étudier le conditionnement chez les chiens éclaire-t-il la psychologie humaine ?", "Parce que les mécanismes d'apprentissage de base sont largement partagés entre les espèces."),
            ("Quel est un avantage éthique de la psychologie comparée ?", "Elle permet d'étudier expérimentalement des questions impossibles à tester chez l'humain pour des raisons éthiques."),
        ],
    },
]

DICTIONNAIRE = [
    ("Abandon", "Sentiment de rejet ou de perte affective, souvent lié aux premières relations d'attachement.", "05-developpement"),
    ("Aboulie", "Incapacité pathologique à agir ou à décider, étudiée par Ribot.", "06-personnalite"),
    ("Addiction", "Dépendance comportementale ou à une substance, impliquant tolérance et syndrome de sevrage.", "09-psychopathologie"),
    ("Agoraphobie", "Peur intense des espaces ouverts ou des situations d'où il est difficile de s'échapper.", "09-psychopathologie"),
    ("Amygdale", "Structure cérébrale clé dans le traitement de la peur et des émotions négatives.", "08-neurosciences"),
    ("Anxiété", "Réaction émotionnelle anticipée face à une menace perçue, associée à tension et évitement.", "09-psychopathologie"),
    ("Attachement", "Lien affectif durable entre l'enfant et sa figure de soin, théorisé par Bowlby.", "05-developpement"),
    ("Autisme (TSA)", "Trouble du neurodéveloppement affectant la communication et les interactions sociales.", "09-psychopathologie"),
    ("Automatisme psychologique", "Concept de Janet désignant des comportements échappant au contrôle conscient.", "09-psychopathologie"),
    ("Behaviorisme", "École de pensée étudiant exclusivement le comportement observable.", "02-histoire"),
    ("Biais cognitif", "Erreur systématique de jugement issue des raccourcis mentaux (heuristiques).", "03-cognitive"),
    ("Big Five (OCEAN)", "Modèle des 5 grands traits de personnalité : Ouverture, Conscienciosité, Extraversion, Agréabilité, Névrosisme.", "06-personnalite"),
    ("Burn-out", "Épuisement professionnel : fatigue extrême, cynisme, perte d'accomplissement.", "12-travail"),
    ("Charge mentale", "Travail cognitif invisible de gestion et d'anticipation du quotidien.", "04-sociale"),
    ("Coaching (positif)", "Accompagnement visant à développer le potentiel et les ressources d'une personne.", "11-positive"),
    ("Cognition", "Ensemble des processus mentaux : perception, mémoire, langage, raisonnement.", "03-cognitive"),
    ("Coping", "Ensemble des stratégies mises en œuvre pour faire face à une situation stressante.", "14-sante"),
    ("Conditionnement classique", "Apprentissage par association entre un stimulus neutre et un stimulus déclencheur (Pavlov).", "13-education"),
    ("Conditionnement opérant", "Apprentissage par les conséquences d'un comportement (Skinner).", "13-education"),
    ("Conscience", "Capacité d'être conscient de soi et de son environnement.", "01-fondamentaux"),
    ("Dépression", "Trouble de l'humeur caractérisé par une tristesse persistante et une perte d'intérêt.", "09-psychopathologie"),
    ("Diffusion de responsabilité", "Tendance à moins intervenir en présence de nombreux témoins.", "04-sociale"),
    ("Dopamine", "Neurotransmetteur impliqué dans la motivation, la récompense et le mouvement.", "08-neurosciences"),
    ("Dyslexie", "Trouble spécifique de l'apprentissage de la lecture.", "05-developpement"),
    ("EMDR", "Thérapie par mouvements oculaires, efficace pour le trauma.", "10-therapies"),
    ("Empathie", "Capacité à comprendre et partager les émotions d'autrui.", "07-emotions"),
    ("Empreinte (imprinting)", "Attachement immédiat d'un jeune animal à la première figure mobile perçue (Lorenz).", "16-comparee"),
    ("Fonctionnalisme", "Courant étudiant l'utilité adaptative des fonctions mentales (James).", "02-histoire"),
    ("Flow", "État d'absorption optimale dans une activité (Csikszentmihalyi).", "11-positive"),
    ("Hippocampe", "Structure cérébrale essentielle à la formation des souvenirs.", "08-neurosciences"),
    ("Hystérie", "Ancien terme désignant des troubles fonctionnels sans cause organique, étudiés par Charcot et Janet.", "09-psychopathologie"),
    ("Identité sociale", "Théorie expliquant la préférence pour son propre groupe (Tajfel).", "04-sociale"),
    ("Inconscient", "Processus mentaux hors du champ de la conscience (Freud).", "10-therapies"),
    ("Intelligences multiples", "Théorie de Gardner postulant 8 formes distinctes d'intelligence.", "06-personnalite"),
    ("Leadership transformationnel", "Style de leadership fondé sur la vision et l'inspiration.", "12-travail"),
    ("Locus de contrôle", "Tendance à attribuer les événements à des causes internes ou externes.", "06-personnalite"),
    ("Loi de régression (Ribot)", "Dans l'amnésie, les souvenirs récents disparaissent avant les anciens.", "09-psychopathologie"),
    ("Mémoire de travail", "Système de mémoire actif permettant de manipuler temporairement l'information.", "03-cognitive"),
    ("Mindfulness", "Pleine conscience : attention non-jugeante portée au moment présent.", "10-therapies"),
    ("Motivation intrinsèque", "Motivation qui vient du plaisir de l'activité elle-même.", "07-emotions"),
    ("Neuroplasticité", "Capacité du cerveau à se réorganiser tout au long de la vie.", "08-neurosciences"),
    ("Névrose", "Ancien terme désignant des troubles psychiques sans altération du rapport à la réalité.", "09-psychopathologie"),
    ("PERMA", "Modèle du bien-être de Seligman : émotions positives, engagement, relations, sens, accomplissement.", "11-positive"),
    ("Personnalité", "Ensemble stable de traits caractérisant un individu.", "06-personnalite"),
    ("Phobie", "Peur intense et irrationnelle d'un objet ou d'une situation spécifique.", "09-psychopathologie"),
    ("Placebo", "Effet thérapeutique observé malgré l'absence de principe actif.", "10-therapies"),
    ("Profilage criminel", "Technique d'aide à l'enquête, non une science exacte de prédiction.", "15-legale"),
    ("Psychanalyse", "Courant fondé par Freud, centré sur l'inconscient et le transfert.", "10-therapies"),
    ("Psychopathologie", "Étude scientifique des troubles mentaux.", "09-psychopathologie"),
    ("Psychose", "État caractérisé par une perte de contact avec la réalité (hallucinations, délires).", "09-psychopathologie"),
    ("PTSD (état de stress post-traumatique)", "Trouble consécutif à un événement traumatique vécu ou observé.", "09-psychopathologie"),
    ("Renforcement", "Conséquence d'un comportement qui augmente sa probabilité de répétition.", "13-education"),
    ("Résilience", "Capacité à s'adapter positivement face à l'adversité.", "11-positive"),
    ("Schizophrénie", "Trouble psychotique majeur combinant symptômes positifs et négatifs.", "09-psychopathologie"),
    ("Sentiment d'auto-efficacité", "Croyance en sa propre capacité à réussir une action (Bandura).", "14-sante"),
    ("Sérotonine", "Neurotransmetteur impliqué dans l'humeur, le sommeil et l'appétit.", "08-neurosciences"),
    ("Stéréotype", "Croyance généralisée, souvent simplifiée, à propos d'un groupe social.", "04-sociale"),
    ("Stress", "Réponse physiologique et psychologique à une demande de l'environnement.", "14-sante"),
    ("Structuralisme", "Premier courant scientifique de la psychologie, fondé par Wundt.", "02-histoire"),
    ("TCC (Thérapie cognitivo-comportementale)", "Approche thérapeutique centrée sur les pensées et comportements, la plus validée empiriquement.", "10-therapies"),
    ("Testing effect", "Amélioration de la mémorisation par le rappel actif plutôt que la relecture passive.", "13-education"),
    ("Théorie de l'esprit", "Capacité à comprendre que les autres ont des croyances différentes des siennes.", "05-developpement"),
    ("Transfert", "Projection de sentiments passés du patient sur son thérapeute (psychanalyse).", "10-therapies"),
    ("Zone proximale de développement", "Écart entre ce qu'un enfant sait faire seul et avec l'aide d'autrui (Vygotsky).", "05-developpement"),
]
