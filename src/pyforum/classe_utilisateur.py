class Utilisateur:

    def __init__(self, id, nom_utilisateur, email, mot_de_passe):  # Attributs publiques/protégés/privés
        self.id = id
        self.nom_utilisateur = nom_utilisateur
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.forums = []

   