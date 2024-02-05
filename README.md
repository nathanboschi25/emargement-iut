# emargement-iut

Script python permettant de générer la fiche d'émargement pour les alternants de l'IUT NFC (Dept. INFO)

## Pré-requis

- Python 3.6 ou supérieur
- python3-venv
- Connexion VPN IUT
- Avoir configuré une connexion SSH par clé publique/privée avec l'IUT
- nmcli pour la connexion VPN

## Installation

- Cloner le dépôt
- Créer un environnement virtuel python3-venv
- Activer l'environnement virtuel
- Installer les dépendances avec `pip install -r requirements.txt`
- Désactiver l'environnement virtuel
- Configurer les variables d'environnement (voir ci-dessous)

> **Note :** Le script `./install` permet d'automatiser l'installation en réalisant les étapes ci-dessus.

### Variables d'environnement

Le fichier `.env.example` contient un exemple de fichier de configuration. Il faut le renommer en `.env` et modifier les
valeurs des variables suivantes :

- `WKHTMLTOPDF_PATH` : Chemin vers l'exécutable `wkhtmltopdf` (ex: `/usr/bin/wkhtmltopdf`) - a modifier si OS != Linux
- `DEPT` : Nom du département (ex: `info`)
- `CLASS` : Nom de la classe (ex: `AltS3-1`)
- `ADE_URL` : URL de l'export .ics de l'emploi du temps sur ADE pour l'année
- `STUDENTS` : Liste des **étudiants** à afficher sur la fiche d'émargement (séparés par des virgules)
- `TEACHERS` : Liste de tous les **enseignants** (séparés par des virgules)
- `VPN_NAME` : Nom de votre connexion VPN (ex: `VPN IUT` - liste des connexions avec `nmcli con show`)
- `SSH_HOST` : Nom d'hôte du serveur SSH (ex: `912e009-01.iut-bm.univ-fcomte.fr`)
- `SSH_USER` : Nom d'utilisateur du serveur SSH (ex: `nboschi`)
- `PRINTER_ADDRESS` : Adresse de l'imprimante (ex: `HP_Espace_Etu`)

## Utilisation

Le script principal est `./generate`. Il s'exécute **automatiquement** dans l'env. virtuel.

### Aide

```
╰─$ ./generate -h
usage: generate [-h] [-e ENV_VERSION] [-q] [-t TEMPLATE] [-o OUTPUT] [-d DAY]

Generate signature paper from a template file.

options:
  -h, --help            show this help message and exit
  -e ENV_VERSION, --env-version ENV_VERSION
                        Env file path
  -q, --quick           Quick mode - no questions asked - document is printed if possible
  -t TEMPLATE, --template TEMPLATE
                        Template file path
  -o OUTPUT, --output OUTPUT
                        Output file path
  -d DAY, --day DAY     Day to generate - format "1999-12-31"
```

