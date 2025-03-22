# Importation des classes nécessaires
from time import sleep
from utilisateur import Utilisateur
from forum import Forum

def afficher_menu():
    """Affiche les options du menu."""
    print("\n---- Menu ----")
    print("1. Créer un utilisateur")
    print("2. Créer un forum")
    print("3. Créer une publication")
    print("4. Ajouter un commentaire à une publication")
    print("5. Joindre un forum")
    print("6. Quitter")

def main():
    utilisateurs = []
    forums = []
    while True:
        afficher_menu()

        # Demander à l'utilisateur de choisir une option
        choix = input("Choisissez une option (1-6): ")

        if choix == '1':
            # Créer un utilisateur
            print("\nCréation d'un utilisateur...")
            nom = input("Nom d'utilisateur : ")
            email = input("Email : ")
            mdp = input("Mot de passe : ")
            utilisateurs.append(Utilisateur(nom, email, mdp))
            print(f"Utilisateur {nom} créé.")

        elif choix == '2':
            # Créer un forum
            print("\nCréation d'un forum...")
            nom = input("Nom du forum : ")
            desc = input("Description : ")
            forums.append(Forum(nom, desc))
            print(f"Forum {nom} créé.")

        elif choix == '3':
            # Créer une publication
            print("\nCréation d'une publication...")
            nom_utilisateur = input("Nom d'utilisateur : ")
            nom_forum = input("Nom du forum : ")
            titre_publication = input("Titre de la publication : ")
            contenu_publication = input("Contenu de la publication : ")

            utilisateur = next((u for u in utilisateurs if u.nom == nom_utilisateur), None)
            forum = next((f for f in forums if f.nom == nom_forum), None)
            
            if utilisateur and forum:
                forum.ajouter_publication(utilisateur.id, titre_publication, contenu_publication)
            else:
                print("Utilisateur ou forum introuvable.")
  
        elif choix == '4':
            # Ajouter un commentaire
            print("\nAjouter un commentaire...")
           
            nom_utilisateur = input("Nom d'utilisateur : ")
            titre_publication = input("Titre de la publication : ")
            contenu_commentaire = input("Votre commentaire : ")

            utilisateur = next((u for u in utilisateurs if u.nom == nom_utilisateur), None)
            publication = None
            for forum in forums:
                publication = next((p for p in forum.publications if p.titre == titre_publication), None)
                if publication:
                    break

            if utilisateur and publication:
                publication.ajouter_commentaire(utilisateur.id, contenu_commentaire)
            else:
                print("Utilisateur ou publication introuvable.")
        elif choix == '5':
            # Joindre un forum
            print("\nJoindre un forum...")

            nom_utilisateur = input("Nom d'utilisateur : ")
            nom_forum = input("Nom du forum à rejoindre : ")

            utilisateur = next((u for u in utilisateurs if u.nom == nom_utilisateur), None)
            forum = next((f for f in forums if f.nom == nom_forum), None)

            if utilisateur and forum:
                utilisateur.joindre_forum(forum.id)
            else:
                print("Utilisateur ou forum introuvable.")

        elif choix == '6':
            # Quitter le programme
            print("\nMerci d'avoir utilisé PyForum. À bientôt!")
            break

        else:
            print("Option invalide. Veuillez essayer à nouveau.")

        sleep(2)  # Pause de 2 secondes pour rendre l'interface plus agréable

if __name__ == "__main__":
    main()
