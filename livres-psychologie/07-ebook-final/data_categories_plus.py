# -*- coding: utf-8 -*-
"""Nouvelles catégories (17 à 27) venant compléter les 16 catégories fondatrices."""

from data_science_psycho import CATEGORY_SCIENCE

IMG = "../../05-larousse-illustre-complet/illustrations/wikimedia"
PDF = "../../06-pdf-domaine-public"

CATEGORIES_PLUS = [
    {
        "id": "17-interculturelle",
        "icon": "🌍", "color": "or", "num": "17",
        "title": "Psychologie Interculturelle",
        "subtitle": "Ce qui est universel, ce qui est culturel — et pourquoi la distinction compte",
        "read_time": "16 min",
        "objectives": [
            "Distinguer les processus psychologiques universels de ceux façonnés par la culture",
            "Maîtriser les dimensions culturelles de Hofstede et le clivage individualisme/collectivisme",
            "Comprendre le biais WEIRD et ses conséquences sur la validité des connaissances",
            "Savoir décrire les phases de l'acculturation et du choc culturel",
        ],
        "sections": [
            ("Pourquoi la culture change la psychologie",
             "<p>Pendant un siècle, la psychologie a considéré ses résultats comme valables pour l'espèce humaine entière. "
             "En 2010, Joseph Henrich et ses collègues montrent que <strong>96 % des participants aux études publiées</strong> "
             "proviennent de pays occidentaux, éduqués, industrialisés, riches et démocratiques — les sociétés "
             "<strong>WEIRD</strong> (<em>Western, Educated, Industrialized, Rich, Democratic</em>), soit environ 12 % de l'humanité.</p>"
             "<p>Le problème n'est pas seulement statistique. Sur de nombreuses tâches, les populations WEIRD sont "
             "<strong>atypiques</strong>, y compris sur des mécanismes réputés élémentaires : sensibilité à l'illusion de "
             "Müller-Lyer, raisonnement analytique contre raisonnement holistique, conception du soi, notions d'équité. "
             "Autrement dit, une partie de ce que nous appelions « la nature humaine » décrivait en réalité une culture particulière.</p>"),
            ("Les dimensions culturelles de Hofstede",
             "<p>À partir d'une enquête menée auprès de plus de 100 000 salariés d'IBM dans 50 pays, Geert Hofstede a "
             "dégagé six dimensions permettant de comparer les cultures nationales :</p>"
             "<ul>"
             "<li><strong>Distance hiérarchique</strong> : degré d'acceptation d'une répartition inégale du pouvoir. Élevée en "
             "Malaisie ou en France, faible au Danemark ou en Israël.</li>"
             "<li><strong>Individualisme / collectivisme</strong> : le soi se définit-il comme indépendant ou comme membre d'un groupe ?</li>"
             "<li><strong>Masculinité / féminité</strong> : valorisation de la compétition et de la réussite, ou de la coopération et de la qualité de vie.</li>"
             "<li><strong>Évitement de l'incertitude</strong> : tolérance à l'ambiguïté et besoin de règles explicites (très élevé en Grèce et au Portugal).</li>"
             "<li><strong>Orientation à long terme</strong> : épargne et persévérance contre satisfaction immédiate et respect des traditions.</li>"
             "<li><strong>Indulgence / retenue</strong> : liberté accordée à la satisfaction des désirs.</li>"
             "</ul>"
             "<p>Limite majeure : assimiler une nation à une culture homogène est une simplification. Les variations "
             "à l'intérieur d'un pays sont souvent plus grandes qu'entre pays.</p>"),
            ("Soi indépendant, soi interdépendant",
             "<p>Markus et Kitayama (1991) ont montré que la conception même du soi varie :</p>"
             "<ul>"
             "<li><strong>Soi indépendant</strong> (plutôt occidental) : je suis défini par mes attributs stables, mes goûts, mes "
             "choix. Se distinguer est valorisé. « La roue qui grince reçoit la graisse. »</li>"
             "<li><strong>Soi interdépendant</strong> (plutôt est-asiatique) : je suis défini par mes relations, mes rôles et ma "
             "place dans un ensemble. S'ajuster est valorisé. « Le clou qui dépasse reçoit le marteau. »</li>"
             "</ul>"
             "<p>Cette différence a des conséquences mesurables : styles d'attribution causale, expression des émotions, "
             "motivation au travail, préférence pour le choix personnel, et jusqu'à la manière de décrire une scène visuelle "
             "(les participants japonais rapportent davantage le contexte, les participants américains l'objet central).</p>"),
            ("Acculturation et choc culturel",
             "<p>John Berry décrit quatre stratégies d'acculturation, selon que la personne conserve sa culture d'origine et "
             "qu'elle adopte celle du pays d'accueil :</p>"
             "<ul>"
             "<li><strong>Intégration</strong> : conserver et adopter. Stratégie associée au meilleur bien-être psychologique.</li>"
             "<li><strong>Assimilation</strong> : abandonner sa culture d'origine au profit de la nouvelle.</li>"
             "<li><strong>Séparation</strong> : conserver sa culture et rejeter la nouvelle.</li>"
             "<li><strong>Marginalisation</strong> : perdre l'une sans acquérir l'autre. Stratégie associée à la plus forte détresse.</li>"
             "</ul>"
             "<p>Le <strong>choc culturel</strong> suit classiquement une courbe en U : lune de miel, crise, ajustement, adaptation. "
             "Le choc du retour au pays est souvent plus déstabilisant que le départ, car il n'est pas anticipé.</p>"),
            ("Culture et santé mentale",
             "<p>Les troubles psychiques existent partout, mais leur expression, leur interprétation et leur prise en charge "
             "varient fortement. On parle d'<strong>idiomes culturels de détresse</strong> : en Asie du Sud-Est, la dépression "
             "s'exprime souvent par des plaintes somatiques plutôt que par la tristesse verbalisée.</p>"
             "<p>Certains syndromes sont propres à un contexte culturel : le <em>taijin kyofusho</em> japonais (peur d'incommoder "
             "autrui par son apparence ou son odeur), l'<em>ataque de nervios</em> latino-américain, le <em>koro</em> en Asie du Sud-Est. "
             "Le DSM-5 intègre désormais un entretien de formulation culturelle pour éviter les erreurs de diagnostic.</p>"
             "<p>Conséquence pratique : un test étalonné sur une population ne peut pas être appliqué tel quel à une autre. "
             "La traduction ne suffit pas, il faut une <strong>validation transculturelle</strong> complète.</p>"),
            ("Communication interculturelle",
             "<p>Edward T. Hall distingue les cultures à <strong>contexte fort</strong> (Japon, pays arabes, France dans une "
             "certaine mesure), où le sens réside largement dans l'implicite, la relation et le non-verbal, et les cultures à "
             "<strong>contexte faible</strong> (Allemagne, Scandinavie, États-Unis), où le message doit être explicite.</p>"
             "<p>Il décrit aussi deux rapports au temps : <strong>monochronique</strong> (une tâche à la fois, ponctualité, "
             "planification) et <strong>polychronique</strong> (plusieurs activités simultanées, souplesse, priorité à la relation). "
             "Beaucoup de malentendus professionnels internationaux naissent de ces écarts, interprétés à tort comme "
             "des manques de respect ou de sérieux.</p>"),
        ],
        "figures": ["portrait-darwin.jpg:Charles Darwin"],
        "pdfs": [
            {"title": "Le Suicide : étude de sociologie", "author": "Émile Durkheim (1897)",
             "path": f"{PDF}/psychologie-sociale/durkheim-le-suicide-1897.pdf",
             "desc": "L'étude fondatrice montrant comment les structures sociales et culturelles déterminent les conduites individuelles."},
        ],
        "fun_fact": "L'illusion de Müller-Lyer (deux lignes de même longueur avec des flèches opposées) trompe massivement les Occidentaux, mais beaucoup moins les San du Kalahari : notre perception elle-même a été façonnée par un environnement plein d'angles droits, celui des bâtiments.",
        "flashcards": [
            ("Que signifie l'acronyme WEIRD ?", "Western, Educated, Industrialized, Rich, Democratic : les sociétés surreprésentées dans les études de psychologie."),
            ("Quelle stratégie d'acculturation est associée au meilleur bien-être ?", "L'intégration : conserver sa culture d'origine tout en adoptant celle du pays d'accueil."),
            ("Qu'est-ce qu'un soi interdépendant ?", "Une conception de soi définie par les relations, les rôles et l'appartenance au groupe plutôt que par des attributs individuels."),
            ("Quelle dimension de Hofstede mesure la tolérance à l'ambiguïté ?", "L'évitement de l'incertitude."),
            ("Qu'est-ce qu'une culture à contexte fort selon Hall ?", "Une culture où l'essentiel du message passe par l'implicite, la relation et le non-verbal."),
        ],
    },
    {
        "id": "18-langage",
        "icon": "🗣️", "color": "vert", "num": "18",
        "title": "Psycholinguistique & Langage",
        "subtitle": "Comment nous acquérons, produisons et comprenons la parole",
        "read_time": "16 min",
        "objectives": [
            "Retracer les étapes de l'acquisition du langage chez l'enfant",
            "Comprendre le débat inné/acquis entre Chomsky, Skinner et les approches actuelles",
            "Connaître l'architecture cérébrale du langage et les aphasies",
            "Évaluer sérieusement l'hypothèse de la relativité linguistique",
        ],
        "sections": [
            ("L'acquisition du langage, étape par étape",
             "<p>Aucun apprentissage humain n'est aussi rapide et aussi universel. Sans enseignement explicite, presque tous "
             "les enfants maîtrisent en quatre ans un système d'une complexité vertigineuse.</p>"
             "<ul>"
             "<li><strong>0-2 mois</strong> : cris, vocalisations réflexes. Le nouveau-né discrimine déjà tous les phonèmes de "
             "toutes les langues du monde.</li>"
             "<li><strong>2-6 mois</strong> : gazouillis, jeux vocaux, tours de parole avec l'adulte.</li>"
             "<li><strong>6-10 mois</strong> : babillage canonique (« bababa »). L'enfant perd progressivement la capacité à "
             "distinguer les sons absents de sa langue maternelle — une spécialisation, pas une perte.</li>"
             "<li><strong>12 mois</strong> : premiers mots, souvent précédés de gestes de pointage.</li>"
             "<li><strong>18-24 mois</strong> : explosion lexicale (jusqu'à 10 mots nouveaux par jour), premières combinaisons.</li>"
             "<li><strong>2-3 ans</strong> : phrases de trois mots et plus, surgénéralisations révélatrices (« il a prendu ») "
             "qui prouvent que l'enfant applique des règles au lieu d'imiter.</li>"
             "<li><strong>4-6 ans</strong> : maîtrise de la syntaxe complexe, récits structurés, humour verbal.</li>"
             "</ul>"),
            ("Chomsky contre Skinner : le débat fondateur",
             "<p>En 1957, Skinner explique le langage comme un comportement verbal appris par renforcement. Deux ans plus tard, "
             "Chomsky publie une recension dévastatrice : l'enfant produit des phrases qu'il n'a jamais entendues, "
             "et la parole qu'il reçoit est trop pauvre et trop irrégulière pour expliquer la grammaire qu'il acquiert. "
             "C'est l'argument de la <strong>pauvreté du stimulus</strong>.</p>"
             "<p>Chomsky postule une <strong>grammaire universelle</strong> innée. Les approches actuelles sont plus nuancées : "
             "les modèles fondés sur l'usage (Tomasello) montrent que l'enfant extrait des régularités statistiques d'un "
             "flux de parole bien plus riche qu'on ne le croyait, grâce à des capacités d'attention conjointe et de lecture "
             "d'intention. Le langage serait moins un module isolé qu'une fonction émergeant d'aptitudes sociales et cognitives générales.</p>"),
            ("Le cerveau du langage",
             "<p>Le modèle classique repose sur deux régions de l'hémisphère gauche :</p>"
             "<ul>"
             "<li><strong>Aire de Broca</strong> (frontal inférieur gauche) : production. Son atteinte donne une aphasie non fluente : "
             "parole laborieuse, télégraphique, agrammatique, avec une compréhension relativement préservée — et une conscience "
             "douloureuse du trouble.</li>"
             "<li><strong>Aire de Wernicke</strong> (temporal supérieur gauche) : compréhension. Son atteinte produit une aphasie fluente : "
             "débit normal voire logorrhéique, mais discours vide, paraphasies, néologismes, et compréhension altérée — souvent "
             "sans que la personne perçoive le problème.</li>"
             "</ul>"
             "<p>Ce modèle est aujourd'hui enrichi par une conception en deux voies : une voie dorsale reliant son et articulation, "
             "une voie ventrale reliant son et signification. L'hémisphère droit n'est pas muet : il porte la prosodie, l'ironie, "
             "les métaphores et la cohérence du récit.</p>"),
            ("Lire : une invention récente que le cerveau bricole",
             "<p>Le langage oral a des centaines de milliers d'années ; l'écriture en a environ 5 000. Aucun circuit cérébral n'a "
             "pu évoluer pour lire. Selon l'hypothèse du <strong>recyclage neuronal</strong> (Dehaene), la lecture réutilise une "
             "région spécialisée dans la reconnaissance des formes visuelles, qui devient la « boîte aux lettres du cerveau » "
             "(aire de la forme visuelle des mots, dans le temporal-occipital gauche).</p>"
             "<p>Apprendre à lire suppose de développer la <strong>conscience phonologique</strong> : comprendre que la parole se "
             "découpe en unités abstraites. C'est un déficit de ce traitement phonologique qui explique l'essentiel des dyslexies. "
             "Les comparaisons internationales montrent que les méthodes fondées sur le décodage explicite des correspondances "
             "graphème-phonème sont plus efficaces que les approches globales.</p>"),
            ("Bilinguisme : mythes et réalités",
             "<p>Le bilinguisme précoce n'entraîne ni retard durable, ni confusion pathologique. On observe un vocabulaire un peu "
             "plus réduit dans chaque langue prise isolément, mais un vocabulaire total équivalent ou supérieur. "
             "L'alternance de codes (<em>code-switching</em>) est un signe de maîtrise, pas de confusion.</p>"
             "<p>L'« avantage cognitif bilingue » sur le contrôle exécutif, longtemps présenté comme acquis, est fortement débattu : "
             "les effets sont faibles, inconstants, et affectés par un biais de publication. En revanche, les données sur un "
             "<strong>report de quelques années de l'apparition des symptômes démentiels</strong> chez les bilingues de longue "
             "date restent relativement robustes.</p>"),
            ("La langue façonne-t-elle la pensée ?",
             "<p>L'hypothèse Sapir-Whorf, dans sa version forte (la langue détermine la pensée), est abandonnée. Sa version faible "
             "— la langue oriente l'attention et facilite certains traitements — est aujourd'hui soutenue par des données solides :</p>"
             "<ul>"
             "<li>Les locuteurs du russe, qui disposent de deux mots distincts pour le bleu clair et le bleu foncé, discriminent "
             "plus rapidement ces nuances.</li>"
             "<li>Les Kuuk Thaayorre d'Australie, dont la langue utilise les points cardinaux au lieu de « gauche » et « droite », "
             "conservent une orientation spatiale remarquable et se représentent le temps d'est en ouest.</li>"
             "<li>Le genre grammatical des objets influence les adjectifs spontanément associés (un pont est décrit comme "
             "« élégant » par des germanophones, « robuste » par des hispanophones).</li>"
             "</ul>"
             "<p>La langue n'emprisonne pas la pensée : elle rend certains chemins plus faciles que d'autres.</p>"),
        ],
        "figures": ["cerveau-lobes-fr.svg:Les lobes cérébraux"],
        "pdfs": [
            {"title": "Précis de psychologie", "author": "William James (1909)",
             "path": f"{PDF}/psychologie-generale/james-precis-de-psychologie-1909.pdf",
             "desc": "Contient des chapitres classiques sur la parole, l'association d'idées et la formation des concepts."},
        ],
        "fun_fact": "À 6 mois, un bébé distingue tous les phonèmes de toutes les langues humaines. À 12 mois, il n'entend plus que ceux de sa langue maternelle : un adulte japonais qui peine avec « r » et « l » ne souffre pas d'un défaut d'oreille, il a été optimisé pour une autre langue.",
        "flashcards": [
            ("Que révèlent les erreurs comme « il a prendu » ?", "Que l'enfant applique des règles grammaticales productives, au lieu de simplement imiter ce qu'il entend."),
            ("Quelle aphasie donne une parole fluente mais vide de sens ?", "L'aphasie de Wernicke, par atteinte de l'aire temporale supérieure gauche."),
            ("Qu'est-ce que l'argument de la pauvreté du stimulus ?", "L'idée de Chomsky selon laquelle la parole entendue est insuffisante pour expliquer la grammaire acquise par l'enfant."),
            ("Qu'est-ce que le recyclage neuronal ?", "L'hypothèse selon laquelle la lecture réutilise un circuit visuel évolué pour la reconnaissance des formes."),
            ("La version forte de l'hypothèse Sapir-Whorf est-elle validée ?", "Non. Seule la version faible — la langue oriente l'attention et facilite certains traitements — est soutenue."),
        ],
    },
    {
        "id": "19-psychometrie",
        "icon": "📏", "color": "gris", "num": "19",
        "title": "Psychométrie & Mesure",
        "subtitle": "Mesurer l'invisible : intelligence, personnalité, aptitudes",
        "read_time": "15 min",
        "objectives": [
            "Comprendre ce que sont la fidélité, la validité et l'étalonnage d'un test",
            "Savoir lire un score de QI et connaître les limites de cette mesure",
            "Distinguer les tests scientifiquement solides des instruments douteux",
            "Situer les enjeux éthiques et sociaux de la mesure psychologique",
        ],
        "sections": [
            ("Les trois qualités d'un bon test",
             "<p>Un instrument psychométrique n'a de valeur que s'il satisfait trois exigences, vérifiables statistiquement :</p>"
             "<ul>"
             "<li><strong>La fidélité</strong> : le test mesure de façon stable. On la vérifie par la cohérence interne (alpha de "
             "Cronbach), la stabilité temporelle (test-retest) et l'accord entre évaluateurs. Un pèse-personne qui affiche "
             "trois poids différents en trois minutes n'est pas fidèle.</li>"
             "<li><strong>La validité</strong> : le test mesure bien ce qu'il prétend mesurer. Validité de contenu, de critère "
             "(prédit-il quelque chose de réel ?) et de construit. Un pèse-personne fidèle qui affiche toujours 10 kg de trop "
             "est fidèle mais non valide.</li>"
             "<li><strong>L'étalonnage</strong> : un score brut ne veut rien dire sans comparaison à un groupe de référence "
             "représentatif, actualisé et pertinent culturellement.</li>"
             "</ul>"),
            ("Comment lire un QI",
             "<p>Le QI est une position relative, pas une quantité absolue d'intelligence. Les échelles de Wechsler fixent la "
             "moyenne à 100 avec un écart-type de 15 :</p>"
             "<ul>"
             "<li>68 % de la population se situe entre 85 et 115</li>"
             "<li>95 % entre 70 et 130</li>"
             "<li>Environ 2,3 % au-dessus de 130 (haut potentiel), 2,3 % en dessous de 70</li>"
             "</ul>"
             "<p>Trois précautions essentielles. D'abord, tout score s'accompagne d'un <strong>intervalle de confiance</strong> "
             "(± 5 points environ) : 112 et 116 ne sont pas différents. Ensuite, un QI total n'a de sens que si les indices "
             "(compréhension verbale, raisonnement, mémoire de travail, vitesse) sont homogènes ; en cas d'écarts importants, "
             "le score global devient trompeur et c'est le profil qui compte. Enfin, le QI prédit une partie de la réussite "
             "scolaire, mais laisse l'essentiel de la variance inexpliquée : motivation, conscienciosité, milieu, santé et "
             "opportunités pèsent au moins autant.</p>"),
            ("Le modèle en g, les intelligences multiples et l'effet Flynn",
             "<p>Spearman a remarqué en 1904 que les performances à des épreuves très différentes sont positivement corrélées, "
             "ce qui l'a conduit à postuler un facteur général <strong>g</strong>. Cattell a ensuite distingué l'intelligence "
             "<strong>fluide</strong> (raisonner sur du nouveau, qui décline avec l'âge) et <strong>cristallisée</strong> "
             "(connaissances accumulées, stable ou croissante). Le modèle CHC, qui organise une dizaine d'aptitudes larges, "
             "est aujourd'hui le cadre de référence des tests modernes.</p>"
             "<p>La théorie des <strong>intelligences multiples</strong> de Gardner, très populaire en pédagogie, n'a jamais reçu "
             "de validation psychométrique : les « intelligences » proposées corrèlent entre elles et ressemblent davantage à "
             "des talents. Son mérite est d'avoir élargi le regard des enseignants, pas d'avoir remplacé le modèle scientifique.</p>"
             "<p>L'<strong>effet Flynn</strong> désigne la hausse continue des scores bruts au cours du XXe siècle — environ "
             "3 points par décennie — trop rapide pour être génétique. Scolarisation, nutrition, familiarité avec le raisonnement "
             "abstrait et complexité de l'environnement l'expliquent. Depuis les années 2000, l'effet s'inverse dans plusieurs pays "
             "nordiques, sans explication consensuelle.</p>"),
            ("Ce qui distingue un vrai test d'un test de magazine",
             "<p>Cinq critères permettent de trancher rapidement :</p>"
             "<ul>"
             "<li><strong>Qui l'a construit ?</strong> Un instrument validé s'accompagne de publications scientifiques et d'un manuel technique.</li>"
             "<li><strong>Quel étalonnage ?</strong> Sur quelle population, de quelle taille, de quelle année ?</li>"
             "<li><strong>Quelles preuves de validité prédictive ?</strong> Le test annonce-t-il quelque chose de vérifiable ?</li>"
             "<li><strong>Le résultat est-il continu ou catégoriel ?</strong> Les traits psychologiques sont continus : classer en "
             "16 types ou 4 « couleurs » crée des frontières arbitraires.</li>"
             "<li><strong>La description est-elle falsifiable ?</strong> Si le portrait pourrait convenir à presque tout le monde, "
             "c'est l'effet Barnum qui opère.</li>"
             "</ul>"
             "<p>Sur ces critères, le Big Five est solide, le MBTI et les typologies en couleurs ne le sont pas, et l'usage de ces "
             "dernières en sélection professionnelle pose un véritable problème déontologique.</p>"),
            ("Statistiques indispensables pour comprendre un résultat",
             "<p>Quelques notions permettent de lire n'importe quelle étude sans se faire abuser :</p>"
             "<ul>"
             "<li><strong>Corrélation</strong> : varie de -1 à +1. En psychologie, 0,10 est faible, 0,30 modérée, 0,50 forte. "
             "Une corrélation n'est jamais une preuve de causalité.</li>"
             "<li><strong>Taille d'effet</strong> (d de Cohen) : 0,2 petit, 0,5 moyen, 0,8 grand. Bien plus informative que le "
             "seul seuil de significativité.</li>"
             "<li><strong>Valeur p</strong> : probabilité d'observer ces données si l'hypothèse nulle est vraie. Un p < 0,05 ne "
             "signifie ni que l'effet est important, ni qu'il est réplicable.</li>"
             "<li><strong>Puissance statistique</strong> : capacité à détecter un effet réel. De nombreuses études anciennes sont "
             "sous-dimensionnées, ce qui produit à la fois des faux négatifs et des effets surestimés.</li>"
             "</ul>"),
            ("Une histoire politiquement chargée",
             "<p>La mesure de l'intelligence a servi le meilleur et le pire. Binet voulait identifier les élèves à aider ; il "
             "protestait explicitement contre l'idée d'une intelligence fixe. Aux États-Unis, ses tests ont pourtant été détournés "
             "pour justifier des quotas d'immigration, des stérilisations forcées et des politiques ségrégationnistes.</p>"
             "<p>Ce passé impose une vigilance permanente : un test est un outil d'aide à la décision, jamais un verdict sur une "
             "personne. Le code de déontologie des psychologues impose la restitution des résultats à l'intéressé, dans un langage "
             "compréhensible, et interdit l'usage d'un instrument hors de son domaine de validité.</p>"),
        ],
        "figures": ["portrait-binet.jpg:Alfred Binet", "rorschach-planche-1.jpg:Planche de Rorschach"],
        "pdfs": [
            {"title": "La Suggestibilité", "author": "Alfred Binet (1900)",
             "path": f"{PDF}/psychologie-generale/binet-suggestibilite.html",
             "desc": "Le laboratoire de Binet au travail : mesure, protocoles et prudence méthodologique avant l'invention du test d'intelligence."},
        ],
        "fun_fact": "Un QI mesuré à 4 ans ne prédit que faiblement celui du même enfant à 17 ans. La stabilité augmente fortement à partir de 7-8 ans : c'est une raison majeure de ne jamais figer un enfant dans un chiffre.",
        "flashcards": [
            ("Quelle différence entre fidélité et validité ?", "La fidélité est la stabilité de la mesure ; la validité est le fait de mesurer réellement ce qu'on prétend mesurer."),
            ("Que signifie un QI de 130 ?", "Un score situé à deux écarts-types au-dessus de la moyenne, dépassé par environ 2,3 % de la population de référence."),
            ("Qu'est-ce que l'effet Flynn ?", "La hausse continue des scores bruts aux tests d'intelligence au cours du XXe siècle, environ 3 points par décennie."),
            ("Pourquoi le MBTI est-il critiqué ?", "Faible fidélité test-retest, dichotomies artificielles alors que les traits sont continus, et validité prédictive insuffisante."),
            ("Que vaut une corrélation de 0,30 en psychologie ?", "Un effet modéré, fréquent dans la discipline — et qui n'établit aucune causalité."),
        ],
    },
    {
        "id": "20-sport",
        "icon": "🏃", "color": "or", "num": "20",
        "title": "Psychologie du Sport & Performance",
        "subtitle": "Préparation mentale, motivation, gestion de la pression",
        "read_time": "14 min",
        "objectives": [
            "Comprendre les mécanismes de la motivation durable en contexte de performance",
            "Connaître les outils validés de préparation mentale",
            "Expliquer pourquoi la performance s'effondre sous pression",
            "Transférer ces méthodes à d'autres domaines exigeants",
        ],
        "sections": [
            ("Motivation : la théorie de l'autodétermination",
             "<p>Deci et Ryan ont montré que toutes les motivations ne se valent pas. La <strong>motivation intrinsèque</strong> "
             "(pratiquer pour le plaisir de l'activité) produit une persévérance et un bien-être bien supérieurs à la "
             "<strong>motivation extrinsèque</strong> (pratiquer pour une récompense ou éviter une sanction).</p>"
             "<p>Trois besoins psychologiques fondamentaux doivent être satisfaits pour que la motivation se maintienne :</p>"
             "<ul>"
             "<li><strong>Autonomie</strong> : avoir des choix, comprendre le sens de ce que l'on fait</li>"
             "<li><strong>Compétence</strong> : percevoir ses progrès, relever des défis à sa mesure</li>"
             "<li><strong>Affiliation</strong> : se sentir relié à un groupe, un entraîneur, une communauté</li>"
             "</ul>"
             "<p>Un résultat contre-intuitif mais robuste : récompenser matériellement une activité déjà appréciée peut "
             "<strong>diminuer</strong> la motivation intrinsèque (effet de surjustification). L'activité devient un moyen "
             "d'obtenir la récompense au lieu d'être une fin en soi.</p>"),
            ("Le paradoxe de la pression : pourquoi on rate au pire moment",
             "<p>La <em>self-focus theory</em> de Sian Beilock explique l'effondrement sous pression (<em>choking</em>). Un geste "
             "surappris s'exécute de façon automatique, en dehors du contrôle conscient. Sous pression, l'athlète recommence à "
             "surveiller consciemment son geste — et ce contrôle explicite désorganise une séquence motrice qui fonctionnait "
             "parfaitement sans lui.</p>"
             "<p>D'où trois parades validées : maintenir une <strong>routine pré-performance</strong> identique quelle que soit "
             "l'importance de l'épreuve ; se focaliser sur un point <strong>externe</strong> (la cible, la trajectoire) plutôt "
             "que sur son propre corps ; et s'entraîner régulièrement en conditions de pression (public, enjeu, fatigue) pour "
             "que la situation de compétition ne soit plus une nouveauté.</p>"),
            ("Imagerie mentale : s'entraîner sans bouger",
             "<p>L'imagerie motrice active en partie les mêmes réseaux corticaux que l'exécution réelle. Répéter mentalement un "
             "geste améliore réellement la performance, avec un effet plus faible que la pratique physique, mais significatif — "
             "et particulièrement précieux en cas de blessure.</p>"
             "<p>Le modèle PETTLEP précise les conditions d'efficacité : contexte <em>Physique</em> proche du réel, "
             "<em>Environnement</em> similaire, <em>Tâche</em> identique, <em>Timing</em> en temps réel (ne pas accélérer la "
             "séquence mentale), <em>Learning</em> actualisé au niveau actuel, <em>Emotion</em> incluse, "
             "<em>Perspective</em> interne de préférence. Il faut aussi imaginer des réussites <em>et</em> la gestion des "
             "difficultés prévisibles, pas seulement le scénario parfait.</p>"),
            ("Fixation d'objectifs et discours interne",
             "<p>Le modèle SMART (spécifique, mesurable, atteignable, réaliste, temporellement défini) reste utile, mais la "
             "distinction la plus opérante en sport oppose trois types d'objectifs :</p>"
             "<ul>"
             "<li><strong>Objectifs de résultat</strong> (gagner la médaille) : motivants, mais dépendants des adversaires, donc "
             "anxiogènes et hors de contrôle.</li>"
             "<li><strong>Objectifs de performance</strong> (améliorer son chrono de 2 secondes) : contrôlables et mesurables.</li>"
             "<li><strong>Objectifs de processus</strong> (maintenir cette position de bras au dernier virage) : entièrement sous "
             "contrôle, ce sont eux qu'il faut placer au centre de l'attention en compétition.</li>"
             "</ul>"
             "<p>Le <strong>discours interne</strong> se travaille aussi. Les auto-instructions techniques (« pousse », « relâche ») "
             "améliorent les tâches précises ; les auto-encouragements motivationnels sont plus efficaces sur les tâches d'endurance "
             "et de force.</p>"),
            ("Activation, anxiété et zone de performance optimale",
             "<p>La loi de Yerkes-Dodson décrit une relation en U inversé entre activation et performance : trop peu d'éveil, on "
             "est mou ; trop d'éveil, on se désorganise. Le niveau optimal varie selon la tâche — élevé pour un sprint ou de la "
             "force, plus bas pour un tir de précision ou un putt.</p>"
             "<p>Hanin a affiné le modèle avec la <strong>zone individuelle de fonctionnement optimal</strong> : chaque athlète a "
             "sa propre plage d'activation idéale, qu'il faut identifier par l'observation plutôt que par une norme générale. "
             "Certains ont besoin de colère et de tension, d'autres de calme total. Autre distinction clé : l'anxiété "
             "<strong>cognitive</strong> (les pensées inquiètes) nuit à la performance, alors qu'une anxiété "
             "<strong>somatique</strong> modérée (cœur qui bat, mains moites) est normale et souvent utile si elle est "
             "interprétée comme de l'excitation plutôt que comme de la peur.</p>"),
            ("Ce qui se transpose hors du stade",
             "<p>Ces outils ne concernent pas que les sportifs. Musiciens, chirurgiens, pilotes, candidats à un examen ou à un "
             "entretien affrontent exactement les mêmes mécanismes.</p>"
             "<ul>"
             "<li>Écrire ses inquiétudes pendant 10 minutes avant une épreuve améliore significativement les résultats, surtout "
             "chez les personnes les plus anxieuses : la mémoire de travail est libérée.</li>"
             "<li>Réinterpréter l'activation comme de l'excitation (« je suis chaud ») plutôt que comme du stress (« je panique ») "
             "améliore réellement la performance.</li>"
             "<li>La routine pré-performance vaut pour un oral comme pour un service au tennis.</li>"
             "<li>La récupération — sommeil en particulier — fait partie de l'entraînement, pas de son interruption.</li>"
             "</ul>"),
        ],
        "figures": ["pyramide-maslow.svg:La pyramide des besoins"],
        "pdfs": [],
        "fun_fact": "Une étude classique sur les tirs au but a montré que les joueurs qui regardaient le gardien juste avant de frapper marquaient nettement moins que ceux qui fixaient l'endroit visé : l'attention portée à la menace attire littéralement le ballon vers elle.",
        "flashcards": [
            ("Quels sont les trois besoins de la théorie de l'autodétermination ?", "Autonomie, compétence et affiliation."),
            ("Qu'est-ce que l'effet de surjustification ?", "La baisse de motivation intrinsèque provoquée par l'ajout d'une récompense externe à une activité déjà appréciée."),
            ("Pourquoi rate-t-on sous pression ?", "Parce que le contrôle conscient reprend la main sur un geste automatisé et désorganise son exécution."),
            ("Quel type d'objectif faut-il privilégier en compétition ?", "Les objectifs de processus, entièrement sous notre contrôle."),
            ("Que dit la loi de Yerkes-Dodson ?", "La performance suit un U inversé en fonction du niveau d'activation : un optimum existe entre trop peu et trop."),
        ],
    },
    {
        "id": "21-consommation",
        "icon": "🛒", "color": "rose", "num": "21",
        "title": "Psychologie de la Consommation",
        "subtitle": "Comment on décide d'acheter — et comment on nous y aide",
        "read_time": "15 min",
        "objectives": [
            "Identifier les principaux leviers d'influence utilisés en marketing",
            "Comprendre l'architecture du choix et les nudges",
            "Repérer les dark patterns dans les interfaces numériques",
            "Développer des réflexes concrets de consommateur averti",
        ],
        "sections": [
            ("Les six principes d'influence de Cialdini",
             "<p>Robert Cialdini a passé trois ans infiltré dans des formations de vendeurs, de publicitaires et de collecteurs "
             "de fonds pour identifier les ressorts réellement utilisés :</p>"
             "<ul>"
             "<li><strong>Réciprocité</strong> : un cadeau, même minuscule, crée une dette. L'échantillon gratuit, le café offert "
             "en concession, le stylo joint à l'appel aux dons.</li>"
             "<li><strong>Engagement et cohérence</strong> : après un premier oui, même anodin, nous voulons rester cohérents. "
             "C'est la technique du pied dans la porte.</li>"
             "<li><strong>Preuve sociale</strong> : « 8 personnes sur 10 choisissent cette option », compteurs de vues, avis clients.</li>"
             "<li><strong>Sympathie</strong> : nous disons plus facilement oui à ceux que nous apprécions, qui nous ressemblent "
             "ou qui nous font des compliments.</li>"
             "<li><strong>Autorité</strong> : blouse blanche, titre, uniforme, « recommandé par les dentistes ».</li>"
             "<li><strong>Rareté</strong> : « plus que 2 en stock », comptes à rebours, éditions limitées.</li>"
             "</ul>"
             "<p>Cialdini a ajouté un septième principe, l'<strong>unité</strong> : l'identité partagée (« nous, les gens d'ici ») "
             "est un levier plus puissant encore que la simple sympathie.</p>"),
            ("L'architecture du choix",
             "<p>Thaler et Sunstein ont montré qu'il n'existe pas de présentation neutre d'un choix. La disposition d'un rayon, "
             "l'ordre d'une liste, le choix par défaut orientent massivement les décisions, même quand tout reste libre :</p>"
             "<ul>"
             "<li><strong>L'option par défaut</strong> est l'outil le plus puissant : les pays où le don d'organes est proposé en "
             "opt-out affichent des taux de consentement supérieurs à 90 %, contre moins de 20 % en opt-in, pour des populations "
             "culturellement proches.</li>"
             "<li><strong>L'effet leurre</strong> : ajouter une troisième option volontairement peu attractive fait basculer le "
             "choix vers l'option la plus chère des deux autres.</li>"
             "<li><strong>L'ancrage par le prix barré</strong> installe une référence qui rend le prix réel avantageux.</li>"
             "<li><strong>La réduction de friction</strong> : chaque clic supprimé augmente la conversion ; chaque clic ajouté "
             "sur le chemin de la résiliation la réduit.</li>"
             "</ul>"
             "<p>Le <em>nudge</em> est moralement neutre : il peut servir l'épargne retraite et la santé publique comme la "
             "surconsommation.</p>"),
            ("Ce qui se passe vraiment en magasin et en ligne",
             "<p>Les décisions d'achat sont largement contextuelles :</p>"
             "<ul>"
             "<li>Une musique lente augmente le temps passé en rayon et le panier moyen ; une musique d'un pays donné oriente le "
             "choix des vins de ce pays, sans que les clients en aient conscience.</li>"
             "<li>Les produits placés à hauteur des yeux se vendent nettement plus ; les emplacements sont facturés aux marques.</li>"
             "<li>Payer sans espèces réduit la « douleur de payer » et augmente les montants dépensés.</li>"
             "<li>Les prix se terminant par 9 exploitent l'encodage de gauche à droite : 19,99 € est encodé « 19 et quelque ».</li>"
             "<li>Sur les sites, la rareté affichée et les compteurs de « 14 personnes regardent cet article » exploitent "
             "rareté et preuve sociale — souvent avec des chiffres fabriqués.</li>"
             "</ul>"),
            ("Dark patterns : quand l'interface travaille contre vous",
             "<p>Le terme désigne les conceptions délibérément trompeuses. Les plus courants :</p>"
             "<ul>"
             "<li><strong>Roach motel</strong> : inscription en deux clics, résiliation en douze étapes et un appel téléphonique.</li>"
             "<li><strong>Confirmshaming</strong> : le bouton de refus est formulé pour culpabiliser (« Non merci, je préfère payer plein tarif »).</li>"
             "<li><strong>Coûts cachés</strong> révélés à la dernière étape du tunnel d'achat, après l'investissement en temps.</li>"
             "<li><strong>Cases précochées</strong> et consentements groupés.</li>"
             "<li><strong>Urgence artificielle</strong> : compte à rebours qui se réinitialise à chaque visite.</li>"
             "<li><strong>Misdirection visuelle</strong> : le bouton du choix rentable est coloré, l'autre est gris pâle.</li>"
             "</ul>"
             "<p>Le règlement européen sur les services numériques (DSA, 2024) interdit explicitement plusieurs de ces pratiques "
             "sur les grandes plateformes.</p>"),
            ("Marques, identité et fidélité",
             "<p>Une marque forte fonctionne comme un raccourci cognitif : elle réduit l'effort de décision et le risque perçu. "
             "Mais son pouvoir va plus loin. Les consommateurs choisissent des marques qui correspondent à l'image qu'ils ont "
             "d'eux-mêmes ou à celle qu'ils veulent projeter — c'est la <strong>congruence de l'image de soi</strong>.</p>"
             "<p>Les programmes de fidélité exploitent l'aversion à la perte (ne pas perdre ses points acquis) et l'effet de "
             "progression dotée : une carte de fidélité offrant deux tampons d'avance sur douze est bien plus efficace qu'une "
             "carte vierge de dix, alors que l'effort restant est identique.</p>"
             "<p>Le neuromarketing promet de lire les préférences dans le cerveau. Les résultats réels restent limités : l'imagerie "
             "prédit un peu mieux les ventes agrégées que les déclarations, mais aucun « bouton d'achat » cérébral n'a jamais été trouvé.</p>"),
            ("Se protéger : cinq réflexes pratiques",
             "<ul>"
             "<li><strong>La règle des 24 heures</strong> pour tout achat non essentiel au-dessus d'un seuil que vous définissez. "
             "Elle neutralise à la fois l'urgence artificielle et l'émotion du moment.</li>"
             "<li><strong>Nommer la technique</strong> quand vous la repérez : la reconnaissance explicite (« c'est de la rareté "
             "artificielle ») réduit fortement son effet.</li>"
             "<li><strong>Décider du budget avant de voir les prix</strong>, pour couper l'ancrage.</li>"
             "<li><strong>Comparer au prix zéro</strong> : la vraie question n'est pas « est-ce une bonne affaire ? » mais "
             "« est-ce que j'en veux à ce prix ? ».</li>"
             "<li><strong>Se méfier des économies affichées</strong> : dépenser 80 € pour en « économiser » 20 reste une dépense de 80 €.</li>"
             "</ul>"),
        ],
        "figures": ["portrait-le-bon.jpg:Gustave Le Bon"],
        "pdfs": [
            {"title": "Psychologie des foules", "author": "Gustave Le Bon (1895)",
             "path": f"{PDF}/psychologie-sociale/le-bon-psychologie-des-foules-1895-complet.pdf",
             "desc": "L'ancêtre direct des théories de l'influence de masse, lu et utilisé par les premiers publicitaires."},
        ],
        "fun_fact": "Une étude sur un étal de confitures a montré que 24 variétés attiraient six fois plus de curieux que 6 variétés — mais généraient dix fois moins d'achats. Trop de choix paralyse la décision.",
        "flashcards": [
            ("Citez trois des principes d'influence de Cialdini.", "Réciprocité, engagement/cohérence, preuve sociale, sympathie, autorité, rareté (trois au choix)."),
            ("Pourquoi l'option par défaut est-elle si puissante ?", "Parce qu'elle exploite l'inertie, le biais de statu quo et l'interprétation du défaut comme recommandation implicite."),
            ("Qu'est-ce que le confirmshaming ?", "Un dark pattern qui formule l'option de refus de façon culpabilisante pour décourager son choix."),
            ("Qu'est-ce que l'effet leurre ?", "L'ajout d'une option volontairement peu attractive qui fait basculer le choix vers une option ciblée."),
            ("Quel réflexe simple neutralise l'urgence artificielle ?", "La règle des 24 heures avant tout achat non essentiel."),
        ],
    },
    {
        "id": "22-numerique",
        "icon": "📱", "color": "vert", "num": "22",
        "title": "Psychologie du Numérique",
        "subtitle": "Écrans, réseaux sociaux, attention et santé mentale",
        "read_time": "16 min",
        "objectives": [
            "Comprendre les mécanismes de captation de l'attention des plateformes",
            "Faire le tri entre les effets démontrés et les paniques morales",
            "Connaître les dynamiques du cyberharcèlement et de la désinformation",
            "Mettre en place une hygiène numérique réaliste",
        ],
        "sections": [
            ("L'économie de l'attention",
             "<p>Quand un service est gratuit, la ressource vendue est le temps d'attention de l'utilisateur. Les interfaces sont "
             "donc optimisées non pour le bien-être mais pour l'engagement, avec des mécanismes directement issus de la "
             "psychologie de l'apprentissage :</p>"
             "<ul>"
             "<li><strong>Renforcement à ratio variable</strong> : le contenu intéressant arrive de façon imprévisible, exactement "
             "comme la récompense d'une machine à sous. C'est le programme de renforcement le plus résistant à l'extinction "
             "identifié par Skinner.</li>"
             "<li><strong>Défilement infini</strong> : supprimer le point d'arrêt naturel supprime la décision de continuer.</li>"
             "<li><strong>Lecture automatique</strong> de la vidéo suivante avant même la fin de la précédente.</li>"
             "<li><strong>Notifications</strong> : interruptions calibrées, souvent regroupées et différées pour maximiser le retour.</li>"
             "<li><strong>Métriques sociales publiques</strong> (likes, vues, séries de jours) qui transforment la relation en score.</li>"
             "</ul>"
             "<p>Ces mécanismes ne sont pas des effets secondaires : ils sont documentés, testés en A/B et optimisés.</p>"),
            ("Attention, multitâche et mémoire",
             "<p>Le multitâche attentionnel n'existe pas pour les tâches exigeantes : il s'agit de commutations rapides, dont "
             "chacune a un coût. Après une interruption, il faut en moyenne plus de vingt minutes pour retrouver un niveau de "
             "concentration équivalent. La seule présence visible d'un smartphone, même éteint, dégrade mesurablement les "
             "performances de mémoire de travail (effet de « fuite cérébrale »).</p>"
             "<p>L'<strong>effet Google</strong> décrit une modification de la stratégie mnésique : nous retenons moins bien "
             "l'information elle-même quand nous savons pouvoir la retrouver, mais mieux l'endroit où la chercher. Ce n'est pas "
             "un déficit, c'est un déplacement — comparable à ce que l'écriture avait déjà provoqué, comme le déplorait déjà "
             "Platon dans le <em>Phèdre</em>.</p>"),
            ("Réseaux sociaux et santé mentale : ce que disent vraiment les données",
             "<p>Le débat est vif et souvent caricatural. État actuel des connaissances :</p>"
             "<ul>"
             "<li>Les corrélations entre temps d'écran global et bien-être sont <strong>faibles</strong> (autour de r = -0,05), "
             "comparables à celles du port de lunettes ou de la consommation de pommes de terre selon une analyse célèbre.</li>"
             "<li>Ce qui compte davantage que la durée, c'est <strong>l'usage</strong> : l'usage passif (faire défiler, comparer) "
             "est associé à une baisse d'humeur, l'usage actif (échanger avec des proches) à un effet neutre ou positif.</li>"
             "<li>Les effets sont plus marqués chez les adolescentes, et particulièrement liés à la comparaison sociale "
             "d'apparence et aux contenus sur l'alimentation.</li>"
             "<li>La causalité reste discutée : les personnes qui vont mal utilisent aussi davantage les écrans.</li>"
             "<li>Les expériences de désintoxication numérique donnent des résultats contrastés, avec des effets modestes.</li>"
             "</ul>"
             "<p>Conclusion honnête : ni « poison pour une génération », ni « rien à signaler ». Le contenu, le contexte et la "
             "vulnérabilité individuelle comptent bien plus que le nombre d'heures.</p>"),
            ("Comparaison sociale et image de soi",
             "<p>Festinger l'avait décrit dès 1954 : nous nous évaluons en nous comparant à autrui. Les plateformes ont "
             "industrialisé la <strong>comparaison ascendante</strong> — vers ceux qui semblent mieux — en mettant à disposition "
             "un flux infini de versions sélectionnées, filtrées et retouchées de la vie des autres.</p>"
             "<p>Le mécanisme central est bien identifié : nous comparons nos coulisses à la scène des autres. S'y ajoute la "
             "<strong>FOMO</strong> (peur de rater quelque chose), qui pousse à consulter davantage, ce qui augmente l'exposition "
             "à la comparaison, dans une boucle qui s'auto-entretient.</p>"),
            ("Cyberharcèlement et désinhibition en ligne",
             "<p>John Suler a décrit l'<strong>effet de désinhibition en ligne</strong>, qui résulte de six facteurs : anonymat, "
             "invisibilité, asynchronie, introjection (on « entend » l'autre dans sa propre voix mentale), dissociation "
             "imaginaire (« ce n'est pas vraiment réel ») et minimisation de l'autorité.</p>"
             "<p>Le cyberharcèlement se distingue du harcèlement classique par quatre caractéristiques aggravantes : il ne "
             "s'arrête pas à la sortie de l'établissement, l'audience est potentiellement illimitée, les traces sont permanentes, "
             "et l'agresseur ne perçoit pas la détresse qu'il provoque — ce qui supprime le frein empathique habituel.</p>"
             "<p>Les programmes efficaces (KiVa, en Finlande) ne ciblent pas seulement la victime et l'agresseur mais le groupe "
             "de témoins, qui détient en réalité le pouvoir de faire cesser la dynamique.</p>"),
            ("Désinformation : pourquoi le faux voyage plus vite",
             "<p>Une étude du MIT portant sur 126 000 rumeurs a montré que les fausses informations se diffusent plus vite, plus "
             "loin et plus profondément que les vraies — principalement parce qu'elles sont plus <strong>nouvelles</strong> et "
             "suscitent plus de <strong>surprise et de dégoût</strong>.</p>"
             "<p>Deux mécanismes psychologiques aggravent le phénomène : l'<strong>effet de vérité illusoire</strong> (une "
             "affirmation répétée paraît plus vraie, même si on l'a d'abord jugée fausse) et le <strong>raisonnement motivé</strong> "
             "(nous examinons sévèrement ce qui contredit notre camp et faiblement ce qui l'arrange).</p>"
             "<p>Ce qui fonctionne : le <strong>prebunking</strong> (exposer les techniques de manipulation avant l'exposition, "
             "comme un vaccin), les incitations à s'interroger sur l'exactitude avant de partager, et le démenti accompagné "
             "d'une explication alternative complète — un simple « c'est faux » laisse un vide que l'esprit comble avec l'information initiale.</p>"),
            ("Hygiène numérique réaliste",
             "<ul>"
             "<li><strong>Agir sur l'environnement plutôt que sur la volonté</strong> : désactiver les notifications non humaines, "
             "passer l'écran en niveaux de gris, retirer les applications problématiques de l'écran d'accueil.</li>"
             "<li><strong>Créer des frictions</strong> : se déconnecter après chaque session, supprimer l'application et passer "
             "par le navigateur.</li>"
             "<li><strong>Définir des lieux et des moments sans écran</strong> plutôt qu'un quota horaire : la chambre et le repas "
             "sont les plus rentables.</li>"
             "<li><strong>Remplacer, ne pas seulement retirer</strong> : un usage supprimé sans activité de remplacement revient.</li>"
             "<li><strong>Passer du passif à l'actif</strong> : commenter, échanger, créer plutôt que faire défiler.</li>"
             "</ul>"),
        ],
        "figures": ["portrait-thorndike.jpg:Edward Thorndike"],
        "pdfs": [],
        "fun_fact": "Le défilement infini a été inventé en 2006 par Aza Raskin, qui a depuis publiquement regretté sa création : il estime que son invention fait perdre collectivement des centaines de milliers d'heures humaines chaque jour.",
        "flashcards": [
            ("Quel programme de renforcement les réseaux sociaux exploitent-ils ?", "Le renforcement à ratio variable, le plus résistant à l'extinction, identifié par Skinner."),
            ("Quelle distinction compte plus que le temps d'écran ?", "La distinction entre usage passif (défilement, comparaison) et usage actif (échange réel)."),
            ("Qu'est-ce que l'effet de vérité illusoire ?", "Une affirmation répétée paraît plus vraie, même lorsqu'on l'avait initialement jugée fausse."),
            ("Qu'est-ce que le prebunking ?", "Exposer à l'avance les techniques de manipulation pour immuniser contre la désinformation."),
            ("Pourquoi le cyberharcèlement est-il plus grave que le harcèlement classique ?", "Continuité 24 h/24, audience illimitée, traces permanentes et absence de frein empathique pour l'agresseur."),
        ],
    },
    {
        "id": "23-evolutionniste",
        "icon": "🧬", "color": "or", "num": "23",
        "title": "Psychologie Évolutionniste",
        "subtitle": "Pourquoi notre esprit a la forme qu'il a",
        "read_time": "14 min",
        "objectives": [
            "Comprendre le raisonnement adaptationniste et ses règles de prudence",
            "Connaître les grandes hypothèses évolutionnistes sur la cognition sociale",
            "Identifier les principales critiques de cette approche",
            "Distinguer explication évolutive et justification morale",
        ],
        "sections": [
            ("Le principe de base",
             "<p>La psychologie évolutionniste part d'un constat simple : le cerveau est un organe, produit par la sélection "
             "naturelle comme le foie ou l'œil. Ses mécanismes ont été façonnés par les problèmes récurrents rencontrés par nos "
             "ancêtres : trouver de la nourriture, éviter les prédateurs et les pathogènes, choisir un partenaire, coopérer, "
             "détecter les tricheurs, élever des enfants.</p>"
             "<p>D'où une conséquence essentielle : nos mécanismes psychologiques sont adaptés à un <strong>environnement "
             "d'adaptation évolutive</strong> qui n'est plus le nôtre. Notre attirance pour le sucre et le gras était adaptative "
             "dans un monde de pénurie ; elle est problématique dans un monde d'abondance. On parle de "
             "<strong>décalage évolutif</strong> (<em>mismatch</em>).</p>"),
            ("Quelques hypothèses centrales",
             "<ul>"
             "<li><strong>Détection de tricheurs</strong> : dans la tâche de sélection de Wason, moins de 25 % des participants "
             "résolvent un problème logique abstrait ; le même problème formulé comme une règle sociale (« si quelqu'un boit de "
             "l'alcool, il doit avoir plus de 18 ans ») est résolu par plus de 75 %. Cosmides y voit un module spécialisé dans "
             "la détection des resquilleurs.</li>"
             "<li><strong>Dégoût et évitement des pathogènes</strong> : le dégoût cible massivement les sources de contamination "
             "(fluides corporels, chair en décomposition) et s'intensifie pendant le premier trimestre de grossesse, période de "
             "vulnérabilité immunitaire maximale.</li>"
             "<li><strong>Peurs préparées</strong> : les phobies portent bien plus souvent sur les serpents, les araignées et les "
             "hauteurs que sur les prises électriques ou les voitures, pourtant bien plus dangereuses aujourd'hui. Seligman parle "
             "de préparation biologique.</li>"
             "<li><strong>Altruisme réciproque et sélection de parentèle</strong> : Hamilton explique l'aide apportée aux "
             "apparentés (<em>r</em> × <em>B</em> > <em>C</em>), Trivers la coopération entre non-apparentés par la réciprocité "
             "différée, qui exige mémoire des interactions et détection de la triche.</li>"
             "<li><strong>Hypothèse du cerveau social</strong> : Dunbar montre une corrélation entre taille du néocortex et taille "
             "du groupe chez les primates, et estime à environ 150 le nombre de relations stables qu'un humain peut entretenir.</li>"
             "</ul>"),
            ("Ce que l'évolution explique de nos biais",
             "<p>De nombreux biais cognitifs, absurdes en logique formelle, deviennent compréhensibles comme compromis adaptatifs. "
             "La <strong>théorie de la gestion des erreurs</strong> l'explique : quand les deux types d'erreur n'ont pas le même "
             "coût, la sélection favorise un biais.</p>"
             "<p>Prendre un bâton pour un serpent coûte un sursaut ; prendre un serpent pour un bâton coûte la vie. Un système "
             "d'alarme hypersensible est donc rationnel au sens évolutif, même s'il produit une majorité de fausses alertes. "
             "Le même raisonnement éclaire le biais de négativité, la détection de visages dans les nuages, ou la tendance à "
             "surinterpréter les intentions d'autrui.</p>"),
            ("Les critiques, prises au sérieux",
             "<p>Cette approche a suscité des objections sérieuses qu'il serait malhonnête d'ignorer :</p>"
             "<ul>"
             "<li><strong>Le risque des « histoires à dormir debout »</strong> : on peut inventer une explication adaptative "
             "plausible pour à peu près n'importe quel trait. Gould et Lewontin ont critiqué cet adaptationnisme systématique : "
             "certains traits sont des sous-produits (des « spandrels ») sans fonction propre.</li>"
             "<li><strong>La difficulté de tester</strong> : on ne peut pas observer l'environnement ancestral, ni faire varier "
             "expérimentalement l'histoire évolutive.</li>"
             "<li><strong>La sous-estimation de la culture</strong> : l'évolution culturelle est bien plus rapide que la "
             "génétique, et l'humain est surtout caractérisé par sa capacité d'apprentissage social.</li>"
             "<li><strong>Le risque politique</strong> : présenter un comportement comme « naturel » peut servir à le justifier. "
             "C'est le <strong>sophisme naturaliste</strong> : ce qui est ne dit rien de ce qui doit être. Expliquer l'origine "
             "évolutive d'une tendance agressive ne la légitime en rien.</li>"
             "</ul>"
             "<p>Une hypothèse évolutionniste sérieuse doit produire des prédictions précises, testables, et qui distinguent "
             "l'explication proposée d'autres explications possibles.</p>"),
            ("Applications concrètes",
             "<p>Bien encadrée, cette perspective est féconde :</p>"
             "<ul>"
             "<li><strong>Santé</strong> : comprendre l'obésité et le diabète comme des décalages entre nos préférences "
             "alimentaires et un environnement transformé.</li>"
             "<li><strong>Sommeil</strong> : l'existence de chronotypes variés dans un groupe assurait une vigilance nocturne "
             "continue (hypothèse de la sentinelle mal ajustée).</li>"
             "<li><strong>Éducation</strong> : Geary distingue les savoirs <strong>biologiquement primaires</strong> (parler, "
             "marcher, reconnaître les visages), acquis sans enseignement, et <strong>secondaires</strong> (lire, écrire, "
             "calculer), qui exigent un enseignement explicite et beaucoup d'effort — ce qui relativise les pédagogies fondées "
             "sur la seule découverte spontanée.</li>"
             "<li><strong>Thérapies</strong> : normaliser l'anxiété comme un système d'alarme utile mais mal calibré aide "
             "considérablement les patients à s'y rapporter autrement.</li>"
             "</ul>"),
        ],
        "figures": ["portrait-darwin.jpg:Charles Darwin", "portrait-lorenz.jpg:Konrad Lorenz"],
        "pdfs": [
            {"title": "L'expression des émotions chez l'homme et les animaux", "author": "Charles Darwin (1877)",
             "path": f"{PDF}/psychologie-comparative/darwin-expression-emotions-1877.pdf",
             "desc": "Le texte fondateur de l'approche évolutionniste des comportements, richement illustré."},
        ],
        "fun_fact": "Le « nombre de Dunbar », environ 150 relations stables, correspond étonnamment bien à la taille des villages néolithiques, des unités militaires romaines et des communautés amish actuelles, qui se scindent au-delà de ce seuil.",
        "flashcards": [
            ("Qu'est-ce que le décalage évolutif (mismatch) ?", "L'inadéquation entre des mécanismes adaptés à l'environnement ancestral et l'environnement moderne."),
            ("Que dit la théorie de la gestion des erreurs ?", "Quand les deux types d'erreur ont des coûts inégaux, la sélection favorise un biais vers l'erreur la moins coûteuse."),
            ("Qu'est-ce que le sophisme naturaliste ?", "Le raisonnement fautif qui déduit ce qui doit être de ce qui est : expliquer n'est pas justifier."),
            ("Quelle est la critique de Gould et Lewontin ?", "Tous les traits ne sont pas des adaptations : certains sont des sous-produits sans fonction propre (spandrels)."),
            ("Quelle distinction Geary applique-t-il à l'éducation ?", "Savoirs biologiquement primaires (acquis spontanément) et secondaires (nécessitant un enseignement explicite)."),
        ],
    },
    {
        "id": "24-vieillissement",
        "icon": "🌿", "color": "gris", "num": "24",
        "title": "Vieillissement & Gérontopsychologie",
        "subtitle": "Ce qui décline, ce qui se maintient, ce qui progresse",
        "read_time": "15 min",
        "objectives": [
            "Distinguer vieillissement normal et vieillissement pathologique",
            "Connaître l'évolution réelle des fonctions cognitives avec l'âge",
            "Comprendre le paradoxe du bien-être au grand âge",
            "Identifier les facteurs protecteurs du vieillissement cognitif",
        ],
        "sections": [
            ("Ce qui décline et ce qui se maintient",
             "<p>Le vieillissement cognitif n'est pas un déclin global. Il est <strong>différentiel</strong> :</p>"
             "<ul>"
             "<li><strong>En baisse</strong> : vitesse de traitement (dès la trentaine, lentement), mémoire épisodique, mémoire "
             "de travail, récupération lexicale (le fameux mot « sur le bout de la langue »), attention divisée, "
             "flexibilité mentale.</li>"
             "<li><strong>Stable</strong> : mémoire procédurale (savoir-faire), mémoire sémantique, langage, reconnaissance, "
             "mémoire implicite.</li>"
             "<li><strong>En hausse</strong> : vocabulaire, connaissances générales, régulation émotionnelle, résolution de "
             "problèmes sociaux complexes, ce que la recherche nomme sagesse pragmatique.</li>"
             "</ul>"
             "<p>Ce profil correspond au modèle de Cattell : l'intelligence fluide décline, l'intelligence cristallisée progresse "
             "ou se maintient jusqu'à un âge avancé.</p>"),
            ("Distinguer le normal du pathologique",
             "<p>La question angoisse légitimement. Quelques repères, qui ne remplacent jamais un bilan :</p>"
             "<ul>"
             "<li><strong>Plainte typique du vieillissement normal</strong> : oublier où l'on a posé ses clés, chercher un mot, "
             "avoir besoin de plus de temps. La personne se plaint elle-même, elle a conscience de ses oublis, et les indices "
             "l'aident à retrouver l'information.</li>"
             "<li><strong>Signaux d'alerte</strong> : oublier des événements entiers et récents, répéter la même question à "
             "quelques minutes d'intervalle, se perdre dans un lieu familier, ne plus savoir utiliser des objets du quotidien, "
             "changement marqué de comportement ou de personnalité. C'est souvent l'entourage qui s'inquiète, pas la personne.</li>"
             "</ul>"
             "<p>Le <strong>trouble neurocognitif majeur</strong> (ancienne « démence ») suppose une atteinte d'au moins un "
             "domaine cognitif retentissant sur l'autonomie. La maladie d'Alzheimer en est la cause la plus fréquente "
             "(60-70 %), devant les formes vasculaires, à corps de Lewy et fronto-temporales — ces dernières débutant souvent "
             "par des troubles du comportement plutôt que de la mémoire.</p>"
             "<p>Attention aux causes réversibles souvent négligées : dépression (qui peut mimer une démence), hypothyroïdie, "
             "carences en vitamine B12, effets secondaires médicamenteux, troubles du sommeil, surdité non appareillée.</p>"),
            ("Le paradoxe du bien-être",
             "<p>Contre toute attente, le bien-être subjectif suit une courbe en U sur la vie entière : élevé dans la jeunesse, "
             "au plus bas vers 45-55 ans, puis en remontée jusqu'à un âge avancé, malgré les pertes de santé et les deuils.</p>"
             "<p>La <strong>théorie de la sélectivité socio-émotionnelle</strong> de Laura Carstensen l'explique : lorsque l'horizon "
             "temporel perçu se raccourcit, les priorités basculent de l'acquisition d'information vers le sens et la qualité "
             "émotionnelle. Les personnes âgées sélectionnent leurs relations, privilégient les proches, évitent les conflits "
             "inutiles et présentent un <strong>effet de positivité</strong> : à mémoire égale, elles retiennent mieux les "
             "informations positives.</p>"
             "<p>Confirmation élégante de la théorie : ce n'est pas l'âge qui compte mais l'horizon perçu. Des jeunes adultes en "
             "situation de fin d'horizon — départ définitif à l'étranger, pandémie — adoptent les mêmes priorités.</p>"),
            ("Réserve cognitive et facteurs protecteurs",
             "<p>À lésions cérébrales équivalentes, certaines personnes présentent bien moins de symptômes. C'est la "
             "<strong>réserve cognitive</strong> : un capital de connexions et de stratégies alternatives construit tout au long "
             "de la vie par l'éducation, la complexité du travail, l'activité intellectuelle et sociale.</p>"
             "<p>La commission du <em>Lancet</em> (2020, actualisée en 2024) estime qu'environ <strong>45 % des cas de démence</strong> "
             "seraient potentiellement évitables en agissant sur quatorze facteurs modifiables, parmi lesquels :</p>"
             "<ul>"
             "<li>Éducation insuffisante dans l'enfance</li>"
             "<li><strong>Surdité non corrigée</strong> — l'un des facteurs les plus importants à l'âge moyen</li>"
             "<li>Hypertension, obésité, diabète, tabac, consommation excessive d'alcool</li>"
             "<li>Dépression non traitée, isolement social</li>"
             "<li>Sédentarité, traumatismes crâniens, pollution de l'air, troubles de la vision non corrigés</li>"
             "</ul>"
             "<p>Ce qui protège réellement : l'activité physique régulière (le facteur le mieux établi), l'engagement social, "
             "le sommeil de qualité, l'appareillage auditif, le contrôle des facteurs cardiovasculaires et l'apprentissage de "
             "choses nouvelles et difficiles. Les jeux d'entraînement cérébral, eux, améliorent surtout… les performances à ces jeux.</p>"),
            ("Accompagner : ce qui aide vraiment",
             "<p>Pour les personnes atteintes de troubles neurocognitifs et leurs proches :</p>"
             "<ul>"
             "<li><strong>Validation plutôt que correction</strong> : contredire une personne désorientée génère de l'angoisse "
             "sans rétablir la réalité. Accueillir l'émotion sous-jacente est plus efficace.</li>"
             "<li><strong>Environnement stable et repères visuels</strong> : réduire les exigences de mémoire plutôt que "
             "l'entraîner de force.</li>"
             "<li><strong>Musique et souvenirs anciens</strong> : la mémoire émotionnelle et procédurale résiste longtemps ; "
             "les chansons de jeunesse restent accessibles quand le reste s'efface.</li>"
             "<li><strong>Soutien aux aidants</strong> : ils présentent des taux de dépression et d'épuisement très élevés. "
             "Le répit n'est pas un luxe mais une condition de la continuité de l'accompagnement.</li>"
             "</ul>"),
            ("Âgisme : le préjugé le plus banalisé",
             "<p>L'âgisme est la discrimination la plus largement tolérée. Il agit de façon mesurable :</p>"
             "<ul>"
             "<li>Les personnes âgées exposées à des stéréotypes négatifs obtiennent immédiatement de moins bons résultats aux "
             "tests de mémoire — c'est la menace du stéréotype.</li>"
             "<li>Une perception positive de son propre vieillissement est associée à une longévité supérieure de plusieurs "
             "années dans des études longitudinales.</li>"
             "<li>Le langage infantilisant (<em>elderspeak</em> : voix aiguë, diminutifs, « on va prendre son petit "
             "médicament ») dégrade l'estime de soi et augmente la résistance aux soins.</li>"
             "</ul>"
             "<p>Le vieillissement n'est pas une maladie : c'est une étape de la vie qui comporte des pertes réelles et des gains "
             "réels, et qui se vit très différemment selon les représentations sociales dans lesquelles elle se déroule.</p>"),
        ],
        "figures": ["cerveau-humain.svg:Le cerveau humain"],
        "pdfs": [
            {"title": "Les maladies de la mémoire", "author": "Théodule Ribot (1898)",
             "path": f"{PDF}/psychopathologie/ribot-maladies-memoire-1898.pdf",
             "desc": "La loi de régression : la mémoire se détruit du plus récent vers le plus ancien, observation toujours pertinente."},
        ],
        "fun_fact": "La mémoire des chansons apprises entre 15 et 25 ans (la « bosse de réminiscence ») reste remarquablement intacte, y compris à un stade avancé de la maladie d'Alzheimer : c'est la base des ateliers musicothérapeutiques en EHPAD.",
        "flashcards": [
            ("Quelle fonction cognitive progresse avec l'âge ?", "L'intelligence cristallisée : vocabulaire, connaissances générales, et la régulation émotionnelle."),
            ("Qu'est-ce que la réserve cognitive ?", "Un capital de connexions et de stratégies alternatives, construit par l'éducation et l'activité, qui retarde l'expression des symptômes."),
            ("Quel facteur modifiable de démence est souvent négligé ?", "La surdité non appareillée, l'un des plus importants à l'âge moyen."),
            ("Que dit la théorie de la sélectivité socio-émotionnelle ?", "Quand l'horizon temporel perçu se raccourcit, on privilégie le sens et la qualité émotionnelle des relations."),
            ("Quel signe distingue un oubli normal d'un signal d'alerte ?", "Dans le vieillissement normal, la personne se plaint elle-même et les indices l'aident ; dans le pathologique, c'est l'entourage qui s'inquiète et les indices n'aident pas."),
        ],
    },
    {
        "id": "25-environnementale",
        "icon": "🌱", "color": "vert", "num": "25",
        "title": "Psychologie Environnementale",
        "subtitle": "Nos lieux de vie, la nature et l'éco-anxiété",
        "read_time": "13 min",
        "objectives": [
            "Comprendre comment l'environnement physique agit sur le comportement",
            "Connaître les effets documentés du contact avec la nature",
            "Expliquer l'écart entre conscience écologique et action",
            "Aborder l'éco-anxiété sans la pathologiser",
        ],
        "sections": [
            ("L'espace agit sur nous",
             "<p>La psychologie environnementale étudie les relations entre l'humain et son cadre physique. Ses résultats sont "
             "souvent concrets et mesurables :</p>"
             "<ul>"
             "<li><strong>Bruit</strong> : l'exposition chronique au bruit des transports dégrade les apprentissages scolaires et "
             "augmente le risque cardiovasculaire, indépendamment du niveau socio-économique.</li>"
             "<li><strong>Lumière naturelle</strong> : les salles de classe et bureaux bien éclairés naturellement améliorent les "
             "performances et régulent les rythmes circadiens.</li>"
             "<li><strong>Densité et contrôle</strong> : ce n'est pas la densité objective qui nuit, mais le sentiment de ne pas "
             "pouvoir contrôler ses interactions. Un couloir de bureau ouvert sans espace de repli est plus délétère qu'un espace "
             "dense mais modulable.</li>"
             "<li><strong>Bureaux paysagers</strong> : une étude harvardienne a montré que le passage en espace ouvert réduit de "
             "70 % les interactions en face-à-face et augmente les échanges écrits — l'inverse de l'objectif affiché.</li>"
             "<li><strong>Design et criminalité</strong> : la visibilité, l'entretien et l'appropriation des espaces réduisent les "
             "incivilités bien davantage que la surveillance seule.</li>"
             "</ul>"),
            ("La nature répare l'attention",
             "<p>Deux théories complémentaires structurent ce champ :</p>"
             "<ul>"
             "<li><strong>Théorie de la restauration de l'attention</strong> (Kaplan) : les environnements naturels sollicitent une "
             "attention involontaire et douce (le mouvement des feuilles, l'eau), ce qui laisse récupérer l'attention dirigée, "
             "épuisée par les tâches urbaines et numériques.</li>"
             "<li><strong>Théorie de la réduction du stress</strong> (Ulrich) : la nature déclenche une réponse physiologique "
             "rapide de baisse du cortisol et de la tension artérielle.</li>"
             "</ul>"
             "<p>L'étude princeps d'Ulrich (1984) reste emblématique : des patients opérés dont la chambre donnait sur des arbres "
             "sortaient en moyenne un jour plus tôt et recevaient moins d'antalgiques que ceux qui faisaient face à un mur de briques. "
             "Les données actuelles convergent vers un seuil d'environ <strong>120 minutes de nature par semaine</strong>, cumulables, "
             "associé à une amélioration nette du bien-être rapporté.</p>"),
            ("L'écart entre valeurs et comportements",
             "<p>La grande majorité des personnes se déclare préoccupée par l'environnement, et une minorité modifie réellement ses "
             "comportements. Cet écart s'explique par plusieurs mécanismes :</p>"
             "<ul>"
             "<li><strong>Actualisation temporelle</strong> : les coûts sont immédiats, les bénéfices lointains et diffus.</li>"
             "<li><strong>Dilemme social</strong> : l'intérêt individuel à court terme s'oppose à l'intérêt collectif à long terme "
             "(tragédie des communs).</li>"
             "<li><strong>Diffusion de responsabilité</strong> à l'échelle planétaire, avec report sur les autres pays, les autres "
             "générations, les entreprises.</li>"
             "<li><strong>Distance psychologique</strong> : un risque perçu comme lointain dans le temps, l'espace et la probabilité "
             "mobilise peu.</li>"
             "<li><strong>Effet rebond</strong> : les gains d'efficacité sont partiellement absorbés par une consommation accrue.</li>"
             "</ul>"
             "<p>Ce qui fonctionne : rendre visible la norme sociale descriptive (« 75 % de vos voisins ont réduit leur "
             "consommation »), qui surpasse largement les messages culpabilisants ; agir sur les options par défaut ; donner un "
             "retour immédiat et comparatif sur les consommations ; mobiliser les identités collectives plutôt que la seule "
             "responsabilité individuelle.</p>"),
            ("Éco-anxiété : une réaction, pas une maladie",
             "<p>L'éco-anxiété désigne l'inquiétude persistante liée aux menaces environnementales. Elle ne figure dans aucune "
             "classification diagnostique, et c'est cohérent : c'est une <strong>réponse proportionnée à une menace réelle</strong>, "
             "pas un trouble.</p>"
             "<p>Une vaste enquête internationale menée auprès de 10 000 jeunes de 16 à 25 ans dans dix pays a montré que 59 % se "
             "disaient très ou extrêmement inquiets, et que plus de 45 % rapportaient un retentissement sur leur vie quotidienne. "
             "Élément notable : la détresse était fortement corrélée au sentiment que les gouvernements trahissaient leurs "
             "engagements — c'est la <strong>trahison morale perçue</strong>, plus que la peur du climat seule, qui blesse.</p>"
             "<p>Elle devient problématique lorsqu'elle produit sidération, insomnie durable, évitement de l'information ou "
             "désespoir paralysant. L'accompagnement ne vise alors pas à rassurer faussement, mais à transformer l'angoisse en "
             "capacité d'agir : passer de l'impuissance à l'action collective, doser son exposition à l'information, autoriser le "
             "deuil écologique, et maintenir des sources de joie — l'épuisement militant est un risque documenté.</p>"),
            ("Concevoir des lieux qui font du bien",
             "<p>Quelques principes issus de la recherche, applicables à un logement, une école ou un bureau :</p>"
             "<ul>"
             "<li><strong>Offrir du contrôle</strong> : pouvoir régler la lumière, la température, le niveau d'interaction. Le "
             "sentiment de contrôle compte souvent plus que le réglage lui-même.</li>"
             "<li><strong>Prévoir des espaces de repli</strong> : la théorie prospect-refuge suggère que nous apprécions les lieux "
             "offrant à la fois une vue dégagée et un adossement protecteur.</li>"
             "<li><strong>Introduire du vivant</strong> : plantes, matériaux naturels, vues sur la végétation (design biophilique).</li>"
             "<li><strong>Soigner les transitions</strong> : les seuils, les entrées et les couloirs structurent la manière dont on "
             "habite un lieu.</li>"
             "<li><strong>Permettre l'appropriation</strong> : personnaliser son espace améliore le bien-être et la performance, "
             "ce que les politiques de bureaux non attribués suppriment.</li>"
             "</ul>"),
        ],
        "figures": [],
        "pdfs": [],
        "fun_fact": "Dans l'étude d'Ulrich, la différence entre une vue sur des arbres et une vue sur un mur représentait en moyenne près d'une journée d'hospitalisation en moins — un effet obtenu sans aucun soin supplémentaire, simplement par la fenêtre attribuée.",
        "flashcards": [
            ("Que dit la théorie de la restauration de l'attention ?", "Les environnements naturels sollicitent une attention involontaire douce, permettant à l'attention dirigée de récupérer."),
            ("Quel message est le plus efficace pour changer un comportement écologique ?", "La norme sociale descriptive (« la majorité de vos voisins le fait »), bien plus que la culpabilisation."),
            ("L'éco-anxiété est-elle un trouble mental ?", "Non : c'est une réponse proportionnée à une menace réelle, qui ne devient problématique qu'en cas de retentissement majeur et durable."),
            ("Qu'est-ce que l'effet rebond ?", "L'absorption partielle des gains d'efficacité par une augmentation de la consommation."),
            ("Quel facteur compte le plus dans le vécu de la densité ?", "Le sentiment de contrôle sur ses interactions, davantage que la densité objective."),
        ],
    },
    {
        "id": "26-politique",
        "icon": "🗳️", "color": "rose", "num": "26",
        "title": "Psychologie Politique & Croyances",
        "subtitle": "Idéologies, polarisation, complotisme et esprit critique",
        "read_time": "15 min",
        "objectives": [
            "Comprendre les fondements psychologiques des orientations politiques",
            "Expliquer les mécanismes de la polarisation affective",
            "Identifier les ressorts psychologiques de l'adhésion complotiste",
            "Connaître les méthodes qui font réellement évoluer les opinions",
        ],
        "sections": [
            ("Les racines psychologiques des orientations politiques",
             "<p>Les positions politiques ne se réduisent pas à des calculs d'intérêt. Plusieurs travaux montrent des corrélations "
             "modestes mais reproductibles avec des dispositions psychologiques.</p>"
             "<p>La <strong>théorie des fondements moraux</strong> de Jonathan Haidt identifie cinq à six intuitions morales : "
             "soin/préjudice, équité/tricherie, loyauté/trahison, autorité/subversion, pureté/dégradation, liberté/oppression. "
             "Les personnes se situant à gauche s'appuient principalement sur les deux premiers ; celles se situant à droite "
             "mobilisent les six de façon plus équilibrée. Beaucoup de désaccords politiques sont donc des désaccords sur les "
             "critères moraux pertinents, pas seulement sur les faits.</p>"
             "<p>Haidt propose aussi la métaphore de l'<strong>éléphant et du cornac</strong> : l'intuition (l'éléphant) décide, "
             "la raison (le cornac) justifie après coup. Cela explique pourquoi des arguments corrects convainquent si rarement.</p>"),
            ("Polarisation affective : on ne se déteste pas pour les idées",
             "<p>Le phénomène le plus documenté des vingt dernières années n'est pas l'éloignement des positions (polarisation "
             "idéologique, relativement stable) mais l'<strong>hostilité croissante envers le camp adverse</strong> "
             "(polarisation affective). Aux États-Unis, la proportion de personnes déclarant qu'elles seraient contrariées par le "
             "mariage de leur enfant avec un partisan de l'autre camp a été multipliée par plusieurs facteurs en quelques décennies.</p>"
             "<p>Trois moteurs se combinent : l'<strong>identité sociale</strong> (le camp politique devient un groupe "
             "d'appartenance, avec la logique « eux/nous » des groupes minimaux de Tajfel) ; la <strong>méta-perception erronée</strong> "
             "(nous surestimons massivement l'extrémisme et l'hostilité de l'autre camp — cet écart peut atteindre un facteur deux) ; "
             "et l'<strong>économie de l'attention</strong>, qui favorise les contenus indignants et les porte-parole les plus extrêmes.</p>"
             "<p>Ce qui réduit l'hostilité : corriger les méta-perceptions avec des données réelles, exposer à des membres ordinaires "
             "de l'autre camp, et créer des interactions coopératives autour d'objectifs concrets et partagés.</p>"),
            ("Pourquoi on croit aux théories du complot",
             "<p>Adhérer à une théorie du complot n'est ni un signe de bêtise ni une maladie. Trois grands besoins psychologiques "
             "sont en jeu (van Prooijen, Douglas) :</p>"
             "<ul>"
             "<li><strong>Besoin épistémique</strong> : comprendre un monde complexe. Un complot offre une explication simple, "
             "cohérente et complète là où la réalité est confuse et hasardeuse.</li>"
             "<li><strong>Besoin existentiel</strong> : retrouver un sentiment de contrôle et de sécurité. Les croyances "
             "complotistes progressent dans les périodes de crise, de menace et d'incertitude.</li>"
             "<li><strong>Besoin social</strong> : maintenir une image positive de soi et de son groupe. Détenir un savoir caché "
             "distingue, valorise, et intègre à une communauté.</li>"
             "</ul>"
             "<p>Certains biais y contribuent : détection excessive d'intentions et de motifs, biais de proportionnalité (un grand "
             "événement doit avoir une grande cause — d'où la difficulté à accepter qu'un homme isolé ait pu changer l'histoire), "
             "et le raisonnement conspirationniste qui transforme toute réfutation en preuve supplémentaire du complot.</p>"),
            ("Ce qui fonctionne (et ce qui échoue) pour faire évoluer une opinion",
             "<p>La confrontation frontale échoue presque toujours : elle active la défense identitaire. Les méthodes ayant produit "
             "des résultats mesurables sont d'un tout autre ordre :</p>"
             "<ul>"
             "<li><strong>Le deep canvassing</strong> : une conversation longue, non jugeante, où l'on invite l'autre à raconter "
             "une expérience personnelle liée au sujet. Des essais randomisés ont montré des changements d'attitude durables sur "
             "plusieurs mois concernant des questions très clivantes.</li>"
             "<li><strong>L'entretien motivationnel</strong> : explorer l'ambivalence de la personne plutôt que d'argumenter contre elle. "
             "Efficacité démontrée en hésitation vaccinale.</li>"
             "<li><strong>Le prebunking</strong> : exposer les techniques de manipulation avant d'être confronté à la désinformation.</li>"
             "<li><strong>L'illusion de profondeur explicative</strong> : demander d'expliquer <em>mécaniquement</em> comment "
             "fonctionnerait la mesure défendue. La plupart découvrent qu'ils ne savent pas, et modèrent spontanément leur position — "
             "un effet que demander des <em>raisons</em> ne produit pas.</li>"
             "</ul>"
             "<p>Le <strong>retour de flamme</strong> (une correction renforçant la fausse croyance), longtemps redouté, s'avère "
             "en réalité rare : corriger reste utile, à condition de fournir une explication alternative complète plutôt qu'un simple démenti.</p>"),
            ("Outils d'esprit critique",
             "<p>L'esprit critique n'est pas le doute généralisé, qui mène au relativisme et paradoxalement au complotisme. "
             "C'est un ensemble d'outils :</p>"
             "<ul>"
             "<li><strong>Calibrer son doute sur la qualité des preuves</strong> : une méta-analyse de 40 essais randomisés ne pèse "
             "pas comme un témoignage isolé.</li>"
             "<li><strong>Le rasoir de Hitchens</strong> : ce qui est affirmé sans preuve peut être rejeté sans preuve.</li>"
             "<li><strong>Chercher le consensus des spécialistes du domaine précis</strong>, pas l'avis d'un expert isolé ni "
             "d'un expert d'un autre domaine.</li>"
             "<li><strong>Distinguer les niveaux</strong> : fait, interprétation, opinion, valeur. Beaucoup de débats mélangent les quatre.</li>"
             "<li><strong>Appliquer le principe de charité</strong> : réfuter la meilleure version de l'argument adverse, pas sa caricature.</li>"
             "<li><strong>Accepter l'incertitude</strong> : « je ne sais pas » et « les données sont partagées » sont des positions "
             "intellectuellement solides, pas des aveux de faiblesse.</li>"
             "</ul>"
             "<p>Dernier point, le plus exigeant : appliquer ces outils en priorité aux affirmations qui nous arrangent. Le "
             "raisonnement motivé est bien plus actif quand une information confirme ce que nous souhaitons croire.</p>"),
        ],
        "figures": ["portrait-le-bon.jpg:Gustave Le Bon", "portrait-durkheim.jpg:Émile Durkheim"],
        "pdfs": [
            {"title": "Psychologie des foules", "author": "Gustave Le Bon (1895)",
             "path": f"{PDF}/psychologie-sociale/le-bon-psychologie-des-foules-1895-complet.pdf",
             "desc": "Le texte fondateur sur les mouvements collectifs et l'influence de masse, à lire avec un regard critique."},
        ],
        "fun_fact": "Demander à quelqu'un d'expliquer en détail le fonctionnement d'une politique qu'il défend le rend spontanément plus modéré. Demander simplement pourquoi il la défend ne produit aucun effet : c'est l'illusion de profondeur explicative.",
        "flashcards": [
            ("Qu'est-ce que la polarisation affective ?", "L'hostilité croissante envers le camp politique adverse, distincte de l'éloignement des positions idéologiques."),
            ("Quels sont les trois besoins qui alimentent les croyances complotistes ?", "Épistémique (comprendre), existentiel (contrôler) et social (se valoriser et appartenir)."),
            ("Qu'est-ce que le deep canvassing ?", "Une conversation longue et non jugeante fondée sur le récit d'expériences personnelles, qui produit des changements d'attitude durables."),
            ("Que dit la métaphore de l'éléphant et du cornac ?", "L'intuition décide et la raison justifie après coup, ce qui explique le faible pouvoir de conviction des arguments."),
            ("Qu'est-ce que le biais de proportionnalité ?", "La tendance à exiger qu'un grand événement ait une grande cause, ce qui rend les explications banales difficiles à accepter."),
        ],
    },
    CATEGORY_SCIENCE,
]
