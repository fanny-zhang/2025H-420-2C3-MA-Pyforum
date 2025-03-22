from bd import BD
from commentaire import Commentaire

class Publication:
    compteur_id = 1
    
    def __init__(self, titre, contenu, auteur, forum_id):
        self.id = Publication.compteur_id
        Publication.compteur_id += 1
        self.titre = titre
        self.contenu = contenu
        self.auteur = auteur
        self.forum_id = forum_id
        self.commentaires = []

    def ajouter_commentaire(self, utilisateur_id, contenu):
        commentaire = Commentaire(contenu, utilisateur_id, self.id)
        self.commentaires.append(commentaire)
        print(f"Commentaire ajouté par {utilisateur_id} sur la publication '{self.titre}'.")
