# -*- coding: utf-8 -*-
"""Les cas cliniques qui ont fait avancer la psychologie et la neuropsychologie.

Chaque fiche présente une histoire réelle, documentée dans la littérature
scientifique, et surtout ce qu'elle a permis de comprendre. Les noms retenus
sont ceux sous lesquels ces personnes sont connues dans les publications.
"""

# (id, nom, periode, domaine, resume, histoire, apport, aujourdhui)
CAS = [
    ("phineas-gage", "Phineas Gage", "1848", "Neuropsychologie",
     "Une barre à mine traverse son crâne — il survit, mais son caractère change.",
     "Contremaître de chantier ferroviaire dans le Vermont, Gage est victime de l'explosion prématurée d'une charge : une barre de fer de plus d'un mètre lui traverse la joue et le lobe frontal gauche avant de ressortir par le sommet du crâne. Il reste conscient, parle, marche. Son médecin, John Harlow, rapporte qu'il perd ensuite la maîtrise de lui-même, devient impulsif, incapable de tenir un plan.",
     "Premier argument clinique fort pour l'idée que les fonctions supérieures — planification, inhibition, conduite sociale — dépendent de régions cérébrales identifiables, et notamment du cortex préfrontal ventromédian.",
     "Le récit a été très romancé : les témoignages d'époque sont minces et contradictoires. On sait aujourd'hui que Gage a retrouvé un emploi de cocher au Chili, ce qui suggère une récupération bien plus importante que ne le veut la légende du « monstre asocial »."),

    ("hm", "Henry Molaison (H.M.)", "1953-2008", "Mémoire",
     "L'homme qui ne pouvait plus former de nouveaux souvenirs, et qui a tout appris à la science sur la mémoire.",
     "Pour traiter une épilepsie sévère, on lui retire à 27 ans les deux hippocampes et une partie des lobes temporaux internes. Les crises diminuent, mais il devient incapable de mémoriser un nouvel événement. Il se présentera à Brenda Milner comme à une inconnue pendant plus de quarante ans, tout en conservant intacte sa mémoire d'avant l'opération et son intelligence.",
     "Démonstration décisive que la mémoire n'est pas une fonction unique : H.M. progressait régulièrement à des tâches motrices (dessin en miroir) sans aucun souvenir de s'y être exercé. D'où la distinction entre mémoire déclarative (hippocampique) et mémoire procédurale.",
     "Son cerveau a été découpé en 2 401 lames en 2009, en direct sur internet. Son identité n'a été révélée qu'à sa mort. Le cas a aussi posé des questions durables sur le consentement de patients incapables de mémoriser ce à quoi ils consentent."),

    ("patient-tan", "Louis Victor Leborgne (« Tan »)", "1861", "Langage",
     "Il ne prononçait plus qu'une syllabe — et il a localisé le langage dans le cerveau.",
     "Hospitalisé à Bicêtre, cet homme ne pouvait plus produire qu'un son, « tan », répété, tout en comprenant ce qu'on lui disait. Paul Broca l'examine quelques jours avant sa mort, puis autopsie son cerveau et découvre une lésion du pied de la troisième circonvolution frontale gauche.",
     "Fonde la neuropsychologie du langage et le principe de localisation cérébrale : « nous parlons avec l'hémisphère gauche ». L'aphasie de production porte depuis le nom d'aphasie de Broca.",
     "L'imagerie moderne du cerveau conservé montre que la lésion débordait largement l'aire aujourd'hui appelée aire de Broca. La production du langage mobilise un réseau bien plus vaste qu'une seule circonvolution."),

    ("anna-o", "Bertha Pappenheim (Anna O.)", "1880-1882", "Psychanalyse",
     "La patiente qui a inventé l'expression « talking cure ».",
     "Jeune femme viennoise soignée par Joseph Breuer pour des symptômes que l'on qualifiait alors d'hystériques : paralysies, troubles de la vision, perte temporaire de sa langue maternelle. Elle remarque que ses symptômes s'atténuent lorsqu'elle raconte, sous hypnose, les circonstances de leur apparition.",
     "Le compte rendu de Breuer, repris avec Freud dans les Études sur l'hystérie, constitue l'acte de naissance de la cure par la parole et de la notion de symptôme porteur de sens.",
     "Le cas n'a pas été la réussite thérapeutique annoncée : Bertha Pappenheim a été hospitalisée ensuite. Elle est devenue une figure majeure du travail social et du féminisme allemand — une biographie longtemps éclipsée par son rôle de « patiente »."),

    ("petit-hans", "Herbert Graf (le petit Hans)", "1909", "Psychanalyse",
     "La première psychanalyse d'enfant, menée par correspondance avec le père.",
     "Un garçon de cinq ans développe une peur intense des chevaux qui l'empêche de sortir. Freud ne le rencontre presque pas : il guide le père, qui note les propos de l'enfant et conduit les entretiens. Freud y lit la peur du père transposée sur l'animal.",
     "Texte fondateur de la psychanalyse de l'enfant et de la théorie du complexe d'Œdipe ; premier exemple de guidance parentale.",
     "Méthodologiquement très fragile : l'observateur est le père, lui-même disciple de Freud, et les interprétations alternatives (l'enfant avait assisté à la chute d'un cheval) sont écartées d'emblée. Devenu metteur en scène d'opéra, Graf ne gardait aucun souvenir de la phobie."),

    ("genie", "Genie", "1970", "Langage / Développement",
     "Une enfant privée de langage jusqu'à treize ans, au cœur d'un dilemme éthique majeur.",
     "Découverte en Californie après une séquestration et une privation extrêmes, elle ne parle pas. Une équipe de chercheurs entreprend de lui enseigner le langage tout en étudiant ses progrès. Elle acquiert un vocabulaire important mais n'accède jamais à une syntaxe ordinaire.",
     "Argument empirique en faveur d'une période sensible pour l'acquisition de la syntaxe : passé un certain âge, l'apprentissage du lexique reste possible, la grammaire beaucoup moins.",
     "Le cas est aussi un scandale éthique : conflits entre besoins de recherche et intérêt de l'enfant, ruptures de placement, fin du financement suivie d'un placement en institution. On perd ensuite sa trace publique — ce qui rappelle qu'un « sujet » d'étude est d'abord une personne."),

    ("victor-aveyron", "Victor de l'Aveyron", "1800-1828", "Éducation spécialisée",
     "L'enfant sauvage qui a fondé l'éducation spécialisée.",
     "Capturé vers douze ans dans les bois du Tarn, il ne parle pas et semble insensible au froid. Le médecin Jean Itard, contre l'avis de Pinel qui le juge irrécupérable, entreprend cinq ans d'éducation méthodique et progressive.",
     "Itard invente une pédagogie sensorielle structurée, avec objectifs, progression et évaluation — dont Maria Montessori se réclamera directement. La question du rôle de l'environnement dans l'humanisation y est posée frontalement.",
     "Victor n'a jamais accédé au langage articulé. On ignore s'il présentait un trouble du développement antérieur à son abandon, ce qui rend l'interprétation du cas définitivement ambiguë."),

    ("clive-wearing", "Clive Wearing", "1985", "Mémoire",
     "Un musicien dont la mémoire dure quelques secondes, mais qui dirige toujours son chœur.",
     "Une encéphalite herpétique détruit ses hippocampes et une partie des lobes temporaux. Il vit dans un présent perpétuel de sept à trente secondes, notant sans cesse dans un carnet « maintenant je suis vraiment éveillé ». Il reconnaît pourtant sa femme avec émotion à chaque apparition.",
     "Illustration saisissante de la dissociation entre mémoire épisodique détruite et mémoire procédurale intacte : il lit une partition, joue du piano et dirige avec la même maîtrise qu'avant.",
     "Le cas montre aussi qu'une mémoire émotionnelle peut subsister sans souvenir conscient. Filmé dans plusieurs documentaires, il est devenu un support pédagogique majeur en neuropsychologie."),

    ("kim-peek", "Kim Peek", "1951-2009", "Neurodéveloppement",
     "Une mémoire encyclopédique associée à une absence de corps calleux.",
     "Né sans corps calleux, il mémorise le contenu de milliers d'ouvrages et lit les deux pages d'un livre simultanément, un œil par page. Il éprouve en revanche de grandes difficultés dans les gestes du quotidien et l'abstraction.",
     "Cas de « savant syndrome » le mieux documenté ; il a nourri la réflexion sur la dissociation entre capacités mnésiques exceptionnelles et fonctions exécutives.",
     "Peek n'était pas autiste, contrairement à ce que la culture populaire laisse croire : son profil relevait d'une anomalie neurodéveloppementale distincte. Il a longtemps accompagné son père dans des conférences publiques."),

    ("patient-elliot", "Elliot", "1982", "Décision / Émotions",
     "Intelligence intacte, raisonnement intact — et pourtant incapable de décider.",
     "Après l'ablation d'une tumeur du cortex préfrontal ventromédian, ce cadre décrit par Antonio Damasio conserve un QI élevé et une logique impeccable. Il perd cependant son emploi, son mariage et son patrimoine, incapable de trancher entre deux options même triviales, et discutant indéfiniment des critères.",
     "Point de départ de l'hypothèse des marqueurs somatiques : les émotions ne parasitent pas la décision, elles la rendent possible en attribuant une valeur aux options.",
     "L'hypothèse reste débattue, notamment à partir des résultats de l'Iowa Gambling Task, dont l'interprétation est contestée. Le cas a néanmoins durablement réconcilié émotion et rationalité."),

    ("patient-sm", "S.M.", "1994", "Émotions",
     "La femme qui ne connaissait pas la peur.",
     "Atteinte d'une maladie génétique rare (Urbach-Wiethe) qui a calcifié ses deux amygdales cérébrales, elle ne manifeste aucune peur devant les serpents, les maisons hantées ou les films d'horreur, et reconnaît mal la peur sur les visages. Elle a été agressée à plusieurs reprises sans développer de méfiance durable.",
     "Preuve du rôle central de l'amygdale dans la détection de la menace et dans l'apprentissage de la peur.",
     "Coup de théâtre en 2013 : l'inhalation de dioxyde de carbone provoque chez elle une attaque de panique intense. La peur peut donc être déclenchée par une voie interne indépendante de l'amygdale."),

    ("patient-dora", "Ida Bauer (Dora)", "1900", "Psychanalyse",
     "Un cas célèbre pour son échec, et pour ce qu'il révèle de l'analyste.",
     "Adolescente adressée à Freud par son père pour toux nerveuse et aphonie, dans un contexte familial où elle est l'objet des avances d'un ami du père. Freud interprète ses symptômes en termes de désir refoulé. Elle interrompt la cure au bout de trois mois.",
     "Freud en tire l'élaboration du transfert et du contre-transfert : il reconnaît après coup avoir négligé les sentiments que la patiente projetait sur lui, et sa propre implication.",
     "Relecture féministe majeure : le récit de Dora sur ce qu'elle subissait était vraisemblablement exact, et la grille interprétative de l'époque a servi à le disqualifier. Cas devenu emblématique de la question de la parole des femmes en clinique."),

    ("petit-albert-cas", "Douglas Merritte (« Petit Albert »)", "1920", "Apprentissage",
     "Le bébé conditionné à avoir peur, dont on a longtemps ignoré l'identité.",
     "John Watson et Rosalie Rayner associent la présentation d'un rat blanc à un bruit violent chez un nourrisson de onze mois, jusqu'à ce que l'animal seul déclenche la détresse, puis observent la généralisation à d'autres objets pelucheux.",
     "Démonstration historique qu'une phobie peut s'acquérir par conditionnement — socle théorique des thérapies comportementales par exposition.",
     "Le protocole serait aujourd'hui interdit : aucun consentement éclairé, aucune procédure d'extinction, l'enfant quittant l'étude avec sa peur. Des travaux récents suggèrent que l'enfant, mort à six ans, présentait une pathologie neurologique connue de Watson, ce qui aggraverait encore le jugement éthique."),

    ("patient-nn", "Les jumelles de Minnesota", "1979-2000", "Génétique du comportement",
     "Des jumeaux séparés à la naissance, réunis à l'âge adulte pour la science.",
     "Thomas Bouchard recrute pendant vingt ans des paires de vrais jumeaux élevés séparément, les soumettant à une semaine d'évaluations complètes. Les similitudes observées en intelligence, en traits de personnalité et jusque dans certaines habitudes surprennent les chercheurs.",
     "L'étude a établi des estimations d'héritabilité élevées pour plusieurs traits psychologiques et relancé le débat inné-acquis sur des bases empiriques.",
     "Attention aux conclusions hâtives : les jumeaux séparés étaient souvent placés dans des milieux socialement similaires, les anecdotes de coïncidences ont été surmédiatisées, et l'héritabilité est une statistique de population, jamais un destin individuel."),

    ("chris-sizemore", "Chris Costner Sizemore", "1952", "Dissociation",
     "Le cas fondateur — et contesté — du trouble dissociatif de l'identité.",
     "Suivie par deux psychiatres qui publient son histoire sous pseudonyme, elle présente des états de conscience alternés aux comportements et aux souvenirs distincts. Le livre puis le film qui en sont tirés rendent le trouble célèbre.",
     "Ouvre la recherche clinique sur les états dissociatifs et leur lien avec les traumatismes précoces.",
     "Sizemore a repris publiquement le contrôle de son récit et poursuivi les studios pour récupérer les droits de sa propre vie. Le rôle de la suggestion et des attentes du thérapeute dans la production des « personnalités » reste au cœur du débat."),

    ("sybil", "Shirley Mason (Sybil)", "1973", "Dissociation",
     "Le best-seller qui a fait exploser les diagnostics — et qui s'est effondré.",
     "Le livre décrit une patiente présentant seize personnalités, liées à des sévices d'enfance. Il devient un phénomène de société ; les diagnostics de personnalité multiple passent de quelques dizaines à plusieurs milliers aux États-Unis.",
     "Cas d'école de l'influence d'un récit médiatique sur l'épidémiologie psychiatrique elle-même.",
     "Des enregistrements et des lettres retrouvés montrent que la patiente avait écrit à sa thérapeute qu'elle inventait, que celle-ci lui administrait des barbituriques et suggérait les personnalités. Le cas est aujourd'hui l'exemple canonique de l'iatrogénie diagnostique."),

    ("david-reimer", "David Reimer", "1966-2004", "Identité de genre",
     "Une expérience d'assignation de genre qui a fini en tragédie.",
     "À la suite d'une circoncision catastrophique dans la petite enfance, un garçon est élevé comme une fille sur les conseils du psychologue John Money, qui présente pendant des années le cas comme la preuve que l'identité de genre est entièrement construite par l'éducation.",
     "Le cas a longtemps servi d'argument central dans le débat sur la construction sociale du genre.",
     "L'enfant a rejeté cette assignation dès l'adolescence, repris une identité masculine, puis s'est suicidé à 38 ans. La publication de la vérité par Milton Diamond a démontré que les rapports de Money étaient faux. Cas majeur d'éthique de la recherche et de responsabilité du chercheur."),

    ("washoe", "Washoe", "1966-2007", "Langage animal",
     "La chimpanzé qui a appris des signes — et divisé la communauté scientifique.",
     "Élevée comme une enfant par Allen et Beatrix Gardner, elle acquiert environ 250 signes de la langue des signes américaine et les combine spontanément. Elle transmettra des signes à son fils adoptif Loulis sans intervention humaine.",
     "A ouvert tout le champ de la communication animale et forcé à préciser ce qu'on entend par « langage » : lexique, syntaxe, intention communicative, référence déplacée.",
     "Les critiques, notamment celles issues du projet Nim Chimpsky, montrent que beaucoup de productions étaient des imitations induites par l'expérimentateur. Un lexique important ne suffit pas à établir une syntaxe."),

    ("nim-chimpsky", "Nim Chimpsky", "1973-1977", "Langage animal",
     "Le projet monté pour prouver Chomsky faux — et qui lui a finalement donné raison.",
     "Herbert Terrace élève un chimpanzé dans un environnement humain pour lui enseigner la langue des signes. L'analyse image par image des vidéos révèle que Nim signe presque toujours en réaction directe à un signe de l'enseignant, sans structure grammaticale ni initiative véritable.",
     "Point de bascule du débat : il impose un standard méthodologique (analyse aveugle des enregistrements) à toutes les études de langage animal.",
     "Le sort de Nim, ballotté entre familles d'accueil puis laboratoires biomédicaux, a aussi nourri la réflexion éthique sur l'expérimentation animale et le devenir des animaux « retraités » de la recherche."),

    ("patient-ka", "Le patient de Wernicke", "1874", "Langage",
     "Il parlait abondamment — sans que rien n'ait de sens.",
     "Carl Wernicke décrit des patients au débit fluide et à l'intonation normale, mais dont les phrases sont remplies de mots inadéquats ou inventés, et qui ne comprennent pas ce qu'on leur dit. L'autopsie révèle une lésion postérieure, dans le lobe temporal gauche.",
     "Complète la découverte de Broca et fonde le premier modèle de réseau : une aire de compréhension, une aire de production, et un faisceau qui les relie. C'est la naissance du connexionnisme neurologique.",
     "Le modèle Wernicke-Geschwind, longtemps enseigné, est aujourd'hui considéré comme trop schématique : l'imagerie révèle deux grandes voies (dorsale et ventrale) et une organisation bien plus distribuée."),

    ("patient-dw", "Le premier patient au cerveau divisé", "1962", "Latéralisation",
     "Deux hémisphères séparés, deux façons de connaître le monde dans un seul crâne.",
     "Pour traiter une épilepsie incontrôlable, on sectionne le corps calleux. Roger Sperry et Michael Gazzaniga présentent ensuite des images dans un seul champ visuel : un objet montré à gauche (hémisphère droit) peut être saisi de la main gauche, mais le patient affirme n'avoir rien vu.",
     "Démonstration expérimentale de la spécialisation hémisphérique et de l'unité illusoire de la conscience : l'hémisphère gauche invente instantanément des explications aux actions initiées par le droit.",
     "Ces patients restent très peu nombreux et leur cerveau était déjà remanié par des années d'épilepsie. Extrapoler de ces cas exceptionnels au cerveau sain — en particulier la mythologie « cerveau gauche / cerveau droit » — est abusif."),

    ("patient-bb", "Les enfants de Roumanie", "1990-2010", "Développement",
     "Ce que la privation précoce de relation fait au développement — et ce que le placement répare.",
     "Après 1989, des dizaines de milliers d'enfants sont découverts dans des institutions roumaines où les soins matériels étaient assurés, mais pas les interactions. Le Bucharest Early Intervention Project assigne ensuite au hasard une partie d'entre eux à des familles d'accueil.",
     "Résultats parmi les plus solides de la psychologie du développement : retards cognitifs et socio-émotionnels majeurs, mais rattrapage substantiel si le placement familial intervient avant deux ans environ.",
     "L'étude a soulevé un débat éthique intense sur la randomisation (laisser des enfants en institution pour constituer un groupe contrôle), et a directement influencé les politiques de désinstitutionnalisation."),

    ("patient-ll", "Louis Leborgne et la méthode anatomo-clinique", "XIXe siècle", "Histoire des méthodes",
     "Comment on a appris à relier un symptôme à une lésion.",
     "La méthode consiste à observer minutieusement un trouble du vivant du patient, puis à examiner son cerveau après sa mort pour identifier la lésion responsable. Elle fut la seule fenêtre sur le cerveau humain pendant plus d'un siècle.",
     "Elle a fondé la neuropsychologie : sans elle, ni Broca, ni Wernicke, ni la cartographie des fonctions cérébrales n'auraient été possibles.",
     "Ses limites sont structurelles : une lésion est rarement pure, elle détruit aussi des fibres de passage, et le cerveau se réorganise. L'imagerie fonctionnelle a permis de dépasser ce raisonnement, sans le rendre obsolète (l'étude des lésions reste la meilleure preuve de <em>nécessité</em> d'une région)."),

    ("patient-eve", "Les patients de la lobotomie", "1935-1955", "Psychochirurgie",
     "Des dizaines de milliers d'opérations, un prix Nobel, et une leçon durable.",
     "La leucotomie préfrontale d'Egas Moniz, puis la lobotomie transorbitaire pratiquée en série par Walter Freeman, sont appliquées à des patients agités, anxieux ou simplement jugés difficiles — parfois en quelques minutes, sans bloc opératoire. Moniz reçoit le prix Nobel de médecine en 1949.",
     "Cas d'école absolu de ce qui arrive quand l'enthousiasme thérapeutique se passe d'évaluation contrôlée : les résultats n'ont jamais été mesurés rigoureusement avant une diffusion massive.",
     "L'arrivée des neuroleptiques dans les années 1950 met fin à la pratique. L'épisode fonde l'exigence moderne d'essais contrôlés, de comités d'éthique et de consentement éclairé — et invite à la prudence face aux promesses actuelles de neuromodulation."),

    ("rosenhan", "Les pseudo-patients de Rosenhan", "1973", "Diagnostic",
     "Huit personnes en bonne santé se font hospitaliser en psychiatrie : personne ne les démasque.",
     "Les participants se présentent à l'hôpital en disant entendre un mot, puis se comportent normalement. Tous sont admis, la plupart avec un diagnostic de schizophrénie, et restent hospitalisés en moyenne dix-neuf jours. Leurs comportements ordinaires (prendre des notes) sont interprétés comme des symptômes.",
     "L'article a provoqué une crise de confiance majeure dans la fiabilité du diagnostic psychiatrique et accéléré la refonte du DSM autour de critères opérationnels explicites.",
     "Une enquête journalistique de 2019 a mis au jour des incohérences graves dans les données de Rosenhan, au point que la réalité de plusieurs pseudo-patients est douteuse. L'étude la plus citée sur la fragilité du diagnostic est peut-être elle-même une fraude — ce qui ne rend pas le problème qu'elle pointait moins réel."),

    ("patient-pn", "Les patients à héminégligence", "1941", "Attention",
     "Ils ne voient pas la moitié du monde — et ne savent pas qu'ils ne la voient pas.",
     "Après une lésion pariétale droite, la personne ignore tout ce qui se trouve à sa gauche : elle ne mange que la moitié de son assiette, ne rase qu'une joue, dessine une horloge avec tous les chiffres tassés à droite. Sa vision est pourtant intacte.",
     "Montre que l'attention spatiale est un système distinct de la perception, et que la conscience d'un déficit (l'anosognosie) est elle-même une fonction cérébrale.",
     "Les travaux de Bisiach ont révélé que la négligence touche aussi les images mentales : invités à décrire de mémoire une place connue, les patients omettent le côté gauche, et inversement s'ils changent de point de vue imaginé."),

    ("syndrome-korsakoff", "Les patients de Korsakoff", "1887", "Mémoire",
     "Ils comblent les trous de leur mémoire par des récits sincères et faux.",
     "Sergueï Korsakoff décrit, chez des patients alcooliques carencés en vitamine B1, une amnésie antérograde massive accompagnée de confabulations : le patient raconte avec assurance des événements qui n'ont pas eu lieu, sans intention de mentir.",
     "Établit le lien entre carence nutritionnelle, lésions des corps mamillaires et du thalamus, et amnésie — et montre que le cerveau produit spontanément des récits cohérents pour combler l'absence de souvenir.",
     "La prévention par supplémentation en thiamine est aujourd'hui systématique en sevrage alcoolique. La confabulation reste un phénomène majeur pour comprendre comment se fabrique le sentiment de savoir."),

    ("prosopagnosie", "Les personnes prosopagnosiques", "1947", "Perception",
     "Elles voient parfaitement les visages, mais ne reconnaissent plus personne.",
     "Joachim Bodamer nomme ce trouble dans lequel la personne décrit sans difficulté les yeux, le nez, l'expression, mais ne peut identifier son conjoint ou son propre reflet. Elle s'appuie sur la voix, la démarche, une coiffure.",
     "Preuve de l'existence d'un module de traitement des visages relativement spécialisé, dont l'aire fusiforme des visages constitue le pivot.",
     "On sait aujourd'hui qu'il existe une forme développementale, présente dès la naissance et touchant environ 2 % de la population, souvent ignorée de la personne elle-même qui pense simplement « avoir une mauvaise mémoire des gens »."),

    ("patient-hm2", "Le patient K.C.", "1981-2014", "Mémoire",
     "Il savait ce qu'il savait, mais ne se souvenait d'avoir rien vécu.",
     "Après un accident de moto, ce patient étudié par Endel Tulving conserve intactes ses connaissances générales — capitales, règles de grammaire, faits historiques — mais perd tout souvenir personnel, avant comme après l'accident. Invité à imaginer son week-end prochain, il décrit un « vide », le même que lorsqu'il tente de se souvenir.",
     "Dissociation décisive entre mémoire sémantique (les faits) et mémoire épisodique (les expériences vécues), et découverte majeure : la même machinerie sert à se souvenir du passé et à imaginer l'avenir.",
     "Ce résultat a ouvert tout le champ contemporain du « voyage mental dans le temps » et de la projection épisodique future, étudiée aujourd'hui dans la dépression, le vieillissement et la prise de décision."),

    ("rat-park", "Le parc à rats", "1978", "Addiction",
     "Et si l'addiction dépendait moins de la substance que des conditions de vie ?",
     "Bruce Alexander compare des rats isolés en cage standard à des rats vivant dans un environnement enrichi et social, tous ayant accès à de l'eau morphinée. Les rats du « parc » en consomment nettement moins.",
     "L'étude a puissamment contribué à déplacer le regard sur l'addiction : d'un défaut moral ou d'une simple dépendance chimique vers un problème de contexte, d'isolement et de conditions sociales.",
     "Ses résultats ont longtemps été difficiles à répliquer et l'expérience a été surinterprétée dans les médias. Le message reste toutefois cohérent avec les données humaines : l'environnement, le lien social et les perspectives pèsent lourd dans les trajectoires d'addiction."),
]
