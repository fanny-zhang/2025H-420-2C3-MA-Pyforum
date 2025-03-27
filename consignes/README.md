# PyForum

## Introduction

Dans ce projet, vous allez développer une application inspiré de
Reddit appelée **PyForum**, qui sera un forum en ligne où les utilisateurs
peuvent créer des discussions, poster des contenus, interagir via des
commentaires, et gérer des forums.

## Objectif du projet

L'objectifs de PyForum est de mettre en pratique les notions de programmation
objet vues depuis le début du cours ainsi que les nouvelles notions qui seront
enseignées au cours des prochaines semaines. Plutôt que d'avoir une série
d'exercices indépendants, vous travaillerez sur un projet qui évoluera
au fil des semaines.


## Description générale de PyForum

Voici une description générale des fonctionnalités de PyForum. Les détails
spécifiques de chaque fonctionnalité seront expliqués dans les consignes.

### 1. Création de Forums

Les utilisateurs pourront créer des forums sur des sujets variés. Chaque forum
aura un modérateur désigné, qui aura des droits supplémentaires pour gérer les
publications et les commentaires. Les utilisateurs pourront se joindre aux
forums sur les sujets qui les intéressent.

### 2. Création de publications et commentaires

Les utilisateurs pourront ajouter des publications dans les forums, et d'autres
utilisateurs pourront commenter ces publications. Chaque commentaire ou
publication pourra être **voté positivement** par les autres utilisateurs. 

### 3. Les types d'utilisateurs

- **Utilisateurs Standards** : Ils pourront créer des forums et joindre des
  forums existants, créer des publications et ajouter des commentaires sur les
  publications. Ils pourront également voter positivement les publications et
  les commentaires des autres utilisateurs.

- **Modérateurs** : Les modérateurs auront des droits supplémentaires, comme la
  possibilité de supprimer des publications ou des commentaires dans le forum
  qu'ils modèrent.  

- **Administrateurs Système** : Ils auront un accès complet au système,
  permettant de gérer la base de données, supprimer des utilisateurs ou des
  forums, et effectuer des sauvegardes ou restaurations de la base de données.

### 4. Gestion des notifications

Les utilisateurs pourront définir leurs préférences de notifications. Par
exemple, un utilisateur pourra être notifié lorsqu'un autre utilisateur vote
pour l’un de ses posts ou commentaires.

### 5. Message entre Utilisateurs

Une fonctionnalité de **messages** permettra aux utilisateurs de discuter
entre eux en privé. Pour simplifier, cette fonctionnalité sera limitée à
l'envoi de messages textuels entre deux utilisateurs du type courriel
plutôt que de créer une messagerie instantanée.

### 6. Base de données

La base de données de PyForum sera simplifiée et stockée sous forme de
fichiers JSON et CSV. Vous devrez manipuler ces fichiers pour enregistrer, mettre
à jour, et récupérer les informations nécessaires au bon fonctionnement de
l’application.

Nous n'utiliserons pas de base de données SQL pour ce projet pour favoriser
l'apprentissage de la manipulation de fichiers. Notez toutefois que normalement
dans un tel projet, une base de données SQL serait utilisée pour gérer les
données.

### 7. Interface Utilisateur

Vous aurez à développer une interface utilisateur. Dans un premier temps, celle-ci
sera une interface en ligne de commande (CLI) pour simplifier le développement.
Par la suite, vous pourrez développer une interface graphique (GUI) pour
améliorer l'expérience utilisateur.


## Collaboration en équipe

Vous travaillerez en équipe **de 2** pour développer l’application. L'intégration de
votre travail se fera via **Git** et chaque membre de l'équipe devra
contribuer à différentes parties du projet.

## Échéancier

Les tâches à effectuer à chaque semaine vous seront communiquées par les
professeurs.

## Et maintenant ?

Voici quelques liens vers les consignes et guides pour vous aider à démarrer :

- [Installation de PyForum](./installation.md)
- [Travail no 1 : MVP](./travaux/01_MVP/01_Enonce.md)
- [Tests unitaires](./tests.md)