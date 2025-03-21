class BD:
    def __init__(self):
        print("Base de données initialisée.")

    def sauvegarder_utilisateur(self, utilisateur):
        """Simule la sauvegarde d'un utilisateur dans la base de données."""
        print(f"[Simulé] Sauvegarde de l'utilisateur: {utilisateur.nom_utilisateur}")

    def sauvegarder_forum(self, forum):
        """Simule la sauvegarde d'un forum dans la base de données."""
        print(f"[Simulé] Sauvegarde du forum: {forum.nom}")

    def sauvegarder_publication(self, forum_id, publication):
        """Simule la sauvegarde d'une publication dans un forum."""
        print(f"[Simulé] Sauvegarde de la publication '{publication.titre}' dans le forum {forum_id}")

    def sauvegarder_commentaire(self, publication_id, commentaire):
        """Simule la sauvegarde d'un commentaire dans une publication."""
        print(f"[Simulé] Sauvegarde du commentaire '{commentaire.contenu}' pour la publication {publication_id}")

    def sauvegarder_utilisateur_forum(self, forum_id, utilisateur):
        """Simule l'ajout d'un utilisateur à un forum."""
        print(f"[Simulé] Ajout de l'utilisateur {utilisateur.nom_utilisateur} au forum {forum_id}")

    def charger_utilisateurs(self):
        """Simule le chargement des utilisateurs."""
        print("[Simulé] Chargement des utilisateurs...")
        return []

    def charger_forums(self):
        """Simule le chargement des forums."""
        print("[Simulé] Chargement des forums...")
        return []

    def charger_publications(self, forum_id):
        """Simule le chargement des publications d'un forum."""
        print(f"[Simulé] Chargement des publications du forum {forum_id}...")
        return []

    def charger_commentaires(self, publication_id):
        """Simule le chargement des commentaires d'une publication."""
        print(f"[Simulé] Chargement des commentaires pour la publication {publication_id}...")
        return []

    def charger_utilisateurs_forums(self):
        """Simule le chargement des utilisateurs inscrits aux forums."""
        print("[Simulé] Chargement des utilisateurs des forums...")
        return []
