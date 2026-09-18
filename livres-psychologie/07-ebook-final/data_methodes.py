# -*- coding: utf-8 -*-
"""Méthodes de recherche, statistiques et esprit critique appliqués à la psychologie.

Deux ensembles :
  * CHAPITRES : le cours proprement dit, en sections rédigées ;
  * NOTIONS   : les fiches de référence, filtrables, pour retrouver une définition.
"""

# (ancre, titre, html)
CHAPITRES = [
    ("pourquoi", "Pourquoi la psychologie a besoin d'une méthode", """
<p>L'intuition est une excellente génératrice d'hypothèses et une très mauvaise juge. Presque toutes les
affirmations « de bon sens » sur le comportement humain ont un contraire tout aussi plausible : « qui se
ressemble s'assemble » et « les opposés s'attirent », « loin des yeux loin du cœur » et « l'absence attise
le désir ». Les deux ne peuvent pas être vraies en même temps dans les mêmes conditions, et seule une mesure
peut trancher.</p>

<p>Le problème est aggravé par le fait que nous sommes des observateurs biaisés de notre propre espèce. Nous
remarquons les cas qui confirment ce que nous pensons, nous oublions les autres, nous reconstruisons nos
souvenirs, et nous avons une propension irrésistible à voir des causes là où il n'y a que des coïncidences.
Une méthode n'est rien d'autre qu'un ensemble de garde-fous contre ces tendances — y compris, et surtout,
celles du chercheur lui-même.</p>

<p>D'où une règle qui structure tout ce chapitre : <strong>en science, la question n'est jamais « est-ce que
c'est vrai ? » mais « quelle est la qualité de la preuve, et de quelle taille est l'effet ? »</strong>.
Apprendre à répondre à ces deux questions, c'est acquérir la compétence la plus transférable de toute la
psychologie.</p>
"""),

    ("hypothese", "De la question à l'hypothèse testable", """
<p>Une hypothèse scientifique doit être <strong>falsifiable</strong> : il faut pouvoir décrire à l'avance
un résultat qui la contredirait. « L'inconscient influence nos actes » n'est pas testable tel quel ; « les
participants amorcés avec des mots liés à la vieillesse marcheront plus lentement dans le couloir » l'est,
et a d'ailleurs été testé — puis infirmé.</p>

<p>Le passage de la question au protocole repose sur l'<strong>opérationnalisation</strong> : traduire un
concept abstrait en quelque chose de mesurable. « Le stress » devient un taux de cortisol salivaire, un score
à une échelle validée, une variabilité cardiaque, ou un temps passé à ruminer. Aucune de ces mesures n'est
« le » stress ; chacune en capture une facette, avec ses angles morts. C'est pourquoi la convergence de
plusieurs mesures indépendantes vaut infiniment mieux qu'une seule, même très précise.</p>

<div class="note-box"><strong>Le réflexe à acquérir.</strong> Devant tout résultat, demandez-vous d'abord :
<em>comment ont-ils mesuré ça, exactement ?</em> Beaucoup de désaccords apparents entre études se dissolvent
dès qu'on regarde la mesure : deux équipes ne parlaient simplement pas de la même chose.</div>
"""),

    ("plans", "Les grands types de plans de recherche", """
<p>Chaque type de plan répond à une question différente et souffre de limites propres. Les confondre est la
source la plus fréquente d'erreurs d'interprétation dans la presse.</p>

<p><strong>L'étude descriptive</strong> (observation, enquête, étude de cas) répond à « que se passe-t-il ? ».
Elle est irremplaçable pour explorer un phénomène nouveau et pour générer des hypothèses, mais elle ne permet
aucune conclusion causale.</p>

<p><strong>L'étude corrélationnelle</strong> répond à « ces deux variables varient-elles ensemble ? ». Elle
permet de prédire, jamais d'expliquer. Trois interprétations restent toujours ouvertes : A cause B, B cause A,
ou une troisième variable C cause les deux. La consommation de glaces et les noyades varient ensemble ; la
variable cachée s'appelle l'été.</p>

<p><strong>L'expérience</strong> répond à « est-ce que A cause B ? ». Elle suppose trois ingrédients : le
chercheur <em>manipule</em> la variable indépendante, il <em>répartit au hasard</em> les participants entre
les conditions, et il <em>contrôle</em> le reste. La randomisation est la pièce maîtresse : elle égalise en
moyenne les groupes sur tout ce qu'on n'a pas mesuré, y compris ce à quoi on n'a pas pensé.</p>

<p><strong>L'étude longitudinale</strong> suit les mêmes personnes dans le temps, ce qui permet d'établir
l'ordre temporel des événements. Elle coûte cher et souffre de l'attrition : ceux qui abandonnent l'étude ne
sont jamais un échantillon au hasard de ceux qui restent.</p>

<p><strong>L'étude transversale</strong> compare des groupes d'âges différents au même moment. Rapide, mais
elle confond l'effet de l'âge avec l'effet de génération : un septuagénaire de 2026 n'a pas eu la même
scolarité ni la même alimentation qu'un trentenaire, et la différence observée n'est pas forcément due au
vieillissement.</p>
"""),

    ("validite", "Les quatre validités", """
<p>Juger une étude, c'est examiner quatre choses distinctes que l'on confond souvent.</p>

<p><strong>La validité interne</strong> : la variation observée est-elle bien due à ce que l'on a manipulé ?
Elle est menacée par tout ce qui diffère entre les groupes hormis le traitement — biais de sélection,
événements extérieurs, maturation des participants, effets de l'ordre de passation, attentes de
l'expérimentateur.</p>

<p><strong>La validité externe</strong> : le résultat se généralise-t-il à d'autres personnes, d'autres lieux,
d'autres époques ? Un effet observé sur 40 étudiants en psychologie un mardi après-midi n'est pas
automatiquement une propriété de l'espèce humaine.</p>

<p><strong>La validité de construit</strong> : mesure-t-on vraiment ce que l'on croit mesurer ? Un
questionnaire de « bonheur » qui corrèle à 0,9 avec un questionnaire de « non-dépression » mesure peut-être
simplement l'humeur du moment.</p>

<p><strong>La validité de conclusion statistique</strong> : les chiffres autorisent-ils la conclusion tirée ?
C'est ici que se logent les échantillons trop petits, les tests multiples non corrigés et les effets minuscules
présentés comme des découvertes.</p>
"""),

    ("biais-recherche", "Les biais qui menacent une étude", """
<p>Le <strong>biais de sélection</strong> apparaît quand les participants ne représentent pas la population
visée. Les enquêtes en ligne sur le bonheur atteignent surtout des gens qui ont du temps, une connexion et
l'envie de répondre.</p>

<p>L'<strong>effet Hawthorne</strong> : le simple fait d'être observé modifie le comportement. D'où les
conditions contrôles où l'on observe aussi ceux qui ne reçoivent rien.</p>

<p>Les <strong>caractéristiques de demande</strong> : les participants devinent l'hypothèse et, par
coopération ou par défi, la confirment ou la contredisent. On y répond par des protocoles en aveugle et des
mesures indirectes.</p>

<p>L'<strong>effet Rosenthal</strong> (ou effet Pygmalion) : les attentes de l'expérimentateur influencent le
résultat, par des micro-signaux involontaires. C'est la raison d'être du <strong>double aveugle</strong> : ni
le participant ni l'expérimentateur en contact avec lui ne savent qui reçoit quoi.</p>

<p>La <strong>régression vers la moyenne</strong> : les valeurs extrêmes tendent à se rapprocher de la moyenne
lors d'une seconde mesure, indépendamment de toute intervention. C'est le mécanisme statistique qui fait
croire à l'efficacité d'innombrables traitements administrés au pire moment d'une maladie fluctuante.</p>

<p>Enfin le <strong>placebo</strong>, qui n'est pas « rien » : l'attente d'amélioration produit des effets
physiologiques mesurables, particulièrement sur la douleur, la fatigue et l'humeur. Une intervention n'est
jugée efficace que si elle fait mieux qu'un placebo crédible, pas mieux que rien.</p>
"""),

    ("stats-descriptives", "Décrire des données sans se tromper", """
<p>La <strong>moyenne</strong> est sensible aux valeurs extrêmes ; la <strong>médiane</strong> ne l'est pas.
Pour des revenus, des temps de réaction ou des durées d'hospitalisation — toutes distributions asymétriques —
la médiane décrit bien mieux « le cas typique ». Quand un article ne donne que la moyenne d'une variable
asymétrique, il faut se méfier.</p>

<p>L'<strong>écart-type</strong> dit à quel point les valeurs s'écartent de la moyenne. Deux groupes de même
moyenne peuvent être radicalement différents : l'un homogène, l'autre polarisé. Une moyenne sans dispersion
est une information incomplète.</p>

<p>La <strong>distribution normale</strong> (la « courbe en cloche ») décrit bien la taille ou les scores de
QI, mal les revenus ou le nombre d'amis. Beaucoup de tests statistiques la supposent ; utiliser ces tests sur
des données très asymétriques produit des conclusions douteuses.</p>

<p>Enfin, un <strong>graphique</strong> ment facilement : un axe des ordonnées tronqué transforme une
différence de 2 % en falaise spectaculaire. Le premier réflexe devant un graphique est de regarder l'échelle.</p>
"""),

    ("p-value", "La valeur p : ce qu'elle dit et ce qu'elle ne dit pas", """
<p>La valeur p est la probabilité d'observer un résultat au moins aussi extrême que celui obtenu <em>si
l'hypothèse nulle était vraie</em>, c'est-à-dire s'il n'y avait aucun effet dans la population. Le seuil
conventionnel de 0,05 a été choisi par Ronald Fisher par commodité, sans justification théorique.</p>

<p>Ce que p <strong>n'est pas</strong> : ce n'est pas la probabilité que l'hypothèse soit vraie ; ce n'est pas
la probabilité que le résultat se réplique ; et un p de 0,001 ne signifie pas que l'effet est trois fois plus
important qu'un p de 0,003. La valeur p mélange la taille de l'effet et la taille de l'échantillon : avec
100 000 participants, une différence totalement négligeable devient « significative ».</p>

<p>D'où la distinction cardinale entre <strong>significativité statistique</strong> (l'effet n'est probablement
pas dû au seul hasard) et <strong>signification pratique</strong> (l'effet est assez grand pour compter). Un
médicament qui réduit la douleur de 0,3 point sur 100 peut être hautement significatif et parfaitement
inutile.</p>

<div class="warn-box"><strong>Le p-hacking.</strong> Tester vingt hypothèses au seuil de 5 %, c'est s'attendre
à un « résultat significatif » purement dû au hasard, en moyenne, à chaque étude. Ajouter des participants
jusqu'à ce que p passe sous 0,05, écarter des valeurs gênantes, essayer plusieurs mesures et ne publier que la
plus flatteuse : ces pratiques, longtemps considérées comme anodines, sont la première cause de la crise de la
réplication.</div>
"""),

    ("taille-effet", "Taille d'effet et intervalles de confiance", """
<p>La <strong>taille d'effet</strong> répond à la seule question qui compte vraiment : de combien ? Le
<em>d</em> de Cohen exprime la différence entre deux moyennes en unités d'écart-type. Repères usuels : 0,2
petit, 0,5 moyen, 0,8 grand — à relativiser selon le domaine, car un petit effet appliqué à des millions de
personnes peut avoir une immense portée en santé publique.</p>

<p>Le coefficient de corrélation <em>r</em> varie de −1 à +1. En psychologie, la plupart des corrélations
robustes se situent entre 0,10 et 0,30. Son carré indique la part de variance partagée : un r de 0,30, souvent
présenté comme un lien fort, n'explique que 9 % de la variance.</p>

<p>L'<strong>intervalle de confiance à 95 %</strong> est plus informatif que la valeur p : il donne une plage
de valeurs plausibles pour l'effet. Un intervalle très large signale un résultat imprécis, même s'il est
« significatif ». C'est l'un des meilleurs indices de la solidité réelle d'une étude.</p>

<p>La <strong>puissance statistique</strong> est la probabilité de détecter un effet qui existe réellement.
Elle dépend de la taille d'effet attendue et du nombre de participants. Une étude sous-puissante ne se contente
pas de rater des effets : quand elle en trouve un, celui-ci est presque nécessairement surestimé.</p>
"""),

    ("meta", "Revues systématiques et méta-analyses", """
<p>Une étude isolée ne prouve à peu près rien. La <strong>revue systématique</strong> recense de façon
exhaustive et pré-spécifiée toutes les études sur une question ; la <strong>méta-analyse</strong> combine
statistiquement leurs résultats pour estimer un effet global et sa variabilité.</p>

<p>C'est le sommet de la hiérarchie des preuves — à condition de se méfier de deux pièges. Le
<strong>biais de publication</strong> : les résultats nuls sont bien moins souvent publiés, ce qui gonfle
artificiellement l'effet moyen. On le détecte par des graphiques en entonnoir (<em>funnel plots</em>)
asymétriques. Et le principe <em>garbage in, garbage out</em> : agréger cinquante études mal conduites ne
produit pas une vérité, seulement une erreur avec une décimale de plus.</p>

<p>Pour naviguer, retenez l'ordre approximatif de solidité : témoignage personnel &lt; étude de cas &lt; étude
corrélationnelle &lt; essai contrôlé randomisé &lt; réplication indépendante &lt; méta-analyse d'essais
préenregistrés.</p>
"""),

    ("reforme", "La réforme en cours : science ouverte", """
<p>Depuis 2011, la psychologie a entrepris une réforme méthodologique d'une ampleur inédite, et elle est
devenue de ce fait une discipline pilote pour les autres sciences.</p>

<p>Le <strong>préenregistrement</strong> consiste à déposer publiquement ses hypothèses, son plan d'analyse et
sa taille d'échantillon avant de collecter les données. Il empêche de transformer après coup une exploration
en confirmation. Les <strong>Registered Reports</strong> vont plus loin : la revue accepte l'article sur la
base du protocole, avant de connaître les résultats — ce qui supprime mécaniquement le biais de publication.</p>

<p>Le <strong>partage des données et du code</strong> permet la vérification indépendante. Les
<strong>réplications multi-laboratoires</strong> (projets Many Labs, ManyBabies) testent le même protocole dans
des dizaines d'équipes et de pays simultanément.</p>

<div class="note-box"><strong>Ce qu'il faut en retenir.</strong> Qu'un tiers seulement des résultats classiques
se réplique n'est pas un scandale à cacher : c'est une discipline qui a mesuré ses propres erreurs et publié le
résultat. Aucune science n'avait osé le faire à cette échelle. Lire aujourd'hui un article préenregistré,
multi-sites, avec données ouvertes, c'est lire une preuve d'une qualité sans commune mesure avec la littérature
des années 1980.</div>
"""),

    ("ethique", "L'éthique de la recherche", """
<p>Les principes actuels sont nés des abus : expérimentations nazies, étude de Tuskegee où l'on a laissé des
hommes noirs américains non traités pour observer l'évolution de la syphilis pendant quarante ans, protocoles
de psychologie sociale infligeant une détresse réelle.</p>

<p>Quatre exigences structurent aujourd'hui toute recherche sur l'humain. Le <strong>consentement libre et
éclairé</strong> : comprendre ce à quoi on participe et pouvoir se retirer à tout moment sans justification.
La <strong>balance bénéfice-risque</strong>, évaluée par un comité indépendant. La
<strong>confidentialité</strong> et la protection des données. Enfin le <strong>débriefing</strong> lorsqu'une
tromperie a été nécessaire : le participant doit repartir en sachant la vérité et sans dommage.</p>

<p>La protection est renforcée pour les personnes vulnérables — mineurs, personnes sous protection juridique,
détenus, patients en situation de dépendance à l'égard du soignant qui les recrute. En France, ces recherches
relèvent de comités de protection des personnes et du cadre du RGPD.</p>
"""),

    ("lire-article", "Lire un article scientifique en dix minutes", """
<p>Un article de recherche suit presque toujours la même structure (le format IMRaD). Voici l'ordre de lecture
le plus efficace, qui n'est pas l'ordre du texte.</p>

<ol>
<li><strong>Le résumé</strong>, pour savoir de quoi il s'agit — sans jamais s'y fier pour conclure.</li>
<li><strong>La méthode</strong> d'abord : qui sont les participants, combien, comment ont-ils été recrutés et
répartis, comment les variables ont-elles été mesurées ? Un protocole faible invalide des résultats brillants ;
l'inverse n'est pas vrai.</li>
<li><strong>Les résultats</strong> : cherchez les tailles d'effet et les intervalles de confiance, pas
seulement les astérisques. Regardez les échelles des graphiques.</li>
<li><strong>La discussion</strong> en dernier, en gardant en tête que c'est la partie la plus interprétative,
donc la plus susceptible de dépasser ce que les données autorisent.</li>
</ol>

<p>Trois questions closent la lecture : l'échantillon permet-il de généraliser à qui l'on prétend ? le plan
autorise-t-il une conclusion causale ? l'effet est-il assez grand pour compter en pratique ? Si l'une des trois
réponses est « non », le titre du communiqué de presse est probablement trompeur.</p>

<div class="note-box"><strong>Des ressources gratuites et sérieuses.</strong> PubMed et Google Scholar pour la
recherche bibliographique, les archives ouvertes HAL et PsyArXiv pour les versions accessibles librement,
Cochrane et Campbell Collaboration pour les synthèses d'efficacité. Et systématiquement : remonter du
communiqué de presse à l'article original, car c'est presque toujours entre les deux que la nuance disparaît.</div>
"""),
]

# (id, nom, famille, definition, exemple, piege)
NOTIONS = [
    ("variable-independante", "Variable indépendante", "Plan de recherche",
     "Ce que l'expérimentateur manipule délibérément pour observer son effet.",
     "Dans une étude sur le sommeil et la mémoire, la durée de sommeil imposée (4 h ou 8 h) est la variable indépendante.",
     "Si elle n'est pas manipulée mais seulement observée (les gens qui dorment peu), l'étude est corrélationnelle : on ne peut plus parler de cause."),
    ("variable-dependante", "Variable dépendante", "Plan de recherche",
     "Ce que l'on mesure pour voir si la manipulation a produit un effet.",
     "Le nombre de mots correctement rappelés le lendemain matin.",
     "Choisir sa variable dépendante après avoir vu les données, parmi plusieurs mesurées, est une forme de p-hacking."),
    ("variable-confondue", "Variable confondue", "Plan de recherche",
     "Une troisième variable qui varie en même temps que la variable indépendante et qui pourrait expliquer le résultat.",
     "Comparer un cours du matin et un cours du soir : l'heure, la fatigue, mais aussi le type d'étudiants inscrits diffèrent.",
     "C'est la menace numéro un sur la validité interne, et la raison d'être de la randomisation."),
    ("randomisation", "Répartition aléatoire", "Plan de recherche",
     "Attribuer les participants aux conditions par tirage au sort, afin d'égaliser en moyenne tout ce qui n'est pas manipulé.",
     "Un logiciel assigne chaque nouveau participant au groupe thérapie ou au groupe liste d'attente.",
     "Ne pas confondre avec l'échantillonnage aléatoire, qui concerne le recrutement dans la population et sert la validité externe."),
    ("double-aveugle", "Double aveugle", "Plan de recherche",
     "Ni le participant ni l'expérimentateur en contact avec lui ne savent quelle condition est administrée.",
     "Dans un essai médicamenteux, les gélules sont identiques et codées par un tiers.",
     "Presque impossible en psychothérapie : le thérapeute sait toujours ce qu'il fait. D'où l'importance d'évaluateurs indépendants et aveugles."),
    ("groupe-controle", "Groupe contrôle", "Plan de recherche",
     "Groupe qui ne reçoit pas l'intervention testée, et auquel on compare le groupe expérimental.",
     "Liste d'attente, traitement habituel, ou placebo actif selon les questions posées.",
     "Une liste d'attente surestime souvent l'effet du traitement, car elle ne contrôle ni l'attention reçue ni l'attente de guérison."),
    ("plan-intra", "Plan intra-sujets", "Plan de recherche",
     "Chaque participant passe toutes les conditions et sert donc de témoin à lui-même.",
     "Tester les mêmes personnes sous caféine et sous placebo, à une semaine d'intervalle.",
     "Introduit des effets d'ordre (fatigue, apprentissage) qu'il faut neutraliser par contrebalancement."),
    ("plan-inter", "Plan inter-sujets", "Plan de recherche",
     "Chaque participant ne passe qu'une seule condition ; les groupes sont comparés entre eux.",
     "Un groupe apprend par relecture, l'autre par auto-test.",
     "Demande plus de participants, car la variabilité entre personnes s'ajoute au bruit de mesure."),
    ("etude-cas", "Étude de cas", "Plan de recherche",
     "Analyse approfondie d'une seule personne ou d'un seul groupe, souvent exceptionnel.",
     "Le patient H.M. a plus appris à la science sur la mémoire que des milliers d'étudiants.",
     "Impossible à généraliser statistiquement : elle génère des hypothèses, elle ne les teste pas."),
    ("longitudinal", "Étude longitudinale", "Plan de recherche",
     "Suivi des mêmes participants sur une longue durée.",
     "L'étude de Dunedin suit plus de mille personnes nées en 1972 depuis leur naissance.",
     "L'attrition sélective : ceux qui abandonnent diffèrent systématiquement de ceux qui restent."),
    ("transversal", "Étude transversale", "Plan de recherche",
     "Comparaison, au même moment, de groupes d'âges ou de catégories différents.",
     "Comparer la mémoire de personnes de 20, 40 et 70 ans un même mois.",
     "Confond l'effet de l'âge avec l'effet de génération (effet de cohorte)."),
    ("echantillon-representatif", "Échantillon représentatif", "Mesure",
     "Échantillon dont la composition reflète celle de la population visée sur les variables pertinentes.",
     "Un sondage national stratifié par âge, sexe, région et catégorie socioprofessionnelle.",
     "La plupart des études de psychologie utilisent des échantillons de convenance, principalement étudiants."),
    ("weird-notion", "Échantillons WEIRD", "Mesure",
     "Acronyme désignant les populations occidentales, éduquées, industrialisées, riches et démocratiques, largement surreprésentées.",
     "Environ 90 % des participants publiés proviennent de pays représentant moins de 15 % de l'humanité.",
     "Ces populations sont souvent atypiques, pas moyennes : généraliser à « l'humain » est rarement justifié."),
    ("fidelite", "Fidélité", "Mesure",
     "Constance d'une mesure : elle donne le même résultat dans des conditions comparables.",
     "Un test repassé à quinze jours d'intervalle donne des scores très proches (fidélité test-retest).",
     "Une mesure peut être parfaitement fidèle et totalement invalide : une balance déréglée pèse toujours 3 kg de trop, avec constance."),
    ("validite-mesure", "Validité d'une mesure", "Mesure",
     "Degré auquel un instrument mesure effectivement ce qu'il prétend mesurer.",
     "Une échelle d'anxiété qui prédit l'évitement réel de situations sociales possède une validité prédictive.",
     "La validité apparente (« ça a l'air de mesurer l'anxiété ») ne vaut rien sans validation empirique."),
    ("alpha-cronbach", "Alpha de Cronbach", "Mesure",
     "Indice de cohérence interne d'un questionnaire : ses items mesurent-ils la même chose ?",
     "Un alpha de 0,85 sur une échelle de dix items est généralement jugé satisfaisant.",
     "Un alpha très élevé (&gt; 0,95) peut signaler que les items sont redondants, pas que l'échelle est excellente."),
    ("etalonnage", "Étalonnage", "Mesure",
     "Normes de référence établies sur un large échantillon, permettant de situer un score individuel.",
     "Un QI de 115 signifie « au-dessus de 84 % des personnes du même âge », pas « 115 unités d'intelligence ».",
     "Un étalonnage vieilli fausse tout : l'effet Flynn impose de réétalonner les tests régulièrement."),
    ("auto-declaration", "Mesure auto-déclarative", "Mesure",
     "Donnée fournie par la personne elle-même via questionnaire ou entretien.",
     "Échelles de bien-être, de stress perçu, de satisfaction au travail.",
     "Sensible à la désirabilité sociale, à l'humeur du moment et à la mauvaise introspection : on estime très mal ses propres causes."),
    ("desirabilite", "Désirabilité sociale", "Mesure",
     "Tendance à se présenter sous un jour favorable dans ses réponses.",
     "Sous-déclaration de la consommation d'alcool, surdéclaration du vote et du sport pratiqué.",
     "Se réduit par l'anonymat, les mesures indirectes ou des items de contrôle, jamais totalement."),
    ("moyenne", "Moyenne", "Statistiques descriptives",
     "Somme des valeurs divisée par leur nombre.",
     "La moyenne des temps de réaction d'un participant sur cent essais.",
     "Très sensible aux valeurs extrêmes ; trompeuse sur les distributions asymétriques comme les revenus."),
    ("mediane", "Médiane", "Statistiques descriptives",
     "Valeur qui sépare l'échantillon en deux moitiés égales.",
     "Le revenu médian décrit bien mieux la situation typique que le revenu moyen.",
     "Moins efficace que la moyenne pour les tests statistiques classiques sur données bien distribuées."),
    ("ecart-type", "Écart-type", "Statistiques descriptives",
     "Mesure de la dispersion des valeurs autour de la moyenne.",
     "Deux classes ont 12/20 de moyenne : l'une avec un écart-type de 1, l'autre de 6. Ce ne sont pas les mêmes classes.",
     "Une moyenne publiée sans dispersion doit toujours éveiller la méfiance."),
    ("distribution-normale", "Distribution normale", "Statistiques descriptives",
     "Distribution symétrique en cloche, où 68 % des valeurs tombent à un écart-type de la moyenne.",
     "Taille adulte, scores de QI par construction, erreurs de mesure.",
     "Beaucoup de variables psychologiques ne la suivent pas (temps de réaction, symptômes, revenus)."),
    ("hypothese-nulle", "Hypothèse nulle", "Inférence",
     "Hypothèse de départ selon laquelle il n'existe aucun effet dans la population.",
     "« La méditation ne modifie pas le niveau d'anxiété. »",
     "On ne « prouve » jamais l'hypothèse nulle : ne pas trouver d'effet n'équivaut pas à démontrer son absence."),
    ("valeur-p", "Valeur p", "Inférence",
     "Probabilité d'obtenir un résultat au moins aussi extrême si l'hypothèse nulle était vraie.",
     "p = 0,03 : un tel écart surviendrait 3 fois sur 100 en l'absence de tout effet réel.",
     "Ce n'est ni la probabilité que l'hypothèse soit vraie, ni la probabilité de réplication, ni une mesure de l'importance de l'effet."),
    ("erreur-type-i", "Erreur de type I", "Inférence",
     "Conclure à un effet qui n'existe pas (faux positif).",
     "Annoncer qu'un programme améliore les notes alors qu'il ne change rien.",
     "Sa probabilité augmente mécaniquement avec le nombre de tests effectués sur les mêmes données."),
    ("erreur-type-ii", "Erreur de type II", "Inférence",
     "Ne pas détecter un effet qui existe réellement (faux négatif).",
     "Une étude sur 20 participants qui conclut à l'inefficacité d'une thérapie pourtant utile.",
     "Presque toujours due à une puissance statistique insuffisante — donc à un échantillon trop petit."),
    ("puissance", "Puissance statistique", "Inférence",
     "Probabilité de détecter un effet réel s'il existe ; on vise conventionnellement 80 %.",
     "Détecter un effet moyen (d = 0,5) entre deux groupes demande environ 64 participants par groupe.",
     "Une étude sous-puissante qui trouve un effet le surestime nécessairement : c'est l'effet « winner's curse »."),
    ("taille-effet-notion", "Taille d'effet", "Inférence",
     "Mesure de l'ampleur d'un phénomène, indépendante de la taille de l'échantillon.",
     "d de Cohen pour une différence de moyennes, r pour une association, odds ratio pour un risque.",
     "C'est l'information la plus importante d'un article, et souvent la plus discrètement présentée."),
    ("intervalle-confiance", "Intervalle de confiance", "Inférence",
     "Plage de valeurs plausibles pour l'effet réel, généralement à 95 %.",
     "Un effet estimé à d = 0,45 [0,10 ; 0,80] est positif mais très imprécis.",
     "Un intervalle qui contient zéro correspond à un résultat non significatif — mais l'intervalle dit bien plus que ce verdict binaire."),
    ("correlation", "Corrélation", "Inférence",
     "Mesure du degré de variation conjointe de deux variables, entre −1 et +1.",
     "r = 0,25 entre temps d'écran et sommeil insuffisant chez l'adolescent.",
     "Une corrélation n'établit jamais la causalité, et son carré (ici 6 % de variance) refroidit souvent l'enthousiasme."),
    ("causalite", "Inférence causale", "Inférence",
     "Conclusion selon laquelle une variable produit un changement dans une autre.",
     "Elle exige la manipulation, la randomisation et le contrôle des variables confondues.",
     "Les verbes des titres de presse (« améliore », « provoque ») précèdent régulièrement toute preuve causale."),
    ("regression-moyenne", "Régression vers la moyenne", "Inférence",
     "Tendance des valeurs extrêmes à se rapprocher de la moyenne lors d'une seconde mesure.",
     "Les personnes recrutées au pic de leur douleur vont statistiquement mieux ensuite, quoi qu'on leur donne.",
     "Explique à elle seule l'apparente efficacité d'innombrables remèdes pris au plus mal."),
    ("p-hacking-notion", "p-hacking", "Intégrité scientifique",
     "Ensemble de choix d'analyse, faits après avoir vu les données, qui font passer un résultat sous le seuil de significativité.",
     "Ajouter des participants jusqu'à obtenir p &lt; 0,05, tester plusieurs variables et ne rapporter que la bonne.",
     "Rarement malhonnête au sens intentionnel : c'est une accumulation de décisions qui semblent raisonnables une par une."),
    ("harking", "HARKing", "Intégrité scientifique",
     "Formuler l'hypothèse après avoir connu les résultats, puis la présenter comme prévue à l'avance.",
     "Une étude exploratoire sur vingt variables, publiée comme un test confirmatoire d'une seule.",
     "Transforme une exploration légitime en fausse confirmation, et gonfle le taux de faux positifs de la littérature."),
    ("biais-publication", "Biais de publication", "Intégrité scientifique",
     "Tendance des revues et des auteurs à publier surtout les résultats positifs et spectaculaires.",
     "Les études ne trouvant aucun effet finissent dans le « tiroir des manuscrits ».",
     "Fausse toutes les méta-analyses vers le haut : l'effet moyen publié est systématiquement surestimé."),
    ("preenregistrement", "Préenregistrement", "Intégrité scientifique",
     "Dépôt public des hypothèses et du plan d'analyse avant la collecte des données.",
     "Plateformes comme l'Open Science Framework ou AsPredicted.",
     "N'améliore pas la qualité d'un protocole médiocre : il empêche seulement de réécrire l'histoire après coup."),
    ("registered-report", "Registered Report", "Intégrité scientifique",
     "Format éditorial où l'article est accepté sur la base du protocole, avant que les résultats soient connus.",
     "Plus d'une centaine de revues le proposent aujourd'hui.",
     "Supprime le biais de publication à la source, mais allonge sensiblement les délais."),
    ("replication", "Réplication", "Intégrité scientifique",
     "Refaire une étude pour vérifier si le résultat tient. Directe (même protocole) ou conceptuelle (autre opérationnalisation).",
     "Les projets Many Labs testent un même protocole dans des dizaines de laboratoires.",
     "Une réplication conceptuelle qui échoue est ambiguë : on ne sait pas si l'effet est faux ou si le protocole diffère trop."),
    ("science-ouverte", "Science ouverte", "Intégrité scientifique",
     "Mise à disposition publique des données, du code, des matériels et des publications.",
     "Archives ouvertes HAL et PsyArXiv, dépôts de données sur l'Open Science Framework.",
     "Partager des données sur l'humain suppose une anonymisation soignée et un cadre juridique respecté (RGPD)."),
    ("consentement", "Consentement libre et éclairé", "Éthique",
     "Accord donné après information complète, sans contrainte, et révocable à tout moment.",
     "Formulaire détaillant les objectifs, la durée, les risques, le traitement des données et le droit de retrait.",
     "Le consentement est fragilisé quand le chercheur détient un pouvoir sur le participant (enseignant, médecin, employeur)."),
    ("debriefing", "Débriefing", "Éthique",
     "Information complète donnée après coup lorsqu'une tromperie était nécessaire au protocole.",
     "Expliquer aux participants d'une étude sur le conformisme que les autres étaient des complices.",
     "Ne répare pas tout : Milgram a été critiqué précisément parce que le débriefing ne suffisait pas à effacer le vécu."),
    ("comite-ethique", "Comité d'éthique", "Éthique",
     "Instance indépendante qui évalue le rapport bénéfice-risque d'un protocole avant son lancement.",
     "En France, comités de protection des personnes pour les recherches interventionnelles.",
     "Son avis ne dispense pas le chercheur de sa responsabilité propre, ni de la vigilance en cours d'étude."),
    ("anonymisation", "Anonymisation et RGPD", "Éthique",
     "Traitement des données garantissant qu'une personne ne puisse pas être réidentifiée.",
     "Suppression des identifiants directs, agrégation des données rares, conservation limitée dans le temps.",
     "La pseudonymisation n'est pas l'anonymisation : tant qu'une table de correspondance existe, le RGPD s'applique pleinement."),
    ("essai-randomise", "Essai contrôlé randomisé", "Preuve",
     "Plan de référence pour évaluer une intervention : participants tirés au sort entre traitement et contrôle.",
     "Comparer une thérapie cognitivo-comportementale à une liste d'attente et à un traitement habituel.",
     "Fort en validité interne, souvent faible en validité externe : les patients inclus ressemblent peu à ceux des consultations réelles."),
    ("meta-analyse-notion", "Méta-analyse", "Preuve",
     "Synthèse statistique de plusieurs études portant sur la même question.",
     "Estimer l'effet global de la pratique de récupération sur la mémorisation à long terme.",
     "Sa qualité ne dépasse jamais celle des études incluses, et elle reste vulnérable au biais de publication."),
    ("niveaux-preuve", "Hiérarchie des preuves", "Preuve",
     "Classement des sources selon leur capacité à établir une conclusion causale fiable.",
     "Témoignage &lt; cas clinique &lt; corrélation &lt; essai randomisé &lt; réplication &lt; méta-analyse d'essais préenregistrés.",
     "Une hiérarchie n'est pas un couperet : un essai randomisé mal conduit vaut moins qu'une étude observationnelle exemplaire."),
    ("neuromythe", "Neuromythe", "Esprit critique",
     "Croyance fausse sur le cerveau, largement répandue y compris chez les enseignants.",
     "« On n'utilise que 10 % de notre cerveau », « cerveau gauche rationnel contre cerveau droit créatif », « styles d'apprentissage ».",
     "Leur résistance vient de leur utilité narrative : ils expliquent simplement, ils rassurent, et ils se vendent bien."),
    ("effet-barnum", "Effet Barnum", "Esprit critique",
     "Tendance à accepter comme personnellement pertinente une description vague valable pour presque tout le monde.",
     "« Vous êtes sociable mais vous avez besoin de moments de solitude. » Horoscopes, tests de personnalité non validés.",
     "C'est la raison pour laquelle un test qui « tombe juste » n'est pas pour autant un test valide."),
    ("temoignage", "Argument du témoignage", "Esprit critique",
     "Se fonder sur des cas individuels marquants plutôt que sur des données agrégées.",
     "« Ma cousine a guéri grâce à cette méthode. »",
     "Un témoignage ne contient aucune information sur ce qui serait arrivé sans l'intervention : il manque toujours le groupe contrôle."),
]
