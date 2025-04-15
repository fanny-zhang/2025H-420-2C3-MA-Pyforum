class Utilisateur:

    def __init__(self, id, username, email, mdp):  # Attributs publiques/protégés/privés
        self.id = id
        self.username = username
        self.email = email
        self.mdp = mdp
        self.forums = []

   