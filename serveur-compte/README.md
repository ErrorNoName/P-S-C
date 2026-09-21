# Comptes étudiants — API SQLite

Serveur HTTP en bibliothèque standard Python : base **SQLite** réelle, sessions
Bearer, hachage **PBKDF2-SHA256** (210 000 itérations), notes de cours, notes de
quiz et instantané de progression.

## Lancer le site avec la base

Depuis la racine du dépôt :

```bash
python3 serveur-compte/compte_server.py --static .
# http://127.0.0.1:8787/
```

Les fichiers de données (`serveur-compte/data/`) ne sont pas versionnés.

## Variables d'environnement

| Variable | Rôle |
|----------|------|
| `PSYCLOPEDIA_GOOGLE_CLIENT_ID` | Identifiant client OAuth Google (public). Sans lui, seule la connexion e-mail/mot de passe est active. |
| `PSYCLOPEDIA_COMPTE_PORT` | Port d'écoute (défaut `8787`). |
| `PSYCLOPEDIA_COMPTE_DB` | Chemin du fichier SQLite. |
| `PSYCLOPEDIA_COMPTE_HOST` | Adresse d'écoute (défaut `127.0.0.1`). |

Aucun secret n'est commité. Un jeton de session est un aléa stocké en base, pas
un JWT signé avec une clé du dépôt.

## GitHub Pages

Le site public reste statique. Sans API joignable, le navigateur enregistre le
compte dans **IndexedDB** (même appareil). Dès que `apiUrl` est renseigné dans
`assets-ebook/js/compte-config.js`, e-mail, notes et notes de quiz synchronisent
vers cette base SQLite.

## Tests

```bash
cd serveur-compte
python3 test_compte.py
```
