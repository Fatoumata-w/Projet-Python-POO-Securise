from keys import generer_trousseau
from DB.BDDScript import InsertQuery, SelectArgQuery, SelectQuery
from cryptographie import *

class Utilisateur:
    
    def __init__(self, username, state=False):
        self.id = None
        self.username = username
        self.cle_publique = None
        self.state = state

    def verifier_mot_de_passe(password):
        # Validation du mot de passe: 8 caracteres min, 1 majuscule, 1 chiffre
        if len(password) < 8:
            print("Erreur : Le mot de passe doit contenir au moins 8 caracteres.")
            return False
        if not any(i.isupper() for i in password):
            print("Erreur : Le mot de passe doit contenir au moins une majuscule.")
            return False
        if not any(i.isdigit() for i in password):
            print("Erreur : Le mot de passe doit contenir au moins un chiffre.")
            return False
        return True
    
    def inscrire_utilisateur(username,password):
        # Vérifier si l'utilisateur existe déjà
        existing_user = SelectQuery("Users", conditions={"username": username})
        if existing_user:
            print("Erreur : Nom d'utilisateur déjà pris.")
            return False
        # Vérifier la validité du mot de passe
        if not Utilisateur.verifier_mot_de_passe(password):
            return False
        # Nouvelle utilisateur, générer les clés et insérer dans la base de données
        InsertQuery("Users", {
            "username": username,
            "password": hasher_mot_de_passe(password),
            "publicKey": generer_trousseau(username) 
        })
        
        print("Inscription réussie !")
        return True
    
    def connexion_utilisateur(username, password):
        # Vérifier si l'utilisateur existe
        user_data = SelectQuery("Users", conditions={"username": username, "password": hasher_mot_de_passe(password)})
        print(hasher_mot_de_passe(password))
        if not user_data:
            print("Erreur : Nom d'utilisateur ou mot de passe incorrect.")
            return False
        print("Connexion réussie !")
        return True
    
    def get_users(current_user_id):
        users = SelectArgQuery("Users", columns=["id", "username"], conditions={"id": current_user_id}, operator="!=")
        return users
