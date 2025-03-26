# Installer PyForum


## Cloner le dépôt

Vous pouvez cloner ce dépôt en utilisant la commande suivante :

```bash
git clone https://github.com/archambaultv-prof/2025H-420-2C3-MA-Pyforum
```

Ceci créera un dossier `2025H-420-2C3-MA-Pyforum` dans le répertoire courant.

## Créer un environnement virtuel

Pour créer un environnement virtuel, vous pouvez utiliser la commande suivante :

```bash
python -m venv .venv
```
ou le créer depuis VSCode directement.

Vous pouvez ensuite activer l'environnement virtuel en utilisant la commande
suivante sur Windows :

```bash
.venv\Scripts\Activate
```


## Installer les dépendances de développement

Pour installer les dépendances de développement, un fois votre environnement
 virtuel activé, vous pouvez utiliser la commande suivante :

```bash
pip install -r requirements-dev.txt
```