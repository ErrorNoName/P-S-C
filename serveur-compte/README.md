# Comptes étudiants — API

GitHub Pages (`https://errornoname.github.io/P-S-C/`) est un site **statique**.
Le compte (notes, scores, photo) vit sur l'API
[`https://psychopedia.onrender.com`](https://psychopedia.onrender.com/api/health)
(PostgreSQL). Le navigateur n'est plus la source de vérité.

## Chez toi

```bash
python3 serveur-compte/compte_server.py --static .
```

Ouvre **http://127.0.0.1:8787/** (SQLite de développement, sans `DATABASE_URL`).

## En ligne

Service Render **Psychopédia**, branche `main`. `DATABASE_URL` pointe vers
PostgreSQL (jamais dans le dépôt). Santé :

`https://psychopedia.onrender.com/api/health`

## Google

Origines JavaScript du client OAuth :

```
https://errornoname.github.io
http://127.0.0.1:8787
http://localhost:8787
https://psychopedia.onrender.com
```

## Variables d'environnement

| Variable | Rôle |
|----------|------|
| `PORT` | Port PaaS (Render). |
| `DATABASE_URL` | PostgreSQL en production. Absent = SQLite local. |
| `PSYCLOPEDIA_GOOGLE_CLIENT_ID` | ID OAuth (défaut : ID Psyclopédia). |
| `PSYCLOPEDIA_COMPTE_DB` | Chemin SQLite si pas de `DATABASE_URL`. |
| `PSYCLOPEDIA_COMPTE_HOST` | `0.0.0.0` en production. |

Aucun secret n'appartient au dépôt.

## Tests

```bash
cd serveur-compte
python3 test_compte.py
```
