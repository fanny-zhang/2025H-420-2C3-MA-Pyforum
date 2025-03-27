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

## Fonctionnalités à développer

Cette section présente les fonctionnalités de base à développer pour le MVP de
PyForum. La section [À vous de jouer !](#à-vous-de-jouer) contient les
instructions détaillées de ce que vous devez réaliser.

### 1. Création d'un utilisateur

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

Une classe **BD** (Base de Données) vous sera fournie  pour gérer
l'enregistrement et la récupération des données dans des fichiers JSON. Cette
classe ne contient pour l'instant que des méthodes "bidon", et qui seront
remplacés par une implémentation logique dans les semaines à venir. Cette
classe contiendra des méthodes pour :

- Sauvegarder un forum, une publication ou un commentaire
- Charger un forum, une publication ou un commentaire
- Gérer l'ajout des utilisateurs aux forums

Les différentes méthodes de la classe BD sont documentées dans le fichier
`src/pyforum/bd.py`. La plupart acceptent des objets de type `Forum`,
`Utilisateur`, etc. en paramètre. Dans le cadre du MVP, ces objets
doivent surcharger la méthode `__str__` pour permettre l'affichage des objets
dans le terminal.

## Fichier main.py - Description et utilisation

Le fichier `__main__.py` représente
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

## À vous de jouer !

## Étape 1 : Diagramme UML

Vous devez commencer par créer des diagramme UML pour modéliser le MVP. Le
fichier [02_Mermaid.md](./02_Mermaid.md) contient une introduction à la syntaxe
Mermaid pour créer des diagrammes UML.

Créez les diagrammes dans le fichier `src/pyforum/UML/mvp.md`.

#### Diagramme de cas d'utilisation

Créer un diagramme de cas d'utilisation pour l'utilisateur en fonction
de la description donnée à la section [Objectifs](#objectifs).

#### Diagramme de classes

En fonction de la description à la section [Fonctionnalités à développer](#fonctionnalités-à-développer),
créez un diagramme de classes pour modéliser les classes et les relations entre
elles. Les classes à modéliser sont :

- Utilisateur
- Forum
- Publication
- Commentaire

N'oubliez pas de modéliser les attributs et les méthodes de chaque classe,
ainsi que les relations d'agrégation et de composition.

## Étape 2 : Implémentation des classes

Créez les classes `Utilisateur`, `Forum`, `Publication`, et `Commentaire` dans
le dossier `src/pyforum` en fonction du diagramme de classes que vous avez
créé. Faite un fichier par classe.

## Étape 3 : Compléter le fichier MVP

Complétez le fichier `src/pyforum/mvp.py` pour permettre à l'utilisateur
d'interagir avec l'application. La partie à compléter est indiquée par des
commentaires `TODO` dans la fonction `main()`.
