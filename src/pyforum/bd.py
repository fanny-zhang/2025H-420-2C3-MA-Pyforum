class BD:
    def __init__(self):
        self.utilisateurs = []
        self.forums = []
        self.publications = []
        self.commentaires = []
        self.utilisateurs_forums = {}
        print("Base de données initialisée.")
    
    def sauvegarder_utilisateur(self, utilisateur):
        for i, existing_user in enumerate(self.utilisateurs):
            if existing_user.id == utilisateur.id:
                self.utilisateurs[i] = utilisateur  # Mise à jour de l'utilisateur existant
                print(f"[Simulé] Mise à jour de l'utilisateur: {utilisateur}")
                return
        self.utilisateurs.append(utilisateur)  # Ajout de l'utilisateur s'il n'existe pas
        print(f"[Simulé] Sauvegarde de l'utilisateur: {utilisateur}")
    
    def sauvegarder_forum(self, forum):
        for i, existing_forum in enumerate(self.forums):
            if existing_forum.id == forum.id:
                self.forums[i] = forum  # Mise à jour du forum existant
                print(f"[Simulé] Mise à jour du forum: {forum}")
                return
        self.forums.append(forum)  # Ajout du forum s'il n'existe pas
        print(f"[Simulé] Sauvegarde du forum: {forum}")

    def sauvegarder_publication(self, publication):
        for i, existing_publication in enumerate(self.publications):
            if existing_publication.id == publication.id:
                self.publications[i] = publication  # Mise à jour de la publication existante
                print(f"[Simulé] Mise à jour de la publication: {publication}")
                return
        self.publications.append(publication)  # Ajout de la publication si elle n'existe pas
        print(f"[Simulé] Sauvegarde de la publication: {publication}")

    def sauvegarder_commentaire(self, commentaire):
        for i, existing_commentaire in enumerate(self.commentaires):
            if existing_commentaire.id == commentaire.id:
                self.commentaires[i] = commentaire  # Mise à jour du commentaire existant
                print(f"[Simulé] Mise à jour du commentaire: {commentaire}")
                return
        self.commentaires.append(commentaire)  # Ajout du commentaire s'il n'existe pas
        print(f"[Simulé] Sauvegarde du commentaire: {commentaire}")

    def obtenir_forum_par_nom(self, nom_forum):
        return next((forum for forum in self.forums if forum.nom == nom_forum), None)
    
    def obtenir_utilisateur_par_nom(self, nom_utilisateur):
        return next((utilisateur for utilisateur in self.utilisateurs if utilisateur.nom == nom_utilisateur), None)
    
    def obtenir_publication_par_titre(self, titre_publication):
        return next((publication for publication in self.publications if publication.titre == titre_publication), None)

     


    