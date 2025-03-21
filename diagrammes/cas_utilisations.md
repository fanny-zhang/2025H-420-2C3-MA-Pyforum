# Diagramme cas d'utilisations

Diagramme utilisateur 
-  Créer un forum
-  Joindre un forum
-  Écrire une publication
-  Écrire un commentaire
-  Voter pour un commentaire
-  Voter pour une publication
-  Clavardage

```mermaid
flowchart LR
    Utilisateur["Utilisateur"]
    Administrateur["Administrateur"]
    Utilisateur --- A["Créer un forum"]
    Utilisateur --- B["Joindre un forum"]
    Utilisateur --- C["Écrire une publication"]
    Utilisateur --- D["Écrire un commentaire"]
    Utilisateur --- E["Voter pour un commentaire"]
    Utilisateur --- F["Voter pour une publication"]
    Utilisateur --- G["Clavardage"]

    Moderateur["Modérateur"]
    Moderateur --- H["Modérer une publication"]
    Moderateur --- I["Modérer un commentaire"]

    Administrateur --- J["Sauvegarder la base de données"]
    Administrateur --- K["Restaurer la base de données"]
    Administrateur --- L["Supprimer un forum"]
    Administrateur --- M["Supprimer un utilisateur"]
```

