# -*- coding: utf-8 -*-
"""
Schémas et planches illustrant les fiches de catégorie.

Chaque entrée : (fichier, légende courte, commentaire pédagogique).
Toutes les images proviennent de Wikimedia Commons et sont dans le domaine
public ou sous licence libre.
"""

SCHEMAS = {
    "02-histoire": [
        ("phrenologie.jpg", "Planche de phrénologie (XIXe siècle)",
         "La phrénologie de Gall prétendait lire le caractère dans les bosses du crâne. Entièrement fausse, "
         "elle a pourtant laissé une idée juste et féconde : les fonctions mentales ne sont pas réparties "
         "uniformément dans le cerveau, elles sont localisées. L'erreur portait sur la méthode, pas sur "
         "l'intuition de départ."),
        ("portrait-fechner.jpg", "Gustav Fechner (1801-1887)",
         "En établissant que la sensation croît comme le logarithme du stimulus, Fechner démontre qu'un "
         "phénomène mental peut être mesuré. C'est l'acte de naissance de la psychologie expérimentale, "
         "vingt ans avant le laboratoire de Wundt."),
    ],
    "03-cognitive": [
        ("courbe-oubli-ebbinghaus.svg", "La courbe de l'oubli d'Ebbinghaus (1885)",
         "Ebbinghaus a mémorisé des milliers de syllabes sans signification puis mesuré ce qu'il en restait "
         "après quelques minutes, heures et jours. La chute est brutale au début puis se stabilise : on perd "
         "l'essentiel dans les vingt-quatre premières heures. C'est précisément pour cela que la révision "
         "espacée fonctionne — elle réinitialise la courbe avant l'effondrement."),
        ("illusion-muller-lyer.svg", "L'illusion de Müller-Lyer",
         "Les deux segments ont exactement la même longueur. Savoir qu'ils sont égaux ne suffit pas à les "
         "voir égaux : la perception est un module largement imperméable au raisonnement. Fait notable, "
         "l'illusion est beaucoup plus faible chez les populations qui ne vivent pas dans un environnement "
         "d'angles droits."),
        ("cube-necker.svg", "Le cube de Necker",
         "Une même image, deux interprétations tridimensionnelles qui alternent spontanément. La perception "
         "n'est donc pas une copie du monde : c'est une hypothèse que le cerveau construit, et qu'il révise "
         "quand les données sont ambiguës."),
        ("vase-rubin.svg", "Le vase de Rubin",
         "Vase ou deux visages ? Cette figure de la Gestalt montre la séparation figure/fond : impossible de "
         "voir les deux à la fois, car le système visuel doit décider ce qui est objet et ce qui est arrière-plan."),
        ("triangle-kanizsa.svg", "Le triangle de Kanizsa",
         "On perçoit nettement un triangle blanc qui n'existe pas : ses contours sont entièrement inférés. "
         "Le cerveau complète activement l'information manquante, ce qui est très efficace… et explique aussi "
         "pourquoi la mémoire des témoins comble les trous sans le signaler."),
        ("illusion-ebbinghaus.svg", "L'illusion d'Ebbinghaus",
         "Les deux disques centraux sont identiques. Le jugement de taille est relatif au contexte, jamais "
         "absolu — un principe qu'on retrouve dans l'effet d'ancrage en économie comportementale."),
    ],
    "05-developpement": [
        ("portrait-piaget.jpg", "Jean Piaget (1896-1980)",
         "Piaget observe ses propres enfants et découvre que leurs erreurs ne sont pas aléatoires : elles "
         "suivent une logique cohérente, propre à chaque stade. L'enfant n'est pas un adulte incomplet, "
         "c'est un penseur avec d'autres règles."),
        ("portrait-vygotski.jpg", "Lev Vygotski (1896-1934)",
         "Contre Piaget, Vygotski soutient que le développement cognitif est d'abord social : l'enfant "
         "apprend avec un adulte ce qu'il saura ensuite faire seul. C'est la zone proximale de développement, "
         "base théorique du tutorat et de l'étayage pédagogique."),
    ],
    "06-personnalite": [
        ("courbe-gauss.svg", "La distribution normale",
         "La plupart des traits psychologiques se répartissent selon cette courbe en cloche : une majorité "
         "de scores moyens, des extrêmes rares et symétriques. C'est elle qui permet de dire qu'un QI de 130 "
         "concerne environ 2 % de la population, et de donner un sens à un écart-type."),
        ("rorschach-planche-1.jpg", "Planche I du test de Rorschach (1921)",
         "Le sujet dit ce qu'il voit dans une tache symétrique ambiguë. La validité des interprétations "
         "cliniques du Rorschach est très discutée : seuls quelques indices, cotés avec le système Exner, "
         "atteignent une fiabilité acceptable. La planche reste un objet culturel emblématique."),
        ("rorschach-planche-2.jpg", "Planche II du test de Rorschach",
         "L'ajout de la couleur rouge est censé solliciter la réactivité émotionnelle. C'est un bon exemple "
         "d'hypothèse séduisante dont la vérification empirique s'est révélée beaucoup plus fragile que prévu."),
    ],
    "07-emotions": [
        ("roue-emotions-plutchik.svg", "La roue des émotions de Plutchik",
         "Plutchik propose huit émotions primaires disposées en couples opposés, avec des degrés d'intensité "
         "du centre vers la périphérie et des émotions composées entre les secteurs. Ce n'est pas une carte "
         "neuroanatomique, mais un excellent outil de vocabulaire pour nommer finement ce que l'on ressent."),
        ("loi-yerkes-dodson.svg", "La loi de Yerkes-Dodson",
         "La performance suit une courbe en U inversé par rapport à l'activation : trop peu de stress endort, "
         "trop de stress désorganise, un niveau intermédiaire est optimal. Le sommet se déplace vers la gauche "
         "quand la tâche est complexe — d'où l'effondrement des performances difficiles sous forte pression."),
        ("pyramide-maslow.svg", "La pyramide des besoins de Maslow",
         "Célèbre et largement invalidée sous sa forme stricte : rien ne prouve qu'un besoin doive être "
         "satisfait avant le suivant, et la représentation pyramidale n'est même pas de Maslow. Elle reste "
         "utile comme inventaire des grandes catégories de motivations humaines."),
        ("systeme-limbique.png", "Le système limbique",
         "Amygdale, hippocampe, hypothalamus, cortex cingulaire : le réseau historiquement associé aux "
         "émotions. La notion de « cerveau émotionnel » séparé du « cerveau rationnel » est aujourd'hui "
         "abandonnée — les mêmes structures participent à la décision, à la mémoire et à l'émotion."),
    ],
    "08-neurosciences": [
        ("neurone.svg", "Structure d'un neurone",
         "Dendrites (réception), corps cellulaire (intégration), axone (transmission), terminaisons "
         "synaptiques (émission). Environ 86 milliards de ces cellules, chacune connectée à des milliers "
         "d'autres : ce n'est pas le nombre de neurones qui fait la puissance du cerveau, c'est le nombre "
         "de connexions."),
        ("synapse-chimique.jpg", "La synapse chimique",
         "Le signal électrique devient chimique : des neurotransmetteurs traversent la fente synaptique et "
         "se fixent sur des récepteurs. C'est à cet endroit précis qu'agissent la quasi-totalité des "
         "psychotropes, des antidépresseurs aux anxiolytiques."),
        ("cerveau-lobes-fr.svg", "Les quatre lobes du cortex",
         "Frontal (décision, inhibition, langage produit), pariétal (espace, toucher), temporal (audition, "
         "mémoire, compréhension du langage), occipital (vision). Cette carte est une simplification utile : "
         "presque toute fonction complexe mobilise plusieurs lobes en réseau."),
        ("aires-brodmann.png", "Les aires de Brodmann",
         "Brodmann a découpé le cortex en 52 aires selon l'organisation de leurs couches cellulaires, en 1909, "
         "bien avant l'imagerie. Un siècle plus tard, ces frontières anatomiques correspondent remarquablement "
         "aux frontières fonctionnelles observées en IRM."),
        ("homonculus-sensoriel.jpg", "L'homoncule sensoriel de Penfield",
         "La surface corticale allouée à chaque partie du corps est proportionnelle à sa finesse sensorielle, "
         "pas à sa taille réelle : d'où ces mains et ces lèvres démesurées. C'est la carte du corps telle que "
         "le cerveau la dessine."),
        ("hippocampe.png", "L'hippocampe",
         "Structure indispensable à la formation de nouveaux souvenirs explicites. Son ablation bilatérale "
         "chez le patient H.M. en 1953 a produit une amnésie antérograde totale — tout en préservant "
         "l'apprentissage de nouvelles habiletés motrices, révélant ainsi l'existence de mémoires multiples."),
        ("corps-calleux.png", "Le corps calleux",
         "Les 200 millions de fibres qui relient les deux hémisphères. Sa section chirurgicale, pratiquée "
         "contre des épilepsies graves, a permis les expériences de Sperry sur le « cerveau divisé » et "
         "nourri le mythe — largement faux — du « cerveau gauche rationnel » et du « cerveau droit créatif »."),
        ("phineas-gage.jpg", "Phineas Gage et sa barre à mine (1848)",
         "Une barre de fer traverse son lobe frontal ; il survit, marche et parle, mais sa personnalité et sa "
         "capacité à planifier sont durablement altérées. Premier cas documenté reliant le cortex préfrontal "
         "au contrôle de soi et à la prise de décision sociale."),
        ("portrait-broca.jpg", "Paul Broca (1824-1880)",
         "En 1861, l'autopsie de son patient « Tan » — qui ne pouvait prononcer que cette syllabe — révèle "
         "une lésion frontale gauche. Première démonstration anatomique d'une fonction mentale localisée."),
        ("portrait-wernicke.jpg", "Carl Wernicke (1848-1905)",
         "Décrit l'aphasie opposée à celle de Broca : le patient parle avec fluidité mais ne comprend plus et "
         "produit un discours vide de sens. Deux aires, deux déficits, un même réseau du langage."),
    ],
    "09-psychopathologie": [
        ("portrait-pinel.jpg", "Philippe Pinel (1745-1826)",
         "Figure du « traitement moral » : écouter les patients, tenir des observations écrites, remplacer la "
         "contention par une relation. Le geste fondateur n'est pas tant d'avoir ôté les chaînes que d'avoir "
         "considéré la folie comme un objet d'observation clinique."),
        ("portrait-charcot.jpg", "Jean-Martin Charcot (1825-1893)",
         "Ses leçons du mardi à la Salpêtrière attirent toute l'Europe — Freud y assiste. En étudiant "
         "l'hystérie sous hypnose, Charcot impose l'idée qu'un symptôme physique peut avoir une cause "
         "psychique, même si sa théorie particulière a été abandonnée."),
    ],
    "10-therapies": [
        ("conditionnement-pavlov.svg", "Le conditionnement classique",
         "Stimulus neutre + stimulus inconditionnel répétés ensemble → le stimulus neutre déclenche seul la "
         "réponse. Ce schéma explique la formation de nombreuses phobies, et sa version inverse — l'exposition "
         "prolongée sans conséquence négative — constitue le traitement le plus efficace dont on dispose."),
        ("boite-skinner.png", "La boîte de Skinner",
         "Un levier, une mangeoire, un enregistrement automatique des réponses. Skinner y établit les lois du "
         "conditionnement opérant, dont le renforcement à ratio variable — le mécanisme exact des machines à "
         "sous et des notifications d'applications."),
        ("portrait-rogers.jpg", "Carl Rogers (1902-1987)",
         "Empathie, congruence, regard positif inconditionnel : Rogers déplace le centre de la thérapie du "
         "savoir du praticien vers la relation. Les recherches actuelles lui donnent largement raison — "
         "l'alliance thérapeutique prédit mieux le résultat que l'orientation théorique."),
    ],
    "19-psychometrie": [
        ("courbe-gauss.svg", "Distribution normale et étalonnage",
         "Un score brut ne veut rien dire tant qu'on ne le situe pas dans une population de référence. "
         "L'étalonnage convertit ce score en position relative : 68 % des personnes se situent à moins d'un "
         "écart-type de la moyenne, 95 % à moins de deux."),
        ("portrait-galton.jpg", "Francis Galton (1822-1911)",
         "Invente la corrélation, la régression vers la moyenne et les premiers tests de capacités. Il est "
         "aussi le fondateur de l'eugénisme : un rappel que les outils statistiques d'une discipline peuvent "
         "naître de projets politiques qu'elle doit ensuite affronter."),
        ("portrait-binet.jpg", "Alfred Binet (1857-1911)",
         "Conçoit en 1905 la première échelle métrique de l'intelligence, pour identifier les élèves ayant "
         "besoin d'un soutien — et non pour les classer. Il mettait explicitement en garde contre l'idée "
         "d'une intelligence fixe et mesurable par un nombre unique."),
    ],
    "01-fondamentaux": [
        ("portrait-wundt.jpg", "Wilhelm Wundt (1832-1920)",
         "Fonde à Leipzig en 1879 le premier laboratoire de psychologie expérimentale. Sa conviction "
         "fondatrice : les processus mentaux élémentaires peuvent être mesurés avec la rigueur de la "
         "physiologie, chronomètre à l'appui."),
        ("portrait-helmholtz.jpg", "Hermann von Helmholtz (1821-1894)",
         "Mesure la vitesse de l'influx nerveux — environ 30 mètres par seconde — et ruine l'idée que la "
         "pensée serait instantanée et immatérielle. Si le signal met du temps, le mental a une durée, "
         "donc il est mesurable."),
    ],
    "04-sociale": [
        ("portrait-le-bon.jpg", "Gustave Le Bon (1841-1931)",
         "Sa Psychologie des foules (1895) popularise l'idée que l'individu en groupe perd son jugement "
         "critique. Théorie datée, souvent élitiste et sans base expérimentale, mais premier effort "
         "systématique pour penser le comportement collectif comme un objet psychologique."),
        ("fenetre-johari.png", "La fenêtre de Johari",
         "Quatre zones croisant ce que je sais de moi et ce que les autres savent de moi : zone publique, "
         "aveugle, cachée et inconnue. Outil classique pour comprendre pourquoi le retour d'autrui apporte "
         "une information à laquelle l'introspection n'accède pas."),
    ],
    "13-education": [
        ("courbe-oubli-ebbinghaus.svg", "Courbe de l'oubli et révision espacée",
         "Chaque révision qui intervient juste avant l'oubli aplatit la courbe suivante. C'est le fondement "
         "mathématique des logiciels de répétition espacée et la raison pour laquelle quatre sessions courtes "
         "battent systématiquement une longue session de bachotage."),
        ("portrait-watson.jpg", "John B. Watson (1878-1958)",
         "Fondateur du behaviorisme, auteur de la célèbre bravade selon laquelle il pourrait faire de "
         "n'importe quel enfant ce qu'il voudrait. Son expérience sur le petit Albert, aujourd'hui "
         "inacceptable sur le plan éthique, a néanmoins montré qu'une peur pouvait être apprise."),
        ("portrait-thorndike.jpg", "Edward Thorndike (1874-1949)",
         "Sa loi de l'effet — une action suivie d'une conséquence satisfaisante se répète — précède et "
         "prépare tout le conditionnement opérant, et reste le socle des systèmes de renforcement scolaires."),
    ],
    "16-comparee": [
        ("portrait-pavlov.jpg", "Ivan Pavlov (1849-1936)",
         "Physiologiste, prix Nobel de médecine pour ses travaux sur la digestion, il découvre presque par "
         "accident le conditionnement en constatant que ses chiens salivaient avant même de voir la nourriture."),
        ("portrait-lorenz.jpg", "Konrad Lorenz (1903-1989)",
         "Décrit l'empreinte : les oisons suivent le premier objet mobile qu'ils voient, pendant une période "
         "critique très courte. La notion de période sensible a durablement marqué la psychologie du "
         "développement humain."),
        ("portrait-darwin.jpg", "Charles Darwin (1809-1882)",
         "Son Expression des émotions (1872) soutient que les expressions faciales sont héritées et partagées "
         "avec d'autres espèces. C'est l'ancêtre direct des travaux d'Ekman sur l'universalité des émotions."),
    ],
    "23-evolutionniste": [
        ("portrait-darwin.jpg", "Charles Darwin (1809-1882)",
         "La sélection naturelle appliquée au comportement : si un mécanisme psychologique a été conservé, "
         "c'est qu'il a apporté un avantage reproductif dans l'environnement ancestral — ce qui n'implique "
         "nullement qu'il soit adapté au nôtre, ni qu'il soit souhaitable."),
    ],
    "27-science-psychologique": [
        ("phrenologie.jpg", "Planche de phrénologie",
         "Ce que l'on montrait au XIXe siècle : des bosses, des facultés. Entièrement faux — et pourtant "
         "l'idée qu'une fonction a une place a survécu, cette fois par la lésion et l'imagerie."),
        ("leborgne-cerveau.jpg", "Cerveau de Leborgne",
         "La pièce à conviction de Broca. Une lésion, une syllabe, une science. Voir la planche I de la zone de découverte."),
        ("homonculus-sensoriel.jpg", "Homoncule sensoriel",
         "Penfield redessine le corps : la carte suit la précision, pas les centimètres. Relier à la fiche et à la galerie."),
        ("aires-brodmann.png", "Aires de Brodmann",
         "1909 : une carte cellulaire avant l'IRM. Encore le langage commun des articles d'imagerie."),
        ("golgi-pyramidal.jpg", "Cellule pyramidale (Golgi)",
         "La coloration qui a rendu l'arbre visible. Sans elle, pas de planches de Cajal."),
        ("cajal-hippocampe.jpg", "Hippocampe de Cajal",
         "Observer pour comprendre : une planche plus dense qu'un schéma de cours, et toujours juste."),
        ("eeg-1020.jpg", "Système 10-20",
         "Où poser les électrodes pour que les laboratoires comparent leurs ondes. Technique, pas décor."),
        ("irm-sagittal.jpg", "IRM sagittale",
         "Une coupe réelle. Corps calleux, cervelet, tronc : ce que les tests de lésion cherchaient à tâtons."),
        ("dti-fibres.jpg", "Tractographie",
         "Les routes de la substance blanche. Base visuelle du Human Connectome Project."),
        ("tms-bobine.jpg", "Bobine de TMS",
         "Perturber une région sans ouvrir. Le complément causal de l'IRMf."),
        ("phineas-gage.jpg", "Phineas Gage",
         "Le frontal et le jugement social — ensuite trop romancé. Lire la fiche et les archives."),
        ("vesale-cerveau.jpg", "Vésale, 1543",
         "La première planche moderne d'un crâne ouvert : dessiner ce que l'on voit, pas ce que Galien prescrit."),
        ("cajal-cortex.png", "Cortex de Cajal",
         "La doctrine du neurone en image : des cellules distinctes, pas un filet continu."),
        ("broca-wernicke.jpg", "Broca et Wernicke",
         "Les deux pôles du langage. Un schéma moderne pour relier Tan et l'aphasie fluide."),
        ("premier-eeg.png", "Premier tracé EEG",
         "Ce que Berger a finalement rendu visible : l'électricité du cerveau, millisecondes après millisecondes."),
    ],
}
