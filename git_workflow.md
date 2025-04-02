# Workflow Git suggéré

## Objectif
Vous allez créer un dépôt Git basé sur ce projet tout en conservant la possibilité de récupérer les mises à jour des nouveaux énoncés. Vous avez le choix de travailler sur Gitlab ou sur Github.

---

## 1. Créer votre propre dépôt Git
### Option 1 : Travailler sur GitHub
1. **Forkez** le dépôt du professeur sur GitHub.
2. **Clonez votre fork** sur votre machine :
   ```sh
   git clone <URL_DU_REPO_ETUDIANT>
   cd <NOM_DU_REPO>
   ```

### Option 2 : Travailler sur GitLab
1. **Créez un nouveau dépôt vide** sur GitLab.
2. **Clonez le dépôt** sur votre machine :
   ```sh
   git clone <URL_DU_REPO_GITLAB>
   cd <NOM_DU_REPO>
   ```
3. **Ajoutez le dépôt du professeur comme remote** (voir section suivante).

---

## 2. Ajouter le dépôt du professeur comme remote (upstream)
Dans votre dépôt local, exécutez :
```sh
git remote add upstream <URL_DU_REPO_PROF>
```

Vérifiez que l’ajout a bien été fait :
```sh
git remote -v
```

Vous devriez voir quelque chose comme :
```
origin    <URL_DU_REPO_ETUDIANT> (fetch)
origin    <URL_DU_REPO_ETUDIANT> (push)
upstream  <URL_DU_REPO_PROF> (fetch)
upstream  <URL_DU_REPO_PROF> (push)
```

---

## 3. Récupérer les mises à jour du professeur
Lorsque de nouveaux énoncés sont publiés, suivez ces étapes pour récupérer les modifications sans écraser votre travail :

1. **Récupérer les changements du professeur** :
   ```sh
   git fetch upstream
   ```
2. **Fusionner les nouvelles mises à jour dans votre branche principale** :
   ```sh
   git merge upstream/main
   ```
3. **Pousser les changements vers votre propre dépôt** :
   ```sh
   git push origin main
   ```

---

## 4. Travailler sur votre projet
Vous pouvez maintenant modifier le code, ajouter des fichiers et committer vos modifications normalement :

```sh
git add .
git commit -m "Ajout d'une nouvelle fonctionnalité"
git push origin main
```

---