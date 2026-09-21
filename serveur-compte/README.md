# Comptes étudiants — API SQLite

GitHub Pages (`https://errornoname.github.io/P-S-C/`) est un site **statique** :
il ne peut pas faire tourner SQLite. Sans API, le navigateur utilise IndexedDB
(un seul appareil).

## Chez toi (base réelle tout de suite)

```bash
python3 serveur-compte/compte_server.py --static .
```

Ouvre **http://127.0.0.1:8787/** (pas github.io). Le bandeau doit dire
« Base SQLite distante ».

## En ligne (sync téléphone + ordinateur)

Il faut une URL HTTPS publique de **cette** API. Le plus rapide :

1. Compte Render : https://dashboard.render.com/register
2. Nouveau Web Service : https://dashboard.render.com/select-repo?type=web
3. Branche le dépôt **ErrorNoName/P-S-C**, branche `main`.
4. Runtime Python, commande de démarrage :

```
python3 serveur-compte/compte_server.py --host 0.0.0.0 --port $PORT
```

5. Health check : `/api/health`
6. Crée le service. Tu obtiens une URL du type `https://psyclopedia-compte.onrender.com`.

Blueprint (même dépôt) : https://dashboard.render.com/blueprint/new

Vérifie : `https://TON-API.onrender.com/api/health` doit renvoyer `{"ok": true, ...}`.

### Google (après l’URL)

Ajoute **l’origine** de l’API (sans chemin) ici :

https://console.cloud.google.com/apis/credentials/oauthclient/340597672237-fscmcisrorgrkh3uppbvtj69848gj6nc.apps.googleusercontent.com?project=vrvaultdatabase

Exemple : `https://psyclopedia-compte.onrender.com`

## Ce qu’il faut renvoyer pour brancher le site

Uniquement l’URL HTTPS de l’API, sans slash final, par exemple :

```
https://psyclopedia-compte.onrender.com
```

On la met dans `assets-ebook/js/compte-config.js` (`apiUrl`) et on publie sur `main`.
Aucun secret n’est nécessaire (l’ID Google est déjà public).

## Variables d’environnement

| Variable | Rôle |
|----------|------|
| `PORT` | Port PaaS (Render/Fly). |
| `PSYCLOPEDIA_GOOGLE_CLIENT_ID` | ID OAuth (défaut : ID Psyclopédia). |
| `PSYCLOPEDIA_COMPTE_DB` | Chemin du fichier SQLite. |
| `PSYCLOPEDIA_COMPTE_HOST` | `0.0.0.0` en production. |

## Tests

```bash
cd serveur-compte
python3 test_compte.py
```
