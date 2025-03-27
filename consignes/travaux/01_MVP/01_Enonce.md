# Projet PyForum – Développement du MVP

## Introduction au MVP

Un **MVP (Minimal Viable Product)** est une version simplifiée d'un produit,
qui contient uniquement les fonctionnalités essentielles pour valider les
hypothèses de base et permettre une première utilisation. Le but du MVP est de
démontrer que l'application fonctionne avec un ensemble limité de
fonctionnalités, tout en laissant place à des évolutions futures.

## Objectifs

Dans cette première étape du projet PyForum, vous allez développer un **MVP**
qui comprend les fonctionnalités de base suivantes :

- Un seul type d'utilisateur, qui pourra :
  - Créer un forum
  - Créer une publication dans un forum
  - Ajouter un commentaire à une publication
  - Joindre un forum

## Étape 1 : Diagramme UML



### Diagramme de cas d'utilisation

Écrire le diagramme de cas d'utilisation pour les fonctionnalités de base du



Vous devrez créer les classes et les méthodes nécessaires pour ces cas
d'utilisation, en respectant les exigences suivantes :

## Fonctionnalités à développer

### 1. Création d'un Utilisateur

Un utilisateur pourra s'inscrire en créant un compte. Chaque utilisateur doit
contenir :
- Un identifiant unique
- Un nom d'utilisateur
- Une adresse email
- Un mot de passe (dans cette première phase, vous pouvez ignorer la gestion
  sécurisée des mots de passe)
- Une liste vide de forums auxquels il est inscrit

### 2. Création d'un forum

L'utilisateur pourra créer un forum. Chaque forum doit contenir :
- Un identifiant unique
- Un nom
- Une description (optionnelle)
- Une liste vide de publications (initialisée à une liste vide)

### 3. Création d'une publication

L'utilisateur pourra créer une publication dans un forum. Chaque publication
doit contenir :
- Un identifiant unique
- Un titre
- Un contenu
- L'identifiant de l'auteur 
- L'identifiant du forum auquel elle appartient
- Une liste de commentaires (qui est initialisée à une liste vide)

### 4. Ajout d'un commentaire

L'utilisateur pourra ajouter un commentaire à une publication. Chaque
commentaire doit contenir :
- Un identifiant unique
- L'identifiant de l'auteur
- Le contenu du commentaire
- L'identifiant de la publication à laquel il appartient

### 5. Joindre un forum

L'utilisateur pourra rejoindre un forum existant. Chaque utilisateur pourra
s'ajouter à un ou plusieurs forums. Lorsqu'un utilisateur rejoint un forum, ce
forum est rajouté a sa liste de forums.

## Classe BD

Une classe **BD** (Base de Données) vous sera fournie (voir
`fichiers_fournis/mvp/bd.py`) pour gérer l'enregistrement et la récupération
des données dans des fichiers JSON. Cette classe ne contient pour l'instant que
des méthodes "bidon", et qui seront remplacés par une implémentation logique
dans les semaines à venir. Cette classe contiendra des méthodes pour :

- Sauvegarder un forum, une publication ou un commentaire
- Charger un forum, une publication ou un commentaire
- Gérer l'ajout des utilisateurs aux forums

**Méthodes de la classe BD à utiliser :**
- **`sauvegarder_forum(forum)`** : Sauvegarde les informations d'un forum.
- **`sauvegarder_publication(forum_id, publication)`** : Sauvegarde une publication dans le forum correspondant (utilise l'ID du forum).
- **`sauvegarder_commentaire(publication_id, commentaire)`** : Sauvegarde un commentaire dans une publication donnée (utilise l'ID de la publication).
- **`sauvegarder_utilisateur(forum_id, utilisateur)`** : Sauvegarde l'inscription d'un utilisateur à un forum.
- **`charger_forums()`** : Charge tous les forums depuis la base de données (fichiers JSON).
- **`charger_publications(forum_id)`** : Charge toutes les publications d'un forum donné.
- **`charger_commentaires(publication_id)`** : Charge tous les commentaires d'une publication donnée.
- **`charger_utilisateurs(forum_id)`** : Charge tous les utilisateurs inscrits à un forum donné.

### Exemple d'utilisation des méthodes BD dans les cas d'utilisation

- **Créer un utilisateur :**
  - L'utilisateur entre un nom d'utilisateur, une adresse email et un mot de passe.
  - La méthode **`sauvegarder_utilisateur(utilisateur)`** est appelée pour enregistrer l'utilisateur dans la base de données.

- **Créer un forum :**
  - L'utilisateur entre un nom et une description pour le forum.
  - La méthode **`sauvegarder_forum(forum)`** est appelée pour enregistrer le forum dans un fichier JSON.

- **Créer une publication :**
  - L'utilisateur entre un titre et un contenu pour la publication.
  - La méthode **`sauvegarder_publication(forum_id, publication)`** est appelée pour enregistrer la publication dans le forum spécifié.

- **Ajouter un commentaire :**
  - L'utilisateur entre le contenu du commentaire.
  - La méthode **`sauvegarder_commentaire(publication_id, commentaire)`** est appelée pour enregistrer le commentaire dans la publication correspondante.

- **Joindre un forum :**
  - L'utilisateur entre l'ID du forum qu'il souhaite rejoindre.
  - La méthode **`sauvegarder_utilisateur(forum_id, utilisateur)`** est appelée pour ajouter l'utilisateur à la liste des membres du forum.

## Fichier main.py - Description et utilisation

Le fichier main.py vous est founir (`fichiers_fournis/mvp/main.py`) représente
l'interface principale de l'application PyForum, permettant de simuler le
fonctionnement de base de l'application à travers un menu interactif dans le
terminal. Ce fichier contient une boucle principale qui affiche un menu et
permet à l'utilisateur de choisir une action parmi plusieurs options
disponibles. Vous devrez rajouter du code à ce fichier afin d'utiliser les
classes et méthodes que vous avez créés.

## Astuces

- Pour gérer les identifiants uniques, il est recommandé d'utiliser des
  attributs de classe, qui enregistre le dernier identifiant unique utilisé, et
  qui s'incrémente à chaque création.

## Exigences techniques

- Utilisez la **programmation orientée objet** pour modéliser les utilisateurs,
  forums, publications, commentaires, et utilisateurs comme des classes avec
  des attributs et des méthodes appropriées.
- Organisez votre code en plusieurs fichiers Python si nécessaire.
