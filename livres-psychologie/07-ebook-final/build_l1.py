# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Dossier pédagogique : les quatre UE de psychologie d'une L1."""

import os

from data_l1_psycho import L1_EXPERIENCES
from shell import page_header, page_shell

BASE = os.path.dirname(os.path.abspath(__file__))


def _write(name, html):
    path = os.path.join(BASE, name)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)


def _lectures():
    cards = ""
    for eid, titre, chercheur, annee, _cat, resume, protocole, resultat, portee, critique in L1_EXPERIENCES:
        cards += f"""<article class="ref-card" id="{eid}">
          <h3>{titre}</h3>
          <p class="compte-hint">{chercheur} · {annee}</p>
          <p>{resume}</p>
          <p><strong>Dispositif.</strong> {protocole}</p>
          <p><strong>Ce qu'on observe.</strong> {resultat}</p>
          <p><strong>Pourquoi ça compte.</strong> {portee}</p>
          <p><strong>Limite.</strong> {critique}</p>
        </article>"""
    return cards


def render():
    header = page_header(
        depth=0,
        breadcrumb=[("Accueil", "../../index.html"), ("Psychologie de licence", None)],
        icon="🎓", color="vert",
        title="Psychologie de licence",
        subtitle="Démarche scientifique, clinique, développement et lectures cognitives — une synthèse pour étudier, pas un polycopié",
        chips=["Méthode", "Clinique", "Développement", "Lectures"],
    )
    lectures = _lectures()
    body = f"""{header}
<div class="section">
  <div class="warn-box">
    <strong>À quoi sert cette page.</strong> Elle rassemble, en français et avec des mots à nous,
    ce qu'il faut tenir d'une première année de psychologie : comment une recherche se construit,
    ce que la clinique regarde, comment on étudie un développement, et ce que disent les articles
    qu'on donne à lire. Les manuels et les PDF restent à leurs auteurs. Rien ici n'est un diagnostic,
    un avis de soin, ni le cours officiel d'une université.
  </div>

  <h2 id="demarche">1. Démarche scientifique</h2>
  <p>La psychologie étudie la vie mentale et la conduite : ce qui est conscient, ce qui ne l'est pas,
  et le ressenti de la personne. Ce programme-là ne se confond pas avec le sens commun, qui cherche
  aussi des causes, ni avec la seule philosophie. Une science construit des modèles de régularités
  et juge un modèle à ce qu'il permet d'anticiper — tout en acceptant d'être contredite.</p>
  <p>Trois critères tiennent ensemble. La démarche est <strong>systématique</strong> : on ne picore pas
  l'anecdote qui arrange. Elle est <strong>précise</strong> : une autre équipe peut refaire le protocole.
  Elle est <strong>communicable</strong> : les résultats se présentent, se discutent, se publient.
  S'il en manque un, on a quitté la science.</p>
  <p>Le <strong>modèle biopsychosocial</strong> (Engel, 1977) place une expérience au croisement
  du biologique, du psychologique et du social. Les spécialités se rangent aussi selon d'autres axes :
  la situation présente, la trajectoire d'une vie, ou l'histoire de l'espèce ; le fonctionnement
  ordinaire, la vulnérabilité, ou le soin. Deux courants peuvent décrire la même scène sans se
  contredire, parce qu'ils ne cherchent pas la même cause. La bonne question n'est pas « qui a raison ? »
  mais « que cette approche permet-elle de voir, et que rate-t-elle si on l'utilise seule ? ».</p>
  <h3>Le cycle d'une étude</h3>
  <ol>
    <li>Observer un phénomène, assez longtemps pour qu'il ne soit pas une coïncidence.</li>
    <li>Formuler des hypothèses : une idée théorique, une version opérationnelle (ce qu'on mesurera), une version statistique (ce qu'on comparera).</li>
    <li>Vérifier : protocole, <strong>variable indépendante</strong> manipulée, <strong>variable dépendante</strong> mesurée. Les modalités de la VI doivent rester sur la même dimension, sinon la comparaison ne veut rien dire.</li>
    <li>Traiter les données, quantitatives ou qualitatives selon la question, et les confronter aux hypothèses.</li>
    <li>Dire ce qui tient, ce qui ne tient pas, et ce qu'on ne peut pas généraliser.</li>
  </ol>
  <p>La <strong>standardisation</strong> (consignes, matériel, durée, lieu) rend les participants comparables.
  Elle ne rend pas la situation « naturelle ». D'où les critiques : morale (on ne manipule pas les gens
  comme Milgram l'a fait), épistémique (un comportement a plusieurs causes ; le labo est artificiel ;
  généraliser est difficile). La recherche est une pratique : la personne qui observe a une histoire
  et des biais. Le troisième temps du cours, la démarche <em>processuelle</em>, insiste là-dessus :
  une étude est un processus, pas une photo. La question se précise en chemin. L'analyse peut mêler
  des chiffres et des paroles. L'observateur fait partie de la situation qu'il décrit.</p>
  <p><a href="categories/01-fondamentaux.html">Fondamentaux et méthodes</a> ·
  <a href="quiz/quiz.html?id=l1-psychologie">Quiz noté</a></p>

  <h2 id="clinique">2. Psychologie clinique</h2>
  <p>Là où la méthode expérimentale isole une variable, la clinique s'intéresse à une
  <strong>personne singulière</strong> : son histoire, ses liens, sa vie affective, de l'ordinaire
  jusqu'à la souffrance. Ce continuum n'est pas une étiquette à poser. Ce site ne pose pas de diagnostic.</p>
  <p>La <strong>méthode clinique</strong> cherche à comprendre, pas à classer d'abord.
  Deux boîtes à outils, souvent citées ensemble :</p>
  <ul>
    <li>la <strong>clinique à mains nues</strong> (Juliette Favez-Boutonnier) : observer, mener un entretien semi-directif ;</li>
    <li>la <strong>clinique armée</strong> (Daniel Lagache) : ajouter des tests et des médiations.</li>
  </ul>
  <p>Les exercer demande une formation, un diplôme et un cadre déontologique. En France, le titre
  de psychologue est protégé. Les terrains sont nombreux — soin, psychiatrie, justice, éducation
  spécialisée, petite enfance, prévention, gérontologie, travail social — et aucun ne s'improvise
  depuis une page web.</p>
  <p>Un référentiel fréquent en première année est psychanalytique, sans être le seul.
  La métapsychologie regarde le psychisme comme un appareil avec des contenus (les deux topiques
  freudiennes : conscient / préconscient / inconscient, puis ça / moi / surmoi), comme un lieu de
  conflits et de défenses, comme une vie pulsionnelle, et comme une construction au fil du développement.
  Une pulsion, dans ce vocabulaire, a une source corporelle, une poussée, un but et un objet.
  Elle se règle selon des principes (plaisir, réalité, et leurs suites). L'objet et l'entourage
  comptent dans la construction affective : un psychisme ne se fabrique pas seul.
  D'autres modèles cliniques existent. En garder un seul, c'est accepter son angle mort.</p>
  <p><a href="categories/09-psychopathologie.html">Psychopathologie</a> ·
  <a href="branches/clinique.html">Branche clinique</a></p>

  <h2 id="developpement">3. Psychologie du développement</h2>
  <p>Question directrice : <strong>comment devient-on qui l'on est</strong>, et qu'est-ce qui continue
  pendant que tout change. La définition classique (Baltes) parle des changements du fonctionnement
  psychologique au cours de la vie <em>et</em> des continuités. Ce n'est pas une échelle qui monterait
  jusqu'à l'âge adulte pour redescendre ensuite. Chaque période a ses adaptations.</p>
  <p>Trois horloges. La <strong>phylogenèse</strong> est celle de l'espèce, sur des temps très longs.
  L'<strong>ontogenèse</strong> est une vie, de la conception à la mort. La <strong>microgenèse</strong>
  est l'apprentissage d'une compétence, sur des jours ou des mois. On étudie surtout l'ontogenèse ;
  les deux autres l'éclairent.</p>
  <p>L'histoire de la discipline croise l'éducation (Érasme, Locke, Rousseau), l'évolution
  (Darwin ; Haeckel et l'idée, aujourd'hui abandonnée comme loi, que l'individu récapitulerait l'espèce),
  les premiers tests (Binet), puis des courants : maturationnisme (Gesell : le calendrier biologique),
  psychanalyse de l'enfant, behaviorisme, constructivisme de Piaget, socio-constructivismes de Wallon
  et de Vygotski, approche écologique (les milieux emboîtés), éthologie, attachement.</p>
  <h3>Ce que les débuts de la vie ont appris</h3>
  <p>Le mythe de l'enfant sauvage laisse croire qu'un humain se construirait hors de toute relation.
  L'<strong>hospitalisme</strong> décrit par Spitz montre le contraire : des nourrissons nourris
  mais privés d'un lien stable se retirent, et le développement se ralentit. Le contact n'est pas un luxe
  ajouté à la ration. Harlow le retrouve chez le singe : on s'attache au contact, pas seulement au lait.
  L'empreinte de Lorenz, sur un autre registre, montre une fenêtre où un petit se lie à une figure.</p>
  <p>Pour les visages, le modèle <strong>CONSPEC / CONLERN</strong> (Johnson et Morton) propose deux temps :
  un biais précoce vers une configuration de type visage, puis un apprentissage des visages rencontrés.</p>
  <h3>Étudier un nourrisson</h3>
  <ul>
    <li><strong>Préférence visuelle</strong> : il regarde plus l'un des deux stimuli.</li>
    <li><strong>Habituation puis nouveauté</strong> : le regard tombe quand la scène se répète, et repart si elle change.</li>
    <li><strong>Transgression des attentes</strong> : il regarde plus longtemps un événement qui viole une régularité physique ou sociale.</li>
    <li><strong>Conditionnement</strong> : une succion ou un tour de tête, renforcé, devient une réponse.</li>
  </ul>
  <p>Ces paradigmes montrent une discrimination ou une attente. Ils ne traduisent pas le bébé
  en phrases d'adulte. Le développement typique sert de repère ; le développement atypique
  n'est pas un échec moral, et ce n'est pas à cette page de le nommer pour une personne réelle.</p>
  <p><a href="categories/05-developpement.html">Catégorie développement</a> ·
  <a href="branches/developpement.html">Branche développement</a></p>

  <h2 id="lectures">4. Lectures de psychologie cognitive</h2>
  <p>Les articles ci-dessous forment un corpus de licence : attention, mémoire, métacognition,
  théorie de l'esprit, cognition animale, transmission culturelle, mémoire externalisée.
  Chaque fiche est une synthèse. Elle ne remplace pas l'article.</p>
  {lectures}
  <p><a href="categories/03-cognitive.html">Catégorie cognitive</a> ·
  <a href="references/experiences.html">Toutes les expériences</a> ·
  <a href="quiz/quiz.html?id=l1-psychologie">Quiz de ce dossier</a></p>
</div>
"""
    _write("l1-psychologie.html", page_shell(
        "Psychologie de licence",
        body,
        depth=0,
        description="Synthèse de licence : démarche scientifique, psychologie clinique, développement du nourrisson à la vie entière, et lectures cognitives.",
    ))
    return 1


if __name__ == "__main__":
    print(render(), "page L1")
