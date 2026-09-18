# -*- coding: utf-8 -*-
"""Laboratoire : mini-expériences jouables directement dans le navigateur.

Chaque entrée décrit une expérience classique reproduite de façon simplifiée.
Les mesures obtenues sont indicatives : un navigateur n'est pas un dispositif de
chronométrie de laboratoire, et un essai unique sur une personne ne prouve rien.
L'objectif est de faire *vivre* l'effet, pas de le mesurer rigoureusement.
"""

# (id, titre, icone, couleur, duree, accroche, consigne_html, explication_html, liens)
EXPERIENCES_LAB = [
    ("stroop", "L'effet Stroop", "🎨", "vert", "2 minutes",
     "Nommez la couleur de l'encre, pas le mot écrit. Vous allez sentir votre cerveau résister.",
     """<p>Des noms de couleurs vont s'afficher, écrits dans une encre qui correspond parfois au mot
     (<em>congruent</em>) et parfois non (<em>incongruent</em>). Votre tâche : cliquer sur la
     <strong>couleur de l'encre</strong>, en ignorant le mot.</p>
     <p>Vingt essais, le plus vite possible sans vous tromper. Le programme compare ensuite vos temps dans
     les deux conditions.</p>""",
     """<h4>Ce que vous venez de mesurer</h4>
     <p>La différence entre vos deux temps moyens s'appelle l'<strong>interférence Stroop</strong>. Chez la
     plupart des adultes lecteurs, la condition incongruente coûte entre 50 et 200 millisecondes
     supplémentaires, et produit davantage d'erreurs.</p>
     <p>L'explication tient à l'automatisation : la lecture est devenue si automatique qu'elle s'effectue sans
     intention et ne peut pas être « éteinte ». Le mot active donc une réponse concurrente qu'il faut inhiber
     activement — travail assuré par le cortex cingulaire antérieur et le cortex préfrontal.</p>
     <p>Publié par John Ridley Stroop en 1935, cet effet est l'un des plus robustes et des plus répliqués de
     toute la psychologie. Il sert aujourd'hui de mesure standard du <strong>contrôle exécutif</strong> en
     neuropsychologie clinique, et des variantes émotionnelles sont utilisées pour étudier l'anxiété et les
     addictions.</p>
     <p>Détail parlant : l'effet disparaît chez les personnes qui ne savent pas lire la langue affichée, et
     il est beaucoup plus faible chez le jeune enfant qui apprend encore à lire. L'interférence est donc le
     prix d'une compétence, pas un défaut.</p>""",
     [("Fiche Psychologie cognitive", "../categories/03-cognitive.html"),
      ("Théorie : systèmes 1 et 2", "../references/theories.html#double-processus")]),

    ("empan", "Votre empan mnésique", "🔢", "or", "3 minutes",
     "Combien de chiffres pouvez-vous retenir d'affilée ? La réponse surprend souvent.",
     """<p>Une suite de chiffres apparaît brièvement, puis disparaît. Vous devez la saisir dans le bon ordre.
     Chaque réussite allonge la suite d'un chiffre ; deux échecs de suite sur la même longueur arrêtent
     l'épreuve.</p>
     <p>Interdit de noter, de répéter à voix haute pendant l'affichage ou de photographier l'écran — cela
     fausserait complètement la mesure.</p>""",
     """<h4>Ce que vous venez de mesurer</h4>
     <p>Votre <strong>empan mnésique</strong> : le nombre d'éléments que votre mémoire de travail maintient
     et restitue dans l'ordre. George Miller a popularisé en 1956 le chiffre de « sept, plus ou moins deux ».
     Les travaux ultérieurs de Nelson Cowan situent plutôt la capacité réelle autour de <strong>quatre
     unités</strong> lorsqu'on empêche les stratégies de regroupement.</p>
     <p>Car la clé est là : ce qui est limité, ce n'est pas le nombre de <em>chiffres</em> mais le nombre
     d'<strong>unités</strong> (<em>chunks</em>). Si vous avez traité « 1 9 8 9 » comme une date plutôt que
     comme quatre chiffres, vous avez économisé trois places. C'est exactement ainsi qu'un joueur d'échecs
     expert mémorise une position entière en quelques secondes : il ne voit pas trente pièces, il voit cinq
     structures connues.</p>
     <p>Conséquence pratique immédiate : votre mémoire de travail ne s'agrandit pas par l'entraînement — les
     programmes de « gym cérébrale » n'obtiennent qu'un transfert très limité. En revanche, vos
     <strong>connaissances</strong> permettent d'y faire tenir toujours plus. Apprendre, c'est fabriquer des
     unités plus grosses.</p>""",
     [("Théorie : mémoire de travail", "../references/theories.html#memoire-travail"),
      ("Fiche Psychologie cognitive", "../categories/03-cognitive.html")]),

    ("reaction", "Votre temps de réaction", "⚡", "rose", "2 minutes",
     "Mesurez la vitesse de votre boucle œil-cerveau-main, et découvrez pourquoi elle varie autant.",
     """<p>La zone grise devient verte à un moment imprévisible. Cliquez dès que possible. Cinq essais, avec
     des délais aléatoires pour empêcher l'anticipation.</p>
     <p>Cliquer avant le signal annule l'essai : c'est volontaire, car anticiper n'est pas réagir.</p>""",
     """<h4>Ce que vous venez de mesurer</h4>
     <p>Un <strong>temps de réaction simple</strong>. Chez l'adulte jeune et reposé, il se situe généralement
     entre 200 et 280 millisecondes pour un stimulus visuel — un peu moins pour un son, la voie auditive étant
     plus courte. Une partie de votre score dépend d'ailleurs de votre matériel : écran, souris et navigateur
     ajoutent leur propre latence.</p>
     <p>Cette mesure est l'une des plus anciennes de la psychologie scientifique. Dès les années 1860,
     Franciscus Donders eut l'idée géniale de la <strong>méthode soustractive</strong> : mesurer un temps de
     réaction simple, puis un temps de réaction à choix, et soustraire les deux pour estimer la durée de
     l'opération mentale ajoutée. Pour la première fois, on chronométrait une pensée.</p>
     <p>Regardez surtout la <strong>variabilité</strong> de vos cinq essais. Elle est presque toujours plus
     informative que la moyenne : une grande instabilité signale un relâchement attentionnel, et l'augmentation
     de cette variabilité est un marqueur classique de la fatigue, du manque de sommeil et du vieillissement
     cognitif.</p>""",
     [("Fiche Neurosciences", "../categories/08-neurosciences.html"),
      ("Chronologie : 1868, Donders", "../references/chronologie.html")]),

    ("muller-lyer", "L'illusion de Müller-Lyer", "📏", "gris", "2 minutes",
     "Deux segments strictement identiques, que vous continuerez à voir différents même en le sachant.",
     """<p>Deux traits sont affichés : l'un terminé par des pointes vers l'extérieur, l'autre par des pointes
     vers l'intérieur. Réglez le curseur jusqu'à ce que les deux <strong>parties centrales</strong> vous
     paraissent de la même longueur, puis validez.</p>
     <p>Le programme affiche ensuite votre écart par rapport à l'égalité réelle.</p>""",
     """<h4>Ce que vous venez de mesurer</h4>
     <p>Votre <strong>biais perceptif</strong>. Décrite par Franz Carl Müller-Lyer en 1889, cette illusion
     produit typiquement une erreur de 15 à 25 % : le segment aux pointes rentrantes paraît plus long.</p>
     <p>L'explication la plus répandue invoque une correction de perspective : dans un environnement fait
     d'angles droits, les pointes ressemblent à un coin de mur proche ou éloigné, et le système visuel applique
     une constance de taille apprise. Un argument frappant soutient cette lecture : l'illusion est
     considérablement plus faible, voire absente, chez des personnes ayant grandi dans des environnements sans
     angles droits — le fameux « monde charpenté » décrit par Segall, Campbell et Herskovits en 1966.</p>
     <p>Le point le plus intéressant vient maintenant. Vous connaissez désormais la réponse, et l'illusion
     persiste malgré tout : elle est <strong>cognitivement impénétrable</strong>. Savoir ne suffit pas à voir
     autrement. C'est un excellent argument contre l'idée que la connaissance corrige automatiquement nos
     biais — et une raison de mettre en place des garde-fous procéduraux plutôt que de compter sur sa
     lucidité.</p>""",
     [("Théorie : lois de la Gestalt", "../references/theories.html#perspective-gestalt"),
      ("Fiche Psychologie interculturelle", "../categories/17-interculturelle.html")]),

    ("serie", "Effet de position sérielle", "📝", "vert", "4 minutes",
     "Quinze mots défilent. Vous allez oublier surtout ceux du milieu — et ce n'est pas un hasard.",
     """<p>Quinze mots vont s'afficher l'un après l'autre, une seconde chacun. Ensuite, écrivez tous ceux dont
     vous vous souvenez, dans l'ordre que vous voulez.</p>
     <p>Le programme situe vos rappels selon la position d'origine des mots dans la liste.</p>""",
     """<h4>Ce que vous venez de mesurer</h4>
     <p>La <strong>courbe de position sérielle</strong>, décrite par Bennet Murdock en 1962. Les premiers mots
     sont mieux rappelés (effet de <strong>primauté</strong>), les derniers aussi (effet de
     <strong>récence</strong>), et le milieu s'effondre.</p>
     <p>Les deux effets ont des causes différentes, ce qui en fait un argument historique majeur en faveur de
     mémoires distinctes. La primauté vient du temps de répétition disponible : les premiers mots ont été
     répétés davantage et ont eu le temps de rejoindre la mémoire à long terme. La récence vient du fait que
     les derniers mots sont encore présents en mémoire immédiate au moment du rappel.</p>
     <p>La démonstration décisive : insérer une tâche interférente de trente secondes entre la liste et le
     rappel — compter à rebours, par exemple — <strong>supprime la récence sans toucher la primauté</strong>.
     Deux effets qu'on peut dissocier expérimentalement, donc deux systèmes.</p>
     <p>Applications quotidiennes : on retient mieux le début et la fin d'une réunion, d'un exposé ou d'un
     entretien. Si vous devez placer un message important, évitez le milieu — et si vous passez un entretien
     d'embauche, l'ordre de passage n'est pas neutre.</p>""",
     [("Théorie : modèle modal de la mémoire", "../references/theories.html#memoire-atkinson"),
      ("Apprendre efficacement", "../apprendre.html")]),

    ("flanker", "Tâche des flèches (Eriksen)", "➡️", "or", "2 minutes",
     "Une flèche centrale entourée de flèches distractrices : mesurez votre capacité d'inhibition.",
     """<p>Cinq flèches s'affichent. Indiquez la direction de celle du <strong>milieu</strong>, en ignorant les
     quatre autres. Elles pointent parfois dans le même sens (condition congruente), parfois dans le sens
     opposé (condition incongruente).</p>
     <p>Répondez avec les touches fléchées ou avec les boutons. Vingt-quatre essais.</p>""",
     """<h4>Ce que vous venez de mesurer</h4>
     <p>Votre <strong>effet flanker</strong> : la différence de temps entre les deux conditions, typiquement
     de 30 à 80 millisecondes. Barbara et Charles Eriksen l'ont décrit en 1974.</p>
     <p>Le résultat démontre que l'attention visuelle sélective n'est pas un projecteur parfaitement étanche.
     Même en sachant exactement où regarder, les distracteurs proches sont traités et activent leur réponse
     associée, qu'il faut ensuite inhiber.</p>
     <p>Cette tâche est devenue un instrument standard : elle constitue le cœur du <em>Attention Network
     Test</em>, qui sépare les trois réseaux attentionnels décrits par Michael Posner — alerte, orientation et
     contrôle exécutif. On l'utilise pour étudier le TDAH, les effets de la privation de sommeil, du
     vieillissement, et même du bilinguisme.</p>
     <p>Un détail contre-intuitif : éloigner spatialement les distracteurs réduit fortement l'effet, alors que
     les rendre plus petits ne suffit pas. Ce qui compte pour l'attention, c'est la distance dans l'espace,
     pas seulement la saillance.</p>""",
     [("Fiche Psychologie cognitive", "../categories/03-cognitive.html"),
      ("Théorie : systèmes 1 et 2", "../references/theories.html#double-processus")]),

    ("ancrage", "Le biais d'ancrage", "⚓", "rose", "1 minute",
     "Un nombre parfaitement arbitraire va influencer votre estimation. Vous ne le sentirez pas.",
     """<p>On va d'abord vous montrer un nombre tiré au hasard, puis vous poser une question d'estimation qui
     n'a aucun rapport avec lui. Répondez spontanément, sans chercher à « corriger ».</p>
     <p>Le programme vous dira ensuite dans quel groupe vous étiez et ce que répondent habituellement les deux
     groupes.</p>""",
     """<h4>Ce que vous venez de vivre</h4>
     <p>Le <strong>biais d'ancrage</strong>, décrit par Amos Tversky et Daniel Kahneman en 1974. Leur
     expérience fondatrice est restée célèbre : ils faisaient tourner une roue de loterie truquée devant les
     participants, puis leur demandaient d'estimer le pourcentage de pays africains membres de l'ONU. Le groupe
     ayant vu le 10 répondait en moyenne 25 %, celui ayant vu le 65 répondait 45 %.</p>
     <p>Un nombre manifestement aléatoire, et dont chacun savait qu'il était aléatoire, déplaçait l'estimation
     de vingt points. Le mécanisme semble être un ajustement insuffisant : on part de la valeur disponible et
     on s'en écarte… pas assez.</p>
     <p>L'effet est l'un des plus robustes de la littérature sur la décision, et il résiste à l'avertissement
     explicite. Il opère dans les négociations salariales, les prix affichés en magasin, les demandes de
     dommages et intérêts, et les estimations d'experts.</p>
     <p>La seule parade réellement efficace n'est pas de « se méfier » : c'est de construire votre propre
     estimation <strong>avant</strong> d'être exposé à un chiffre, et d'annoncer le premier chiffre quand vous
     disposez d'une information fiable.</p>""",
     [("Biais cognitifs", "../references/biais.html"),
      ("Fiche pratique : préparer une négociation", "../pratique.html#negociation")]),
]
