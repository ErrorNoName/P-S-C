# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Questions fréquentes.

Format : (id, question, famille, reponse_html)
Les réponses visent la précision plutôt que la brièveté : chacune doit pouvoir
être lue seule et dire honnêtement ce qu'on sait et ce qu'on ignore.
"""

FAQ = [
    # ---------------------------------------------------------------- Discipline
    (
        "qu-est-ce-que-la-psychologie",
        "Qu'est-ce que la psychologie, exactement ?",
        "La discipline",
        "<p>C'est l'étude scientifique du comportement et des processus mentaux. Les trois mots comptent. "
        "<em>Scientifique</em> : les affirmations sont soumises à des observations qui pourraient les "
        "contredire. <em>Comportement</em> : ce qu'un organisme fait, y compris ce qu'on peut mesurer "
        "indirectement comme un temps de réaction. <em>Processus mentaux</em> : percevoir, mémoriser, "
        "raisonner, ressentir, décider.</p>"
        "<p>La discipline va de l'étude d'un canal ionique dans un neurone à celle des différences "
        "culturelles de raisonnement. Cette amplitude explique qu'elle paraisse parfois incohérente : "
        "ce n'est pas une théorie unique mais un ensemble de questions abordées à des niveaux distincts.</p>",
    ),
    (
        "psycho-est-elle-une-science",
        "La psychologie est-elle une vraie science ?",
        "La discipline",
        "<p>Oui, au sens où elle formule des hypothèses réfutables, les teste avec des protocoles "
        "contrôlés, quantifie l'incertitude et corrige ses conclusions. Elle a même fait mieux que "
        "beaucoup d'autres champs sur un point : elle a mesuré son propre taux d'erreur. La crise de la "
        "réplication des années 2010 a montré qu'une part importante de résultats publiés ne se "
        "reproduisait pas, et la discipline a réagi par des réformes concrètes — préenregistrement des "
        "analyses, échantillons plus grands, réplications multi-laboratoires, partage des données.</p>"
        "<p>Ses difficultés propres sont réelles : les objets varient d'une personne et d'une culture à "
        "l'autre, les effets sont souvent petits, et l'expérimentation est limitée par l'éthique. Cela "
        "rend la psychologie difficile, pas non scientifique.</p>",
    ),
    (
        "difference-psycho-philo",
        "Quelle différence avec la philosophie de l'esprit ?",
        "La discipline",
        "<p>Les questions se ressemblent, la méthode d'arbitrage diffère. La philosophie procède par "
        "analyse conceptuelle et argumentation : elle clarifie ce que signifie « se souvenir » ou "
        "« vouloir ». La psychologie construit des situations dans lesquelles deux hypothèses rivales "
        "prédisent des résultats différents, puis regarde ce qui se produit.</p>"
        "<p>Les deux restent liées : une expérience mal conçue conceptuellement mesure autre chose que "
        "ce qu'elle croit mesurer, et beaucoup de débats en psychologie — sur la conscience, le libre "
        "arbitre, la nature des émotions — sont d'abord des problèmes de définition.</p>",
    ),
    (
        "pourquoi-tant-de-theories",
        "Pourquoi y a-t-il autant de théories contradictoires ?",
        "La discipline",
        "<p>Parce que la plupart décrivent des niveaux ou des domaines différents plutôt que des vérités "
        "concurrentes. Expliquer une phobie par un conditionnement, par une pensée automatique ou par une "
        "hyperactivité de l'amygdale, ce n'est pas se contredire : ce sont trois descriptions du même "
        "phénomène à trois échelles.</p>"
        "<p>Il existe aussi de vraies rivalités, et là le critère est ordinaire : quelle théorie prédit "
        "le plus de faits nouveaux, avec le moins d'hypothèses ad hoc, et survit aux tentatives de "
        "réfutation ?</p>",
    ),
    # ---------------------------------------------------------------- Cerveau
    (
        "cerveau-esprit",
        "Le cerveau et l'esprit, c'est la même chose ?",
        "Cerveau et corps",
        "<p>La position dominante en sciences cognitives est que les états mentaux sont réalisés par des "
        "états cérébraux, sans s'y réduire au sens descriptif : décrire une décision en termes de "
        "regrets anticipés et la décrire en termes de décharges neuronales sont deux niveaux également "
        "légitimes, comme la description d'un logiciel et celle des transistors qui l'exécutent.</p>"
        "<p>Ce qui est solidement établi : modifier le cerveau modifie l'esprit, de façon parfois très "
        "spécifique. Ce qui reste ouvert : comment une activité physique produit une expérience vécue.</p>",
    ),
    (
        "imagerie-lit-pensees",
        "L'imagerie cérébrale permet-elle de lire les pensées ?",
        "Cerveau et corps",
        "<p>Pas au sens courant. On sait décoder, avec un entraînement préalable sur la même personne et "
        "dans un ensemble de possibilités restreint, des catégories grossières : quelle image parmi "
        "plusieurs la personne regarde, quel mot d'une liste elle se répète. C'est déjà remarquable et "
        "c'est très loin de lire une pensée libre.</p>"
        "<p>Une IRM fonctionnelle mesure d'ailleurs un signal indirect — les variations d'oxygénation du "
        "sang — avec une résolution temporelle de quelques secondes, alors qu'une pensée se déploie en "
        "quelques centaines de millisecondes.</p>",
    ),
    (
        "hormones-comportement",
        "Les hormones expliquent-elles nos comportements ?",
        "Cerveau et corps",
        "<p>Elles les modulent, elles ne les dictent pas. La testostérone n'augmente pas l'agressivité de "
        "façon mécanique : elle accroît plutôt les comportements de recherche de statut, qui peuvent "
        "prendre la forme d'une générosité ostentatoire dans un contexte où c'est la voie du prestige. "
        "L'ocytocine n'est pas une hormone de l'amour : elle renforce l'attachement au groupe proche, "
        "y compris parfois la méfiance envers l'extérieur.</p>"
        "<p>La règle générale : les hormones modifient la probabilité de certaines réponses dans un "
        "contexte donné, et le contexte détermine quelle réponse.</p>",
    ),
    (
        "genetique-part",
        "Quelle est la part du génétique dans la personnalité ?",
        "Cerveau et corps",
        "<p>Les études de jumeaux situent l'héritabilité des grands traits de personnalité autour de 40 à "
        "50 %. Ce chiffre est souvent mal compris : il ne dit pas que la moitié de votre caractère est "
        "génétique, il dit que, dans la population étudiée, environ la moitié des <em>différences</em> "
        "entre individus est associée à des différences génétiques.</p>"
        "<p>Deux conséquences contre-intuitives. D'abord, l'héritabilité change avec l'environnement : "
        "plus les conditions de vie sont homogènes, plus la part génétique des différences augmente "
        "mécaniquement. Ensuite, ce qui reste n'est pas surtout l'éducation partagée : les frères et "
        "sœurs élevés ensemble se ressemblent moins qu'on ne le croit, et l'environnement qui compte "
        "semble être celui, non partagé, propre à chacun.</p>",
    ),
    # ---------------------------------------------------------------- Apprentissage
    (
        "meilleure-methode-reviser",
        "Quelle est la meilleure façon de réviser ?",
        "Apprendre",
        "<p>Deux techniques dominent toutes les autres dans les comparaisons : se tester de mémoire "
        "plutôt que relire, et répartir ses sessions dans le temps plutôt que les masser la veille. "
        "L'effet est important et robuste sur des dizaines d'études, tous niveaux confondus.</p>"
        "<p>Le piège est que ces deux méthodes donnent pendant l'apprentissage une impression de "
        "difficulté et d'inefficacité, alors que la relecture procure un sentiment de fluidité "
        "trompeur. Il faut accepter de se sentir moins performant sur le moment pour retenir davantage "
        "plus tard. C'est ce qu'on appelle une difficulté désirable.</p>",
    ),
    (
        "surligner-utile",
        "Surligner et relire, ça ne sert vraiment à rien ?",
        "Apprendre",
        "<p>Les évaluations rangent ces techniques parmi les moins efficaces par unité de temps investie. "
        "Elles ne sont pas nulles : elles permettent de repérer l'essentiel. Le problème est ce qu'elles "
        "remplacent — le temps passé à relire n'est pas passé à se tester.</p>"
        "<p>Une version utile : surligner très peu, puis fermer le document et reconstituer de mémoire "
        "ce qui était surligné. Le surlignage devient alors une préparation à la récupération, pas un "
        "substitut.</p>",
    ),
    (
        "musique-travail",
        "Peut-on travailler avec de la musique ?",
        "Apprendre",
        "<p>Cela dépend de la tâche et de la musique. Pour une tâche verbale — lire, rédiger, mémoriser du "
        "texte — une musique avec paroles dégrade mesurablement la performance parce qu'elle occupe la "
        "même ressource de traitement verbal. Pour une tâche répétitive et peu exigeante, la musique "
        "maintient la vigilance et améliore souvent le rendement.</p>"
        "<p>Un environnement bruyant et imprévisible est pire que tout : dans ce cas, une musique "
        "instrumentale stable ou un bruit constant est préférable au silence intermittent.</p>",
    ),
    (
        "oublier-normal",
        "Pourquoi j'oublie ce que j'ai appris hier ?",
        "Apprendre",
        "<p>Parce que c'est le fonctionnement normal de la mémoire. La courbe classique montre une perte "
        "très rapide dans les premières heures, puis un ralentissement. Oublier n'est pas une défaillance : "
        "c'est le tri qui empêche la mémoire d'être saturée d'informations sans usage.</p>"
        "<p>Ce qui résiste à l'oubli, c'est ce qui a été récupéré activement au moins une fois après un "
        "délai. Une seule tentative de rappel réussie le lendemain change davantage la rétention à long "
        "terme que trois relectures le jour même.</p>",
    ),
    (
        "apprendre-en-dormant",
        "Peut-on apprendre en dormant ?",
        "Apprendre",
        "<p>On ne peut pas acquérir un contenu nouveau et complexe en diffusant un cours pendant la nuit : "
        "les tentatives sérieuses ont échoué. En revanche, le sommeil consolide ce qui a été appris "
        "pendant la journée, et l'on peut renforcer une association déjà apprise en rediffusant pendant "
        "le sommeil lent un son ou une odeur qui lui était liée à l'encodage.</p>"
        "<p>La conséquence pratique est simple : dormir après avoir étudié fait partie de l'étude.</p>",
    ),
    (
        "age-apprendre-langue",
        "Est-il trop tard pour apprendre une langue à l'âge adulte ?",
        "Apprendre",
        "<p>Non pour le vocabulaire, la grammaire et la compréhension, où les adultes progressent souvent "
        "plus vite que les enfants à temps d'exposition égal. Oui, partiellement, pour la prononciation "
        "sans accent perceptible, qui devient très difficile après l'adolescence.</p>"
        "<p>Le vrai facteur limitant chez l'adulte n'est pas le cerveau mais le temps d'exposition et "
        "l'obligation de produire : un enfant passe des milliers d'heures à devoir se faire comprendre.</p>",
    ),
    # ---------------------------------------------------------------- Émotions
    (
        "emotions-universelles",
        "Les émotions sont-elles universelles ?",
        "Émotions",
        "<p>Le débat est vif et instructif. La position classique identifie quelques émotions de base avec "
        "des expressions faciales reconnues partout. Les critiques montrent que la reconnaissance chute "
        "fortement quand on cesse de proposer une liste de mots à choisir, et que des populations isolées "
        "n'associent pas les mêmes visages aux mêmes catégories.</p>"
        "<p>La position intermédiaire aujourd'hui répandue : les ingrédients — activation physiologique, "
        "valence agréable ou désagréable — sont universels, mais leur découpage en émotions nommées est "
        "largement construit par la culture et la langue.</p>",
    ),
    (
        "controler-emotions",
        "Peut-on contrôler ses émotions ?",
        "Émotions",
        "<p>On ne choisit pas de ressentir, on agit sur ce qui précède et ce qui suit. Les stratégies les "
        "plus efficaces interviennent tôt : choisir ou modifier la situation, déplacer son attention, et "
        "surtout réévaluer — se redire ce que la situation signifie avant que l'émotion ne culmine.</p>"
        "<p>La stratégie la moins efficace est la suppression expressive, c'est-à-dire garder un visage "
        "neutre en ressentant intensément : elle ne réduit pas le vécu, augmente l'activation "
        "physiologique, consomme des ressources attentionnelles et dégrade la qualité des interactions.</p>",
    ),
    (
        "stress-toujours-mauvais",
        "Le stress est-il toujours mauvais ?",
        "Émotions",
        "<p>Non. Une activation brève face à un défi mobilise l'attention, l'énergie et la mémoire : c'est "
        "un système conçu pour être utile. Ce qui nuit, c'est la chronicité — une activation entretenue "
        "sans résolution ni récupération — et l'absence de contrôle perçu.</p>"
        "<p>Un résultat contre-intuitif mais reproduit : la manière dont on interprète ses propres signes "
        "de stress modifie leur effet. Considérer un cœur qui s'accélère comme une préparation à l'action "
        "plutôt que comme un signe de panique s'accompagne d'un profil cardiovasculaire plus favorable et "
        "de meilleures performances.</p>",
    ),
    (
        "pleurer-soulage",
        "Est-ce que pleurer soulage vraiment ?",
        "Émotions",
        "<p>Les études par journal quotidien donnent une réponse nuancée : l'amélioration rapportée dépend "
        "surtout du contexte social. Pleurer en recevant du soutien est associé à un soulagement ; pleurer "
        "seul ou dans un contexte honteux est souvent suivi d'une humeur dégradée.</p>"
        "<p>En laboratoire, la mesure de l'humeur immédiatement après des pleurs montre généralement une "
        "dégradation, suivie d'un retour au niveau initial puis parfois au-dessus. Le sentiment de "
        "soulagement pourrait donc en partie être un effet de mémoire.</p>",
    ),
    # ---------------------------------------------------------------- Clinique
    (
        "quand-consulter",
        "Quand faut-il consulter un professionnel ?",
        "Santé mentale",
        "<p>Trois critères simples, indépendants de la gravité apparente du problème. La durée : une "
        "difficulté qui persiste au-delà de deux à quatre semaines sans amélioration. L'intensité : une "
        "souffrance qui domine les journées. Le retentissement : le travail, les études, les relations ou "
        "le sommeil sont durablement atteints.</p>"
        "<p>Deux situations justifient de consulter sans attendre : les idées suicidaires, et une "
        "consommation d'alcool ou de substances qui augmente pour tenir. Il n'est pas nécessaire d'aller "
        "mal « assez » pour consulter — l'intervention précoce donne de meilleurs résultats.</p>",
    ),
    (
        "psychotherapie-efficace",
        "La psychothérapie est-elle vraiment efficace ?",
        "Santé mentale",
        "<p>Oui, avec des tailles d'effet comparables à beaucoup de traitements médicaux courants pour les "
        "troubles anxieux et dépressifs. Les méta-analyses situent le bénéfice moyen bien au-dessus de "
        "l'absence de traitement et de la plupart des conditions contrôles actives.</p>"
        "<p>Deux nuances honnêtes. La taille d'effet réelle est probablement un peu inférieure aux "
        "chiffres publiés, en raison du biais de publication. Et les différences entre approches "
        "structurées sont plus faibles que les différences entre thérapeutes : la qualité de l'alliance "
        "prédit mieux le résultat que l'étiquette de la méthode.</p>",
    ),
    (
        "choisir-therapeute",
        "Comment choisir un psychothérapeute ?",
        "Santé mentale",
        "<p>Trois vérifications d'abord : le titre est-il protégé et vérifiable, la formation est-elle "
        "identifiable, le cadre est-il explicite sur le tarif, la fréquence et la durée envisagée ?</p>"
        "<p>Ensuite, un critère que la recherche soutient : après trois ou quatre séances, vous sentez-vous "
        "écouté sans jugement, comprenez-vous ce qui est visé et sur quoi vous travaillez ? Une alliance "
        "qui ne s'installe pas au bout de quelques séances est un motif légitime de changer de "
        "professionnel, et un thérapeute compétent l'entend sans le prendre mal.</p>"
        "<p>Signaux d'alerte : promesse de guérison rapide, refus d'expliquer la méthode, découragement "
        "de vos autres liens, contact hors cadre, demande d'engagement financier important à l'avance.</p>",
    ),
    (
        "medicaments-ou-therapie",
        "Médicaments ou thérapie ?",
        "Santé mentale",
        "<p>Cela dépend du trouble et de sa sévérité. Pour une dépression légère à modérée, la "
        "psychothérapie structurée obtient des résultats comparables aux antidépresseurs, avec un "
        "avantage sur le maintien après l'arrêt. Pour une dépression sévère, l'association des deux est "
        "généralement supérieure à l'une ou l'autre seule.</p>"
        "<p>Pour le trouble bipolaire et les troubles psychotiques, le traitement médicamenteux est le "
        "socle, et la psychothérapie et la psychoéducation s'y ajoutent. La décision relève d'un médecin, "
        "en discussion avec la personne concernée.</p>",
    ),
    (
        "difference-anxiete-angoisse",
        "Quelle différence entre anxiété, angoisse et crise de panique ?",
        "Santé mentale",
        "<p>L'anxiété est l'anticipation d'une menace future, diffuse, avec tension et hypervigilance. "
        "L'angoisse désigne, dans l'usage clinique français, une anxiété intense à forte composante "
        "corporelle — oppression, boule dans la gorge.</p>"
        "<p>L'attaque de panique est un épisode brutal, culminant en quelques minutes, avec palpitations, "
        "souffle court, vertiges, sensation de mourir ou de devenir fou. Elle est très impressionnante et "
        "physiquement inoffensive. Ce qui installe le trouble panique, c'est ensuite la peur d'avoir une "
        "nouvelle attaque et l'évitement des situations associées.</p>",
    ),
    (
        "aider-un-proche",
        "Comment aider un proche qui va mal ?",
        "Santé mentale",
        "<p>Nommer ce que vous observez sans interpréter : « je te vois dormir moins et refuser les "
        "sorties depuis plusieurs semaines » est recevable, « tu déprimes » l'est moins. Poser une "
        "question ouverte, puis écouter sans proposer de solution immédiatement.</p>"
        "<p>Si vous craignez un risque suicidaire, posez la question directement et simplement : cela "
        "n'induit pas l'idée, et cela ouvre presque toujours la parole. Proposez une aide concrète — "
        "chercher un numéro, accompagner à un rendez-vous — plutôt qu'un encouragement général.</p>"
        "<p>Enfin, protégez-vous : accompagner durablement quelqu'un qui va mal épuise, et vous avez le "
        "droit de chercher du soutien pour vous-même.</p>",
    ),
    (
        "burnout-depression",
        "Le burn-out, est-ce une dépression ?",
        "Santé mentale",
        "<p>Ce sont des entités qui se recouvrent partiellement. L'épuisement professionnel est décrit par "
        "trois dimensions : épuisement émotionnel, distance cynique vis-à-vis du travail, et sentiment "
        "d'inefficacité. Il est défini par rapport au contexte professionnel, ce qui n'est pas le cas de "
        "la dépression.</p>"
        "<p>En pratique, un épuisement prolongé évolue fréquemment vers un épisode dépressif "
        "caractérisé, et les deux tableaux coexistent souvent. La classification internationale des "
        "maladies le range parmi les facteurs influençant l'état de santé, non parmi les troubles "
        "mentaux.</p>",
    ),
    # ---------------------------------------------------------------- Vie quotidienne
    (
        "pourquoi-procrastiner",
        "Pourquoi procrastine-t-on, même quand on sait que c'est contre-productif ?",
        "Vie quotidienne",
        "<p>La procrastination est d'abord un problème de régulation des émotions, pas de gestion du "
        "temps. On repousse la tâche qui déclenche de l'ennui, du doute ou la peur de mal faire, et le "
        "soulagement immédiat qui suit renforce l'évitement. C'est un apprentissage par renforcement "
        "négatif, très efficace.</p>"
        "<p>Ce qui marche découle de ce mécanisme : réduire l'aversivité de la première étape en la "
        "rendant absurdement petite, préciser où et quand vous commencerez, et traiter l'auto-reproche "
        "comme un facteur aggravant — les personnes qui se pardonnent un épisode de procrastination "
        "procrastinent moins la fois suivante.</p>",
    ),
    (
        "changer-habitude",
        "Comment changer durablement une habitude ?",
        "Vie quotidienne",
        "<p>Une habitude est un couple entre un contexte et une action. Agir sur le contexte est plus "
        "efficace qu'agir sur la volonté : modifier l'environnement, augmenter le nombre de gestes "
        "nécessaires pour le comportement indésirable et le réduire pour le comportement souhaité.</p>"
        "<p>Ajoutez une intention de mise en œuvre — une phrase de la forme « quand telle situation se "
        "produit, je fais telle action » — dont l'effet est bien documenté, et arrimez le nouveau "
        "comportement à un déclencheur déjà stable de votre journée. Comptez plusieurs semaines, avec "
        "des ratés : les rechutes ponctuelles ne prédisent pas l'échec, l'abandon après une rechute si.</p>",
    ),
    (
        "mieux-dormir",
        "Que fait-on de vraiment efficace pour mieux dormir ?",
        "Vie quotidienne",
        "<p>La mesure la mieux établie n'est pas relaxante : c'est la régularité de l'heure de lever, sept "
        "jours sur sept, qui stabilise l'horloge interne. Ensuite, réserver le lit au sommeil, et quitter "
        "la chambre après une vingtaine de minutes d'éveil au lieu de rester à lutter — sinon le lit "
        "devient le signal de l'insomnie.</p>"
        "<p>Pour une insomnie chronique installée, le traitement de première intention recommandé n'est "
        "pas médicamenteux : c'est une thérapie cognitivo-comportementale de l'insomnie, dont l'efficacité "
        "dépasse celle des somnifères à moyen terme et se maintient après l'arrêt.</p>",
    ),
    (
        "decider-mieux",
        "Comment prendre de meilleures décisions ?",
        "Vie quotidienne",
        "<p>Trois leviers bien étayés. D'abord, écrire les critères et leur importance <em>avant</em> de "
        "comparer les options, sinon on ajuste les critères pour justifier l'option déjà préférée. "
        "Ensuite, pratiquer l'imagination d'un échec futur : se projeter un an plus tard en supposant que "
        "la décision a mal tourné et en chercher les raisons fait apparaître des risques qu'une simple "
        "liste d'inconvénients ne révèle pas.</p>"
        "<p>Enfin, distinguer les décisions réversibles des décisions coûteuses à défaire. Les premières "
        "méritent d'être prises vite ; seules les secondes justifient une délibération longue.</p>",
    ),
    (
        "motivation-durable",
        "Comment rester motivé sur la durée ?",
        "Vie quotidienne",
        "<p>La motivation n'est pas un carburant qu'on attend : elle suit souvent l'action. Trois besoins "
        "psychologiques soutiennent l'engagement durable — se sentir à l'origine de ses choix, percevoir "
        "sa progression en compétence, et se sentir relié à d'autres. Un objectif imposé, hors de portée "
        "ou solitaire épuise les trois.</p>"
        "<p>Pratiquement : formulez des objectifs de processus plutôt que de résultat, rendez la "
        "progression visible, et acceptez que la motivation fluctue. Les personnes régulières ne sont pas "
        "celles qui ont envie tous les jours, ce sont celles qui ont réduit le nombre de décisions à "
        "prendre.</p>",
    ),
    (
        "biais-se-corriger",
        "Peut-on corriger ses biais cognitifs ?",
        "Vie quotidienne",
        "<p>Les connaître ne suffit pas : on continue de les commettre tout en les repérant chez les "
        "autres. Ce qui fonctionne, ce sont des procédures qui rendent le biais inopérant : critères "
        "définis à l'avance, évaluation en aveugle, avis sollicités séparément avant toute discussion de "
        "groupe, statistiques de base rappelées explicitement.</p>"
        "<p>Autrement dit, on corrige les biais en changeant le dispositif de décision plus qu'en "
        "changeant l'individu qui décide.</p>",
    ),
    (
        "intuition-fiable",
        "Peut-on se fier à son intuition ?",
        "Vie quotidienne",
        "<p>Cela dépend de deux conditions. L'intuition est fiable quand l'environnement est "
        "suffisamment régulier pour contenir des régularités apprenables, et quand la personne a eu "
        "l'occasion de les apprendre grâce à un retour d'information rapide et clair. Un pompier "
        "expérimenté ou un joueur d'échecs remplissent ces conditions.</p>"
        "<p>Un recruteur ou un analyste boursier, non : le retour est tardif, bruité ou absent. Dans ces "
        "domaines, des règles simples et explicites battent régulièrement le jugement intuitif des "
        "experts, et le savoir est souvent plus utile que d'affiner son intuition.</p>",
    ),
    (
        "bonheur-facteurs",
        "Qu'est-ce qui rend les gens durablement heureux ?",
        "Vie quotidienne",
        "<p>Ce que les données longitudinales font ressortir le plus nettement, c'est la qualité des "
        "relations proches — davantage que le revenu au-delà d'un seuil de confort, davantage que la "
        "réussite professionnelle. La santé, le sentiment d'avoir prise sur sa vie et un engagement dans "
        "des activités qui ont du sens complètent le tableau.</p>"
        "<p>Un mécanisme explique beaucoup de déceptions : l'adaptation hédonique. On s'habitue vite aux "
        "améliorations de circonstances, moins vite à la qualité d'un lien ou à une activité qui procure "
        "de l'engagement. Investir dans des expériences et des relations résiste mieux que d'investir "
        "dans des acquisitions.</p>",
    ),
    # ---------------------------------------------------------------- Relations
    (
        "couple-duree",
        "Qu'est-ce qui prédit qu'un couple dure ?",
        "Relations",
        "<p>Les travaux d'observation des interactions conjugales isolent un facteur défavorable "
        "particulièrement net : le mépris — sarcasme, dévalorisation, regard levé au ciel. La critique "
        "globale de la personne, la position défensive et le retrait silencieux complètent le tableau "
        "des interactions à risque.</p>"
        "<p>À l'inverse, ce qui protège est la capacité à réparer après un conflit, l'attention portée "
        "aux petites sollicitations quotidiennes, et un rapport nettement favorable d'échanges positifs "
        "sur négatifs. Les couples durables ne se disputent pas moins : ils se réconcilient mieux.</p>",
    ),
    (
        "styles-attachement",
        "Les styles d'attachement de l'enfance déterminent-ils la vie amoureuse ?",
        "Relations",
        "<p>La continuité existe mais elle est modérée, loin du déterminisme souvent présenté. Les "
        "corrélations entre attachement mesuré dans la petite enfance et style relationnel adulte sont "
        "réelles et modestes, et les changements de trajectoire sont fréquents après une relation "
        "stable, un deuil, une thérapie.</p>"
        "<p>La notion reste utile comme description du fonctionnement actuel — ce qu'on redoute, comment "
        "on réagit à la distance ou au conflit — plus que comme diagnostic de l'enfance.</p>",
    ),
    (
        "solitude-sante",
        "La solitude est-elle mauvaise pour la santé ?",
        "Relations",
        "<p>L'isolement social prolongé est associé à une surmortalité comparable à celle de facteurs de "
        "risque médicaux bien connus. Le mécanisme passe par le stress chronique, l'inflammation, le "
        "sommeil dégradé et des comportements de santé moins bien maintenus.</p>"
        "<p>Il faut distinguer isolement objectif et sentiment de solitude : on peut être entouré et se "
        "sentir seul, et c'est le sentiment qui prédit le mieux les effets sur la santé mentale. Les "
        "interventions les plus efficaces ne se contentent pas d'augmenter les occasions de rencontre : "
        "elles travaillent les attentes et les interprétations, souvent devenues défavorables.</p>",
    ),
    (
        "manipulation-reconnaitre",
        "Comment reconnaître une relation manipulatrice ?",
        "Relations",
        "<p>Quelques marqueurs récurrents : l'isolement progressif de vos autres liens, la remise en "
        "cause systématique de votre perception des faits, l'alternance imprévisible de valorisation et "
        "de dévalorisation, la culpabilisation à chaque tentative de poser une limite, et le contrôle des "
        "ressources — argent, papiers, déplacements.</p>"
        "<p>Un indicateur simple et fiable : vous vous surprenez à préparer vos phrases à l'avance pour "
        "éviter une réaction. Ce n'est pas une preuve, c'est un signal qui mérite d'être examiné avec "
        "quelqu'un d'extérieur.</p>",
    ),
    # ---------------------------------------------------------------- Méthode
    (
        "lire-une-etude",
        "Comment lire une étude scientifique sans être spécialiste ?",
        "Méthode",
        "<p>Quatre questions suffisent à éliminer l'essentiel des conclusions fragiles. Sur qui ? Un "
        "effectif de quelques dizaines d'étudiants ne fonde pas une recommandation générale. Comparé à "
        "quoi ? Sans groupe contrôle, on ne sait pas ce qui serait arrivé sans l'intervention. Quelle "
        "taille d'effet ? Un résultat significatif peut être minuscule. Réplication ? Un résultat isolé "
        "et spectaculaire est plus souvent faux qu'un résultat modeste et confirmé.</p>"
        "<p>Ajoutez une vérification de cohérence : le titre de l'article de presse dit-il la même chose "
        "que le résumé de l'étude ? La réponse est souvent non.</p>",
    ),
    (
        "correlation-causalite",
        "Pourquoi répète-t-on que corrélation n'est pas causalité ?",
        "Méthode",
        "<p>Parce que trois explications rendent compte d'une association entre A et B : A cause B, B "
        "cause A, ou une troisième variable cause les deux. Les personnes qui pratiquent un sport sont en "
        "meilleure santé — le sport améliore la santé, une bonne santé permet de faire du sport, et un "
        "milieu social favorable produit les deux.</p>"
        "<p>Seule la répartition aléatoire des participants entre conditions élimine les explications "
        "alternatives. Quand elle est impossible pour des raisons éthiques, on s'en approche par des "
        "méthodes statistiques qui restent toujours plus fragiles.</p>",
    ),
    (
        "p-value",
        "Que signifie vraiment « p < 0,05 » ?",
        "Méthode",
        "<p>C'est la probabilité d'observer un résultat au moins aussi extrême que celui obtenu <em>si "
        "l'hypothèse nulle était vraie</em>. Ce n'est ni la probabilité que l'hypothèse nulle soit vraie, "
        "ni la probabilité que le résultat se reproduise, ni une mesure de l'importance de l'effet.</p>"
        "<p>Le seuil de 0,05 est une convention, pas une loi de la nature. Une p-value juste en dessous "
        "du seuil, sur un petit échantillon, constitue une preuve faible — et c'est précisément ce profil "
        "de résultats qui a le plus mal survécu aux tentatives de réplication.</p>",
    ),
    (
        "crise-replication",
        "Qu'est-ce que la crise de la réplication ?",
        "Méthode",
        "<p>À partir de 2011, des projets ont tenté de reproduire des résultats publiés dans des revues "
        "de premier plan. Une part importante ne s'est pas reproduite, et les effets retrouvés étaient en "
        "moyenne nettement plus petits que les effets d'origine.</p>"
        "<p>Les causes sont identifiées : échantillons trop petits, flexibilité excessive dans les "
        "analyses, publication préférentielle des résultats positifs, et absence d'incitation à "
        "répliquer. Les réponses le sont aussi : préenregistrement, rapports enregistrés acceptés avant "
        "les résultats, partage des données, réplications coordonnées entre laboratoires. La psychologie "
        "est aujourd'hui l'une des disciplines les plus avancées sur ces réformes.</p>",
    ),
    (
        "placebo",
        "L'effet placebo, c'est dans la tête ?",
        "Méthode",
        "<p>Il est dans la tête et dans le corps : on mesure des libérations d'opioïdes endogènes lors "
        "d'une analgésie placebo, qu'un antagoniste de ces opioïdes bloque. L'attente d'un effet modifie "
        "réellement des paramètres physiologiques.</p>"
        "<p>Son ampleur varie fortement selon ce qu'on mesure : importante sur la douleur, la nausée et "
        "l'anxiété, faible ou nulle sur une tumeur ou une infection. Une part de ce qu'on attribue au "
        "placebo dans les essais tient aussi à des phénomènes statistiques comme le retour à la moyenne.</p>",
    ),
    (
        "generaliser-etudiants",
        "Pourquoi tant d'études sont-elles faites sur des étudiants ?",
        "Méthode",
        "<p>Parce qu'ils sont accessibles aux chercheurs universitaires. Le problème a été nommé : les "
        "échantillons occidentaux, éduqués, industrialisés, riches et démocratiques sont statistiquement "
        "atypiques à l'échelle mondiale sur de nombreuses mesures, de la perception des illusions "
        "visuelles aux notions d'équité.</p>"
        "<p>Conséquence pratique : une conclusion établie sur ces échantillons doit être présentée comme "
        "valable pour cette population, jusqu'à preuve du contraire. C'est rarement le cas dans les "
        "résumés de presse.</p>",
    ),
    # ---------------------------------------------------------------- Études et métiers
    (
        "etudes-psycho",
        "Comment devient-on psychologue en France ?",
        "Études et métiers",
        "<p>Le titre de psychologue est protégé et suppose cinq années d'études : une licence de "
        "psychologie puis un master de psychologie comprenant un mémoire de recherche et un stage "
        "professionnel long, supervisé par un psychologue.</p>"
        "<p>La spécialité se joue au master : clinique et psychopathologie, neuropsychologie, travail et "
        "organisations, développement, cognition, éducation. L'inscription au répertoire ADELI, ou son "
        "successeur, est nécessaire pour exercer.</p>",
    ),
    (
        "psycho-debouches",
        "La psychologie offre-t-elle des débouchés ?",
        "Études et métiers",
        "<p>Les débouchés existent mais la sélection est réelle : la licence accueille beaucoup "
        "d'étudiants et les places en master sont nettement moins nombreuses. Une licence seule ne permet "
        "pas de porter le titre de psychologue.</p>"
        "<p>Au-delà du soin, les compétences du cursus — méthodologie, statistiques, entretien, analyse "
        "du comportement — mènent à la recherche, aux ressources humaines, à l'ergonomie, à la recherche "
        "utilisateur, à la formation, à la santé publique et aux études.</p>",
    ),
    (
        "maths-en-psycho",
        "Faut-il être bon en mathématiques pour étudier la psychologie ?",
        "Études et métiers",
        "<p>Il faut accepter les statistiques, qui occupent une place importante du cursus et surprennent "
        "beaucoup d'étudiants. Le niveau requis relève surtout de la logique et de la rigueur : "
        "comprendre une distribution, un test, une taille d'effet, et savoir lire un tableau de "
        "résultats.</p>"
        "<p>La biologie est également présente dès la première année, et la rédaction scientifique "
        "structurée compte autant que le calcul.</p>",
    ),
    (
        "neuropsy-role",
        "Que fait concrètement un neuropsychologue ?",
        "Études et métiers",
        "<p>Il évalue les fonctions cognitives — mémoire, attention, langage, fonctions exécutives, "
        "praxies — à l'aide de tests standardisés, pour caractériser un fonctionnement après un "
        "traumatisme crânien, un accident vasculaire, une maladie neurodégénérative ou dans le cadre de "
        "troubles du neurodéveloppement.</p>"
        "<p>Le compte rendu sert au diagnostic médical, mais aussi à des décisions très concrètes : "
        "aménagements scolaires ou professionnels, stratégies de compensation, orientation vers une "
        "rééducation. Une partie du métier consiste à expliquer les résultats à la personne et à ses "
        "proches.</p>",
    ),
    # ---------------------------------------------------------------- Le site
    (
        "site-fiabilite",
        "Sur quoi repose le contenu de ce site ?",
        "À propos du site",
        "<p>Les textes sont rédigés à partir de résultats consensuels de la littérature en psychologie "
        "scientifique, avec un souci constant de distinguer ce qui est solidement établi, ce qui est "
        "discuté et ce qui relève de la croyance populaire. Les pages de débats et d'idées reçues sont "
        "là pour rendre cette distinction explicite plutôt que de la laisser implicite.</p>"
        "<p>Les illustrations et les ouvrages proviennent du domaine public, avec leur source et leur "
        "licence indiquées sur la page de crédits. Les livres anciens sont proposés pour leur intérêt "
        "historique : leur contenu scientifique est daté, et c'est précisément ce qui les rend "
        "instructifs.</p>",
    ),
    (
        "site-diagnostic",
        "Puis-je m'auto-diagnostiquer avec ce site ?",
        "À propos du site",
        "<p>Non, et c'est important. Les descriptions de troubles servent à comprendre, pas à conclure. "
        "Un diagnostic repose sur un entretien clinique, sur la durée des symptômes, sur leur "
        "retentissement et sur l'élimination d'autres causes, médicales notamment — rien de tout cela ne "
        "se fait en lisant une fiche.</p>"
        "<p>Les auto-évaluations proposées ici sont pédagogiques : elles illustrent comment on construit "
        "une mesure en psychologie, avec des items rédigés pour le site et sans valeur diagnostique.</p>",
    ),
    (
        "site-utiliser",
        "Comment utiliser ce site pour apprendre efficacement ?",
        "À propos du site",
        "<p>Trois usages complémentaires. Pour découvrir : suivez un parcours guidé, qui alterne "
        "volontairement les formats. Pour approfondir : lisez une catégorie en entier, puis vérifiez ce "
        "que vous avez retenu avec son quiz avant de relire.</p>"
        "<p>Pour retenir durablement : passez par la révision espacée quelques minutes par jour plutôt "
        "qu'une heure par semaine, et imprimez la fiche du domaine que vous travaillez. Le laboratoire "
        "sert à éprouver sur vous-même des effets que vous venez de lire, ce qui les ancre nettement "
        "mieux qu'une définition.</p>",
    ),
]
