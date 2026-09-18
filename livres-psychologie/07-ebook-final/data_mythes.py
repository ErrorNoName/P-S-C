# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Idées reçues et neuromythes.

Format : (id, affirmation, famille, verdict, ce_qu_on_sait, origine, nuance)
`verdict` vaut "faux", "exagere" ou "partiel" et sert au filtrage.
"""

MYTHES = [
    (
        "dix-pourcent",
        "« Nous n'utilisons que 10 % de notre cerveau »",
        "Cerveau",
        "faux",
        "L'imagerie montre une activité dans l'ensemble de l'encéphale au cours d'une journée, et aucune "
        "région n'est silencieuse. Le cerveau consomme environ 20 % de l'énergie du corps pour 2 % de sa "
        "masse : une telle dépense pour 90 % de tissu inutile serait aberrante d'un point de vue évolutif. "
        "Surtout, les lésions cérébrales, même petites, produisent presque toujours un déficit — ce qui "
        "serait impossible si l'essentiel du cerveau était en réserve.",
        "L'idée circule depuis le début du XXᵉ siècle, nourrie par une mauvaise lecture des travaux sur "
        "les neurones « silencieux » et par le constat, vrai, que les neurones ne déchargent pas tous "
        "simultanément.",
        "Ce qui est vrai : à un instant donné, seule une fraction des neurones décharge, et un cerveau où "
        "tous les neurones s'activeraient ensemble s'appelle une crise d'épilepsie.",
    ),
    (
        "cerveau-gauche-droit",
        "« Il y a des cerveaux gauches logiques et des cerveaux droits créatifs »",
        "Cerveau",
        "faux",
        "Les études d'imagerie portant sur plus de mille personnes n'ont trouvé aucune preuve qu'un "
        "individu utilise globalement plus un hémisphère que l'autre. Toute tâche un peu complexe "
        "mobilise les deux côtés, reliés par 200 millions de fibres qui échangent en permanence.",
        "Les travaux réels sur les patients au cerveau divisé, dont le corps calleux avait été sectionné "
        "pour traiter une épilepsie grave, ont montré des spécialisations fines — puis la vulgarisation "
        "les a transformées en types de personnalité.",
        "Ce qui est vrai : certaines fonctions sont latéralisées, notamment le langage, majoritairement à "
        "gauche chez les droitiers. Mais latéralisation d'une fonction ne veut pas dire dominance d'un "
        "hémisphère chez une personne.",
    ),
    (
        "styles-apprentissage",
        "« Chacun a son style d'apprentissage : visuel, auditif ou kinesthésique »",
        "Apprentissage",
        "faux",
        "Des dizaines d'expériences ont testé l'hypothèse décisive : enseigner à quelqu'un dans son style "
        "déclaré devrait améliorer ses résultats plus que l'enseigner dans un autre. Presque aucune ne "
        "l'observe. Les préférences existent, mais elles ne prédisent pas la manière dont on apprend le "
        "mieux.",
        "L'idée est intuitive, flatteuse et commercialement rentable : elle a nourri une industrie entière "
        "de formations et de questionnaires.",
        "Ce qui est vrai : le format optimal dépend du contenu, pas de l'élève. On apprend la géographie "
        "avec des cartes et la prononciation avec du son, quel que soit son « style ». Et présenter la "
        "même idée sous deux formats à la fois — texte et image — aide presque tout le monde.",
    ),
    (
        "mozart",
        "« Écouter Mozart rend les bébés plus intelligents »",
        "Apprentissage",
        "faux",
        "L'étude d'origine portait sur des étudiants adultes, montrait un gain de quelques minutes sur une "
        "tâche de rotation mentale, et ne parlait ni de bébés ni d'intelligence générale. Les tentatives "
        "de réplication attribuent l'effet à une simple hausse temporaire de la vigilance et de l'humeur, "
        "que n'importe quelle musique appréciée produit aussi.",
        "Un article de 1993 amplifié par la presse, puis par un gouverneur d'État américain qui fit "
        "distribuer des disques classiques aux nouveau-nés.",
        "Ce qui est vrai : apprendre à jouer d'un instrument, sur des années, s'accompagne de bénéfices "
        "cognitifs modestes. C'est la pratique musicale active qui compte, pas l'écoute passive.",
    ),
    (
        "subliminal",
        "« Les messages subliminaux manipulent nos achats »",
        "Perception",
        "exagere",
        "L'expérience fondatrice du cinéma qui aurait fait vendre du pop-corn n'a jamais eu lieu : son "
        "auteur a reconnu l'avoir inventée. En laboratoire, une amorce subliminale peut légèrement "
        "orienter un choix déjà envisagé, pendant quelques secondes, chez une personne déjà motivée — "
        "elle ne crée pas un désir ni ne renverse une intention.",
        "Un coup publicitaire de 1957, entretenu par la crainte des techniques de persuasion cachée.",
        "Ce qui est vrai : beaucoup d'influences échappent réellement à la conscience, mais ce sont "
        "surtout des messages parfaitement visibles — un cadrage, un prix de référence, un visage souriant "
        "— dont on ignore l'effet sur soi.",
    ),
    (
        "polygraphe",
        "« Le détecteur de mensonge dit si l'on ment »",
        "Mesure",
        "faux",
        "L'appareil enregistre le rythme cardiaque, la respiration et la conductance de la peau : il "
        "mesure une activation, pas une intention de tromper. Un innocent terrifié produit le même profil "
        "qu'un coupable, et des contre-mesures simples suffisent à fausser le résultat. Les expertises "
        "scientifiques concluent à une validité insuffisante pour la preuve judiciaire.",
        "Une invention du début du XXᵉ siècle, popularisée par la fiction et par des usages policiers où "
        "l'appareil sert surtout à impressionner l'interrogé.",
        "Ce qui est vrai : la variante dite du test des informations dissimulées, qui vérifie si la "
        "personne réagit à un détail que seul l'auteur des faits peut connaître, repose sur une logique "
        "plus solide.",
    ),
    (
        "multitache",
        "« Certaines personnes sont douées pour le multitâche »",
        "Attention",
        "faux",
        "Sauf automatisation complète de l'une des tâches, le cerveau alterne au lieu de traiter en "
        "parallèle, et chaque bascule coûte du temps et des erreurs. Paradoxalement, les personnes qui se "
        "déclarent excellentes en multitâche obtiennent en moyenne de moins bons résultats aux mesures "
        "objectives d'attention et d'inhibition.",
        "La confusion entre alternance rapide et simultanéité, entretenue par le sentiment subjectif de "
        "fluidité.",
        "Ce qui est vrai : on peut combiner une tâche automatisée et une tâche contrôlée — marcher et "
        "discuter. Deux tâches exigeant la même ressource, comme écrire et écouter, se dégradent "
        "toujours mutuellement.",
    ),
    (
        "schizophrenie-personnalite",
        "« La schizophrénie, c'est avoir plusieurs personnalités »",
        "Clinique",
        "faux",
        "La schizophrénie associe des symptômes dits positifs — hallucinations, idées délirantes — des "
        "symptômes négatifs comme le retrait et l'appauvrissement affectif, et une désorganisation de la "
        "pensée. Le trouble dissociatif de l'identité, très rare et très discuté, est une entité "
        "clinique entièrement distincte.",
        "L'étymologie du mot, qui évoque un esprit fendu, et un usage figuré répandu dans les médias.",
        "Ce qui est vrai : le mot grec signifie bien « esprit divisé », mais son auteur désignait la "
        "dissociation entre pensée, émotion et comportement, pas la coexistence de plusieurs personnes.",
    ),
    (
        "violence-malades",
        "« Les personnes atteintes de troubles psychiques sont dangereuses »",
        "Clinique",
        "faux",
        "Les personnes vivant avec un trouble psychique sévère sont bien plus souvent victimes qu'auteurs "
        "de violences. La part des actes violents attribuable à ces troubles reste très minoritaire, et "
        "les facteurs qui prédisent réellement la violence sont les mêmes que dans la population générale : "
        "antécédents de violence, consommation d'alcool ou de substances, précarité.",
        "La surreprésentation médiatique des faits divers impliquant un trouble psychiatrique.",
        "Ce qui est vrai : certains états aigus non traités, surtout associés à une consommation de "
        "substances, élèvent le risque. C'est un argument pour l'accès aux soins, pas pour l'exclusion.",
    ),
    (
        "depression-tristesse",
        "« La dépression, c'est de la tristesse qu'on peut secouer »",
        "Clinique",
        "faux",
        "La dépression caractérisée est un trouble qui associe, pendant au moins deux semaines et presque "
        "toute la journée, une humeur abaissée ou une perte de plaisir, avec des atteintes du sommeil, de "
        "l'appétit, de la concentration, de l'énergie et de l'estime de soi. L'incapacité à réagir fait "
        "partie du trouble : demander à une personne déprimée de se reprendre revient à demander à une "
        "personne asthmatique de mieux respirer.",
        "La confusion entre un mot du langage courant et une catégorie clinique portant le même nom.",
        "Ce qui est vrai : la tristesse ordinaire est une émotion normale et utile. Elle est réactive, "
        "circonscrite dans le temps, et n'abolit pas la capacité à éprouver du plaisir.",
    ),
    (
        "autisme-vaccins",
        "« Les vaccins provoquent l'autisme »",
        "Développement",
        "faux",
        "L'étude à l'origine de cette affirmation portait sur douze enfants, comportait des données "
        "falsifiées, a été rétractée et son auteur radié. Des cohortes totalisant plusieurs millions "
        "d'enfants n'ont retrouvé aucune association. Les premiers signes d'autisme apparaissent "
        "simplement à l'âge où sont administrés certains vaccins, ce qui crée une coïncidence temporelle.",
        "Un article frauduleux de 1998 et sa reprise médiatique massive.",
        "Ce qui est vrai : les causes de l'autisme sont largement génétiques et précoces, souvent "
        "antérieures à la naissance.",
    ),
    (
        "autisme-froid",
        "« L'autisme vient d'un manque d'affection maternelle »",
        "Développement",
        "faux",
        "Cette hypothèse, sans aucun fondement empirique, a causé un tort considérable à des générations "
        "de familles. Les études de jumeaux montrent une héritabilité élevée, et l'on connaît aujourd'hui "
        "de nombreuses variantes génétiques et facteurs prénataux impliqués.",
        "Une théorie des années 1950 qui tenait l'attitude maternelle pour responsable, reprise pendant "
        "des décennies dans certains milieux cliniques.",
        "Ce qui est vrai : l'environnement compte pour l'accompagnement et la qualité de vie — les "
        "interventions précoces améliorent nettement la trajectoire — mais il n'est pas la cause.",
    ),
    (
        "sucre-hyperactivite",
        "« Le sucre rend les enfants hyperactifs »",
        "Développement",
        "faux",
        "Les essais en double aveugle, où ni l'enfant ni l'observateur ne sait si la boisson contenait du "
        "sucre, ne retrouvent aucune différence de comportement. En revanche, les parents persuadés que "
        "leur enfant a consommé du sucre le jugent plus agité — même quand ce n'est pas le cas.",
        "La coïncidence entre les occasions festives, riches en sucre, et l'excitation liée à la fête "
        "elle-même.",
        "Ce qui est vrai : l'alimentation influence le comportement par d'autres voies, notamment le "
        "sommeil et la régularité des repas.",
    ),
    (
        "periode-critique",
        "« Après trois ans, tout est joué »",
        "Développement",
        "exagere",
        "Le cerveau conserve une plasticité importante toute la vie : on apprend à lire à l'âge adulte, "
        "on récupère après un accident vasculaire, on modifie durablement des habitudes. Les enfants "
        "adoptés tardivement après une privation sévère progressent souvent de façon spectaculaire.",
        "Une lecture rigide des périodes sensibles observées chez l'animal, amplifiée par des campagnes de "
        "sensibilisation à la petite enfance.",
        "Ce qui est vrai : certaines fenêtres sont réellement sensibles — la vision binoculaire, la "
        "phonologie d'une langue — et les premières années sont particulièrement rentables. Rentable ne "
        "signifie pas irréversible.",
    ),
    (
        "hypnose-controle",
        "« Sous hypnose, on perd le contrôle de soi »",
        "Clinique",
        "faux",
        "Une personne hypnotisée reste consciente, garde ses valeurs et refuse ce qui lui répugne "
        "profondément. L'hypnose se caractérise par une attention focalisée et une suggestibilité accrue, "
        "pas par une abolition de la volonté. La susceptibilité varie fortement d'un individu à l'autre et "
        "reste assez stable.",
        "La scène et le cinéma, qui mettent en scène une soumission spectaculaire.",
        "Ce qui est vrai : l'hypnose a des effets mesurables et utiles, notamment sur la douleur et "
        "l'anxiété procédurale. Elle est en revanche à proscrire pour retrouver des souvenirs, car elle "
        "augmente la confiance sans augmenter l'exactitude.",
    ),
    (
        "souvenirs-refoules",
        "« Les souvenirs traumatiques refoulés peuvent être retrouvés intacts »",
        "Mémoire",
        "faux",
        "La mémoire ne fonctionne pas comme un enregistrement scellé. Le traumatisme est bien plus souvent "
        "sur-mémorisé qu'oublié. Surtout, des expériences ont montré qu'on peut implanter chez une "
        "personne le souvenir détaillé et sincèrement vécu d'un événement qui n'a jamais eu lieu, "
        "simplement par des entretiens suggestifs répétés.",
        "Des pratiques thérapeutiques des années 1980-1990 visant à « récupérer » des souvenirs, qui ont "
        "donné lieu à des accusations judiciaires ensuite invalidées.",
        "Ce qui est vrai : on peut ne pas penser à un événement pendant des années puis s'en souvenir. "
        "Cela n'implique ni refoulement ni fidélité du souvenir.",
    ),
    (
        "temoignage",
        "« Un témoin sûr de lui est un témoin fiable »",
        "Mémoire",
        "faux",
        "La confiance et l'exactitude d'un témoignage ne sont que faiblement liées, surtout après une "
        "identification. La simple manière de formuler une question modifie le souvenir rapporté, et la "
        "confiance augmente à chaque récit, y compris quand le contenu se déforme.",
        "L'intuition, partagée par les jurys, qu'un souvenir vif est un souvenir exact.",
        "Ce qui est vrai : la confiance exprimée immédiatement après une première identification, dans "
        "des conditions non suggestives, a une valeur informative — qui s'effondre ensuite.",
    ),
    (
        "photographique",
        "« Certaines personnes ont une mémoire photographique »",
        "Mémoire",
        "exagere",
        "Aucune étude contrôlée n'a mis en évidence chez l'adulte une capacité à lire mentalement une "
        "image stockée comme on lirait une photographie. Les performances exceptionnelles documentées "
        "reposent sur des stratégies d'encodage entraînées, comme le palais mental, et restent limitées à "
        "un domaine précis.",
        "Des récits anecdotiques et une forme réelle mais rare d'imagerie persistante observée chez "
        "certains enfants.",
        "Ce qui est vrai : l'hypermnésie autobiographique existe — quelques dizaines de personnes "
        "documentées se souviennent de presque chaque jour de leur vie — mais elle ne concerne pas les "
        "images arbitraires.",
    ),
    (
        "qi-fixe",
        "« Le QI est fixé à la naissance et ne change pas »",
        "Mesure",
        "faux",
        "Le score de QI varie avec la scolarisation, la santé, la nutrition et l'environnement : une année "
        "de scolarité supplémentaire élève le score de plusieurs points. À l'échelle des populations, les "
        "scores bruts ont augmenté régulièrement pendant des décennies, ce qui exclut une détermination "
        "purement innée.",
        "Une confusion entre héritabilité, qui décrit la part de variance attribuable aux différences "
        "génétiques dans une population donnée, et immuabilité individuelle.",
        "Ce qui est vrai : le QI est relativement stable à l'âge adulte et prédit statistiquement "
        "certaines réussites. Un score reste une mesure de performance dans un contexte, pas une essence.",
    ),
    (
        "test-personnalite-mbti",
        "« Les tests de personnalité en seize types révèlent qui l'on est »",
        "Mesure",
        "faux",
        "Ces outils découpent en catégories des dimensions en réalité continues : la plupart des gens se "
        "situent au milieu et basculent d'un type à l'autre selon le jour de passation. La fidélité "
        "test-retest est faible et la validité prédictive sur la réussite professionnelle est très "
        "limitée.",
        "Un questionnaire élaboré hors du champ académique, puis massivement diffusé en entreprise pour "
        "sa lisibilité.",
        "Ce qui est vrai : les modèles dimensionnels comme celui des cinq grands facteurs reposent sur "
        "des décennies de validation et prédisent, modestement mais de façon reproductible, plusieurs "
        "comportements.",
    ),
    (
        "graphologie",
        "« L'écriture révèle la personnalité »",
        "Mesure",
        "faux",
        "Les études contrôlées, où les graphologues analysent des textes de contenu neutre pour éviter "
        "qu'ils s'appuient sur le sens, ne trouvent pas de validité supérieure au hasard. Les "
        "appréciations obtenues sont assez vagues pour sembler justes à presque n'importe qui.",
        "Une tradition ancienne et l'impression subjective de reconnaître une personne à son écriture.",
        "Ce qui est vrai : l'écriture varie avec l'état du moment — fatigue, hâte, émotion — et certaines "
        "pathologies neurologiques la modifient de façon diagnostique. Cela ne concerne pas les traits de "
        "caractère.",
    ),
    (
        "horoscope-barnum",
        "« Mon horoscope me décrit vraiment bien »",
        "Mesure",
        "faux",
        "Lorsqu'on distribue à tout un groupe le même portrait de personnalité, la plupart des personnes "
        "le jugent remarquablement exact. Ce texte est composé d'énoncés assez généraux et légèrement "
        "flatteurs pour convenir à chacun. C'est l'effet Barnum.",
        "La formulation volontairement ambiguë des descriptions, combinée à notre tendance à retenir ce "
        "qui nous correspond.",
        "Ce qui est vrai : la sensation de justesse est authentique. Elle mesure la souplesse du texte, "
        "pas sa validité.",
    ),
    (
        "opposes-attirent",
        "« Les opposés s'attirent »",
        "Relations",
        "faux",
        "Les couples durables se ressemblent davantage que le hasard ne le prédirait : sur l'âge, le "
        "niveau d'éducation, les valeurs, les habitudes et les attitudes. La similitude prédit "
        "l'attirance initiale comme la satisfaction à long terme.",
        "Le caractère mémorable des couples contrastés et une lecture romanesque de la complémentarité.",
        "Ce qui est vrai : une complémentarité sur des rôles concrets — qui organise, qui apaise — peut "
        "être fonctionnelle. Elle s'exerce sur un fond de valeurs partagées.",
    ),
    (
        "defouler-colere",
        "« Se défouler fait retomber la colère »",
        "Émotions",
        "faux",
        "Frapper un coussin ou crier augmente l'activation physiologique et rend le comportement agressif "
        "ultérieur plus probable, pas moins. Les expériences comparant défoulement, distraction et "
        "attente montrent systématiquement que le défoulement est la pire option.",
        "Un modèle hydraulique de l'émotion, hérité de la première psychanalyse, où la pression "
        "s'accumule et doit s'évacuer.",
        "Ce qui est vrai : ce qui apaise réellement, c'est le délai, la réévaluation de la situation, "
        "l'activité physique non agressive et la mise en mots à distance de l'épisode.",
    ),
    (
        "sourire-bonheur",
        "« Il suffit de sourire pour se sentir mieux »",
        "Émotions",
        "exagere",
        "L'hypothèse selon laquelle la contraction des muscles du sourire améliore l'humeur a échoué lors "
        "d'une réplication coordonnée entre de nombreux laboratoires. Si un effet existe, il est très "
        "faible et fortement dépendant du contexte.",
        "Une expérience célèbre des années 1980 où les participants tenaient un stylo entre leurs dents.",
        "Ce qui est vrai : l'expression et le ressenti s'influencent mutuellement, mais bien plus "
        "faiblement que la version populaire ne le suggère.",
    ),
    (
        "estime-de-soi",
        "« Augmenter l'estime de soi améliore les résultats scolaires »",
        "Éducation",
        "faux",
        "La corrélation existe mais la causalité va principalement dans l'autre sens : réussir élève "
        "l'estime de soi. Les programmes visant directement à valoriser les élèves sans améliorer leurs "
        "compétences n'ont pas d'effet sur les résultats, et un excès d'auto-évaluation positive est "
        "associé à une réaction plus agressive face à l'échec.",
        "Des politiques éducatives des années 1980-1990 fondées sur l'idée que l'estime de soi était la "
        "clé de tout.",
        "Ce qui est vrai : un sentiment d'efficacité fondé sur des réussites réelles, lui, soutient "
        "l'effort et la persévérance.",
    ),
    (
        "punition-efficace",
        "« La punition est le moyen le plus efficace de corriger un comportement »",
        "Éducation",
        "exagere",
        "La punition supprime rapidement un comportement en présence de celui qui punit, mais elle "
        "n'enseigne pas quoi faire à la place, provoque évitement et dissimulation, et son effet "
        "s'estompe. Le renforcement du comportement souhaité produit des apprentissages plus stables.",
        "Son efficacité immédiate, très visible, qui renforce celui qui punit.",
        "Ce qui est vrai : une conséquence négative immédiate, proportionnée, prévisible et accompagnée "
        "d'une alternative explicite a sa place. C'est la punition sévère, tardive ou imprévisible qui "
        "échoue.",
    ),
    (
        "pleine-lune",
        "« La pleine lune agite les gens »",
        "Croyances",
        "faux",
        "Les analyses portant sur les admissions aux urgences psychiatriques, les naissances, les "
        "accidents et les crimes ne trouvent pas d'effet lunaire. Le personnel soignant y croit pourtant "
        "largement, parce qu'on remarque et mémorise les nuits agitées coïncidant avec une pleine lune, "
        "et pas les autres.",
        "Une tradition ancienne et un biais de confirmation particulièrement puissant en milieu "
        "hospitalier.",
        "Ce qui est vrai : la luminosité nocturne peut perturber le sommeil de certaines personnes, ce "
        "qui est un effet de lumière, pas de lune.",
    ),
    (
        "eau-cerveau",
        "« Le cerveau est un muscle qu'il faut faire travailler avec des jeux »",
        "Cerveau",
        "exagere",
        "L'entraînement cérébral commercial améliore surtout la performance à l'exercice entraîné. Le "
        "transfert vers la mémoire quotidienne, l'attention au travail ou la prévention du déclin cognitif "
        "reste très faible dans les essais rigoureux.",
        "Un marché de programmes d'entraînement promettant un gain général de capacités.",
        "Ce qui est vrai : l'activité physique régulière, le sommeil, la vie sociale et l'apprentissage "
        "réel d'une compétence nouvelle — une langue, un instrument — ont des effets mieux étayés.",
    ),
    (
        "neurones-pas-nouveaux",
        "« On ne fabrique plus de neurones à l'âge adulte »",
        "Cerveau",
        "partiel",
        "La question reste vivement débattue : certaines équipes rapportent une neurogenèse persistante "
        "dans l'hippocampe adulte, d'autres ne la retrouvent pas avec des méthodes différentes. Ce qui "
        "est certain, c'est que le cerveau adulte se réorganise massivement — synapses, myéline, "
        "connexions — même si le nombre de neurones varie peu.",
        "Un dogme du XXᵉ siècle, puis un renversement médiatique enthousiaste, puis un retour de la "
        "prudence.",
        "Ce qui est vrai dans tous les cas : la plasticité adulte est réelle et considérable, sans avoir "
        "besoin de nouveaux neurones pour s'exercer.",
    ),
    (
        "alcool-tue-neurones",
        "« Chaque verre d'alcool tue des neurones »",
        "Cerveau",
        "exagere",
        "L'alcool ne détruit pas les neurones à chaque prise ; il altère la transmission synaptique et, en "
        "consommation chronique élevée, endommage les dendrites et certaines structures, notamment par "
        "carence en vitamine B1. Le dommage est réel mais son mécanisme n'est pas celui qu'on imagine.",
        "Une simplification pédagogique des campagnes de prévention.",
        "Ce qui est vrai : la consommation chronique importante réduit bien le volume cérébral et altère "
        "la mémoire, et une partie de ces effets régresse à l'arrêt.",
    ),
    (
        "somnambule-reveil",
        "« Il ne faut jamais réveiller un somnambule »",
        "Sommeil",
        "faux",
        "Réveiller un somnambule provoque au pire une confusion passagère. Le laisser déambuler près d'un "
        "escalier ou d'une fenêtre est bien plus dangereux. La conduite recommandée est de le guider "
        "doucement vers son lit, en le réveillant si nécessaire.",
        "Une croyance ancienne selon laquelle l'âme s'absenterait pendant l'épisode.",
        "Ce qui est vrai : le somnambulisme survient en sommeil lent profond, ce qui explique la "
        "désorientation au réveil et l'absence de souvenir.",
    ),
    (
        "huit-heures",
        "« Tout le monde a besoin de huit heures de sommeil »",
        "Sommeil",
        "exagere",
        "Le besoin individuel varie, en gros, entre sept et neuf heures chez l'adulte, avec une "
        "composante génétique. Le bon critère n'est pas un chiffre mais la vigilance diurne sans "
        "somnolence et le réveil spontané sans réveille-matin les jours libres.",
        "Une moyenne statistique transformée en norme universelle.",
        "Ce qui est vrai : la dette de sommeil s'accumule et dégrade réellement l'humeur, l'attention et "
        "la mémoire. Les très courts dormeurs authentiques sont extrêmement rares.",
    ),
    (
        "reves-sens",
        "« Chaque rêve a une signification cachée qu'on peut décoder »",
        "Sommeil",
        "exagere",
        "Aucune clé des songes ne résiste à l'épreuve : les mêmes images renvoient à des expériences "
        "différentes selon les personnes. Les rêves reprennent largement les préoccupations, les lieux et "
        "les personnes de la vie éveillée, ce qui les rend interprétables sans symbolique universelle.",
        "La tradition onirocritique et la diffusion des premières théories psychanalytiques du rêve.",
        "Ce qui est vrai : le contenu des rêves est informatif sur ce qui préoccupe le rêveur, et les "
        "cauchemars répétés post-traumatiques répondent à des thérapies spécifiques de répétition "
        "d'imagerie.",
    ),
    (
        "detox-numerique-dopamine",
        "« Les écrans provoquent des décharges de dopamine comme une drogue »",
        "Numérique",
        "exagere",
        "La dopamine n'est pas une molécule du plaisir mais de l'anticipation et de l'apprentissage par "
        "la récompense : elle est libérée par une bonne nouvelle, une conversation, un repas. L'amplitude "
        "observée avec les écrans est sans commune mesure avec celle des substances addictives.",
        "Un raccourci de vulgarisation qui assimile toute activité gratifiante à une addiction chimique.",
        "Ce qui est vrai : les interfaces sont conçues pour exploiter la récompense variable, et l'usage "
        "problématique existe. Le décrire correctement rend la prévention plus crédible, pas moins.",
    ),
    (
        "ecrans-qi",
        "« Les écrans détruisent le cerveau des enfants »",
        "Numérique",
        "exagere",
        "Les études trouvent des associations faibles entre temps d'écran total et bien-être, souvent "
        "du même ordre que celles observées avec la consommation de pommes de terre. Ce qui compte "
        "davantage est ce qui est fait à l'écran, avec qui, et surtout ce que l'écran remplace : sommeil, "
        "activité physique, interactions.",
        "La vitesse du changement technologique et une inquiétude légitime des parents, amplifiée par des "
        "titres alarmistes.",
        "Ce qui est vrai : l'exposition le soir dégrade le sommeil, et l'usage très précoce en "
        "remplacement d'interactions langagières est réellement défavorable.",
    ),
    (
        "besoin-parler-trauma",
        "« Après un choc, il faut absolument en parler tout de suite »",
        "Clinique",
        "faux",
        "Les séances de débriefing psychologique imposées immédiatement après un événement traumatique "
        "n'ont pas montré de bénéfice et, dans plusieurs essais, ont été associées à une évolution moins "
        "favorable. Reparcourir les détails avant stabilisation peut renforcer la trace.",
        "L'intuition que verbaliser soulage toujours, et des protocoles institutionnels des années 1990.",
        "Ce qui est vrai : le soutien social, la sécurité, l'information et l'accès à une prise en charge "
        "structurée si les symptômes persistent au-delà de quelques semaines sont efficaces.",
    ),
    (
        "besoin-toucher-fond",
        "« Il faut avoir touché le fond pour s'en sortir »",
        "Clinique",
        "faux",
        "L'idée que la dégradation serait un préalable au changement n'est étayée par aucune donnée et "
        "retarde l'accès aux soins. En addictologie comme en psychiatrie, l'intervention précoce améliore "
        "nettement le pronostic.",
        "Une transmission issue de certains groupes d'entraide, généralisée à tort.",
        "Ce qui est vrai : la perception d'un décalage entre sa situation et ses valeurs favorise le "
        "changement. Cette prise de conscience n'exige pas d'avoir tout perdu.",
    ),
    (
        "psy-tous-pareils",
        "« Psychologue, psychiatre, psychanalyste, psychothérapeute : c'est pareil »",
        "Métiers",
        "faux",
        "Le psychiatre est médecin, prescrit et peut hospitaliser. Le psychologue a un cursus "
        "universitaire de cinq ans en psychologie, un titre protégé, et ne prescrit pas. Le titre de "
        "psychothérapeute est réglementé et suppose une formation clinique complémentaire. Le "
        "psychanalyste se réfère à une formation propre, sans encadrement légal du titre.",
        "La proximité des mots et l'absence d'information claire au moment où l'on cherche de l'aide.",
        "Ce qui est vrai : les compétences se recoupent en pratique, mais le cadre légal, le "
        "remboursement et la possibilité de prescrire diffèrent réellement.",
    ),
    (
        "psychologue-lit-pensees",
        "« Un psychologue devine ce que je pense »",
        "Métiers",
        "faux",
        "Aucun professionnel ne lit dans les pensées. Le travail clinique repose sur l'entretien, "
        "l'observation, parfois des outils standardisés, et sur des hypothèses explicitement validées "
        "avec la personne concernée.",
        "La représentation fictionnelle du psychologue clairvoyant.",
        "Ce qui est vrai : l'expérience clinique affine la lecture des indices non verbaux et des "
        "incohérences du récit — c'est une compétence entraînée, faillible, et vérifiée en la disant.",
    ),
    (
        "ocd-rangement",
        "« Être maniaque du rangement, c'est être un peu TOC »",
        "Clinique",
        "faux",
        "Le trouble obsessionnel compulsif se définit par des pensées intrusives génératrices d'angoisse "
        "et des rituels accomplis pour la soulager, qui consomment souvent plus d'une heure par jour et "
        "entravent la vie. La personne les vit comme absurdes et subis, pas comme une préférence.",
        "L'usage banalisé de l'abréviation dans le langage courant.",
        "Ce qui est vrai : aimer l'ordre est un trait de personnalité courant et sans souffrance. C'est "
        "précisément ce qui le distingue du trouble.",
    ),
    (
        "bipolaire-humeur",
        "« Changer souvent d'humeur, c'est être bipolaire »",
        "Clinique",
        "faux",
        "Le trouble bipolaire se caractérise par des épisodes durables — des jours à des semaines — "
        "d'élévation de l'humeur avec réduction du besoin de sommeil, accélération de la pensée et prise "
        "de risque, alternant avec des épisodes dépressifs. Il ne s'agit pas de variations d'humeur dans "
        "la journée.",
        "L'usage courant du mot pour désigner une humeur instable.",
        "Ce qui est vrai : d'autres troubles comportent une instabilité émotionnelle rapide, ce qui "
        "explique une partie des confusions diagnostiques réelles entre professionnels.",
    ),
    (
        "hypersensibilite",
        "« L'hypersensibilité est un diagnostic »",
        "Clinique",
        "partiel",
        "La sensibilité au traitement sensoriel est un trait dimensionnel mesurable, non une catégorie "
        "clinique : elle ne figure dans aucune classification diagnostique. Se reconnaître dans une "
        "description n'établit pas l'existence d'une entité séparée.",
        "Le succès de livres grand public présentant un trait continu comme une identité distincte.",
        "Ce qui est vrai : les différences individuelles de réactivité sensorielle et émotionnelle "
        "existent bel et bien, et peuvent justifier des aménagements concrets.",
    ),
    (
        "surdoue-reussite",
        "« Un enfant à haut potentiel réussit forcément »",
        "Éducation",
        "faux",
        "Un score élevé prédit statistiquement de meilleurs résultats scolaires, mais la dispersion est "
        "grande : motivation, méthodes de travail, soutien familial et santé mentale pèsent lourdement. "
        "Une part de ces élèves est en difficulté scolaire.",
        "L'assimilation entre potentiel mesuré et performance réalisée.",
        "Ce qui est vrai : les besoins pédagogiques spécifiques sont réels, et l'ennui prolongé est un "
        "facteur de décrochage documenté.",
    ),
    (
        "besoin-9-mois-habitude",
        "« Il faut 21 jours pour prendre une habitude »",
        "Apprentissage",
        "faux",
        "L'étude de référence sur l'automatisation des comportements quotidiens trouve une médiane de "
        "l'ordre de deux mois, avec une variabilité considérable selon le comportement — boire un verre "
        "d'eau s'automatise bien plus vite que faire du sport.",
        "Une remarque d'un chirurgien esthétique des années 1960 sur le délai d'adaptation à un changement "
        "d'apparence, transformée en loi.",
        "Ce qui est vrai : la régularité et un déclencheur contextuel stable comptent davantage que le "
        "nombre de jours.",
    ),
    (
        "genie-inspiration",
        "« La créativité, c'est l'inspiration soudaine »",
        "Créativité",
        "exagere",
        "Les moments d'illumination existent mais surviennent presque toujours après une longue période "
        "de préparation consciente sur le problème. Les productions créatives majeures s'appuient sur une "
        "expertise construite pendant des années et sur un volume important de tentatives, dont la "
        "plupart échouent.",
        "Le récit romantique du génie inspiré, plus mémorable que le travail préparatoire invisible.",
        "Ce qui est vrai : l'incubation — s'éloigner d'un problème — améliore réellement la résolution, à "
        "condition d'avoir d'abord travaillé intensément dessus.",
    ),
    (
        "temoins-inaction",
        "« Face à une urgence, la foule aide toujours »",
        "Social",
        "partiel",
        "Plus il y a de témoins, moins chacun se sent responsable d'intervenir, et l'inaction des autres "
        "est interprétée comme le signe qu'il n'y a pas d'urgence. Cet effet est solidement établi en "
        "laboratoire.",
        "Le récit, en partie inexact, d'un fait divers new-yorkais de 1964 a popularisé l'idée.",
        "Ce qui est vrai : les analyses de vidéosurveillance d'agressions réelles montrent qu'une "
        "intervention finit par survenir dans une large majorité des cas, souvent à plusieurs. La "
        "diffusion de responsabilité retarde l'aide plus qu'elle ne l'empêche.",
    ),
    (
        "milgram-obéissance",
        "« L'expérience de Milgram prouve que n'importe qui torturerait sur ordre »",
        "Social",
        "exagere",
        "Les archives montrent une réalité plus nuancée : les participants discutaient, protestaient, "
        "doutaient de la réalité du dispositif, et l'expérimentateur devait insister bien au-delà du "
        "protocole annoncé. Les taux d'obéissance varient énormément selon les variantes — proximité de "
        "la victime, présence d'un pair désobéissant, autorité institutionnelle.",
        "La puissance du chiffre de 65 %, cité hors de son contexte expérimental.",
        "Ce qui est vrai : le résultat central tient. La situation pèse bien plus qu'on ne l'imagine sur "
        "le comportement, et la plupart des gens sous-estiment massivement cette influence.",
    ),
    (
        "stanford-prison",
        "« L'expérience de la prison de Stanford montre que les rôles nous transforment »",
        "Social",
        "faux",
        "Les enregistrements et les entretiens révélés depuis montrent que les gardiens ont reçu des "
        "consignes explicites de dureté, que certains jouaient délibérément un rôle, et que "
        "l'expérimentateur est intervenu pour orienter les comportements. Il s'agit d'une démonstration "
        "mise en scène plus que d'une expérience contrôlée.",
        "Un dispositif spectaculaire, largement diffusé avant que ses archives ne soient examinées.",
        "Ce qui est vrai : l'influence des rôles et des normes de groupe sur le comportement est réelle "
        "et bien documentée — par d'autres travaux, mieux contrôlés.",
    ),
    (
        "besoin-confiance-soi",
        "« Il faut avoir confiance en soi avant d'agir »",
        "Pratique",
        "faux",
        "La confiance suit l'action bien plus qu'elle ne la précède : c'est en accumulant des expériences "
        "de maîtrise, même modestes, que le sentiment d'efficacité se construit. Attendre de se sentir "
        "prêt est l'un des mécanismes les mieux décrits de l'évitement.",
        "L'ordre intuitif des choses, où l'émotion semblerait devoir précéder le comportement.",
        "Ce qui est vrai : une préparation sérieuse réduit l'anxiété. Elle ne la supprime pas avant le "
        "passage à l'acte, et c'est normal.",
    ),
]
