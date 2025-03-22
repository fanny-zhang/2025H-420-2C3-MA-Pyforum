class BD:
    def __init__(self):
        print("Base de données initialisée.")
    
    @staticmethod
    def sauvegarder_utilisateur(utilisateur):
        """Simule la sauvegarde d'un utilisateur dans la base de données."""
        print(f"[Simulé] Sauvegarde de l'utilisateur: {utilisateur.nom}")
    @staticmethod
    def sauvegarder_forum(forum):
        """Simule la sauvegarde d'un forum dans la base de données."""
        print(f"[Simulé] Sauvegarde du forum: {forum.nom}")
    
    @staticmethod
    def sauvegarder_publication(forum_id, publication):
        """Simule la sauvegarde d'une publication dans un forum."""
        print(f"[Simulé] Sauvegarde de la publication '{publication.titre}' dans le forum {forum_id}")

    @staticmethod
    def sauvegarder_commentaire(publication_id, commentaire):
        """Simule la sauvegarde d'un commentaire dans une publication."""
        print(f"[Simulé] Sauvegarde du commentaire '{commentaire.contenu}' pour la publication {publication_id}")

    @staticmethod
    def sauvegarder_utilisateur_forum(forum_id, utilisateur):
        """Simule l'ajout d'un utilisateur à un forum."""
        print(f"[Simulé] Ajout de l'utilisateur {utilisateur.nom_utilisateur} au forum {forum_id}")

    @staticmethod
    def charger_utilisateurs():
        """Simule le chargement des utilisateurs."""
        print("[Simulé] Chargement des utilisateurs...")
        return []

    @staticmethod
    def charger_forums():
        """Simule le chargement des forums."""
        print("[Simulé] Chargement des forums...")
        return []

    @staticmethod
    def charger_publications(forum_id):
        """Simule le chargement des publications d'un forum."""
        print(f"[Simulé] Chargement des publications du forum {forum_id}...")
        return []

    @staticmethod
    def charger_commentaires(publication_id):
        """Simule le chargement des commentaires d'une publication."""
        print(f"[Simulé] Chargement des commentaires pour la publication {publication_id}...")
        return []

    @staticmethod
    def charger_utilisateurs_forums():
        """Simule le chargement des utilisateurs inscrits aux forums."""
        print("[Simulé] Chargement des utilisateurs des forums...")
        return []
