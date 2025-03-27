# Tests unitaires

Tout projet de programmation nécessite des tests unitaires pour valider le bon
fonctionnement de l'application. Dans ce projet, vous devrez écrire des tests
unitaires et certains tests seront fournis pour valider le bon fonctionnement de
votre application.

Pour vous aider, la structure des tests est déjà en place dans le dossier
`tests` du dépôt et le module `pytest` de Python est déjà installé dans le
fichier `requirements-dev.txt`.

## Pytest

Pytest est un framework de test pour Python qui permet d'écrire des tests
unitaires. Dans le cadre de ce projet, on utilisera sa capacité à détecter les
tests automatiquement et à les exécuter automatiquement.

Pour exécuter les tests, vous pouvez utiliser la commande suivante :

```bash
pytest
```

Ceci n'est pas de la magie. Le fichier `pyproject.toml` contient une section
`[tool.pytest.ini_options]` qui indique à `pytest` de chercher les fichiers de
tests dans le dossier `tests`. Ensuite `pytest` va chercher les fichiers de
tests qui commencent par `test_` et exécuter les fonctions qui commencent par
`test_`.

Chaque fonction de test doit retourner `True` si le test est réussi et `False`
sinon. On utilise des assertions pour vérifier les résultats des fonctions.
Voici un exemple trivial de test :

```python
def test_addition():
    assert 1 + 1 == 2
```