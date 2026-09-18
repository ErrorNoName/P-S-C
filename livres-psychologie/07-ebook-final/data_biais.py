# -*- coding: utf-8 -*-
"""Catalogue des biais cognitifs, heuristiques et effets psychologiques."""

# (id, nom, famille, definition, exemple, parade)
BIAIS = [
    ("confirmation", "Biais de confirmation", "Traitement de l'information",
     "Tendance à chercher, retenir et interpréter les informations qui confirment nos croyances, en négligeant celles qui les contredisent.",
     "Après avoir choisi une voiture, on ne lit plus que les avis positifs la concernant et on écarte les essais critiques comme « mal faits ».",
     "Chercher activement l'argument le plus fort contre sa propre position et se demander : « qu'est-ce qui me ferait changer d'avis ? »"),

    ("ancrage", "Effet d'ancrage", "Jugement numérique",
     "Le premier chiffre rencontré sert de point de départ et influence toutes les estimations suivantes, même s'il est arbitraire.",
     "Un prix barré de 200 € fait paraître 120 € avantageux, indépendamment de la valeur réelle du produit.",
     "Estimer la valeur avant de voir le prix affiché, et chercher des points de comparaison indépendants."),

    ("disponibilite", "Heuristique de disponibilité", "Estimation de fréquence",
     "Nous jugeons la probabilité d'un événement à la facilité avec laquelle des exemples nous viennent à l'esprit.",
     "On surestime massivement le risque d'accident d'avion après un crash médiatisé, alors que la voiture est bien plus dangereuse.",
     "Chercher les statistiques réelles plutôt que de se fier à l'impression laissée par les récits marquants."),

    ("representativite", "Heuristique de représentativité", "Estimation de probabilité",
     "Nous jugeons la probabilité qu'un cas appartienne à une catégorie selon sa ressemblance au stéréotype, en ignorant les fréquences de base.",
     "Décrit comme timide et méticuleux, quelqu'un est spontanément jugé bibliothécaire plutôt que commercial — alors que les commerciaux sont bien plus nombreux.",
     "Toujours demander : combien y a-t-il de personnes dans chaque catégorie au départ ?"),

    ("survivants", "Biais des survivants", "Sélection des données",
     "On analyse uniquement les cas qui ont « survécu » à un filtre, en oubliant ceux qui ont disparu de l'échantillon.",
     "Étudier les habitudes des entrepreneurs à succès sans examiner ceux qui ont eu les mêmes habitudes et ont échoué.",
     "Se demander systématiquement : où sont les données manquantes ? Qui n'apparaît pas dans cet échantillon ?"),

    ("dunning-kruger", "Effet Dunning-Kruger", "Métacognition",
     "Les personnes les moins compétentes dans un domaine surestiment leur niveau, car il faut de la compétence pour évaluer sa propre incompétence.",
     "Après deux articles lus sur un sujet, se sentir capable de contredire des spécialistes de vingt ans d'expérience.",
     "Chercher un retour extérieur mesurable et se rappeler que la sensation de maîtrise n'est pas une preuve de maîtrise."),

    ("attribution-fondamentale", "Erreur fondamentale d'attribution", "Cognition sociale",
     "Nous expliquons le comportement d'autrui par sa personnalité et le nôtre par les circonstances.",
     "Un automobiliste qui nous double est « un imbécile » ; quand nous doublons, c'est parce que nous sommes en retard pour une raison valable.",
     "Se demander quelle situation pourrait expliquer ce comportement si nous étions à la place de l'autre."),

    ("retrospective", "Biais rétrospectif", "Mémoire et jugement",
     "Une fois l'issue connue, elle nous semble avoir été prévisible depuis le début (« je le savais »).",
     "Après un résultat électoral, chacun explique qu'il était évident, alors que les prédictions d'avant-scrutin étaient partagées.",
     "Écrire ses prédictions avant l'événement et les relire ensuite, sans les réviser de mémoire."),

    ("halo", "Effet de halo", "Formation d'impression",
     "Une caractéristique positive saillante colore l'évaluation de toutes les autres qualités de la personne.",
     "Une personne séduisante est spontanément jugée plus intelligente, plus honnête et plus compétente.",
     "Évaluer chaque critère séparément, dans un ordre imposé, idéalement à l'aveugle."),

    ("aversion-perte", "Aversion à la perte", "Décision et risque",
     "Une perte fait environ deux fois plus mal qu'un gain équivalent ne fait plaisir.",
     "On conserve une action qui s'effondre pour ne pas « acter » la perte, alors qu'on vendrait sans hésiter à gain égal.",
     "Reformuler la décision comme si l'on partait de zéro : achèterais-je cet actif aujourd'hui à ce prix ?"),

    ("cout-irrecuperables", "Erreur des coûts irrécupérables", "Décision",
     "Nous persistons dans un choix perdant à cause de ce qui a déjà été investi et ne sera pas récupéré.",
     "Finir un film ennuyeux « parce qu'on a payé la place » ou poursuivre un projet évidemment voué à l'échec.",
     "Ne considérer que les coûts et bénéfices futurs : le passé est passé quoi qu'on fasse."),

    ("statu-quo", "Biais de statu quo", "Décision",
     "Préférence irrationnelle pour l'état actuel des choses, même quand une alternative est clairement meilleure.",
     "Conserver le même contrat d'assurance pendant quinze ans sans jamais comparer les offres.",
     "Programmer des révisions périodiques et imaginer que l'on part de zéro : choisirais-je encore cette option ?"),

    ("dotation", "Effet de dotation", "Évaluation",
     "Nous valorisons davantage un objet du simple fait qu'il nous appartient.",
     "Des étudiants à qui l'on offre une tasse demandent en moyenne deux fois plus pour la vendre que ce que d'autres acceptent de payer pour l'acquérir.",
     "Demander à une personne extérieure ce qu'elle paierait réellement pour cet objet."),

    ("optimisme", "Biais d'optimisme", "Prédiction",
     "Nous nous croyons moins exposés que la moyenne aux événements négatifs et plus susceptibles de connaître les événements positifs.",
     "80 % des conducteurs s'estiment meilleurs que la moyenne, ce qui est arithmétiquement impossible.",
     "Consulter les statistiques de base de la population concernée et raisonner comme un observateur extérieur."),

    ("planification", "Illusion de planification", "Prédiction",
     "Nous sous-estimons systématiquement le temps, le coût et les risques d'un projet, même en connaissant nos retards passés.",
     "L'Opéra de Sydney, prévu pour 4 ans et 7 millions de dollars, a demandé 14 ans et 102 millions.",
     "Utiliser la prévision par référence externe : combien de temps ont pris des projets comparables, en moyenne ?"),

    ("negativite", "Biais de négativité", "Attention et mémoire",
     "Les informations négatives captent plus l'attention, sont mieux mémorisées et pèsent plus lourd que les positives.",
     "Un seul commentaire critique efface l'effet de dix retours élogieux reçus le même jour.",
     "Pondérer explicitement les retours reçus et noter aussi les signaux positifs, qui s'effacent naturellement."),

    ("faux-consensus", "Effet de faux consensus", "Cognition sociale",
     "Nous surestimons la proportion de gens qui partagent nos opinions, nos goûts et nos comportements.",
     "Être persuadé que « tout le monde pense la même chose » sur un sujet clivant, parce que notre entourage le pense.",
     "Sortir de son environnement informationnel et consulter des enquêtes représentatives."),

    ("angle-mort", "Biais de l'angle mort", "Métacognition",
     "Nous repérons facilement les biais chez les autres, beaucoup moins chez nous-mêmes.",
     "Reconnaître que la publicité influence les gens, tout en se croyant personnellement immunisé.",
     "Partir du principe qu'on est concerné par défaut, et faire appel à un regard extérieur critique."),

    ("autorite", "Biais d'autorité", "Influence sociale",
     "Nous accordons une crédibilité excessive à une figure d'autorité, même hors de son domaine de compétence.",
     "Un prix Nobel de physique s'exprimant sur la nutrition est écouté comme un expert du sujet.",
     "Vérifier que l'expertise porte précisément sur la question posée, et chercher le consensus du domaine."),

    ("conformisme", "Biais de conformisme", "Influence sociale",
     "Nous alignons nos jugements sur ceux du groupe, parfois contre l'évidence perceptive.",
     "Dans une réunion, personne n'ose objecter alors que plusieurs participants ont des doutes en privé.",
     "Faire écrire les avis avant la discussion collective, et désigner un avocat du diable officiel."),

    ("groupthink", "Pensée de groupe", "Dynamique de groupe",
     "Un groupe cohésif privilégie l'unanimité et l'harmonie au détriment de l'examen réaliste des options.",
     "L'analyse rétrospective de la baie des Cochons ou de l'explosion de Challenger : les doutes existaient mais n'ont pas été exprimés.",
     "Solliciter explicitement les objections, consulter des experts externes, permettre le vote anonyme."),

    ("bulle-filtre", "Bulle de filtres", "Environnement informationnel",
     "Les algorithmes nous exposent surtout à des contenus conformes à nos préférences, ce qui renforce nos convictions.",
     "Deux personnes tapant la même requête reçoivent des résultats différents, adaptés à leur historique.",
     "Diversifier volontairement ses sources, s'abonner à des points de vue contradictoires argumentés."),

    ("recence", "Effet de récence", "Mémoire",
     "Les derniers éléments d'une série sont mieux rappelés que ceux du milieu.",
     "Lors d'un entretien, le dernier candidat de la journée bénéficie souvent d'une évaluation plus favorable.",
     "Étaler les évaluations dans le temps et utiliser des grilles de notation remplies immédiatement."),

    ("primaute", "Effet de primauté", "Mémoire et impression",
     "Les premières informations reçues structurent durablement l'interprétation des suivantes.",
     "Décrit d'abord comme « intelligent, travailleur, impulsif », quelqu'un est mieux jugé que décrit dans l'ordre inverse.",
     "Prendre connaissance des éléments dans un ordre aléatoire et réévaluer après avoir tout lu."),

    ("zeigarnik", "Effet Zeigarnik", "Mémoire",
     "Les tâches inachevées restent mieux en mémoire que celles qui ont été terminées.",
     "Les séries télévisées terminent chaque épisode sur un cliffhanger pour exploiter cet effet.",
     "Utiliser l'effet à son avantage : commencer une tâche cinq minutes suffit souvent à vaincre la procrastination."),

    ("simple-exposition", "Effet de simple exposition", "Préférence",
     "Plus nous sommes exposés à un stimulus, plus nous l'apprécions, même sans en avoir conscience.",
     "Une chanson d'abord agaçante finit par plaire à force d'être diffusée.",
     "Distinguer familiarité et qualité : ce que je préfère, est-ce parce que c'est bon ou parce que je l'ai déjà vu ?"),

    ("illusion-controle", "Illusion de contrôle", "Perception de causalité",
     "Nous surestimons notre capacité à influencer des événements largement aléatoires.",
     "Souffler sur les dés, choisir soi-même ses numéros de loto, croire qu'un rituel améliore ses chances.",
     "Identifier précisément ce qui dépend de nous et ce qui n'en dépend pas, puis n'agir que sur le premier."),

    ("apophenie", "Apophénie et paréidolie", "Perception",
     "Tendance à percevoir des structures, des visages ou des liens significatifs dans des données aléatoires.",
     "Voir un visage dans une prise électrique, ou une « tendance » dans une série de tirages purement aléatoires.",
     "Tester si le motif résiste à de nouvelles données indépendantes."),

    ("joueur", "Sophisme du joueur", "Probabilités",
     "Croire qu'un événement aléatoire est « dû » parce qu'il n'est pas survenu depuis longtemps.",
     "Après dix rouges consécutives à la roulette, parier sur le noir « qui doit bien tomber ».",
     "Se rappeler que les événements indépendants n'ont aucune mémoire : la probabilité reste identique."),

    ("regression-moyenne", "Méconnaissance de la régression vers la moyenne", "Statistiques intuitives",
     "Après une performance extrême, la suivante est statistiquement plus proche de la moyenne — ce qu'on attribue à tort à une cause.",
     "Un pilote félicité après un excellent vol fait moins bien ensuite : l'instructeur conclut que les éloges nuisent.",
     "Comparer à la moyenne habituelle plutôt qu'à la performance exceptionnelle précédente."),

    ("barnum", "Effet Barnum (ou Forer)", "Évaluation de soi",
     "Nous acceptons comme personnellement pertinentes des descriptions vagues qui s'appliquent à presque tout le monde.",
     "« Vous avez besoin d'être aimé, tout en étant parfois critique envers vous-même » : horoscopes et tests de personnalité douteux.",
     "Vérifier si l'énoncé serait accepté par quelqu'un ayant obtenu un profil opposé."),

    ("pygmalion-biais", "Effet Pygmalion et effet Golem", "Attentes",
     "Les attentes d'autrui à notre égard influencent nos performances, à la hausse comme à la baisse.",
     "Un élève désigné comme prometteur reçoit plus d'attention et de feedback, et progresse davantage.",
     "Évaluer sur des critères objectifs et se méfier des étiquettes précoces."),

    ("stereotype-menace", "Menace du stéréotype", "Performance et identité",
     "La conscience d'un stéréotype négatif visant son groupe dégrade la performance dans le domaine concerné.",
     "Rappeler leur genre à des étudiantes avant un test de mathématiques abaisse leurs résultats.",
     "Neutraliser les rappels identitaires avant l'évaluation, présenter la capacité comme développable, exposer à des contre-modèles."),

    ("effet-cadrage", "Effet de cadrage", "Décision",
     "La façon de formuler une option — en gains ou en pertes — modifie le choix, à information identique.",
     "Une opération « avec 90 % de survie » est choisie plus souvent qu'une opération « avec 10 % de mortalité ».",
     "Reformuler systématiquement l'option dans l'autre sens avant de décider."),

    ("statu-autorite", "Effet de la première offre", "Négociation",
     "Celui qui annonce le premier chiffre fixe le terrain de la négociation entière.",
     "Le salaire final d'une embauche reste fortement corrélé à la première fourchette évoquée.",
     "Préparer sa propre fourchette étayée avant la discussion et ne pas se laisser enfermer dans celle de l'autre."),

    ("reciprocite", "Norme de réciprocité", "Influence sociale",
     "Recevoir quelque chose crée une obligation implicite de rendre, même non sollicitée et disproportionnée.",
     "Les échantillons gratuits, les cadeaux d'entreprise et les « petits services » des représentants commerciaux.",
     "Identifier le cadeau comme technique d'influence et dissocier la décision de la dette ressentie."),

    ("rarete", "Effet de rareté", "Influence sociale",
     "Un bien perçu comme rare ou d'accès limité devient plus désirable.",
     "« Plus que 2 en stock », « offre valable 24 h », files d'attente organisées devant les boutiques.",
     "Se demander si l'on voudrait l'objet au même prix s'il était disponible en quantité illimitée."),

    ("engagement", "Escalade d'engagement", "Cohérence",
     "Après un premier engagement, même minime, nous acceptons plus facilement des demandes croissantes.",
     "La technique du « pied dans la porte » : une petite signature amène à une adhésion complète.",
     "Réévaluer chaque demande indépendamment, comme si c'était la première."),

    ("amorcage", "Amorçage (priming)", "Traitement implicite",
     "Une exposition préalable à un stimulus influence la réponse à un stimulus ultérieur, sans conscience du lien.",
     "Après des mots liés à la vieillesse, les participants marchent légèrement plus lentement — effet célèbre mais dont la réplication est contestée.",
     "Prudence : de nombreux effets d'amorçage social n'ont pas résisté à la crise de la réplication."),

    ("ikea", "Effet IKEA", "Évaluation",
     "Nous surévaluons ce que nous avons contribué à fabriquer nous-mêmes.",
     "Un meuble monté soi-même est jugé plus beau et plus précieux qu'un meuble identique livré assemblé.",
     "Demander l'avis de quelqu'un qui n'a pas participé à la création."),

    ("bizarrerie", "Effet de bizarrerie", "Mémoire",
     "L'information inhabituelle ou absurde est mieux retenue que l'information banale.",
     "Les techniques de mémorisation recommandent d'associer un chiffre à une image incongrue et vivante.",
     "Exploiter délibérément l'effet pour apprendre, mais vérifier que le contenu réel est bien mémorisé."),

    ("generation", "Effet de génération", "Apprentissage",
     "On retient mieux une information qu'on a produite soi-même que celle qu'on a simplement lue.",
     "Compléter « la capitale du Japon est T___ » est plus efficace que lire la phrase complète.",
     "Transformer sa révision en questions à se poser plutôt qu'en relecture passive."),

    ("test", "Effet de test", "Apprentissage",
     "Se tester sur un contenu améliore beaucoup plus la rétention que le relire, même sans correction immédiate.",
     "Deux groupes révisent le même texte : celui qui se teste retient jusqu'à 50 % de plus à une semaine.",
     "Remplacer systématiquement la relecture par des questions, flashcards ou rappel libre."),

    ("espacement", "Effet d'espacement", "Apprentissage",
     "Des sessions d'apprentissage réparties dans le temps produisent une rétention bien supérieure à une session massée.",
     "Quatre fois trente minutes sur quatre jours battent largement deux heures d'affilée la veille.",
     "Planifier des révisions à intervalles croissants (1 jour, 3 jours, 1 semaine, 1 mois)."),

    ("fluence", "Illusion de fluence", "Métacognition",
     "Un contenu facile à lire nous donne l'impression fausse de l'avoir maîtrisé.",
     "Un cours surligné et relu paraît acquis, jusqu'à ce que l'examen révèle le contraire.",
     "Tester le rappel sans support : si l'on ne peut pas expliquer sans regarder, ce n'est pas acquis."),

    ("charge-cognitive", "Surcharge cognitive", "Traitement de l'information",
     "Au-delà de quelques éléments simultanés, la mémoire de travail sature et la performance s'effondre.",
     "Un diaporama dense lu à voix haute empêche de comprendre : la lecture et l'écoute entrent en concurrence.",
     "Découper l'information en unités, supprimer le superflu, éviter la redondance texte/parole simultanée."),

    ("choix-paradoxe", "Paradoxe du choix", "Décision",
     "Trop d'options augmente l'hésitation, le regret et la probabilité de ne rien choisir.",
     "Un étal de 24 confitures attire plus de monde mais génère dix fois moins d'achats qu'un étal de 6.",
     "Présélectionner un nombre restreint d'options selon des critères définis à l'avance."),

    ("actualisation", "Actualisation hyperbolique", "Décision temporelle",
     "Nous dévaluons fortement les récompenses futures par rapport aux récompenses immédiates, de façon incohérente dans le temps.",
     "Préférer 100 € aujourd'hui à 110 € demain, mais préférer 110 € dans 31 jours à 100 € dans 30 jours.",
     "Automatiser les décisions de long terme (épargne, rendez-vous, engagements) pour ne pas avoir à les reprendre."),

    ("omission", "Biais d'omission", "Éthique et décision",
     "Nous jugeons une action nuisible plus grave qu'une inaction aux conséquences identiques, voire pires.",
     "Refuser un vaccin par peur d'un effet indésirable rare, tout en acceptant un risque de maladie bien supérieur.",
     "Comparer explicitement les risques des deux branches, agir et ne pas agir."),

    ("proportion", "Insensibilité à la taille de l'échantillon", "Statistiques intuitives",
     "Nous accordons autant de crédit à un résultat issu d'un petit échantillon qu'à celui d'un grand.",
     "« Trois de mes amis ont essayé, ça marche » pèse autant qu'une étude sur 2 000 personnes.",
     "Vérifier systématiquement la taille de l'échantillon et l'intervalle de confiance."),

    ("just-world", "Croyance en un monde juste", "Cognition sociale",
     "Besoin de croire que chacun obtient ce qu'il mérite, ce qui conduit à blâmer les victimes.",
     "Chercher ce que la victime d'une agression « a fait » pour que cela lui arrive.",
     "Nommer le mécanisme : la recherche d'une explication rassurante ne doit pas se transformer en jugement moral."),

    ("effet-spectateur", "Diffusion de la responsabilité", "Comportement collectif",
     "Plus il y a de personnes présentes, moins chacune se sent responsable d'agir.",
     "Un malaise dans une gare bondée peut rester sans intervention pendant de longues minutes.",
     "Désigner nommément une personne : « vous, avec le sac rouge, appelez le 15 »."),

    ("attribution-succes", "Biais d'auto-complaisance", "Estime de soi",
     "Nous attribuons nos succès à nos qualités et nos échecs aux circonstances extérieures.",
     "Un bon résultat prouve mon travail ; un mauvais résultat prouve que le sujet était injuste.",
     "Tenir un journal de décisions avec les raisons anticipées, relu après coup."),

    ("effet-autruche", "Effet autruche", "Évitement informationnel",
     "Nous évitons activement les informations négatives mais utiles.",
     "Ne pas ouvrir ses relevés bancaires en période de difficultés financières, ou repousser un résultat d'analyse.",
     "Planifier la confrontation à l'information à un moment défini, avec un plan d'action associé."),

    ("effet-contraste", "Effet de contraste", "Perception et jugement",
     "Un stimulus est évalué par rapport à ce qui le précède immédiatement plutôt que dans l'absolu.",
     "Un appartement correct paraît excellent après la visite de deux logements volontairement médiocres.",
     "Évaluer chaque option sur une grille de critères fixe, indépendamment de l'ordre de présentation."),

    ("moral-licensing", "Permis moral", "Cohérence morale",
     "Après un comportement vertueux, nous nous autorisons plus facilement un écart.",
     "Faire un don caritatif puis se montrer moins scrupuleux dans une décision professionnelle.",
     "Considérer les actes séparément et ne pas tenir de « comptabilité morale » implicite."),

    ("effet-dodo", "Verdict du Dodo", "Psychothérapie",
     "Constat selon lequel des psychothérapies très différentes obtiennent des résultats globalement comparables.",
     "TCC, thérapie psychodynamique brève et thérapie humaniste donnent des effets proches sur la dépression modérée.",
     "Nuance importante : certaines approches sont clairement supérieures pour des troubles précis (EPR pour le TOC, exposition pour les phobies)."),

    ("effet-nocebo", "Effet nocebo", "Attentes et santé",
     "L'attente d'un effet négatif produit réellement des symptômes désagréables.",
     "La lecture détaillée de la notice augmente significativement la survenue des effets indésirables rapportés.",
     "Informer de façon équilibrée, en mentionnant aussi la fréquence des effets chez les patients sous placebo."),
]
