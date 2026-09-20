# -*- coding: utf-8 -*-
"""Gonflement de la base de références.

Même arité que les tuples existants. Un id déjà présent remplace la fiche
mince ; un id nouveau s'ajoute. EXTRA_PLUS s'empile sur les catégories.
"""

# (id, titre, chercheur, annee, categorie, resume, protocole, resultat, portee, critique)
EXPERIENCES_PLUS = [
    ("petit-albert", "Le petit Albert", "John Watson & Rosalie Rayner", "1920", "09-psychopathologie",
     "Une phobie peut s'apprendre par conditionnement — démonstration historique, scandale éthique durable.",
     "Albert B., 11 mois, n'a d'abord pas peur d'un rat blanc. Watson et Rayner font précéder ou accompagner le rat d'un bruit violent (barre d'acier frappée derrière la tête). Ils répètent les associations, testent la généralisation (lapin, manteau de fourrure, barbe de coton, masque de Père Noël) et notent les réactions. Aucune procédure d'extinction n'est prévue : l'enfant quitte l'hôpital avec sa peur.",
     "La peur du rat apparaît et se généralise à d'autres objets blancs et poilus. Le compte rendu de 1920 devient le manifeste vivant du behaviorisme : l'émotion n'est pas une essence, elle s'installe par association.",
     "Socle théorique des thérapies comportementales des phobies (exposition, contre-conditionnement). Relie le conditionnement classique de Pavlov à la clinique. À lire avec la fiche de cas Douglas Merritte et la rubrique éthique de la psychopathologie.",
     "Inacceptable aujourd'hui : pas de consentement éclairé, sujet mineur, aucun soin de la peur induite. Les résultats n'ont jamais été répliqués proprement. Des travaux d'identification (Beck, Levinson, Irons) proposent Douglas Merritte, enfant neurologiquement vulnérable déjà connu de Watson — ce qui aggrave encore le jugement. D'autres contestent l'identité. Quoi qu'il en soit, le protocole reste un contre-exemple fondateur des comités d'éthique."),

    ("harlow-singes", "Les singes de Harlow", "Harry Harlow", "1958", "05-developpement",
     "Le contact réconfortant est un besoin primaire, pas un sous-produit de la nourriture.",
     "De jeunes macaques rhésus sont élevés avec deux leurres : une « mère » de fil de fer qui donne du lait, une « mère » de tissu éponge sans nourriture. Harlow mesure le temps passé agrippé, la réaction à un objet effrayant, puis, dans des suites plus sombres, l'effet d'un isolement social prolongé.",
     "Les petits s'accrochent au tissu. Ils n'utilisent le fil de fer que pour téter, puis reviennent au doux. En cas de peur, c'est la mère de tissu qui sert de base de sécurité. Sans contact social réel, le développement socio-émotionnel s'effondre.",
     "Relie directement Bowlby (besoin d'attachement, pas de simple « conditionnement alimentaire ») et Ainsworth (base de sécurité, situation étrange). Change les nurseries, les orphelinats et l'idée qu'il ne faudrait pas « trop » porter un bébé. Voir aussi la psychologie comparée et la fiche attachement.",
     "Cruauté assumée : isolement, « puits de désespoir ». Interdit aujourd'hui. Harlow a aussi nourri le mouvement de protection animale. Un leurre n'est pas une mère : le résultat prouve le besoin de contact, pas qu'un tissu suffit à élever un primate."),

    ("robbers-cave", "La caverne des voleurs", "Muzafer Sherif", "1954", "04-sociale",
     "On peut fabriquer un « eux » et un « nous », puis les désarmer par une tâche commune.",
     "Vingt-deux garçons d'environ onze ans, soigneusement appariés, ignorent qu'ils participent à une expérience. Au parc d'État de Robbers Cave (Oklahoma), deux groupes (Aigles, Serpents) se forment séparément, se découvrent, s'affrontent (base-ball, tir à la corde, prix), puis doivent réparer une canalisation d'eau et tirer un camion en panne — buts supraordonnés.",
     "La compétition produit très vite sobriquets, drapeaux brûlés, raids. Le simple contact (repas communs) n'apaise pas. Seule l'interdépendance réelle abaisse l'hostilité. Une première session, ailleurs, avait échoué : les garçons avaient compris le montage et fraternisé trop tôt.",
     "Base de la théorie du conflit réaliste et, avec Allport, de l'hypothèse du contact sous conditions. Planche de découverte : deux camps, une canalisation. Relie Tajfel (identité même sans enjeu) : ici l'enjeu matériel existe, là il n'est pas nécessaire.",
     "Archives : les expérimentateurs ont parfois attisé le conflit. Échantillon de garçons blancs protestants des années 1950. On ne « résout » pas un conflit historique en une après-midi de camion. Le contact sans statut égal ni but commun peut aggraver."),

    ("rosenhan", "L'étude de Rosenhan", "David Rosenhan", "1973", "09-psychopathologie",
     "Huit « pseudo-patients » auraient ébranlé le diagnostic psychiatrique — et l'enquête de Cahalan a ébranlé Rosenhan.",
     "Selon Science (1973), huit personnes saines se présentent en disant entendre le mot « thud », puis se comportent normalement. Tous seraient hospitalisés, surtout pour schizophrénie, en moyenne 19 jours. Leurs notes de recherche sont lues comme des symptômes. Une seconde phase annonce des imposteurs à un hôpital qui « détecte » des dizaines de faux positifs… alors que Rosenhan n'en envoie aucun.",
     "L'article conclut que l'étiquette diagnostique colore toute observation. Il accélère le passage au DSM-III (1980) : critères opérationnels, durée, exclusion.",
     "Le problème qu'il nomme — fidélité inter-juges, pouvoir de l'étiquette, asile — reste réel. À relier aux fiches troubles (pédagogie, pas auto-diagnostic) et au débat classification.",
     "Susannah Cahalan, The Great Pretender (2019), ne retrouve pas les huit dossiers tels que décrits. Données manquantes, contradictions, un cas (Rosenhan lui-même ?) romancé. L'étude la plus citée sur la fragilité du diagnostic est elle-même fragile. On enseigne désormais les deux : le choc de 1973 et l'enquête."),

    ("pygmalion", "L'effet Pygmalion", "Robert Rosenthal & Lenore Jacobson", "1968", "13-education",
     "Les attentes d'un enseignant peuvent légèrement déplacer les scores — moins qu'on ne l'a chanté.",
     "À Oak School, on fait passer un test, puis on dit aux enseignants que certains élèves (tirés au sort) sont des « éclosions tardives » à fort potentiel. On reteste en fin d'année.",
     "Ces élèves progressent davantage, surtout en petites classes. Rosenthal parle d'effet Pygmalion (attentes positives) ; l'inverse sera nommé effet Golem.",
     "Sensibilise aux étiquettes en classe, en management, en santé. Relie l'effet Rosenthal (attentes de l'expérimentateur) et la prophétie autoréalisatrice.",
     "Réplications : effet réel mais modeste, instable, plus net sur le comportement de l'adulte que sur le QI. Critique des instruments et de la communication des résultats. Jussim : les enseignants sont aussi assez justes, leurs attentes suivent souvent la performance passée. On n'en fait ni un miracle ni un mythe."),

    ("kitty-dissonance", "La dissonance cognitive", "Leon Festinger & James Carlsmith", "1959", "04-sociale",
     "Quand l'acte contredit l'idée, c'est souvent l'idée qui plie — surtout si l'on n'a pas été assez payé pour mentir.",
     "Tâche volontairement ennuyeuse (bobines, plateaux). On paie 1 $ ou 20 $ pour dire à un « autre participant » (complice) que c'était intéressant. On redemande ensuite le vrai jugement sur la tâche. Festinger avait déjà infiltré une secte dont la fin du monde n'avait pas eu lieu (When Prophecy Fails, 1956) : les plus engagés redoublaient de prosélytisme.",
     "Le groupe 1 $ juge la tâche plus plaisante que le groupe 20 $ : justification insuffisante, donc changement d'attitude. Le groupe bien payé a une raison externe et n'a pas besoin de se mentir.",
     "Explique l'engagement, la justification de l'effort, la rationalisation d'un choix difficile, le « je l'ai choisi donc je l'aime ». Relie la fiche auteur Festinger, la comparaison sociale, et les biais d'escalade.",
     "Reformulations nombreuses (auto-perception de Bem, menace du soi). Toutes les incohérences ne produisent pas de tension. Culture et estime de soi modulent l'effet. Ce n'est pas une licence à « n'importe quel mensonge transforme les gens »."),

    ("zajonc-exposition", "L'effet de simple exposition", "Robert Zajonc", "1968", "04-sociale",
     "La familiarité, à elle seule, fait aimer — même sans souvenir conscient.",
     "Idéogrammes, visages, mélodies ou mots inventés sont présentés 1, 2, 5, 10, 25 fois. Les participants notent ensuite l'agrément, parfois après un masquage trop bref pour une reconnaissance explicite. Zajonc relie aussi l'exposition à l'activation (arousal) et à la facilitation sociale (présence d'autrui).",
     "Plus on a vu (sans saturer), plus on aime. L'effet survit à l'absence de rappel conscient. La simple présence d'autrui facilite les tâches simples et gêne les tâches complexes.",
     "Publicité par répétition, familiarité des visages politiques, « je le connais donc je lui fais confiance ». Pont vers le biais de statu quo et l'illusion de vérité (un énoncé répété paraît plus vrai).",
     "S'inverse à force de répétition (lassitude) ou si la première impression est franchement négative. Ne lave pas un préjugé hostile. Les stimulations trop complexes saturent plus vite."),

    ("tajfel-groupes", "Les groupes minimaux", "Henri Tajfel", "1971", "04-sociale",
     "Un critère trivial suffit à créer une discrimination — même sans histoire, ni haine, ni profit.",
     "Des adolescents sont répartis selon une préférence picturale (Klee / Kandinsky) ou un tirage. Aucun contact. Ils distribuent des points à des numéros anonymes « de leur groupe » ou de l'autre, selon des matrices qui opposent gain absolu et écart intergroupe.",
     "Ils maximisent l'écart en faveur du nous, quitte à réduire le gâteau commun. Ce n'est pas de la cupidité simple : c'est de l'identité.",
     "Naissance de la théorie de l'identité sociale (Tajfel & Turner). Relie Robbers Cave (conflit à enjeu) : ici l'enjeu est symbolique. Éclaire stéréotypes, sport, partis, rivalités d'équipe.",
     "Demande expérimentale possible (« on attend de moi que je favorise les miens »). Cultures plus collectivistes ou consignes d'équité atténuent. Un groupe minimal n'est pas un pogrom : c'est le germe, pas toute la plante."),

    ("hofling-infirmieres", "L'expérience de Hofling", "Charles K. Hofling", "1966", "04-sociale",
     "L'obéissance à l'autorité, hors laboratoire, dans un hôpital réel.",
     "Un « Dr Smith » inconnu téléphone à 22 infirmières : administrer 20 mg d'Astroten (produit fictif, étiquette max. 10 mg) à un patient. Trois règles sont violées : ordre téléphonique, dose excessive, médicament non listé. Un groupe témoin de 22 autres infirmières dit ce qu'elles feraient.",
     "21 sur 22 préparent l'injection. Presque toutes les collègues interrogées affirment qu'elles refuseraient. L'écart entre le dit et le fait est le résultat.",
     "Complète Milgram (labo) par le terrain. Justifie les protocoles modernes : double contrôle, droit de refuser, check-lists. Relie le biais d'autorité.",
     "Hôpital des années 1960, hiérarchie très verticale. Réplications ultérieures (Rank & Jacobson) montrent plus de refus quand le médicament est connu (valium). L'éthique d'une fausse prescription reste discutée."),

    ("effet-placebo", "L'effet placebo en chirurgie", "Bruce Moseley et al.", "2002", "14-sante",
     "Une arthroscopie simulée du genou soulage autant que la « vraie » chez certains patients arthrosiques.",
     "Essai randomisé en double aveugle (New England Journal of Medicine) : 180 vétérans, arthrose du genou. Trois bras — lavage, débridement, placebo (incisions cutanées, simulation sonore de l'opération, même séjour). Suivi jusqu'à deux ans, scores de douleur et de fonction.",
     "Aucun avantage de la chirurgie réelle sur le placebo pour la douleur et la fonction. Le rituel, l'attente et le soin suffisent à une part majeure du soulagement rapporté.",
     "Change les recommandations sur cette indication. Montre qu'un placebo n'est pas « rien » : c'est un contexte de soin. Relie nocebo, attentes, et la fiche Santé.",
     "Agit surtout sur des symptômes subjectifs. Ne « guérit » pas une infection, une rupture franche, une tumeur. Généraliser à toute la chirurgie serait une erreur. Un bras placebo chirurgical pose des questions éthiques strictes."),

    ("change-blindness", "La cécité au changement", "Ronald Rensink, Daniel Simons & Daniel Levin", "1997", "03-cognitive",
     "Un élément énorme peut changer sous les yeux sans être vu — la scène n'est pas une photo stockée.",
     "Flicker : deux images alternent avec un masque gris ; un détail important a changé. Autre paradigme : un interlocuteur est remplacé derrière une porte ou une planche portée (Simons & Levin). On demande si quelque chose a changé, puis quoi.",
     "La détection est lente, parfois absente. On n'encode pas toute la scène, seulement ce que l'attention a sélectionné. Complète le gorille invisible (cécité inattentionnelle à l'inattendu) : ici l'objet peut être central et malgré tout manqué.",
     "Sécurité, radiologie, cockpit, témoignage, interfaces. À vivre aussi dans la fiche Cognitive, pas seulement en science psychologique. Relie N400/P300 : le cerveau signale parfois un écart que le rapport conscient rate, ou l'inverse.",
     "Le masque et la tâche pèsent lourd. « Nous ne voyons rien » est faux : nous voyons ce qui sert l'action en cours. Un cas de laboratoire n'épuise pas la perception quotidienne."),

    ("n400", "L'onde N400", "Marta Kutas & Steven Hillyard", "1980", "18-langage",
     "Le cerveau marque un mot sémantiquement tordu bien avant qu'on le commente.",
     "Phrases lues ou entendues dont le dernier mot est inattendu (« je prends le café avec du ciment ») mais souvent grammaticalement correct. EEG moyen : négativité centro-pariétale vers 400 ms. On fait varier cloze probability, métaphore, bilingue, discours.",
     "L'amplitude suit la surprise sémantique. Un mot rare dans le contexte, même possible, gonfle la N400. Ce n'est pas une simple onde « d'erreur grammaticale » (plutôt LAN / P600).",
     "Outil central de psycholinguistique. Fait vivre le potentiel évoqué hors de la seule catégorie 27 : ici le langage. Relie P300 (pertinence / oddball) et MMN (écart sensoriel automatique).",
     "Marqueur de laboratoire, pas définition de « la compréhension ». Latence et forme varient avec l'attention, la langue, l'âge. On n'en fait pas un détecteur de mensonge."),

    ("p300", "Le potentiel P300", "Samuel Sutton et al.", "1965", "03-cognitive",
     "Une positivité vers 300 ms suit un événement rare et pertinent pour la tâche.",
     "Paradigme oddball : sons ou images fréquents, un déviant à détecter (bouton, comptage). On moyenne l'EEG. Distinguer P3a (nouveauté, plus frontale) et P3b (mise à jour contextuelle, pariétale).",
     "L'amplitude croît avec la rareté et la pertinence ; la latence avec la difficulté de la décision. Base de certains épelleurs cerveau-ordinateur.",
     "Montre qu'on peut extraire une catégorisation sans parole, en conditions contrôlées. Vit désormais aussi en cognitive (attention, décision), pas seulement en planche EEG.",
     "N'est pas un polygraphe. Sensible à la fatigue, aux psychotropes, à la consigne. Une application commerciale « lisez les pensées » n'est pas de la science."),

    ("okeefe-cellules-lieu", "Les cellules de lieu", "John O'Keefe", "1971", "08-neurosciences",
     "Un neurone de l'hippocampe s'allume à un endroit de l'espace — une carte, pas une photo.",
     "Rat qui explore un labyrinthe ou une arène. Microélectrode dans l'hippocampe : certaines cellules ne déchargent que dans une zone (place field). Plus tard, May-Britt et Edvard Moser (2005) décrivent dans le cortex entorhinal des cellules de grille : décharges en nœuds d'un hexagone, une métrique.",
     "L'espace interne a des neurones dédiés. Nobel 2014 (O'Keefe et les Moser). Relie H.M. : même région, mémoire et navigation. La mémoire autobiographique a une géométrie.",
     "Fait vivre la découverte hors de la seule cat. 27 : neurosciences, développement de l'orientation, taxi londonien. Voir la fiche Moser ci-dessous.",
     "D'abord le rongeur. Homologues humains surtout via électrodes d'épilepsie. Une cellule de lieu n'est pas « le souvenir de grand-mère » à elle seule."),

    ("moser-cellules-grille", "Les cellules de grille", "May-Britt & Edvard Moser", "2005", "08-neurosciences",
     "Le cortex entorhinal pose une grille hexagonale sur l'espace — un compteur de distance.",
     "Chez le rat qui se déplace librement, des neurones de l'entorhinal médian déchargent en plusieurs lieux régulièrement espacés, formant une triangulation. On fait varier la taille de l'environnement, la direction, la vitesse (cellules de direction de tête, de bord, de vitesse).",
     "Le cerveau n'a pas seulement des « j'y suis » (lieu) : il a une métrique. Combinées aux cellules de lieu, elles fondent un GPS interne.",
     "Complète O'Keefe. Éclaire désorientation, vieillissement, certains tableaux Alzheimer précoces (entorhinal atteint tôt) — sans en faire un test diagnostique.",
     "Modèle animal. La « grille » humaine est inférée, plus rare à enregistrer. Une métaphore GPS ne doit pas cacher que l'espace vécu est aussi social et émotionnel."),

    ("patient-sm", "La patiente S.M. et l'amygdale", "Ralph Adolphs, Daniel Tranel, Antonio Damasio", "1994-2010", "07-emotions",
     "Sans amygdale, la peur des menaces extérieures s'émousse — un cas, pas une loi universelle.",
     "S.M., Urbach-Wiethe, amygdales calcifiées. On lui montre visages (Ekman), films, serpents, maison hantée ; on suit aussi sa vie quotidienne (approches risquées). En 2013, inhalation de CO₂ : panique intense.",
     "Reconnaissance de la peur faciale très altérée ; curiosité plutôt que recul face aux menaces externes. Autres émotions plus préservées. La peur interne (suffocation) peut rester.",
     "Dissociation précieuse pour la fiche Émotions et le cas S.M. L'amygdale participe à la détection de menace et à l'apprentissage de la peur, elle n'est pas « l'organe de la peur ».",
     "Un cas unique. Cerveau entier, biographie, culture. Généraliser de S.M. à « sans amygdale on est sans peur » est faux. Toujours rappeler les limites d'une N=1."),

    ("heminegligence", "La négligence spatiale unilatérale", "Edoardo Bisiach & Claudio Luzzatti", "1978", "08-neurosciences",
     "Oublier la moitié du monde — y compris dans l'image mentale — sans être aveugle.",
     "Après lésion pariétale droite surtout : bissection de lignes, dessin d'horloge, repas. Bisiach demande d'imaginer la Piazza del Duomo de Milan depuis un bord, puis depuis l'autre.",
     "Le côté omis de la place mentale s'inverse avec le point de vue imaginé. Ce n'est pas un trou dans l'œil : c'est un trou dans l'espace représenté. Souvent associé à l'anosognosie (Babinski).",
     "Relie attention, conscience, cas d'héminégligence. Rééducation : balayage, prisme, indices. Planche mentale : la ville à deux orientations.",
     "Tableau variable. Un patient n'est pas tous les patients. La négligence n'est pas un « manque de volonté »."),

    ("two-streams-goodale", "Les deux voies visuelles — la patiente D.F.", "Melvyn Goodale & David Milner", "1992", "03-cognitive",
     "Voir un objet et s'en saisir ne passent pas par le même chemin.",
     "D.F., lésion occipito-temporale (intoxication au monoxyde de carbone) : agnosie de forme. On lui demande de décrire l'orientation d'une fente, puis d'y poster une carte. Tâches de copie vs préhension calibrée.",
     "Elle ne peut pas rapporter la forme, mais oriente la main correctement. Voie ventrale (« quoi », temporal) et voie dorsale (« comment », pariétal). La conscience visuelle n'est pas l'action visuelle.",
     "Cadre encore central. Relie blindsight (Weiskrantz), fiche Cognitive, cas D.F. Deux voies communiquent : la séparation n'est pas étanche.",
     "Un cas princeps, répliqué ensuite sur d'autres patients, jamais une preuve que « personne n'a besoin de voir pour agir ». Toujours borner la N=1."),
]

# (id, nom, dates, pays, courant, apport, bio, citation, oeuvres)
AUTEURS_PLUS = [
    ("fechner", "Gustav Theodor Fechner", "1801-1887", "Allemagne", "Psychophysique",
     "Fonde la mesure de la sensation : la sensation croît comme le logarithme de l'intensité (loi de Weber-Fechner).",
     "Physicien devenu philosophe après une crise de vue, Fechner veut une science exacte du rapport corps-esprit. Dans les Elemente der Psychophysik (1860), il formalise le seuil différentiel de Weber : la plus petite différence perceptible est proportionnelle au stimulus de départ. Il distingue psychophysique interne et externe et ouvre la porte à Wundt. Sans lui, pas d'échelles, pas de juste perceptible, pas de psychologie quantitative.",
     "« La psychophysique est une science exacte des relations de dépendance entre le corps et l'âme. »",
     "Elemente der Psychophysik (1860)"),

    ("helmholtz", "Hermann von Helmholtz", "1821-1894", "Allemagne", "Physiologie sensorielle",
     "Mesure la vitesse de l'influx nerveux et montre que la perception est une inférence inconsciente.",
     "Médecin, physicien, physiologiste. Il chronomètre l'influx sur le nerf de grenouille — l'esprit a un temps. Il explique la vision des couleurs (Young-Helmholtz) et l'audition (résonance cochléaire). Pour lui, nous ne « recevons » pas le monde : nous le concluons à partir de signes sensoriels pauvres. Ancêtre direct de la perception bayésienne et de la psychologie cognitive.",
     "« Les sensations sont des signes dont nous apprenons à interpréter la signification. »",
     "Handbuch der physiologischen Optik (1856-1866), Die Lehre von den Tonempfindungen (1863)"),

    ("cajal", "Santiago Ramón y Cajal", "1852-1934", "Espagne", "Neurohistologie",
     "Impose la doctrine du neurone : le système nerveux est fait de cellules distinctes, pas d'un filet continu.",
     "Médecin et dessinateur hors pair, Cajal utilise la coloration de Golgi — que Golgi interprétait comme un réseau fusionné — pour montrer des neurones séparés communiquant par contacts (plus tard : synapses). Nobel 1906, partagé avec Golgi, dans un désaccord resté fameux. Ses planches d'hippocampe et de cortex sont encore pédagogiques. Relie Hebb, Kandel, et toute la plasticité synaptique.",
     "« Tout homme peut être, s'il le veut, sculpteur de son propre cerveau. »",
     "Textura del sistema nervioso (1899-1904), Recuerdos de mi vida (1917)"),

    ("penfield", "Wilder Penfield", "1891-1976", "États-Unis / Canada", "Neurochirurgie cartographique",
     "Cartographie le cortex éveillé : homoncule moteur et sensoriel, parfois un souvenir ou une odeur.",
     "Formé à Oxford et à Baltimore, Penfield fonde l'Institut neurologique de Montréal. Pendant les chirurgies d'épilepsie, faible courant sur le cortex : un doigt bouge, une lèvre picote, rarement une scène vécue. Il dessine l'homoncule — mains et bouche démesurées. La carte n'est pas le corps, elle est la précision. Relie Fritsch-Hitzig, Wada, et la fiche neurosciences.",
     "« Le cerveau humain est l'organe le plus compliqué de l'univers connu. »",
     "The Cerebral Cortex of Man (1950), Speech and Brain Mechanisms (1959, avec Roberts)"),

    ("berger", "Hans Berger", "1873-1941", "Allemagne", "Électrophysiologie",
     "Enregistre le premier EEG humain (1924-1929) : le rythme alpha, et l'idée qu'on peut lire l'activité du cortex depuis le scalp.",
     "Psychiatre à Iéna, Berger cherche d'abord une « énergie psychique » après un accident de son père. Il pose des électrodes sur son fils Klaus, puis des patients. Les ondes régulières (alpha) disparaissent à l'ouverture des yeux. Moqué, puis devenu l'outil du sommeil, de l'épilepsie, des potentiels évoqués (P300, N400). Suicide en 1941, dans un climat politique et dépressif.",
     "« J'ai enfin, après cinq années, obtenu des tracés d'un cerveau humain. »",
     "Über das Elektrenkephalogramm des Menschen (1929)"),

    ("erikson", "Erik H. Erikson", "1902-1994", "Allemagne / États-Unis", "Psychologie psychosociale",
     "Huit âges de la vie, huit crises : de la confiance de base à l'intégrité.",
     "Artiste devenu analyste, analysé par Anna Freud, Erikson élargit les stades psychosexuels à des crises psychosociales (identité vs confusion à l'adolescence, générativité vs stagnation à l'âge adulte). Il popularise la crise d'identité. Moins expérimental que Piaget, plus narratif : utile comme carte, dangereux comme destin. Relie la fiche Développement.",
     "« L'identité n'est jamais « établie » une fois pour toutes. »",
     "Childhood and Society (1950), Identity: Youth and Crisis (1968)"),

    ("mischel", "Walter Mischel", "1930-2018", "Autriche / États-Unis", "Personnalité et autorégulation",
     "Le test du marshmallow, et surtout la critique situationniste : le trait seul prédit mal le comportement.",
     "Mischel montre en 1968 (Personality and Assessment) que la corrélation trait-comportement plafonne souvent vers 0,30. D'où le débat personne-situation. Le marshmallow (1972) popularise le délai de gratification ; les réplications de 2018 réduisent fortement le lien avec la réussite, largement confondu avec le milieu et la confiance envers l'adulte. Il développe ensuite les stratégies « si-alors » et le système chaud / froid de l'autocontrôle.",
     "« Le pouvoir n'est pas dans le trait, il est dans les stratégies. »",
     "Personality and Assessment (1968), The Marshmallow Test (2014)"),

    ("baumeister", "Roy F. Baumeister", "1953-", "États-Unis", "Soi et autocontrôle",
     "Théoricien de l'ego depletion — et de sa crise de réplication — et de l'estime de soi sans magie.",
     "Baumeister explore le soi, l'appartenance, le sens, le mal. L'idée que la volonté serait un muscle qui se fatigue (ego depletion) a dominé les années 2000, puis échoué à de grandes réplications : effet surestimé, parfois nul. Leçon plus durable : l'estime de soi élevée n'améliore pas à elle seule les notes ou la vertu ; le sentiment d'appartenance et l'autocontrôle prédisent mieux. Relie Mischel, Nolen-Hoeksema, psychologie positive critique.",
     "« L'appartenance est un besoin, l'estime de soi un baromètre. »",
     "Willpower (2011, avec Tierney), travaux sur l'appartenance (1995, avec Leary)"),

    ("nolen-hoeksema", "Susan Nolen-Hoeksema", "1959-2013", "États-Unis", "Cognition et dépression",
     "Montre que la rumination — et non seulement la tristesse — entretient et allonge les épisodes dépressifs.",
     "Professeure à Yale, elle documente pourquoi les femmes, en moyenne, rumine davantage et présentent plus de dépressions unipolaires — sans essentialiser : styles de réponse, rôles, stress. Le Response Styles Theory oppose rumination et distraction constructive. Ses travaux irriguent les TCC, la MBCT et la prévention. Morte à 53 ans, elle laisse un lexique clinique devenu quotidien.",
     "« La rumination est une tentative de comprendre qui empêche de bouger. »",
     "Women Who Think Too Much (2003), manuels et articles sur les styles de réponse"),

    ("dehaene", "Stanislas Dehaene", "1965-", "France", "Neurosciences cognitives",
     "Cartographie la lecture, le nombre et l'accès conscient ; vulgarise sans céder au neuromythe.",
     "Mathématicien devenu neuroscientifique, professeur au Collège de France. Il isole le « recyclage neuronal » : le cerveau recycle des circuits de reconnaissance des objets pour la lecture (aire de la forme visuelle des mots). Travaux sur le sens du nombre, l'effet distance, et l'espace de travail neuronal global (avec Changeux, Naccache). Plaidoyer pour les méthodes d'apprentissage alignées sur les données (espacement, test, clarté). Relie dyslexie, dyscalculie, fiche Cognitive.",
     "« L'éducation est une neurochirurgie sans bistouri. »",
     "Les Neurones de la lecture (2007), Le Code de la conscience (2014)"),

    ("changeux", "Jean-Pierre Changeux", "1936-", "France", "Neurosciences moléculaires",
     "Du récepteur nicotinique à une théorie biologique de l'espace de travail conscient.",
     "Neurobiologiste à l'Institut Pasteur et au Collège de France. Il isole le récepteur de l'acétylcholine, pense la sélection des synapses (théorie de l'épigenèse par stabilisation sélective, avec Danchin), puis propose avec Dehaene un modèle de l'accès conscient : amplification globale de coalitions neuronales. L'Homme neuronal (1983) a choqué et ouvert le débat français esprit-cerveau.",
     "« Le cerveau n'est pas un ordinateur programmé, c'est une machine qui se sélectionne. »",
     "L'Homme neuronal (1983), Matière à pensée (avec Connes, 1989)"),

    ("ramachandran", "Vilayanur S. Ramachandran", "1951-", "Inde / États-Unis", "Neuropsychologie des illusions",
     "Membre fantôme, synesthésie, boîte à miroir : prendre l'illusion au sérieux pour soigner et pour comprendre.",
     "Formé en médecine à Madras, chercheur à San Diego. Il relie douleur du membre fantôme et carte corticale déplacée (Merzenich), propose le miroir pour dénouer le conflit visuo-moteur. Travaux sur la synesthésie, le Capgras, la négligence. Vulgarisateur brillant, parfois trop prompt à la grande théorie. Relie Weiskrantz, Damasio, fiche science psychologique.",
     "« Les illusions ne sont pas des erreurs : elles sont des fenêtres. »",
     "Phantoms in the Brain (1998), The Tell-Tale Brain (2011)"),

    ("weiskrantz", "Lawrence Weiskrantz", "1926-2018", "Royaume-Uni", "Neuropsychologie de la conscience",
     "Décrit la vision aveugle (blindsight) : pointer mieux que le hasard dans un champ « aveugle ».",
     "À Oxford, Weiskrantz étudie le patient D.B. et d'autres après lésion du cortex visuel primaire. Ils disent ne rien voir dans une région, mais devinent orientation, mouvement, parfois émotion d'un visage, au-dessus du hasard. Une voie sous-corticale (colliculus, pulvinar) survit à la conscience. Relie D.F., N400/P300, le débat « que faut-il pour qu'il y ait du vu ».",
     "« Absence de rapport n'est pas absence de traitement. »",
     "Blindsight (1986, rééd. 2009)"),

    ("amunts", "Katrin Amunts", "1962-", "Allemagne", "Cartographie cérébrale",
     "Dirige les atlas contemporains du cerveau (Julich, Human Brain Project) : la carte de Brodmann, en haute résolution.",
     "Médecin et neuroanatomiste, elle combine cytoarchitectonie, IRM et données ouvertes pour redessiner les frontières corticales — plus fines, plus variables d'un cerveau à l'autre que les 52 aires de 1909. Elle insiste sur la variabilité interindividuelle : une « aire de Broca » n'a pas les mêmes bords chez tout le monde. Relie Cajal, Penfield, Poldrack.",
     "« Une carte utile dit aussi où elle se trompe. »",
     "Atlas Julich-Brain, travaux Human Brain Project / EBRAINS"),

    ("poldrack", "Russell A. Poldrack", "1967-", "États-Unis", "IRMf et science ouverte",
     "Critique les excès de l'imagerie (« reverse inference ») et bâtit OpenNeuro, un dépôt ouvert de données cérébrales.",
     "À Stanford, Poldrack montre qu'activer une région pendant une tâche ne prouve pas que cette région « est » la fonction (un même voxel sert plusieurs métiers). Il milite pour le préenregistrement, le partage des raw data, des tailles d'échantillon honnêtes. The New Mind Readers explique ce que l'IRMf peut et ne peut pas lire. Relie la crise de la réplication et la zone de découverte.",
     "« Voir un blob coloré n'est pas comprendre une pensée. »",
     "The New Mind Readers (2018), OpenNeuro, Handbook of Functional MRI Data Analysis"),
]

# (id, nom, periode, domaine, resume, histoire, apport, aujourdhui)
CAS_PLUS = [
    ("patient-tan", "Louis Victor Leborgne (« Tan ») — cas complet", "1861", "Langage",
     "Un homme, une syllabe, une lésion, et la naissance de la neuropsychologie du langage.",
     "Né en 1809, artisan puis malade de longue durée à Bicêtre. Depuis des années il ne produit plus qu'une syllabe, « tan », parfois jurons, tout en comprenant beaucoup. Hémiplégie droite progressive. Paul Broca l'examine du 12 au 17 avril 1861, jour de sa mort. L'autopsie montre une lésion chronique du pied de la 3ᵉ circonvolution frontale gauche, plus vaste qu'on ne l'a d'abord dit. Cerveau conservé, photographié, réimagé au XXIe siècle.",
     "Fonde la méthode anatomo-clinique moderne et le principe : une fonction (parole articulée) peut dépendre d'un territoire. L'aphasie de production porte le nom de Broca. Relie Wernicke (1874), D.F., science psychologique.",
     "Limite d'un cas unique : un cerveau, une biographie, une lésion impure (fibres de passage, réorganisation). L'imagerie du spécimen montre que « l'aire de Broca » classique ne couvre pas toute la lésion. On parle aujourd'hui de réseau, pas d'un îlot. Leborgne n'a pas consenti à devenir une icône."),

    ("patient-hm2", "Kent Cochrane (K.C.)", "1981-2014", "Mémoire",
     "Il savait les faits du monde, pas sa propre vie — et ne pouvait plus imaginer demain.",
     "Canadien, accident de moto en 1981. Lésions hippocampiques et plus étendues. Endel Tulving et ses collègues montrent une mémoire sémantique largement préservée (capitales, métier, grammaire) et une mémoire épisodique dévastée, rétrograde et antérograde. Invité à se souvenir d'hier ou à inventer demain, il décrit le même vide. Il n'est pas H.M. : autre lésion, autre dissociation, identité publique (Kent Cochrane) progressivement assumée dans la littérature.",
     "Dissociation sémantique / épisodique, et découverte que se souvenir et se projeter partagent une machinerie. Ouvre le « voyage mental dans le temps ».",
     "Un cas. D'autres amnésies ne montrent pas le même profil. Cochrane a vécu des décennies comme sujet : dette éthique. Ne pas fondre K.C. et H.M. en un seul « patient mémoire »."),

    ("patient-sm", "S.M.", "1994-", "Émotions",
     "La femme dont les amygdales ont disparu — et qui a réappris à la science ce que n'est pas la peur.",
     "Maladie d'Urbach-Wiethe : calcifications amygdaliennes bilatérales. Adolphs, Tranel, Damasio documentent l'échec à reconnaître la peur sur les visages, l'absence de recul face aux serpents ou aux maisons hantées, une vie sociale trop confiante, des agressions sans méfiance durable. En 2013, le CO₂ inhalé déclenche une panique : la peur intéroceptive peut contourner l'amygdale.",
     "L'amygdale est nécessaire à certaines peurs, pas à toutes. Relie Iowa (Damasio), fiche Émotions, expérience S.M.",
     "Cas unique, identité protégée. On ne réduit pas une personne à deux noyaux. Aucun enseignement clinique individuel ne se déduit d'elle seule."),

    ("patient-df", "La patiente D.F. (deux voies visuelles)", "1988-1992", "Perception / Action",
     "Elle ne « voyait » plus les formes, mais sa main les saisissait.",
     "Intoxication au CO, lésions latérales occipito-temporales. Agnosie visuelle de forme : décrire une fente, copier un dessin, reconnaître un objet par la vue sont très déficitaires. Goodale et Milner lui font poster une carte dans une fente : l'orientation de la main est juste. La voie ventrale (conscient, identification) est atteinte ; la voie dorsale (guidage de l'action) tient.",
     "Preuve dissociative des deux flux visuels. Relie blindsight, Weiskrantz, cognitive.",
     "Un cas princeps. Les voies dialoguent. On n'en tire pas que « la vision consciente est inutile ». Limite classique de la N=1 : précieuse pour réfuter une théorie, insuffisante pour en fonder une à elle seule."),

    ("patient-na", "Le patient N.A.", "1960-", "Mémoire",
     "Une minuscule lésion, une amnésie durable : la mémoire n'habite pas que l'hippocampe.",
     "En 1960, un camarade de chambrée lui plante un fleuret de miniature dans la narine : le fer traverse vers le thalamus / fornix / corps mamillaires. Philipps et Squire, puis d'autres, décrivent une amnésie antérograde verbale massive, mémoire procédurale plus préservée, QI relativement intact. Ce n'est pas H.M. : ici le circuit de Papez est touché hors de l'hippocampe lui-même.",
     "Montre que le circuit diencéphalique est nécessaire à la consolidation déclarative. Relie Korsakoff, H.M., K.C.",
     "Un accident, un cerveau. Généraliser « une piqûre au thalamus efface la mémoire » serait une bande dessinée. Toujours borner le cas unique."),

    ("babinski-anosognosie", "L'anosognosie de Babinski", "1914", "Conscience du déficit",
     "Ne pas savoir que l'on est paralysé — et parfois inventer pourquoi on ne bouge pas.",
     "Joseph Babinski décrit des patients hémiplégiques gauches (lésion droite) qui nient la paralysie, en minimisent l'importance, ou attribuent l'inertie du bras à la paresse, au rhumatisme, à « l'autre ». Souvent liée à la négligence. Ce n'est pas un mensonge : le sentiment d'ownership et de possibilité d'action est cassé.",
     "La conscience d'un déficit est elle-même une fonction. Relie Bisiach, locked-in (l'inverse : conscience intacte, corps muet), main étrangère.",
     "Plusieurs formes (négligence, déni motivé, confusion). Un tableau de 1914 n'épuise pas tous les dénis. Ne pas confondre avec le refus psychologique d'une maladie dont on a par ailleurs conscience."),

    ("locked-in", "Le locked-in (enfermement)", "XXe siècle", "Conscience / Moteur",
     "Éveillé, pensant, parfois ne pouvant plus que cligner — le corps est une prison, pas le soi.",
     "Lésion du ventral du pont (souvent vasculaire) : tétraplégie et anarthrie, vigilance et cognition souvent préservées. Communication par clignement ou interface. Le Scaphandre et le papillon (Bauby) a rendu le tableau visible. À distinguer de l'éveil non répondant et de l'anosognosie.",
     "Sépare radicalement conscience et comportement moteur. Relie P300 (certains protocoles de détection de conscience), éthique de la réanimation, Weiskrantz (traitement sans rapport).",
     "Chaque patient est un monde : cognition, humeur, douleur varient. Un récit célèbre n'est pas une statistique. Jamais un « cas pédagogique » sans dire la dignité et le consentement."),

    ("main-etrangere", "La main étrangère (alien hand)", "1908 / 1972", "Schéma corporel",
     "Une main qui agit, et dont le propriétaire dit : ce n'est pas moi.",
     "Après lésion du corps calleux, du frontal médian ou pariétal, une main (souvent gauche) saisit, défait les boutons, interfère. Le patient la désigne à la troisième personne. Distinct de la main en caoutchouc (illusion chez le sujet sain) et du membre fantôme.",
     "L'agentivité est construite. Relie split-brain, Ramachandran, rubber-hand, fiche neurosciences.",
     "Rare, hétérogène (plusieurs sous-types). Un geste « autonome » n'implique pas un second esprit complet. Limite du cas : spectaculaire, donc trop raconté."),

    ("cotard", "Le syndrome de Cotard", "1880", "Délires rares",
     "L'idée d'être mort, d'être vide, d'avoir perdu les organes ou le sang.",
     "Jules Cotard décrit le « délire des négations » : patients déprimés graves qui nient exister, avoir un cœur, pouvoir mourir (immortalité paradoxale). Tableau rare, souvent dans des dépressions mélancoliques ou des lésions (hémisphère non dominant, Parkinson, etc.).",
     "Montre que le sentiment d'exister a des conditions cérébrales et affectives. Relie Damasio (soi), Capgras, dépression.",
     "Pédagogie, pas diagnostic de poche. Extrêmement rare. Un cas de manuel n'autorise aucun étiquetage d'autrui. Toujours N petite, mécanismes multiples."),

    ("charles-bonnet", "Le syndrome de Charles Bonnet", "1760 / 1769", "Perception",
     "Voir des scènes, des visages, des arabesques — en sachant que ce n'est pas réel — quand la vue baisse.",
     "Charles Bonnet décrit son grand-père, presque aveugle, qui voit des personnages et des architectures tout en jugeant l'hallucination. Fréquent chez les basans de vue âgés, sous-diagnostiqué par honte. Ce n'est pas une psychose : l'insight est souvent conservé.",
     "Le cortex visuel, privé d'entrée, produit. Relie membres fantômes (privation → activité), Weiskrantz, négligence.",
     "Un syndrome, beaucoup de personnes, mais chaque hallucination a sa forme. Ne pas confondre avec hallucinose psychiatrique. Un récit unique (le grand-père de Bonnet) a ouvert la porte ; il ne ferme pas la clinique."),

    ("rosenhan", "Les pseudo-patients de Rosenhan — et l'enquête Cahalan", "1973 / 2019", "Diagnostic",
     "Huit sains à l'asile : un mythe fondateur, puis un dossier d'historienne.",
     "Rosenhan (Science, 1973) raconte huit admissions. Cahalan (2019) cherche les archives, les collègues, les carnets : le récit se délite. Reste la seconde partie (hôpital qui « détecte » des imposteurs absents) et le vrai problème de fidélité diagnostique des années 1970.",
     "A poussé des critères plus explicites. A aussi enseigné à douter des études trop belles.",
     "On enseigne les deux couches. Ni « la psychiatrie ne sait rien » ni « Rosenhan avait tout juste ». Un article n'est pas un dossier patient."),
]

# (id, nom, famille, prevalence, signes, comprendre, traitements)
TROUBLES_PLUS = [
    ("tdah", "TDAH — trois présentations", "Troubles neurodéveloppementaux", "≈ 5 % des enfants, 2,5 % des adultes",
     ["Présentation inattentive : distractibilité, oublis, tâches non finies, « dans la lune » — sans agitation visible",
      "Présentation hyperactive-impulsive : remue, interrompt, décide trop vite, peine à attendre",
      "Présentation combinée : les deux pôles, la plus étudiée dans les essais",
      "Symptômes avant 12 ans, dans au moins deux contextes, retentissement réel",
      "Chez l'adulte : désorganisation, procrastination, hyperfocus paradoxal sur ce qui intéresse"],
     "Ce n'est pas « trop d'énergie » ni un défaut d'éducation. Le TDAH concerne la régulation de l'attention et des fonctions exécutives (circuits fronto-striataux, dopamine/noradrénaline). L'héritabilité est haute (~75 %), l'expression dépend de l'environnement. Une fille inattentive est encore sous-repérée : elle ne dérange pas la classe. Distinguer du haut potentiel (mythe du « HP = TDAH »), de l'anxiété, du manque de sommeil. Pédagogie, pas DSM de poche : seuls un bilan et un clinicien posent un diagnostic.",
     "Psychostimulants (méthylphénidate, etc.) efficaces chez une majorité, jamais magiques ; TCC des fonctions exécutives ; aménagements (consignes écrites, temps, environnement épuré) ; guidance parentale. Structurer l'extérieur plutôt que sermonner le « manque de volonté »."),

    ("dys", "Dyslexie, dyscalculie, dyspraxie — côte à côte", "Troubles neurodéveloppementaux", "≈ 5 à 8 % des enfants (ensemble des troubles spécifiques)",
     ["Dyslexie : déchiffrage lent, coûteux, confusions, fluence de lecture durablement basse malgré un enseignement adapté",
      "Dyscalculie : sens du nombre fragile, dénombrement, faits numériques, comparaison de grandeurs (Dehaene)",
      "Dyspraxie / trouble développemental de la coordination : gestes maladroits, habillage, écriture, organisation spatiale du mouvement",
      "Dysorthographie et dysgraphie souvent associées, jamais automatiques",
      "Intelligence globale préservée ; ce n'est pas un retard global ni un manque de travail"],
     "Trois portes d'entrée différentes vers la même idée : un apprentissage spécifique peut échouer alors que le reste tient. La dyslexie est surtout phonologique chez beaucoup d'enfants francophones ; la dyscalculie touche la magnitude et les procédures ; la dyspraxie est motrice et praxique, pas « la dyslexie du corps » au sens strict — on les enseigne ensemble pour éviter qu'on n'oublie les deux dernières. Comorbidités fréquentes (TDAH, anxiété scolaire). Un seul signe à l'école ne fait pas un trouble.",
     "Orthophonie, ergothérapie, psychomotricité selon le profil ; outils de compensation (synthèse vocale, clavier, tables, géométrie assistée) ; PAP/PPS, tiers-temps. Soutien de l'estime de soi. Aucune « gymnastique des yeux » miracle."),

    ("tourette", "Syndrome de Gilles de la Tourette", "Troubles neurodéveloppementaux", "≈ 0,3 à 1 % des enfants (formes variées)",
     ["Tics moteurs multiples (cligner, hausser les épaules, grimacer) pendant plus d'un an",
      "Au moins un tic vocal (raclement, son, mot) — la coprolalie est spectaculaire et minoritaire",
      "Sensation de besoin préalable, soulagement transitoire après le tic",
      "Fluctuation, aggravation souvent pré-pubertaire, amélioration fréquente à l'âge adulte",
      "Comorbidités fréquentes : TDAH, TOC, anxiété — ce n'est pas « juste des tics »"],
     "Réseaux cortico-striataux, pas un « caprice ». Les tics s'inhibent un moment (coût attentionnel) puis rebondissent : ce n'est pas la preuve qu'on « pourrait s'arrêter si on voulait ». Pédagogie : dédramatiser la coprolalie médiatique. Pas un diagnostic de poche devant un enfant qui cligne des yeux une semaine.",
     "Psychoéducation de l'entourage (souvent le plus utile) ; thérapie d'inversion de l'habitude / CBIT ; parfois traitements médicamenteux encadrés. Aménagements scolaires : autoriser le mouvement, éviter l'humiliation."),

    ("accumulation", "Accumulation (syllogomanie / hoarding)", "TOC et apparentés", "≈ 2 à 6 % selon les critères et l'âge",
     ["Difficulté persistante à jeter, même des objets sans valeur marchande",
      "Encombrement qui rend des pièces inutilisables",
      "Détresse ou danger (incendie, chute, hygiène, conflit familial)",
      "Croyances : « ça peut servir », « c'est une partie de moi », évitement de la décision",
      "Début souvent insidieux à l'adolescence, visible à l'âge adulte"],
     "Distinct du collectionneur organisé et du simple désordre. Proche du TOC mais pas identique : moins de rituels de vérification, plus d'attachement et d'indécision. Le « nettoyage surprise » par la famille aggrave souvent la rupture de confiance. Pédagogie, pas expédition punitive.",
     "TCC spécifique (tri, exposition à jeter, décisions répétées), parfois visite à domicile ; ISRS si comorbidité. Éviter l'ultimatum-benne sans soin : taux de rechute élevé."),

    ("jeu-argent", "Jeu d'argent problématique", "Addictions", "≈ 0,5 à 2 % en population générale, plus chez certains jeunes hommes",
     ["Perte de contrôle sur les mises, poursuite malgré les pertes (chasse à la perte)",
      "Préoccupation, tolérance (mises croissantes), irritabilité à l'arrêt",
      "Mensonges, emprunts, retentissement familial ou professionnel",
      "Illusion de contrôle (dés, rituels) et biais du joueur (une série « doit » s'inverser)",
      "Jeux à renforcement variable (machines, paris en ligne) particulièrement accrocheurs"],
     "Ce n'est pas un vice isolé ni « toutes les addictions comportementales se valent ». Skinner est ici pédagogique : ratio variable. Distinguer jeu social, jeu excessif, trouble. Relie biais d'illusion de contrôle, sophisme du joueur, fiche tests Iowa (prise de risque).",
     "TCC du jeu, limitation des moyens de paiement, interdiction des salles, groupes d'entraide ; traiter dépression/TDAH comorbides. En France, interlocuteurs spécialisés (centres de soin en addictologie). Pas un conseil financier."),

    ("arfid", "ARFID — évitement / restriction alimentaire", "Troubles des conduites alimentaires", "Prévalence encore mal fixée ; plus visible chez l'enfant",
     ["Restriction qui n'est pas une peur de grossir : textures, peur de s'étouffer, manque d'intérêt pour manger",
      "Déficit nutritionnel, cassure de courbe, dépendance à des compléments, ou retentissement social",
      "Répertoire parfois limité à quelques aliments « sûrs »",
      "Souvent antécédents sensoriels, anxiété, TDAH ou TSA",
      "Insight variable : « je ne peux pas », pas « je ne dois pas maigrir »"],
     "Distinct de l'anorexie (pas de dysmorphie ni de quête de maigreur) et d'un simple « enfant difficile » transitoire. L'ARFID est un repère pédagogique récent (DSM-5) : il évite d'attendre une phobie du poids pour soigner. Pas un DSM de poche : la frontière avec le picky eating développemental demande un clinicien.",
     "Exposition alimentaire graduée, travail sensoriel, parfois guidance familiale type FBT adaptée ; jamais forcer à table comme punition. Bilan somatique si cassure de poids."),

    ("schizo-affectif", "Trouble schizo-affectif — un repère, pas une étiquette de couloir", "Troubles psychotiques", "Plus rare que la schizophrénie et le bipolaire ; chiffres instables",
     ["Épisodes psychotiques (idées délirantes, hallucinations) ET épisodes thymiques francs (maniaques ou dépressifs)",
      "Des symptômes psychotiques aussi en dehors des phases d'humeur — c'est le nœud du repère",
      "Retentissement durable sur le fonctionnement",
      "Souvent un long chemin diagnostique : « c'était un bipolaire » / « c'était une schizo »",
      "Risque suicidaire à prendre au sérieux comme dans les deux familles voisines"],
     "Catégorie-frontière, fidélité inter-juges imparfaite : d'où l'insistance pédagogique. On la distingue de la schizophrénie (l'humeur n'est pas le premier plan continu) et du bipolaire avec caractéristiques psychotiques (la psychose ne survit pas longtemps hors de l'épisode d'humeur). Les frontières bougent selon DSM et CIM. Ce n'est pas un mot pour dire « un peu des deux, donc plus grave ».",
     "Soins combinés : thymorégulation, antipsychotiques selon le tableau, psychoéducation, TCC des psychoses, réhabilitation. Décision clinique, jamais d'après une page web."),

    ("personnalite-antisociale", "Personnalité antisociale — à distinguer", "Troubles de la personnalité", "≈ 1 à 4 % selon les critères, plus élevée en milieu carcéral",
     ["Mépris durable des droits d'autrui depuis l'adolescence (une conduite isolée ne suffit pas)",
      "Impulsivité, tromperie, irresponsabilité, absence de remords dans les critères historiques",
      "À distinguer de : acte délinquant unique, trouble des conduites de l'enfant (nécessaire mais non suffisant), psychopathie au sens de Hare (construits qui se recouvrent sans s'équivaloir)",
      "À distinguer aussi du borderline (peur de l'abandon, instabilité identitaire) et du narcissique (besoin d'admiration)",
      "Plus fréquent chez les hommes dans les études — biais de repérage possible"],
     "Mot trop souvent lancé comme insulte. En pédagogie : un trouble de la personnalité est un schéma durable, envahissant, dès le jeune adulte, pas un week-end violent. La « psychopathie » médiatique (charme, froideur, calcul) n'est pas le texte du DSM. L'antisocial n'est pas « le criminel » : beaucoup de crimes n'y correspondent pas, et le diagnostic n'est pas une fatalité génétique simple. Relie psychologie légale, débats, pas un portrait-robot.",
     "Pronostic difficile, peu de traitements « spécifiques » miracles ; interventions sur l'impulsivité, les addictions, la prévention de la violence, parfois thérapies structurées. Aucune page ne permet de qualifier un proche."),
]

# (id, nom, famille, definition, exemple, parade)
BIAIS_PLUS = [
    ("dunning-kruger", "Effet Dunning-Kruger", "Métacognition",
     "Les moins compétents surestiment souvent leur rang, faute des outils mêmes qui permettraient de se voir. Les plus compétents se sous-estiment parfois un peu (ils surestiment les autres). L'article de 1999 est réel ; sa caricature en « courbe en D » virale l'est beaucoup moins.",
     "Après deux tutoriels, se sentir prêt à corriger un chercheur. À l'inverse, un expert qui dit « c'est plus compliqué » passe pour hésitant face à un confident ignorante.",
     "Demander une mesure externe (examen, revue par les pairs, erreur comptée). Se méfier des graphiques internet. Gare à l'artefact statistique : même sans psychologie, des scores extrêmes régressent vers la moyenne. La leçon utile reste : le sentiment de maîtrise n'est pas la maîtrise."),

    ("ikea", "Effet IKEA", "Évaluation",
     "Nous surévaluons un objet (ou une idée) dès que nous avons fourni un effort de construction — même minime. Norton, Mochon et Ariely (2012) : des boîtes pliées par soi valent plus, subjectivement, que les mêmes déjà montées.",
     "Un meuble bancal « a du cachet parce que c'est moi ». Un diaporama collectif devient intouchable. Un modèle théorique qu'on a soi-même bricolé résiste aux réfutations.",
     "Faire évaluer par quelqu'un qui n'a pas tourné la vis. Dans un travail de groupe, tourner le rôle de « l'avocat du diable ». Distinguer fierté légitime et prix de marché."),

    ("identifiabilite", "Effet de l'identifiabilité", "Éthique et décision",
     "Une victime identifiée (un visage, un prénom, une photo) déclenche plus d'aide qu'un nombre statistique plus grave. Schelling, puis Small, Loewenstein : « une personne » bat « deux cents personnes » dans les dons.",
     "Un enfant portraituré lève plus de fonds qu'un rapport sur la mortalité infantile. En science : un cas clinique célèbre pèse plus qu'une méta-analyse — d'où nos propres mises en garde N=1.",
     "Tenir les deux : le visage pour la motivation, le dénominateur pour la justice. Dans une décision publique, afficher le nombre attendu de personnes concernées, pas seulement l'histoire."),

    ("omission", "Biais d'omission", "Éthique et décision",
     "Faire du mal par action paraît pire que laisser advenir le même mal par inaction. Ritov & Baron : vacciner avec un risque rare d'effet indésirable est jugé plus fautif que ne pas vacciner face à une maladie plus risquée.",
     "Refuser un traitement dont l'abstention tue davantage. En recherche : ne pas répliquer (omission) passe moins pour une faute que publier un faux positif (action).",
     "Comparer les deux branches sur la même unité (morts, erreurs). Écrire à l'avance la règle (« nous agissons si… »). Distinguer intention et bilan."),

    ("statu-quo", "Biais de statu quo", "Décision",
     "L'état actuel sert de référence : tout changement se vit comme une perte. Voisin de l'aversion à la perte et de l'effet de dotation. Samuelson & Zeckhauser : on garde l'option par défaut, même médiocre.",
     "Le même contrat d'assurance quinze ans. En science : un paradigme (DSM, test projectif, p < 0,05) survit à ses critiques parce qu'il est déjà là.",
     "Imaginer que l'on choisit aujourd'hui pour la première fois. Inverser le défaut (opt-out). Programmer une date de révision."),

    ("hot-cold-empathy", "Fossé d'empathie chaud-froid", "Métacognition affective",
     "À froid, on sous-estime ce que l'on fera à chaud (faim, colère, désir, douleur, craving) ; à chaud, on oublie l'état froid. Loewenstein : hot-cold empathy gap. On se trompe sur soi autant que sur autrui.",
     "Décider d'un régime après le dîner. Promettre « je resterai calme » avant l'examen. Un clinicien reposé qui ne croit pas un patient en crise.",
     "Décider les règles à froid (si-alors de Mischel). Reporter les choix irréversibles hors pic émotionnel. En soin : croire que l'état change le jugement, sans infantiliser."),

    ("illusion-controle", "Illusion de contrôle", "Perception de causalité",
     "Surestimer son influence sur le hasard. Langer (1975) : choisir soi-même ses billets de loterie les fait juger plus « gagnants ». Relie le jeu d'argent, le placebo rituel, certains managements magiques.",
     "Souffler sur les dés, un « système » à la roulette, croire qu'un slide de plus a fait gagner le marché.",
     "Séparer zone d'influence et bruit. Au jeu : l'avantage de la maison n'a pas d'oreille. En recherche : un p-hacking n'est pas « contrôler » le phénomène."),

    ("survivants", "Biais des survivants", "Sélection des données",
     "On n'analyse que ce qui a passé un filtre (avions revenus, entreprises encore debout, articles publiés) et l'on prend leurs traits pour des causes de succès.",
     "Abraham Wald : blinder les zones non touchées des avions rentrés — les impacts manquants sont ceux des avions abattus. « Tous les milliardaires se lèvent à 5 h » ignore ceux qui se levaient à 5 h et ont échoué.",
     "Chercher les disparus de l'échantillon. Demander le dénominateur. En histoire de vie, se méfier des autobiographies de gagnants."),

    ("survivants-science", "Biais de survivant en science", "Méthodes / publication",
     "La littérature visible est celle qui a survécu : résultats positifs, effets gros, narrations nettes. Les null, les échecs de réplication, les tiroirs restent au sol — comme les avions qui ne rentrent pas. C'est le biais des survivants appliqué au savoir.",
     "Un paradigme (amorçage social spectaculaire, ego depletion, pouvoir des poses) « survit » en citations longtemps après que les réplications ont échoué. Un cas unique célèbre (Gage, Tan, Rosenhan) occupe plus de manuels qu'une méta-analyse terne.",
     "Lire les dépôts (OSF, Registered Reports), les méta-analyses avec biais de publication, les échecs. Préenregistrer. Enseigner Cahalan à côté de Rosenhan, Jussim à côté de Pygmalion. C'est déjà la réforme de la discipline."),
]

# (id, nom, categorie, auteur_annee, mesure, passation, interpretation, limites)
TESTS_PLUS = [
    ("wcst", "Wisconsin Card Sorting Test (WCST)", "Neuropsychologie", "Grant & Berg, 1948 (formes modernes Heaton)",
     "Flexibilité mentale : découvrir une règle de tri (couleur, forme, nombre), s'y tenir, puis en changer sans qu'on l'annonce, d'après le seul feedback juste/faux.",
     "Individuelle, cartes à classer, 15 à 30 minutes, souvent informatisée. On compte catégories achevées, erreurs persévératives, échecs à maintenir un set.",
     "Beaucoup d'erreurs persévératives orientent vers une rigidité dysexécutive, historiquement « frontale ». Utile en bilan, jamais isolément.",
     "Tâche impure (attention, mémoire de travail, compréhension de consignes, frustration). Un mauvais score ne localise pas une lésion. Effet d'apprentissage si on le repasse. Ce n'est pas un QI."),

    ("trail-making", "Trail Making Test (A et B)", "Neuropsychologie", "Partington / Armée US, 1940s ; Reitan",
     "Vitesse visuo-motrice (partie A : relier 1-2-3…) et flexibilité (partie B : 1-A-2-B…). Le coût B − A isole à peu près le bascule de set.",
     "Papier-crayon, quelques minutes, chronométré. Consigne claire, correction d'une erreur en cours.",
     "Allongement de B, surtout de l'écart B−A, évoque un coût exécutif. Très utilisé en dépistage (avec MMSE/MoCA) et en suivi.",
     "Sensible à l'âge, à la scolarité, à la vision, à la main, à l'anxiété. Une lenteur A déjà pathologique rend B ininterprétable. Pas un test de « démence » à lui seul."),

    ("rey-osterrieth", "Figure complexe de Rey-Osterrieth", "Neuropsychologie", "André Rey, 1941 ; Osterrieth, 1944",
     "Organisation perceptive, planification, mémoire visuelle immédiate et différée. On copie une figure absurde géométrique, puis on la redessine de mémoire.",
     "Individuelle. Trois temps souvent : copie, rappel immédiat, rappel différé (20-30 min). Cotation des unités et, surtout, de la stratégie (global → détails vs juxtaposition).",
     "Une copie « pièce par pièce » sans structure oriente vers un trouble organisationnel ; un oubli massif vers un trouble mnésique visuel. La BEM francophone s'en inspire.",
     "Sensible au moteur, à la vision, à la culture graphique. Cotation exige un entraînement. Ne pas confondre un style de dessin avec un diagnostic."),

    ("hayling", "Test de Hayling", "Neuropsychologie", "Burgess & Shallice, 1996 (adapt. française)",
     "Initiation verbale et, surtout, inhibition : terminer une phrase par un mot qui n'a rien à voir, en évitant le mot évident.",
     "Deux blocs. A : finir vite et justement (« On allume une… allumette »). B : finir par un mot sans lien (« On allume une… kangourou »), sans rire ni se corriger trop tard. Temps et erreurs d'inhibition.",
     "Le bloc B coûte cher en contrôle. Utile dans les tableaux frontaux, certains TDAH adultes, certaines démences, toujours en batterie.",
     "Dépend du lexique, de la langue, de la créativité. Une blague n'est pas une réussite. Pas un test de personnalité."),

    ("iowa-gambling", "Iowa Gambling Task", "Neuropsychologie / Décision", "Bechara, Damasio et al., 1994",
     "Apprentissage des risques sous incertitude : quatre paquets, gains et pertes cachés. Les paquets A/B sont toxiques à long terme ; C/D sont meilleurs.",
     "100 à 200 essais, souvent avec conductance cutanée. On observe si le sujet se détourne des paquets punitifs avant de pouvoir l'expliquer.",
     "Les sujets sains développent une préférence et des « marqueurs » corporels anticipateurs. Certaines lésions ventromédianes persistent à choisir le toxique. Relie la fiche Damasio.",
     "Tâche de labo : quatre paquets ≠ une vie. Stratégies verbales, impulsivité, niveau mathématique brouillent. Un score n'est pas une « intelligence émotionnelle » chiffrée."),

    ("wada", "Test de Wada", "Neuropsychologie / Épilepsie", "Juhn Atsushi Wada, 1949",
     "Latéralisation du langage et, secondairement, de la mémoire : on endort un hémisphère via la carotide, on teste l'autre.",
     "Examen hospitalier invasif. Injection d'un barbiturique. Pendant quelques minutes : dénomination, compréhension, souvenirs. Puis l'autre côté, un autre jour parfois.",
     "Chez la plupart des droitiers, le langage s'effondre à gauche. Guide la chirurgie d'épilepsie. Complète Broca sans attendre l'autopsie. Relie l'expérience Wada.",
     "Invasif, risque vasculaire. De plus en plus concurrencé par l'IRMf de langage, qui n'a pas la même valeur causale. Jamais un test de salon."),

    ("mmpi", "MMPI — objet historique critiqué", "Personnalité clinique", "Hathaway & McKinley, 1943 ; MMPI-2, MMPI-3",
     "Inventaire empirique : les items ont été retenus s'ils discriminaient des groupes cliniques des années 1940, pas s'ils « avaient l'air » valides. Échelles cliniques (Hs, D, Hy, Pd, Pa, Pt, Sc, Ma…) et, surtout, échelles de validité (mensonge, infréquence, incohérence).",
     "Auto-questionnaire long (338 à 567 items selon la version), 60 à 90 minutes. Réservé aux professionnels. Des versions « MMPI en ligne gratuit » n'ont aucune valeur.",
     "Historiquement massif en clinique nord-américaine et en expertise. Les échelles de validité restent pédagogiquement intéressantes : on peut mesurer la manière de répondre.",
     "Échantillon initial étroit (Minnesota, blanc, hospitalier). Noms d'échelles trompeurs (« Schizophrénie » ≠ diagnostic). Construction empirique opaque. Ne pose pas un diagnostic. Objet à enseigner comme monument et comme mise en garde, pas comme vérité sur soi."),

    ("big-five", "NEO-PI-R / NEO-PI-3 / BFI (Big Five)", "Personnalité", "Costa & McCrae, 1985-1992",
     "Cinq dimensions (OCEAN) et, dans le NEO-PI, six facettes par dimension : le grain fin de l'ouverture, de la conscienciosité, etc. Le BFI est la version courte de recherche.",
     "NEO-PI : ~240 items, 30-45 min, normes. BFI : ~44 items, 5-10 min. Auto-rapport. Pas un test projeté : items explicites.",
     "Modèle le mieux répliqué. La conscienciosité prédit la réussite scolaire/professionnelle mieux que beaucoup de discours motivationnels ; le névrosisme, la vulnérabilité au stress. Utile en recherche et, avec prudence, en orientation.",
     "Désirabilité sociale. Décrit des tendances, pas l'acte d'un mardi. Ce n'est pas le MBTI. Un profil n'est pas un destin ni un recrutement à lui seul."),

    ("rorschach", "Test de Rorschach — ce que ça vaut", "Projectif", "Hermann Rorschach, 1921",
     "Dix taches. On note ce qui est vu, où, grâce à quelle propriété (forme, couleur, mouvement). Les systèmes Exner puis R-PAS ont tenté de standardiser.",
     "Individuelle, 45-90 min + enquête. Formation longue. Les planches sont aussi un objet culturel (voir le dossier projectifs).",
     "Quelques indices (complexité, certaines scores formels) ont une fidélité acceptable. Beaucoup d'interprétations symboliques (« le rouge = le sang = l'agressivité ») n'en ont pas.",
     "Validité très inégale. Usage judiciaire particulièrement contesté. Ne « révèle » pas un inconscient comme une radiographie. À comparer au TAT dans le dossier « Ce que ça vaut »."),

    ("tat", "TAT — ce que ça vaut", "Projectif", "Murray & Morgan, 1935",
     "Planches figuratives ambiguës : on raconte une histoire (avant, pendant, après, pensées des personnages). Murray y lisait besoins et pressions ; en France, l'école de Shentoub lit les procédés du discours.",
     "Individuelle, nombre de planches variable, une à deux heures. Production langagière riche, utile parfois pour nouer un entretien.",
     "Peut éclairer des thèmes relationnels dans un faisceau clinique. N'est pas un score de personnalité comparable au NEO-PI.",
     "Cotation dépendante du clinicien, faible standardisation, peu de validité incrémentielle démontrée une fois qu'on a déjà un entretien et des échelles. Voir le dossier TAT vs Rorschach."),

    ("bem", "Batterie BEM 144 / figure de Rey", "Neuropsychologie", "Rey, 1941 ; Signoret, 1991",
     "Mémoire (histoires, figures, mots) et, via la figure de Rey, organisation du rappel visuel.",
     "Batterie francophone classique en clinique de la mémoire, à côté de Grober & Buschke, Rey verbal, etc.",
     "Permet de comparer profils (verbal/visuel, encodage/récupération). La stratégie de copie de la figure compte autant que le score.",
     "Étalonnages à tenir à jour. Sensible au moteur et à la culture scolaire. Un oubli isolé n'est pas une maladie."),
]

# (annee, titre, desc, periode)
CHRONOLOGIE_PLUS = [
    ("1860", "Fechner, Elemente der Psychophysik", "La sensation devient mesurable : seuil différentiel et logarithme de l'intensité. La psychologie quantitative a une date de naissance, avant Leipzig.", "fondations"),
    ("1863", "Helmholtz, Die Lehre von den Tonempfindungen", "L'audition et, déjà, l'idée que percevoir c'est inférer. Le temps de l'influx nerveux n'est plus infini.", "fondations"),
    ("1906", "Nobel de Golgi et Cajal", "Même coloration, deux doctrines : réseau continu contre neurone. Cajal l'emporte, et le dessin scientifique avec lui.", "neurosciences"),
    ("1914", "Babinski nomme l'anosognosie", "Ne pas savoir que l'on est paralysé devient un fait neurologique, pas une « mauvaise volonté ».", "neurosciences"),
    ("1924", "Berger enregistre un EEG humain", "Des ondes sur le scalp. D'abord incrédule, la discipline tiendra là P300, N400, sommeil, épilepsie.", "neurosciences"),
    ("1935", "Morgan et Murray publient le TAT", "Des images ambiguës pour raconter. Le projectif entre dans le laboratoire clinique — sa validité s'y discutera un siècle.", "psychometrie"),
    ("1944", "Osterrieth cote la figure de Rey", "Une figure absurde devient un test de stratégie, pas seulement de mémoire.", "psychometrie"),
    ("1948", "Wisconsin Card Sorting Test", "Changer de règle quand le monde change de feedback : la flexibilité a une épreuve.", "psychometrie"),
    ("1949", "Wada endort un hémisphère", "Le langage a une adresse clinique avant l'imagerie.", "neurosciences"),
    ("1950", "Erikson, Childhood and Society", "Huit crises psychosociales : l'identité devient un âge, pas seulement un concept.", "developpement"),
    ("1966", "Hofling téléphone aux infirmières", "L'obéissance hors du labo de Milgram : 21 sur 22 préparent une dose impossible.", "sociale"),
    ("1971", "O'Keefe : cellules de lieu", "L'hippocampe contient une carte. Les Moser y ajouteront une grille en 2005.", "neurosciences"),
    ("1978", "Bisiach et la place du Dôme", "La négligence habite aussi l'espace imaginé.", "neurosciences"),
    ("1980", "Kutas et Hillyard : N400", "Un mot qui ne va pas laisse une trace électrique à 400 ms.", "cognitive"),
    ("1992", "Goodale, Milner et D.F.", "Deux voies visuelles : le quoi et le comment se séparent chez une patiente.", "neurosciences"),
    ("1994", "Iowa Gambling Task et S.M.", "Damasio relie émotion et décision ; Adolphs décrit une vie sans peur externe.", "emotions"),
    ("1997", "Cécité au changement", "Rensink, Simons : la scène n'est pas stockée en photo.", "cognitive"),
    ("2002", "Moseley : placebo chirurgical", "Une fausse arthroscopie égale la vraie pour certains genoux arthrosiques.", "sante"),
    ("2005", "Cellules de grille (Moser)", "Une métrique hexagonale dans l'entorhinal. Nobel 2014 avec O'Keefe.", "neurosciences"),
    ("2012", "Effet IKEA", "Ce que l'on monte soi-même vaut plus — y compris les théories.", "cognitive"),
    ("2018", "Marshmallow répliqué", "L'attente à 4 ans prédit beaucoup moins la réussite une fois le milieu contrôlé (Mischel relu).", "developpement"),
    ("2019", "Cahalan enquête sur Rosenhan", "The Great Pretender : l'étude-choc du diagnostic est elle-même un dossier à trous.", "clinique"),
]

GLOSSAIRE_PLUS_REF = [
    ("Loi de Fechner", "La sensation croît comme le logarithme de l'intensité physique du stimulus, à partir du seuil différentiel de Weber.", "03-cognitive"),
    ("Inférence inconsciente", "Chez Helmholtz : percevoir, c'est conclure à une cause externe à partir de signes sensoriels pauvres.", "03-cognitive"),
    ("Doctrine du neurone (Cajal)", "Le système nerveux est fait de cellules distinctes qui communiquent par contacts, non d'un reticulum continu à la Golgi.", "08-neurosciences"),
    ("Homoncule de Penfield", "Carte corticale du corps : les régions les plus précises (main, bouche) occupent plus de cortex que le tronc.", "08-neurosciences"),
    ("Rythme alpha de Berger", "Ondes EEG d'environ 8-12 Hz, visibles yeux fermés au repos, bloquées à l'ouverture des yeux.", "27-science-psychologique"),
    ("Crise psychosociale", "Chez Erikson, conflit caractéristique d'un âge (confiance, identité, générativité…) dont l'issue oriente la suite.", "05-developpement"),
    ("Situationnisme (Mischel)", "Le comportement varie fortement selon la situation ; un trait global prédit mal un acte précis.", "06-personnalite"),
    ("Ego depletion", "Hypothèse (Baumeister) d'une volonté-muscle qui se fatigue — effet surestimé, mal répliqué à grande échelle.", "06-personnalite"),
    ("Rumination", "Style de réponse (Nolen-Hoeksema) qui ressasse causes et conséquences d'une tristesse, et allonge les épisodes dépressifs.", "09-psychopathologie"),
    ("Recyclage neuronal", "Chez Dehaene : un circuit ancien (objets, formes) est réutilisé par la culture (lettres, chiffres).", "03-cognitive"),
    ("Espace de travail global", "Modèle Changeux-Dehaene : une information devient consciente en étant amplifiée et partagée à grande échelle.", "08-neurosciences"),
    ("Vision aveugle", "Capacité à « deviner » un stimulus dans un champ aveugle après lésion occipitale (Weiskrantz), sans expérience visuelle rapportée.", "08-neurosciences"),
    ("Reverse inference", "Erreur (Poldrack) : conclure d'une activation cérébrale à un état mental unique (« le gyrus X s'allume donc c'est de l'amour »).", "27-science-psychologique"),
    ("Cellule de grille", "Neurone de l'entorhinal qui décharge en nœuds hexagonaux : une métrique de l'espace (Moser, 2005).", "08-neurosciences"),
    ("Cellule de lieu", "Neurone hippocampique qui décharge surtout quand l'animal est à un endroit (O'Keefe, 1971).", "08-neurosciences"),
    ("Cécité au changement", "Échec à remarquer une modification importante d'une scène lorsque l'attention n'y était pas (Rensink, Simons).", "03-cognitive"),
    ("But supraordonné", "Objectif qui exige la coopération de deux groupes en conflit (Sherif, Robbers Cave) : le contact seul ne suffit pas.", "04-sociale"),
    ("Justification insuffisante", "Paradigme Festinger-Carlsmith : un petit paiement pour un mensonge pousse à changer d'avis, un gros non.", "04-sociale"),
    ("Placebo chirurgical", "Bras d'un essai où l'on simule l'opération (Moseley, 2002) pour isoler l'effet du rituel de soin.", "14-sante"),
    ("Anosognosie", "Méconnaissance d'un déficit (Babinski, 1914), souvent après lésion droite, distincte du déni psychologique.", "08-neurosciences"),
    ("Héminégligence", "Ignorance d'un côté de l'espace — y compris mental (Bisiach) — malgré une vision périphérique souvent intacte.", "08-neurosciences"),
    ("Voie ventrale / dorsale", "Deux flux visuels : « quoi » (temporal) et « comment » (pariétal), dissociés chez D.F. (Goodale & Milner).", "03-cognitive"),
    ("Locked-in", "Éveil et conscience souvent préservés, motricité quasi nulle (pont ventral) : l'absence de mouvement n'est pas l'absence de pensée.", "08-neurosciences"),
    ("Main étrangère", "Une main agit dont le sujet récuse l'agentivité, après lésion calleuse ou frontale médiane.", "08-neurosciences"),
    ("Syndrome de Cotard", "Délire rare de négation d'exister ou d'avoir des organes, souvent dans une dépression très sévère.", "09-psychopathologie"),
    ("Charles Bonnet", "Hallucinations visuelles avec insight fréquent, liées à une baisse de vue, sans psychose.", "03-cognitive"),
    ("ARFID", "Restriction alimentaire sans peur de grossir : textures, peur de s'étouffer, ou désintérêt — distincte de l'anorexie.", "09-psychopathologie"),
    ("Trouble schizo-affectif", "Repère-frontière : psychose et épisodes d'humeur, avec des symptômes psychotiques aussi hors des phases thymiques.", "09-psychopathologie"),
    ("Personnalité antisociale", "Schéma durable de mépris des droits d'autrui — à distinguer d'un acte, du trouble des conduites, et de la psychopathie médiatique.", "09-psychopathologie"),
    ("Identifiabilité", "Une victime pourvue d'un visage lève plus d'aide qu'un nombre statistique plus grave.", "04-sociale"),
    ("Fossé chaud-froid", "À froid on sous-estime ce que l'on fera à chaud (faim, colère, craving) ; à chaud on oublie l'état calme.", "07-emotions"),
    ("Survivant en science", "On ne cite que les études et les cas qui ont « survécu » à la publication, comme on n'étudie que les avions rentrés.", "01-fondamentaux"),
    ("Trail Making", "Test chronométré : relier des chiffres (A) puis alterner chiffres et lettres (B) pour estimer la flexibilité.", "19-psychometrie"),
    ("Hayling", "Terminer une phrase par un mot sans rapport : mesure d'inhibition verbale (Burgess & Shallice).", "19-psychometrie"),
    ("NEO-PI", "Inventaire des cinq grands facteurs de personnalité et de leurs facettes (Costa & McCrae).", "06-personnalite"),
    ("The Great Pretender", "Enquête de Susannah Cahalan (2019) sur les trous et contradictions de l'étude de Rosenhan.", "09-psychopathologie"),
]


# Sections, mythes, chiffres et flashcards à empiler sur les catégories existantes.
EXTRA_PLUS = {
    "03-cognitive": {
        "sections": [
            ("Cécité au changement et gorille : deux aveuglements, un cerveau",
             "<p>Le <a href=\"../references/experiences.html#gorille-invisible\">gorille invisible</a> montre qu'un événement "
             "inattendu échappe quand l'attention est occupée. La "
             "<a href=\"../references/experiences.html#change-blindness\">cécité au changement</a> (Rensink, Simons) montre "
             "autre chose : même un élément central peut être remplacé si un masque coupe le mouvement. La leçon commune : "
             "la scène n'est pas une photographie stockée. On encode ce qui sert l'action en cours.</p>"
             "<p>Conséquences : un radiologue, un conducteur, un témoin peuvent être sincères et incomplets. Relier à "
             "<a href=\"../references/experiences.html#loftus-témoignage\">Loftus</a> (la mémoire se reconstruisant) sans "
             "conclure que « personne ne voit rien ».</p>"),
            ("P300 : l'attention laisse une trace électrique",
             "<p>Le <a href=\"../references/experiences.html#p300\">P300</a> de Sutton (1965) n'appartient pas qu'à la "
             "catégorie science psychologique. En cognitive, c'est un marqueur de <em>pertinence</em> : un stimulus rare "
             "et à détecter évoque une positivité vers 300 ms. On distingue souvent une P3a (nouveauté) et une P3b "
             "(mise à jour du contexte).</p>"
             "<p>Utile pour comprendre l'attention et certains épelleurs cerveau-ordinateur. Inutile comme détecteur de "
             "mensonge. Voir aussi la <a href=\"../references/experiences.html#n400\">N400</a> côté langage.</p>"),
            ("Deux voies chez D.F. : voir n'est pas saisir",
             "<p>La <a href=\"../references/cas.html#patient-df\">patiente D.F.</a> (Goodale &amp; Milner, 1992) ne décrit "
             "plus les formes mais poste une carte dans une fente. Voie ventrale (« quoi ») et voie dorsale (« comment »). "
             "C'est le même cerveau que celui du gorille et du changement : plusieurs traitements visuels, une seule "
             "histoire consciente après coup. <strong>Limite d'un cas unique</strong> : D.F. réfute une théorie trop "
             "simple, elle n'en fonde pas une à elle seule.</p>"),
        ],
        "flashcards": [
            ("En quoi la cécité au changement diffère-t-elle du gorille invisible ?",
             "Le gorille est inattendu pendant une tâche ; le changement peut porter sur un objet déjà là, manqué à cause du masque et de l'attention."),
            ("Que marque le P300 ?", "Un événement rare et pertinent pour la tâche, vers 300 ms, pas un mensonge."),
        ],
        "chiffres": [
            ("≈ 400 ms", "Pic de la N400 après un mot sémantiquement tordu"),
            ("≈ 300 ms", "Fenêtre classique du P300 dans une tâche oddball"),
        ],
    },
    "04-sociale": {
        "sections": [
            ("De Robbers Cave à Tajfel : deux recettes du « eux »",
             "<p><a href=\"../references/experiences.html#robbers-cave\">Sherif (1954)</a> fabrique un conflit avec un "
             "enjeu (un trophée, une canalisation). <a href=\"../references/experiences.html#tajfel-groupes\">Tajfel (1971)</a> "
             "montre qu'un tirage au sort suffit. Les deux se complètent : le conflit réaliste n'est pas obligatoire, "
             "l'identité non plus n'épuise pas les guerres. Le contact sans but commun (repas des Aigles et des Serpents) "
             "échoue ; le <em>but supraordonné</em> réussit mieux.</p>"
             "<p>Planche : <a href=\"../decouverte.html#planche-robbers-cave\">la caverne des voleurs</a>.</p>"),
            ("Festinger au-delà du 1 dollar",
             "<p>La <a href=\"../references/experiences.html#kitty-dissonance\">tâche ennuyeuse</a> est le protocole d'école. "
             "Festinger avait déjà vécu la dissonance dans une secte dont la fin du monde n'avait pas eu lieu : les plus "
             "engagés ont prêché davantage (<em>When Prophecy Fails</em>). La fiche "
             "<a href=\"../references/auteurs.html#festinger\">auteur</a> relie comparaison sociale et réseaux.</p>"),
            ("Hofling : Milgram à l'hôpital",
             "<p><a href=\"../references/experiences.html#hofling-infirmieres\">21 infirmières sur 22</a> préparent une "
             "dose impossible sur un simple coup de fil. Leurs collègues, interrogées, jurent qu'elles refuseraient. "
             "L'obéissance n'est pas un artefact de Yale. Les check-lists modernes existent pour cela.</p>"),
        ],
        "flashcards": [
            ("Quelle différence entre Sherif et Tajfel ?",
             "Sherif donne un enjeu matériel ; Tajfel obtient une discrimination avec un critère trivial, sans contact."),
            ("Pourquoi 1 $ change-t-il plus l'avis que 20 $ ?",
             "Justification insuffisante : sans bonne raison externe de mentir, on ajuste l'attitude."),
        ],
    },
    "05-developpement": {
        "sections": [
            ("Harlow, Bowlby, Ainsworth : une même phrase en trois laboratoires",
             "<p>Les <a href=\"../references/experiences.html#harlow-singes\">macaques de Harlow</a> s'accrochent au tissu, "
             "pas au lait. Bowlby en tire un besoin primaire d'attachement. Ainsworth le mesure dans la "
             "<a href=\"../references/experiences.html#situation-etrange\">situation étrange</a> : c'est le retour, pas la "
             "séparation, qui classe. Relier les trois évite de raconter Harlow comme une curiosité cruelle isolée.</p>"
             "<p>Éthique : ces isolements sont aujourd'hui interdits. Ils ont aussi nourri le refus de laisser un nourrisson "
             "« crier pour ne pas le gâter ». Erikson place au premier âge la crise <em>confiance vs méfiance</em> : même "
             "idée, autre vocabulaire. Mischel, plus tard, montrera que l'attente (marshmallow) dépend aussi de la "
             "<em>fiabilité</em> de l'adulte — donc encore de l'attachement.</p>"),
        ],
        "flashcards": [
            ("Que relie Harlow à Bowlby ?",
             "Le réconfort tactile est un besoin primaire, pas un sous-produit de l'alimentation."),
        ],
    },
    "07-emotions": {
        "sections": [
            ("S.M. : ce que l'amygdale n'est pas",
             "<p>La <a href=\"../references/cas.html#patient-sm\">patiente S.M.</a> approche serpents et maisons hantées, "
             "reconnaît mal la peur sur les visages, puis panique sous CO<sub>2</sub>. L'amygdale participe à la menace "
             "externe, pas à toute la peur. <strong>Un cas</strong> : on n'en fait pas l'organe unique de l'émotion. "
             "Relier <a href=\"../references/auteurs.html#damasio\">Damasio</a> (Iowa, marqueurs somatiques) et "
             "<a href=\"../references/experiences.html#patient-sm\">la fiche expérience</a>.</p>"),
        ],
    },
    "08-neurosciences": {
        "sections": [
            ("Cartes de l'espace : lieu, grille, H.M.",
             "<p><a href=\"../references/experiences.html#okeefe-cellules-lieu\">O'Keefe (1971)</a> : un neurone s'allume "
             "à un endroit. <a href=\"../references/experiences.html#moser-cellules-grille\">Les Moser (2005)</a> : une "
             "grille hexagonale dans l'entorhinal. Nobel 2014. Même famille que l'hippocampe de "
             "<a href=\"../references/cas.html#hm\">H.M.</a> et de <a href=\"../references/cas.html#patient-hm2\">Kent Cochrane</a> : "
             "se souvenir, se situer et imaginer demain partagent du tissu.</p>"),
            ("Bisiach, Babinski, locked-in : trois rapports à l'espace et au corps",
             "<p><a href=\"../references/experiences.html#heminegligence\">Bisiach</a> : la moitié gauche de la place du "
             "Dôme disparaît — puis l'autre moitié si l'on inverse le point de vue mental. "
             "<a href=\"../references/cas.html#babinski-anosognosie\">Babinski</a> : on peut ne pas savoir qu'on est "
             "paralysé. <a href=\"../references/cas.html#locked-in\">Locked-in</a> : on sait, on pense, on ne peut plus "
             "le montrer. Trois leçons contre « le corps dit toujours la vérité du soi ».</p>"),
            ("Penfield, Berger, Cajal, Amunts, Poldrack : cinq manières de cartographier",
             "<p>Cajal dessine le neurone. Penfield stimule le cortex éveillé. Berger pose des électrodes. Amunts refait "
             "Brodmann en haute résolution. Poldrack rappelle qu'un blob IRMf n'est pas une pensée. Les fiches auteurs "
             "sont dans les <a href=\"../references/auteurs.html\">grandes figures</a>.</p>"),
        ],
        "flashcards": [
            ("Que distingue une cellule de lieu d'une cellule de grille ?",
             "Le lieu s'allume à un endroit ; la grille s'allume en plusieurs nœuds hexagonaux : une métrique."),
        ],
    },
    "09-psychopathologie": {
        "sections": [
            ("Petit Albert : le conditionnement, et la dette éthique",
             "<p>Watson et Rayner (1920) montrent qu'une peur s'apprend. Ils n'éteignent pas cette peur. L'identité "
             "(Douglas Merritte ?) reste discutée ; la vulnérabilité neurologique possible aggrave le dossier. Voir "
             "<a href=\"../references/experiences.html#petit-albert\">l'expérience</a> et "
             "<a href=\"../references/cas.html#petit-albert-cas\">le cas</a>. C'est un pilier des TCC par exposition — "
             "et un pilier des comités d'éthique.</p>"),
            ("Rosenhan lu deux fois : 1973 et Cahalan 2019",
             "<p>L'article de <em>Science</em> a poussé le DSM-III vers des critères opérationnels. "
             "<a href=\"../references/experiences.html#rosenhan\">Cahalan</a> (<em>The Great Pretender</em>) n'a pas "
             "retrouvé les huit dossiers tels quels. On enseigne désormais le choc <em>et</em> l'enquête. Le problème "
             "de fidélité diagnostique n'a pas disparu parce que le messager est fragile.</p>"),
            ("Repères, pas un DSM de poche",
             "<p>Cette encyclopédie ajoute des tableaux souvent oubliés des manuels courts : "
             "<a href=\"../references/troubles.html#tourette\">Tourette</a> (la coprolalie est minoritaire), "
             "<a href=\"../references/troubles.html#accumulation\">accumulation</a>, "
             "<a href=\"../references/troubles.html#jeu-argent\">jeu d'argent</a>, "
             "<a href=\"../references/troubles.html#arfid\">ARFID</a> (restriction sans peur de grossir), "
             "<a href=\"../references/troubles.html#schizo-affectif\">schizo-affectif</a> (frontière à manier), "
             "<a href=\"../references/troubles.html#personnalite-antisociale\">personnalité antisociale</a> "
             "(à distinguer d'un acte et de la psychopathie de magazine), "
             "<a href=\"../references/troubles.html#tdah\">TDAH en trois présentations</a>, "
             "<a href=\"../references/troubles.html#dys\">dyscalculie et dyspraxie à côté de la dyslexie</a>.</p>"
             "<p>Reconnaître un signe n'est pas un diagnostic. En souffrance : un médecin, un psychologue ; urgence "
             "France : 3114 ou 15.</p>"),
        ],
    },
    "13-education": {
        "sections": [
            ("Pygmalion répliqué : attentes réelles, miracle non",
             "<p>Rosenthal et Jacobson (1968) : des élèves tirés au sort, dits « à fort potentiel », progressent un peu "
             "plus. Les réplications et les revues (Jussim notamment) disent : effet <strong>modeste</strong>, plus "
             "clair sur le comportement de l'enseignant que sur le QI, et les enseignants ont aussi souvent raison "
             "parce qu'ils ont déjà vu travailler l'élève. On garde la vigilance sur les étiquettes ; on lâche le mythe "
             "du professeur-magicien. Fiche : <a href=\"../references/experiences.html#pygmalion\">effet Pygmalion</a>.</p>"),
        ],
    },
    "14-sante": {
        "sections": [
            ("Moseley : quand le bistouri placebo suffit",
             "<p>En 2002, <a href=\"../references/experiences.html#effet-placebo\">Bruce Moseley</a> compare arthroscopie "
             "réelle et incisions simulées pour l'arthrose du genou : douleur et fonction ne diffèrent pas sur deux ans. "
             "Le rituel de soin est une intervention. Cela n'autorise pas à « tout soigner par du vent » : un placebo "
             " palie surtout des symptômes subjectifs.</p>"),
        ],
    },
    "18-langage": {
        "sections": [
            ("La N400 : le sens a une latence",
             "<p>Kutas et Hillyard (1980) : « je prends le café avec du ciment » évoque une négativité vers 400 ms. "
             "Ce n'est pas une faute de grammaire (plutôt P600) : c'est la surprise <em>sémantique</em>. La fiche "
             "n'habite plus seulement la science psychologique : "
             "<a href=\"../references/experiences.html#n400\">elle est ici</a>, à côté de Broca, Wernicke et "
             "<a href=\"../references/cas.html#patient-tan\">Leborgne en cas complet</a>.</p>"
             "<p>Compléter par le <a href=\"../references/experiences.html#p300\">P300</a> (pertinence) et la "
             "<a href=\"../references/experiences.html#mismatch-negativity\">MMN</a> (écart sensoriel automatique).</p>"),
        ],
        "flashcards": [
            ("Que distingue N400 et P600 ?",
             "N400 : incongruence de sens. P600 : souvent réanalyse syntaxique ou accord."),
        ],
    },
    "19-psychometrie": {
        "sections": [
            ("Ce que valent Rorschach et TAT",
             "<p>Deux projectifs, deux promesses, une même exigence : la validité se mesure, elle ne se décrète pas. "
             "Le <a href=\"../references/projectifs.html\">dossier TAT vs Rorschach</a> dit ce qui tient (quelques "
             "indices formels, parfois un entretien riche) et ce qui ne tient pas (symbolique libre, expertise "
             "judiciaire décorée de taches). À côté : <a href=\"../references/tests.html#mmpi\">MMPI comme monument "
             "critiqué</a>, <a href=\"../references/tests.html#big-five\">NEO-PI</a>, "
             "<a href=\"../references/tests.html#wcst\">WCST</a>, "
             "<a href=\"../references/tests.html#trail-making\">Trail Making</a>, "
             "<a href=\"../references/tests.html#rey-osterrieth\">figure de Rey</a>, "
             "<a href=\"../references/tests.html#hayling\">Hayling</a>, "
             "<a href=\"../references/tests.html#iowa-gambling\">Iowa</a>, "
             "<a href=\"../references/tests.html#wada\">Wada</a>.</p>"),
        ],
    },
    "01-fondamentaux": {
        "sections": [
            ("Le biais de survivant appliqué aux revues",
             "<p>On n'étudie que les avions qui rentrent. En science, on n'enseigne souvent que les articles qui ont "
             "survécu au tiroir : effets positifs, cas célèbres, belles histoires. Voir "
             "<a href=\"../references/biais.html#survivants-science\">biais de survivant en science</a>, "
             "Rosenhan + Cahalan, Pygmalion répliqué, ego depletion. La réforme (préenregistrement, rapports enregistrés) "
             "est une parade collective, pas une vertu individuelle.</p>"),
        ],
    },
    "06-personnalite": {
        "sections": [
            ("Mischel, Baumeister, le Big Five : traits, situations, mythes de la volonté",
             "<p><a href=\"../references/auteurs.html#mischel\">Mischel</a> plafonne le trait à ~0,30 pour un acte "
             "précis. <a href=\"../references/auteurs.html#baumeister\">Baumeister</a> a popularisé une volonté-muscle "
             "dont les grandes réplications ont réduit la taille. Le "
             "<a href=\"../references/tests.html#big-five\">NEO-PI</a> reste le meilleur portrait <em>moyen</em> — "
             "pas un destin. Relier Nolen-Hoeksema (rumination) pour la vulnérabilité dépressive, sans en faire un "
             "trait de caractère moral.</p>"),
        ],
    },
}
