class Utilisateur:
    identifiant_unique = 0
    def __init__(self, nom_utilisateur, adresse_email, mot_de_passe):  # Attributs publiques/protégés/privés
        self.identifiant_unique = Utilisateur.identifiant_unique
        Utilisateur.identifiant_unique += 1
        self.nom_utilisateur = nom_utilisateur
        self.adresse_email = adresse_email
        self.mot_de_passe = mot_de_passe
        self.forums = []