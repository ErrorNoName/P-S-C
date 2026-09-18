#!/usr/bin/env python3
"""Generate the enriched illustrated psychology guide."""

from pathlib import Path

BASE = Path(__file__).parent
CHAP = BASE / "chapitres"
ILLUS = BASE / "illustrations"
CHAP.mkdir(exist_ok=True)
ILLUS.mkdir(exist_ok=True)


def svg_brain():
    return '''<svg viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg" class="diagram">
  <defs><linearGradient id="bg1" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" style="stop-color:#6B46C1"/><stop offset="100%" style="stop-color:#553C9A"/>
  </linearGradient></defs>
  <rect width="400" height="300" rx="12" fill="url(#bg1)"/>
  <text x="200" y="30" fill="white" text-anchor="middle" font-size="16" font-weight="bold">Cerveau — Aire fonctionnelle</text>
  <ellipse cx="200" cy="160" rx="120" ry="90" fill="#E9D8FD" stroke="#553C9A" stroke-width="2"/>
  <ellipse cx="130" cy="130" rx="50" ry="40" fill="#D6BCFA" stroke="#553C9A" stroke-width="1.5"/>
  <text x="130" y="125" text-anchor="middle" fill="#44337A" font-size="10">Cortex</text>
  <text x="130" y="138" text-anchor="middle" fill="#44337A" font-size="9">préfrontal</text>
  <ellipse cx="270" cy="130" rx="45" ry="38" fill="#B794F4" stroke="#553C9A" stroke-width="1.5"/>
  <text x="270" y="128" text-anchor="middle" fill="#44337A" font-size="10">Cortex</text>
  <text x="270" y="141" text-anchor="middle" fill="#44337A" font-size="9">visuel</text>
  <ellipse cx="200" cy="195" rx="35" ry="28" fill="#9F7AEA" stroke="#553C9A" stroke-width="1.5"/>
  <text x="200" y="200" text-anchor="middle" fill="white" font-size="9">Tronc</text>
  <path d="M 80 160 Q 60 200 90 230" fill="none" stroke="#F6E05E" stroke-width="3"/>
  <text x="55" y="250" fill="#F6E05E" font-size="9">Hippocampe</text>
  <path d="M 320 160 Q 340 200 310 230" fill="none" stroke="#68D391" stroke-width="3"/>
  <text x="295" y="250" fill="#68D391" font-size="9">Amygdale</text>
  <text x="200" y="285" fill="#E9D8FD" text-anchor="middle" font-size="11">Mémoire • Émotion • Décision</text>
</svg>'''


def svg_mindmap(title, branches):
    lines = []
    y_start = 80
    colors = ["#FC8181", "#68D391", "#63B3ED", "#F6AD55", "#B794F4", "#F687B3", "#4FD1C5", "#F6E05E"]
    for i, (label, items) in enumerate(branches):
        color = colors[i % len(colors)]
        angle = (360 / len(branches)) * i
        import math
        rad = math.radians(angle - 90)
        cx, cy = 200, 150
        bx = cx + 100 * math.cos(rad)
        by = cy + 80 * math.sin(rad)
        lines.append(f'<line x1="{cx}" y1="{cy}" x2="{bx:.0f}" y2="{by:.0f}" stroke="{color}" stroke-width="2"/>')
        lines.append(f'<circle cx="{bx:.0f}" cy="{by:.0f}" r="35" fill="{color}" opacity="0.85"/>')
        lines.append(f'<text x="{bx:.0f}" y="{by:.0f}" text-anchor="middle" fill="white" font-size="8" font-weight="bold">{label}</text>')
    inner = "\n  ".join(lines)
    return f'''<svg viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg" class="diagram">
  <rect width="400" height="300" rx="12" fill="#1A202C"/>
  <text x="200" y="25" fill="white" text-anchor="middle" font-size="14" font-weight="bold">{title}</text>
  <circle cx="200" cy="150" r="45" fill="#6B46C1"/>
  <text x="200" y="155" text-anchor="middle" fill="white" font-size="11" font-weight="bold">PSYCHO</text>
  {inner}
</svg>'''


def svg_timeline(events):
    items = []
    x = 30
    for year, name in events:
        items.append(f'<circle cx="{x}" cy="150" r="8" fill="#6B46C1"/>')
        items.append(f'<text x="{x}" y="130" text-anchor="middle" fill="#E9D8FD" font-size="9">{year}</text>')
        items.append(f'<text x="{x}" y="175" text-anchor="middle" fill="white" font-size="8">{name}</text>')
        if x < 370:
            items.append(f'<line x1="{x+8}" y1="150" x2="{x+42}" y2="150" stroke="#553C9A" stroke-width="2"/>')
        x += 50
    inner = "\n  ".join(items[: min(len(items), 40)])
    return f'''<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg" class="diagram">
  <rect width="400" height="200" rx="12" fill="#2D3748"/>
  <text x="200" y="25" fill="white" text-anchor="middle" font-size="14" font-weight="bold">Frise chronologique</text>
  {inner}
</svg>'''


def svg_pavlov():
    return '''<svg viewBox="0 0 400 250" xmlns="http://www.w3.org/2000/svg" class="diagram">
  <rect width="400" height="250" rx="12" fill="#FFF5F5"/>
  <text x="200" y="25" text-anchor="middle" fill="#742A2A" font-size="14" font-weight="bold">Conditionnement classique (Pavlov, 1897)</text>
  <rect x="30" y="50" width="150" height="60" rx="8" fill="#FEB2B2" stroke="#C53030"/>
  <text x="105" y="75" text-anchor="middle" fill="#742A2A" font-size="10">Stimulus neutre</text>
  <text x="105" y="92" text-anchor="middle" fill="#742A2A" font-size="11" font-weight="bold">Sonnette 🔔</text>
  <text x="210" y="85" fill="#C53030" font-size="20">+</text>
  <rect x="220" y="50" width="150" height="60" rx="8" fill="#FEB2B2" stroke="#C53030"/>
  <text x="295" y="75" text-anchor="middle" fill="#742A2A" font-size="10">Stimulus inconditionné</text>
  <text x="295" y="92" text-anchor="middle" fill="#742A2A" font-size="11" font-weight="bold">Nourriture 🍖</text>
  <text x="200" y="130" text-anchor="middle" fill="#C53030" font-size="16">↓ Répétitions ↓</text>
  <rect x="125" y="150" width="150" height="60" rx="8" fill="#FC8181" stroke="#C53030" stroke-width="2"/>
  <text x="200" y="175" text-anchor="middle" fill="white" font-size="10">Stimulus conditionné</text>
  <text x="200" y="195" text-anchor="middle" fill="white" font-size="12" font-weight="bold">Sonnette → Salivation</text>
  <text x="60" y="230" fill="#742A2A" font-size="24">🐕</text>
  <text x="90" y="235" fill="#742A2A" font-size="10">Chien de Pavlov</text>
</svg>'''


def svg_maslow():
    return '''<svg viewBox="0 0 300 350" xmlns="http://www.w3.org/2000/svg" class="diagram">
  <text x="150" y="20" text-anchor="middle" fill="#2D3748" font-size="14" font-weight="bold">Pyramide de Maslow</text>
  <polygon points="150,40 260,320 40,320" fill="none" stroke="#CBD5E0" stroke-width="1"/>
  <polygon points="150,40 230,130 70,130" fill="#6B46C1"/><text x="150" y="95" text-anchor="middle" fill="white" font-size="9">Accomplissement</text>
  <polygon points="150,130 240,190 60,190" fill="#805AD5"/><text x="150" y="168" text-anchor="middle" fill="white" font-size="9">Estime</text>
  <polygon points="150,190 245,250 55,250" fill="#9F7AEA"/><text x="150" y="228" text-anchor="middle" fill="white" font-size="9">Appartenance</text>
  <polygon points="150,250 250,290 50,290" fill="#B794F4"/><text x="150" y="278" text-anchor="middle" fill="white" font-size="9">Sécurité</text>
  <polygon points="150,290 255,320 45,320" fill="#D6BCFA"/><text x="150" y="312" text-anchor="middle" fill="#44337A" font-size="9">Besoins physiologiques</text>
</svg>'''


def write_illustrations():
    (ILLUS / "cerveau.svg").write_text(svg_brain(), encoding="utf-8")
    (ILLUS / "pavlov.svg").write_text(svg_pavlov(), encoding="utf-8")
    (ILLUS / "maslow.svg").write_text(svg_maslow(), encoding="utf-8")
    (ILLUS / "mindmap-cognitive.svg").write_text(
        svg_mindmap("Psychologie cognitive", [
            ("Perception", []), ("Mémoire", []), ("Attention", []),
            ("Langage", []), ("Raisonnement", []), ("Biais", []),
        ]), encoding="utf-8"
    )
    (ILLUS / "timeline.svg").write_text(
        svg_timeline([
            ("1879", "Wundt"), ("1890", "James"), ("1900", "Freud"),
            ("1913", "Watson"), ("1920", "Piaget"), ("1950", "Rogers"),
            ("1960", "Milgram"), ("1970", "Beck"), ("1998", "Seligman"),
        ]), encoding="utf-8"
    )


CHAPTERS = [
    ("00-introduction", "Introduction à la psychologie", "introduction"),
    ("01-cognitive", "Psychologie cognitive", "cognitive"),
    ("02-sociale", "Psychologie sociale", "sociale"),
    ("03-apprentissage", "Apprentissage", "apprentissage"),
    ("04-biologique", "Psychologie biologique", "biologique"),
    ("05-developpement", "Psychologie du développement", "developpement"),
    ("06-differences", "Différences individuelles", "differences"),
    ("07-therapie", "Thérapie", "therapie"),
    ("08-positive", "Psychologie positive", "positive"),
    ("09-dictionnaire", "Dictionnaire des notions essentielles", "dictionnaire"),
]


CONTENT = {
    "introduction": """
<h2>Qu'est-ce que la psychologie ?</h2>
<p>La psychologie est la <strong>science du comportement et des processus mentaux</strong>. Elle cherche à comprendre comment nous percevons, pensons, ressentons et agissons — individuellement et collectivement.</p>

<figure class="illus">{timeline}</figure>

<h3>Les grandes écoles de pensée</h3>
<div class="card-grid">
<div class="card"><h4>🔬 Structuralisme (Wundt, 1879)</h4><p>Première laboratory psychology à Leipzig. Analyse des éléments de base de la conscience par introspection.</p></div>
<div class="card"><h4>🌊 Fonctionnalisme (James, 1890)</h4><p>Étudie l'adaptation de l'esprit à l'environnement. Précurseur de la psychologie évolutionniste.</p></div>
<div class="card"><h4>🛋️ Psychanalyse (Freud, 1900)</h4><p>Inconscient, pulsions, transfert. Révolution conceptuelle malgré les critiques méthodologiques.</p></div>
<div class="card"><h4>🐀 Behaviorisme (Watson, Skinner)</h4><p>Seul le comportement observable compte. Conditionnement classique et opérant.</p></div>
<div class="card"><h4>🧠 Cognitivisme (années 1960)</h4><p>Retour à l'étude des processus mentaux : mémoire, attention, résolution de problèmes.</p></div>
<div class="card"><h4>🌱 Humanisme (Rogers, Maslow)</h4><p>Potentiel humain, croissance personnelle, thérapie centrée sur la personne.</p></div>
</div>

<h3>Comment lire ce guide</h3>
<p>Ce guide reprend la structure pédagogique des ouvrages <em>Short Cuts Psychologie</em> (8 thématiques + cartes mentales) et <em>Le Petit Larousse de la Psychologie</em> (dossiers + dictionnaire), avec un contenu <strong>original</strong> et des illustrations créées pour l'apprentissage.</p>
""",

    "cognitive": """
<h2>Psychologie cognitive</h2>
<p>La psychologie cognitive étudie les <strong>processus mentaux</strong> : perception, attention, mémoire, langage, raisonnement et prise de décision.</p>

<figure class="illus">{brain}</figure>
<figure class="illus">{mindmap_cog}</figure>

<h3>La perception est-elle juste une expérience ?</h3>
<p>Non. La perception est un <strong>processus actif de construction</strong>. Le cerveau ne reproduit pas fidèlement le monde : il l'interprète à partir d'indices sensoriels incomplets.</p>
<ul>
<li><strong>Illusions visuelles</strong> : Le vase de Rubin, les lignes de Müller-Lyer démontrent que voir ≠ enregistrer.</li>
<li><strong>Théorie de l'attribution</strong> : Nous interprétons les causes des comportements (internes vs externes).</li>
<li><strong>Perception sélective</strong> : L'expérience « gorille invisible » (Simons & Chabris, 1999) montre que l'attention filtre massivement l'information.</li>
</ul>

<h3>Comment le cerveau construit-il la mémoire ?</h3>
<p>La mémoire n'est pas une vidéo. C'est un <strong>processus reconstructif</strong> impliquant plusieurs systèmes :</p>
<table class="data-table">
<tr><th>Système</th><th>Durée</th><th>Capacité</th><th>Exemple</th></tr>
<tr><td>Mémoire sensorielle</td><td>&lt; 1 seconde</td><td>Très grande</td><td>Écho iconique (visuel)</td></tr>
<tr><td>Mémoire à court terme</td><td>15–30 secondes</td><td>7±2 items</td><td>Numéro de téléphone</td></tr>
<tr><td>Mémoire de travail</td><td>Active</td><td>Limitée</td><td>Résoudre un calcul mental</td></tr>
<tr><td>Mémoire à long terme</td><td>Illimitée</td><td>Quasi-illimitée</td><td>Souvenirs d'enfance</td></tr>
</table>

<h3>Peut-on compter sur votre témoignage ?</h3>
<p>Les recherches d'<strong>Elizabeth Loftus</strong> démontrent que la mémoire est <strong>suggestible</strong>. Des études montrent que 25 à 50 % des sujets peuvent « se souvenir » d'événements fictifs après suggestion.</p>
<div class="highlight"><strong>Effet de désinformation</strong> : Une information post-événement altère le souvenir original. Implications majeures pour la justice.</div>

<h3>Le raccourci est-il la voie du danger ?</h3>
<p>Les <strong>heuristiques</strong> (raccourcis mentaux) permettent des décisions rapides mais engendrent des biais :</p>
<ul>
<li><strong>Heuristique de disponibilité</strong> : Juger la probabilité par la facilité de rappel (ex. peur de l'avion vs voiture).</li>
<li><strong>Heuristique de représentativité</strong> : Ignorer les statistiques de base (problème de Linda).</li>
<li><strong>Ancrage</strong> : Première information influence les jugements suivants.</li>
<li><strong>Biais de confirmation</strong> : Chercher ce qui confirme nos croyances.</li>
</ul>
""",

    "sociale": """
<h2>Psychologie sociale</h2>
<p>Comment les <strong>autres</strong> influencent notre pensée, nos émotions et nos actions.</p>

<h3>Les humains sont-ils tous des moutons ?</h3>
<p>L'<strong>expérience de conformité d'Asch</strong> (1951) : face à un groupe donnant une réponse manifestement fausse, <strong>75 %</strong> des participants se conformaient au moins une fois. La pression sociale modifie même la perception de réalités objectives.</p>

<h3>Quand cessons-nous de suivre les ordres ?</h3>
<p>L'<strong>expérience de Milgram</strong> (1963) : sous consigne d'un chercheur en blouse blanche, <strong>65 %</strong> des participants administraient ce qu'ils croyaient être des chocs dangereux. L'autorité légitime l'emporte sur la conscience morale chez la majorité.</p>

<h3>Interviendriez-vous en cas de meurtre ?</h3>
<p>L'<strong>effet du témoin</strong> (Darley & Latané, 1968) : plus il y a de témoins, moins chacun intervient (diffusion de responsabilité). Le meurtre de Kitty Genovese (1964) a popularisé ce concept.</p>

<h3>Est-ce toujours « eux » contre « nous » ?</h3>
<p>La <strong>théorie de l'identité sociale</strong> (Tajfel, 1979) : nous favorisons automatiquement notre groupe (in-group) et dévaluons les autres (out-group), même pour des catégorisations arbitraires (expérience des minimal groups).</p>

<h3>Affichons-nous tous les mêmes émotions ?</h3>
<p>Le débat <strong>universel vs culturel</strong> des émotions : Ekman identifie 6 émotions de base universelles (joie, tristesse, colère, peur, dégoût, surprise), mais leur <em>expression</em> et <em>régulation</em> varient selon les cultures (display rules).</p>

<h3>Pourquoi as-tu fait ça ?</h3>
<p><strong>Attribution</strong> : Nous sur-attribuons les comportements d'autrui à des causes <em>internes</em> (erreur fondamentale d'attribution) et les nôtres aux circonstances <em>externes</em> (bénéfice acteur-observateur).</p>
""",

    "apprentissage": """
<h2>Apprentissage</h2>

<figure class="illus">{pavlov}</figure>

<h3>Salivez-vous quand sonne l'heure du dîner ?</h3>
<p>Le <strong>conditionnement classique</strong> (Pavlov, 1897) : un stimulus neutre (sonnette) associé répétitivement à un stimulus inconditionné (nourriture) devient capable de provoquer la réponse (salivation) seul.</p>

<h3>Apprenons-nous de nos récompenses ?</h3>
<p>Le <strong>conditionnement opérant</strong> (Skinner) : le comportement est modelé par ses conséquences.</p>
<ul>
<li><strong>Renforcement positif</strong> : Ajouter quelque chose d'agréable → augmente le comportement.</li>
<li><strong>Renforcement négatif</strong> : Retirer quelque chose d'aversif → augmente le comportement.</li>
<li><strong>Punition</strong> : Diminue le comportement (effets secondaires possibles).</li>
<li><strong>Extinction</strong> : Cesser le renforcement → le comportement disparaît.</li>
</ul>

<h3>Apprendre est-il un jeu d'imitation ?</h3>
<p>L'<strong>apprentissage social</strong> (Bandura, 1961) : l'expérience Bobo doll montre que les enfants imitent les comportements observés, surtout si le modèle est valorisé. L'apprentissage ne nécessite pas de renforcement direct.</p>

<h3>Dix mille heures de pratique feront-elles de vous un génie ?</h3>
<p>La règle des <strong>10 000 heures</strong> (Ericsson) est simplifiée. La pratique délibérée compte, mais le talent initial, la qualité de l'encadrement et le domaine influencent aussi les performances d'expert.</p>

<h3>Comment un enfant voit-il le monde ?</h3>
<p><strong>Piaget</strong> décrit 4 stades : sensorimoteur (0–2 ans), préopératoire (2–7), opératoire concret (7–11), opératoire formel (11+). Chaque stade restructure la compréhension du monde.</p>
""",

    "biologique": """
<h2>Psychologie biologique (neurosciences)</h2>

<figure class="illus">{brain}</figure>

<h3>Avons-nous bien cinq sens ?</h3>
<p>Non. Nous avons au minimum : <strong>vue, ouïe, toucher, goût, odorat</strong>, plus <strong>proprioception</strong> (position du corps), <strong>vestibulaire</strong> (équilibre), <strong>nociception</strong> (douleur), <strong>thermoréception</strong> (température).</p>

<h3>Travaillons-nous mieux sous la pression ?</h3>
<p>La <strong>loi de Yerkes-Dodson</strong> : performance optimale à arousal modéré. Trop peu de stress = ennui ; trop = anxiété paralysante. La courbe est inversée pour les tâches complexes.</p>

<h3>Comment les drogues font-elles planer ?</h3>
<p>Les substances psychoactives modulent les <strong>neurotransmetteurs</strong> :</p>
<table class="data-table">
<tr><th>Substance</th><th>Mécanisme</th><th>Effet</th></tr>
<tr><td>Dopamine (cocaïne)</td><td>Bloque recapture</td><td>Euphorie, addiction</td></tr>
<tr><td>Sérotonine (LSD, MDMA)</td><td>Agoniste/modulateur</td><td>Altération perception</td></tr>
<tr><td>GABA (alcool, benzodiazépines)</td><td>Agoniste</td><td>Sédation, anxiolyse</td></tr>
<tr><td>Glutamate (Kétamine)</td><td>Antagoniste NMDA</td><td>Dissociation</td></tr>
</table>

<h3>Comment reconnaître un visage ?</h3>
<p>Le <strong>fusiform face area</strong> (FFA) dans le cortex temporal inférieur est spécialisé dans la reconnaissance faciale. La prosopagnosie (face blindness) démontre cette spécialisation.</p>
""",

    "developpement": """
<h2>Psychologie du développement</h2>

<h3>Doit-on être sûr quand on s'attache ?</h3>
<p>La <strong>théorie de l'attachement</strong> (Bowlby, Ainsworth) : les premiers liens avec les figures parentales modèles la sécurité relationnelle future.</p>
<ul>
<li><strong>Attachement sûr</strong> (65 %) : exploration confiante, retour au parent en cas de stress.</li>
<li><strong>Attachement anxieux</strong> : hypervigilance, peur de l'abandon.</li>
<li><strong>Attachement évitant</strong> : distance émotionnelle, autonomie excessive.</li>
<li><strong>Attachement désorganisé</strong> : comportements contradictoires.</li>
</ul>

<h3>Quel âge a l'ego ?</h3>
<p><strong>Erikson</strong> propose 8 stades psychosociaux (confiance vs méfiance, identité vs confusion…). L'identité (stade 5, adolescence) cristallise le « moi » social.</p>

<h3>Les enfants lisent-ils dans les pensées ?</h3>
<p>La <strong>théorie de l'esprit</strong> émerge vers 4 ans : comprendre que les autres ont des croyances, désirs et intentions différents. Test classique : fausses croyances (Sally-Anne).</p>

<h3>Quel est votre rôle dans le théâtre de la vie ?</h3>
<p>L'approche <strong>écologique de Bronfenbrenner</strong> : le développement s'inscrit dans des systèmes emboîtés (micro, méso, exo, macro, chrono).</p>
""",

    "differences": """
<h2>Différences individuelles</h2>

<h3>Combien y a-t-il d'intelligences ?</h3>
<p><strong>Gardner</strong> propose 8 intelligences (linguistique, logico-mathématique, spatiale, musicale, kinesthésique, interpersonnelle, intrapersonnelle, naturaliste). Critiqué scientifiquement mais influent pédagogiquement.</p>
<p>Le modèle dominant reste le <strong>facteur g</strong> (intelligence générale), corrélé aux performances dans de nombreux domaines cognitifs.</p>

<h3>Comment mesurer la personnalité ?</h3>
<p>Le modèle <strong>Big Five (OCEAN)</strong> :</p>
<ul>
<li><strong>O</strong>uverture — curiosité, créativité</li>
<li><strong>C</strong>onscienciosité — organisation, discipline</li>
<li><strong>E</strong>xtraversion — sociabilité, énergie</li>
<li><strong>A</strong>gréabilité — coopération, confiance</li>
<li><strong>N</strong>évrosisme — stabilité émotionnelle (inversé)</li>
</ul>

<h3>Construisons-nous notre propre monde ?</h3>
<p>La <strong>théorie des constructs personnels</strong> (Kelly, 1955) : nous interprétons le monde via des « constructs » bipolaires (bon/mauvais, actif/passif) qui filtrent toute expérience.</p>
""",

    "therapie": """
<h2>Thérapie et santé mentale</h2>

<h3>D'où viennent les pensées négatives ?</h3>
<p>Le modèle <strong>ABC de Beck</strong> (TCC) :</p>
<ul>
<li><strong>A</strong>ctivating event (événement déclencheur)</li>
<li><strong>B</strong>elief (croyance/pensée automatique)</li>
<li><strong>C</strong>onsequence (émotion et comportement)</li>
</ul>
<p>Les distorsions cognitives (tout-ou-rien, catastrophisme, surgénéralisation) alimentent la dépression et l'anxiété.</p>

<h3>Pourquoi sommes-nous irrationnels ?</h3>
<p>La <strong>thérapie cognitivo-comportementale (TCC)</strong> est la plus étayée empiriquement pour l'anxiété, la dépression, les TOC. Elle restructure les pensées et modifie les comportements d'évitement.</p>

<h3>Le comportement modifie-t-il les pensées ?</h3>
<p>Oui. L'<strong>exposition progressive</strong> (pour phobies) et l'<strong>activation comportementale</strong> (pour dépression) démontrent que l'action précède parfois le changement cognitif.</p>

<h3>Panorama des approches thérapeutiques</h3>
<table class="data-table">
<tr><th>Approche</th><th>Fondateur</th><th>Focus</th></tr>
<tr><td>Psychanalyse</td><td>Freud</td><td>Inconscient, transfert</td></tr>
<tr><td>TCC</td><td>Beck, Ellis</td><td>Pensées, comportements</td></tr>
<tr><td>Humaniste</td><td>Rogers</td><td>Empathie, acceptation</td></tr>
<tr><td>Systémique</td><td>Minuchin</td><td>Relations familiales</td></tr>
<tr><td>EMDR</td><td>Shapiro</td><td>Trauma, retraitement</td></tr>
<tr><td>ACT</td><td>Hayes</td><td>Acceptation, valeurs</td></tr>
</table>
""",

    "positive": """
<h2>Psychologie positive</h2>

<figure class="illus">{maslow}</figure>

<h3>Quel est le raccourci vers le bonheur ?</h3>
<p>Pas de raccourci miracle. Seligman (PERMA) identifie 5 piliers du bien-être :</p>
<ul>
<li><strong>P</strong>ositive emotions — émotions positives</li>
<li><strong>E</strong>ngagement — flow, absorption</li>
<li><strong>R</strong>elationships — relations de qualité</li>
<li><strong>M</strong>eaning — sens, purpose</li>
<li><strong>A</strong>ccomplishment — réalisation de soi</li>
</ul>

<h3>Doit-on se laisser porter par le flow ?</h3>
<p>Le <strong>flow</strong> (Csikszentmihalyi) : état d'absorption totale quand défi et compétence sont équilibrés. Conditions : objectifs clairs, feedback immédiat, perte de conscience de soi.</p>

<h3>Changer de mentalité change-t-il l'esprit ?</h3>
<p>Les recherches sur la <strong>growth mindset</strong> (Dweck) montrent que croire que l'intelligence est développable améliore la persévérance. Effets réels mais parfois sur-estimés dans la vulgarisation.</p>
""",

    "dictionnaire": """
<h2>Dictionnaire des notions essentielles</h2>
<p>Plus de 80 entrées sélectionnées, dans l'esprit du Petit Larousse de la Psychologie.</p>
<div class="dict-grid">
{dict_entries}
</div>
""",
}


DICT = [
    ("Abandon", "Sentiment de rejet ou de perte affective, souvent lié aux premières relations d'attachement."),
    ("Addiction", "Dépendance comportementale ou substance, impliquant tolérance et sevrage."),
    ("Agoraphobie", "Peur des espaces ouverts ou des situations d'évasion difficile."),
    ("Amygdale", "Structure cérébrale clé du traitement de la peur et des émotions."),
    ("Anxiété", "Réaction émotionnelle face à une menace perçue, avec composantes cognitives et somatiques."),
    ("Attachement", "Lien affectif durable entre l'enfant et sa figure de soin (Bowlby)."),
    ("Autisme (TSA)", "Trouble du neurodéveloppement affectant communication et interactions sociales."),
    ("Behaviorisme", "École étudiant le comportement observable, excluant l'introspection."),
    ("Biais cognitif", "Erreur systématique de jugement due aux heuristiques mentales."),
    ("Burn-out", "Épuisement professionnel : fatigue, cynisme, sentiment d'inefficacité."),
    ("Charge mentale", "Travail cognitif invisible de gestion du quotidien familial."),
    ("Cognition", "Ensemble des processus mentaux : perception, mémoire, raisonnement."),
    ("Conditionnement", "Apprentissage par association (classique) ou conséquences (opérant)."),
    ("Conscience", "Awareness de soi et de l'environnement ; débat philosophique et scientifique."),
    ("Contre-transfert", "Réactions émotionnelles du thérapeute envers le patient."),
    ("Dépression", "Trouble de l'humeur caractérisé par tristesse persistante et anhédonie."),
    ("Dopamine", "Neurotransmetteur impliqué dans la récompense, motivation et addiction."),
    ("Dyslexie", "Trouble spécifique de la lecture, indépendant de l'intelligence."),
    ("EMDR", "Thérapie par retraitement des mouvements oculaires pour le trauma."),
    ("Empathie", "Capacité à comprendre et partager les émotions d'autrui."),
    ("Flow", "État de concentration optimale décrit par Csikszentmihalyi."),
    ("Freud", "Fondateur de la psychanalyse (1856–1939), concept d'inconscient."),
    ("Hippocampe", "Structure cérébrale essentielle à la formation des souvenirs."),
    ("Hypnose", "État modifié de conscience utilisé thérapeutiquement."),
    ("Inconscient", "Processus mentaux hors de la conscience (Freud, puis cognitivisme)."),
    ("Intelligence", "Capacité d'adaptation, d'apprentissage et de résolution de problèmes."),
    ("Introversion", "Orientation vers le monde intérieur ; trait de personnalité."),
    ("Mémoire", "Système d'encodage, stockage et récupération de l'information."),
    ("Métacognition", "Réflexion sur ses propres processus de pensée."),
    ("Mindfulness", "Pleine conscience : attention au moment présent sans jugement."),
    ("Motivation", "Forces orientant le comportement vers un objectif."),
    ("Narcissisme", "Investissement excessif de la libido sur le moi (Freud) ; trait de personnalité."),
    ("Neuroplasticité", "Capacité du cerveau à se réorganiser par l'expérience."),
    ("Neurotransmetteur", "Molécule chimique transmettant les signaux entre neurones."),
    ("OCD (TOC)", "Trouble obsessionnel compulsif : pensées intrusives et rituels."),
    ("Perception", "Organisation et interprétation des stimuli sensoriels."),
    ("Personnalité", "Ensemble stable de traits caractérisant un individu."),
    ("Phobie", "Peur intense et irrationnelle d'un objet ou situation spécifique."),
    ("Piaget", "Psychologue du développement (1896–1980), stades cognitifs."),
    ("Placebo", "Effet thérapeutique d'une intervention sans principe actif."),
    ("PTSD", "Trouble de stress post-traumatique après événement traumatique."),
    ("Psychose", "Perte de contact avec la réalité (hallucinations, délire)."),
    ("Psychothérapie", "Traitement des troubles psychiques par entretiens structurés."),
    ("Résilience", "Capacité à rebondir face à l'adversité."),
    ("Rogers", "Fondateur de la thérapie centrée sur la personne (1902–1987)."),
    ("Schizophrénie", "Trouble psychotique majeur avec symptômes positifs et négatifs."),
    ("Sérotonine", "Neurotransmetteur impliqué dans l'humeur, sommeil, appétit."),
    ("Skinner", "Behavioriste (1904–1990), conditionnement opérant."),
    ("Stress", "Réponse de l'organisme à une demande environnementale."),
    ("TCC", "Thérapie cognitivo-comportementale, la plus validée empiriquement."),
    ("Transfert", "Projection de sentiments passés sur le thérapeute (psychanalyse)."),
    ("Trauma", "Expérience émotionnellement bouleversante laissant des séquelles."),
    ("Zézaiement", "Répétition involontaire de sons ou syllabes (trouble fluency)."),
]


def build_dict_html():
    entries = []
    for term, defn in DICT:
        entries.append(f'<div class="dict-entry"><dt>{term}</dt><dd>{defn}</dd></div>')
    return "\n".join(entries)


def render_chapter(key, title, slug):
    body = CONTENT[key]
    body = body.replace("{brain}", '<img src="../illustrations/cerveau.svg" alt="Cerveau">')
    body = body.replace("{mindmap_cog}", '<img src="../illustrations/mindmap-cognitive.svg" alt="Carte mentale cognitive">')
    body = body.replace("{pavlov}", '<img src="../illustrations/pavlov.svg" alt="Pavlov">')
    body = body.replace("{maslow}", '<img src="../illustrations/maslow.svg" alt="Maslow">')
    body = body.replace("{timeline}", '<img src="../illustrations/timeline.svg" alt="Timeline">')
    body = body.replace("{dict_entries}", build_dict_html())
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Guide Psychologie</title>
<link rel="stylesheet" href="../styles.css">
</head>
<body>
<nav class="sidebar">
  <a href="../index.html" class="home">🏠 Accueil</a>
  <h3>Chapitres</h3>
  <ul>{nav_links(slug)}</ul>
</nav>
<main class="content">
  <header><h1>{title}</h1></header>
  {body}
  <nav class="chapter-nav">{prev_next(slug)}</nav>
</main>
</body>
</html>"""


def nav_links(current):
    links = []
    for fid, title, slug in CHAPTERS:
        cls = ' class="active"' if slug == current else ""
        links.append(f'<li><a href="{fid}.html"{cls}>{title}</a></li>')
    return "\n".join(links)


def prev_next(current):
    slugs = [s for _, _, s in CHAPTERS]
    idx = slugs.index(current)
    parts = []
    if idx > 0:
        prev_id, prev_title, _ = CHAPTERS[idx - 1]
        parts.append(f'<a href="{prev_id}.html" class="prev">← {prev_title}</a>')
    if idx < len(CHAPTERS) - 1:
        next_id, next_title, _ = CHAPTERS[idx + 1]
        parts.append(f'<a href="{next_id}.html" class="next">{next_title} →</a>')
    return " ".join(parts)


def write_chapters():
    for fid, title, slug in CHAPTERS:
        (CHAP / f"{fid}.html").write_text(render_chapter(slug, title, slug), encoding="utf-8")


def write_index():
    cards = []
    for fid, title, slug in CHAPTERS:
        cards.append(f'<a href="chapitres/{fid}.html" class="chapter-card"><h3>{title}</h3><span>Lire →</span></a>')
    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Guide Enrichi de Psychologie — Illustré</title>
<link rel="stylesheet" href="styles.css">
</head>
<body class="landing">
<header class="hero">
  <div class="hero-inner">
    <p class="badge">Création originale • Gratuit • Illustré</p>
    <h1>Guide Enrichi de Psychologie</h1>
    <p class="subtitle">Naviguer au fil des grandes idées — 10 chapitres, cartes mentales, dictionnaire et illustrations</p>
    <a href="chapitres/00-introduction.html" class="cta">Commencer la lecture →</a>
  </div>
</header>
<section class="chapters-grid">
  <h2>Table des matières</h2>
  <div class="grid">{"".join(cards)}</div>
</section>
<footer>
  <p>Inspiré des structures de <em>Short Cuts Psychologie</em> (Wild, EDP Sciences) et <em>Le Petit Larousse de la Psychologie</em> (Antoine & Angel).</p>
  <p>Contenu pédagogique original — Usage personnel et éducatif.</p>
</footer>
</body>
</html>"""
    (BASE / "index.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    write_illustrations()
    write_chapters()
    write_index()
    print("Guide generated successfully.")
