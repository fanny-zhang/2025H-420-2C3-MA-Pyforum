class Commentaire:
    compteur_id = 1
    
    def __init__(self, contenu, auteur, publication_id):
        self.id = Commentaire.compteur_id
        Commentaire.compteur_id += 1
        self.contenu = contenu
        self.auteur = auteur
        self.publication_id = publication_id