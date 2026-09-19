# Discord communautaire Psyclopédia

Architecture, textes d'orientation et scripts pour **effacer le plan par défaut**
et rebâtir le serveur [Psyclopédia](https://errornoname.github.io/P-S-C).

La liste exacte des catégories, salons, tags et rôles est dans
[`structure.md`](structure.md) et [`blueprint.py`](blueprint.py).
Les embeds (accueil, règles, guide en 7 parties, cours, soutien, numéros d'aide)
sont dans [`embeds.py`](embeds.py).

## Ne jamais exposer le jeton

Le jeton du bot **ne doit pas** figurer dans le dépôt, les tickets ou les captures.

```bash
# recommandé
export DISCORD_BOT_TOKEN='…'          # dans le shell uniquement
# ou
install -m 600 /dev/stdin /tmp/.psyc_discord_token
# ou copier .env.example → discord/.env (déjà gitignoré)
```

Si un jeton a déjà circulé en clair, **le régénérer** sur
<https://discord.com/developers/applications> → Bot → Reset Token.

## Déployer le serveur (une fois)

Le script parle à l'API REST v10, sans dépendance tierce.

```bash
cd discord
python3 test_blueprint.py
python3 deploy_server.py --dry-run    # inventaire, zéro appel réseau
python3 deploy_server.py              # crée rôles, Community, salons, embeds
```

Ordre réel du déploiement :

1. Créer les rôles (équipe, modération, niveaux, intérêts).
2. Créer `📜-regles` et `🛠️-journal-equipe`, activer **Community**
   (forums + salons d'annonces). Si Discord refuse, repli en salons texte.
3. Créer les 7 catégories et **tous** les salons, dans l'ordre.
4. Verrouiller les salons d'information ; masquer 🔒・Équipe.
5. Poster et épingler les embeds ; ouvrir un fil « Accueil » dans chaque forum.
6. Renommer la guilde en **Psyclopédia**, locale `fr`, salon système = bienvenue.
7. Enregistrer les slash commands de guilde.
8. Supprimer les salons Discord d'origine (`général`, `Lounge`, etc.).

Relancer le script est **idempotent** : les salons existants sont mis à jour,
les embeds déjà épinglés ne sont pas doublés (sauf `--repost`).

## Bot long-courrier

`deploy_server.py` laisse un serveur **déjà lisible**. `bot.py` ajoute :

- rôle **🌱 Nouveau** à l'arrivée ;
- message de bienvenue ;
- `/guide` `/regles` `/planning` `/site` `/aide` `/cours` `/roles`
  (menus de sélection pour niveau et intérêts).

```bash
python3 -m pip install -r requirements.txt
# Portail développeur : Privileged Gateway Intents → Server Members Intent
python3 bot.py
```

Sans processus hôte, les commandes slash resteront sans réponse : ce n'est
pas bloquant, les murs d'orientation suffisent.

Inviter le bot (permissions Administrateur, une fois) :

```
https://discord.com/oauth2/authorize?client_id=APPLICATION_ID&permissions=8&scope=bot%20applications.commands
```

## Charte

| Jeton | Couleur | Usage |
|---|---|---|
| Vert | `#50A67E` | Accueil, cours, savoir |
| Or | `#E3AE33` | Planning, rôles, méthodes |
| Rose | `#C7395D` | Règles, clinique, aide |
| Gris | `#575E5B` | Histoire, hors-sujet, staff |

## Cadre pédagogique

Le serveur **n'est pas un soin**. Les embeds de 🤍-soutien-mutuel et de
🩺-clinique rappellent 15 / 112 / 3114 / 3919 / 119 et la
[page Aide](https://errornoname.github.io/P-S-C/livres-psychologie/07-ebook-final/aide.html).
Aucun instrument psychométrique propriétaire n'est recopié.
