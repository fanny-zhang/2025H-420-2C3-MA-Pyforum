# Exemple d'utilisation des méthodes BD dans les cas d'utilisation

class BD:
    def __init__(self):
        print("Base de données initialisée.")

    @staticmethod
    def sauvegarder_utilisateur(utilisateur):
        """Simule la sauvegarde d'un utilisateur dans la base de données.

        Paramètre:
            utilisateur (Utilisateur): L'utilisateur à sauvegarder.
        """
        print(f"[Simulé] Sauvegarde de l'utilisateur: {utilisateur}")

    @staticmethod
    def sauvegarder_forum(forum):
        """Simule la sauvegarde d'un forum dans la base de données.

        Paramètre:
            forum (Forum): Le forum à sauvegarder.
        """
        print(f"[Simulé] Sauvegarde du forum: {forum}")

    @staticmethod
    def sauvegarder_publication(forum_id, publication):
        """Simule la sauvegarde d'une publication dans un forum.

        Paramètres:
            forum_id (int): L'identifiant du forum.
            publication (Publication): La publication à sauvegarder.
        """
        print(f"[Simulé] Sauvegarde de la publication '{publication}' dans le forum {forum_id}")

    @staticmethod
    def sauvegarder_commentaire(publication_id, commentaire):
        """Simule la sauvegarde d'un commentaire dans une publication.

        Paramètres:
            publication_id (int): L'identifiant de la publication.
            commentaire (Commentaire): Le commentaire à sauvegarder.
        """
        print(
            f"[Simulé] Sauvegarde du commentaire '{commentaire}' pour "
            f"la publication {publication_id}"
        )

    @staticmethod
    def sauvegarder_utilisateur_forum(forum_id, utilisateur):
        """Simule l'ajout d'un utilisateur à un forum.

        Paramètres:
            forum_id (int): L'identifiant du forum.
            utilisateur (Utilisateur): L'utilisateur à ajouter.
        """
        print(f"[Simulé] Ajout de l'utilisateur {utilisateur} au forum {forum_id}")

    @staticmethod
    def charger_utilisateurs():
        """Simule le chargement des utilisateurs.

        Retourne:
            list: La liste des utilisateurs.
        """
        print("[Simulé] Chargement des utilisateurs...")
        return []

    @staticmethod
    def charger_forums():
        """Simule le chargement des forums.

        Retourne:
            list: La liste des forums.
        """
        print("[Simulé] Chargement des forums...")
        return []

    @staticmethod
    def charger_publications(forum_id):
        """Simule le chargement des publications d'un forum.

        Paramètre:
            forum_id (int): L'identifiant du forum.

        Retourne:
            list: La liste des publications.
        """
        print(f"[Simulé] Chargement des publications du forum {forum_id}...")
        return []

    @staticmethod
    def charger_commentaires(publication_id):
        """Simule le chargement des commentaires d'une publication.

        Paramètre:
            publication_id (int): L'identifiant de la publication.

        Retourne:
            list: La liste des commentaires.
        """
        print(f"[Simulé] Chargement des commentaires pour la publication {publication_id}...")
        return []

    @staticmethod
    def charger_utilisateurs_forums():
        """Simule le chargement des utilisateurs inscrits aux forums.

        Retourne:
            list: La liste des inscriptions des utilisateurs aux forums.
        """
        print("[Simulé] Chargement des utilisateurs des forums...")
        return []
