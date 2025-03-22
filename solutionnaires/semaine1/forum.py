from bd import BD
from publication import Publication

class Forum:
    compteur_id = 1
    
    def __init__(self, nom, description=""):
        self.id = Forum.compteur_id
        Forum.compteur_id += 1
        self.nom = nom
        self.description = description
        self.publications = []
        BD.sauvegarder_forum(self)

    def ajouter_publication(self, utilisateur_id, titre, contenu):
        publication = Publication(titre, contenu, utilisateur_id, self.id)
        self.publications.append(publication)
        BD.sauvegarder_forum(self)
        print(f"Publication '{titre}' ajoutée au forum '{self.nom}' par {utilisateur_id}.")
