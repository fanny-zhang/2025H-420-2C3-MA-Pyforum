class Publication:
    identifiant = 0
    def __init__(self, titre, contenu, id_auteur, id_forum):
        self.identifiant = Publication.identifiant
        Publication.identifiant += 1
        self.titre = titre
        self.contenu = contenu
        self.id_auteur = id_auteur  # à revoir
        self.id_forum = id_forum  # à revoir
        self.commentaires = []
