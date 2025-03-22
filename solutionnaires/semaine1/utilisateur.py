import json
import os
from bd import BD

class Utilisateur:
    compteur_id = 1

    def __init__(self, nom, email, mot_de_passe):
        self.id = Utilisateur.compteur_id
        Utilisateur.compteur_id += 1
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.forums = []
        BD.sauvegarder_utilisateur(self)

    def joindre_forum(self, forum_id):
        if forum_id not in self.forums:
            self.forums.append(forum_id)
            BD.sauvegarder_utilisateur(self)
            print(f"{self.nom} a rejoint le forum {forum_id}.")
        else:
            print(f"{self.nom} est déjà membre du forum {forum_id}.")
