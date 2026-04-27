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
            return "Erreur : Le mot de passe doit contenir au moins 8 caracteres."
        if not any(i.isupper() for i in password):
            return "Erreur : Le mot de passe doit contenir au moins une majuscule."
        if not any(i.isdigit() for i in password):
            return "Erreur : Le mot de passe doit contenir au moins un chiffre."
        return "Succes"
    
    def inscrire_utilisateur(username,password):
        print(f"Inscription de l'utilisateur : {username}")
        # Vérifier si l'utilisateur existe déjà
        existing_user = SelectQuery("Users", conditions={"username": username})
        if existing_user:
            print("Erreur : Nom d'utilisateur déjà pris.")
            return False
        # Vérifier la validité du mot de passe
        password_verification = Utilisateur.verifier_mot_de_passe(password)
        print(password_verification)
        if password_verification != "Succes":            
            return False
        # Nouvelle utilisateur, générer les clés et insérer dans la base de données
        InsertQuery("Users", {
            "username": username,
            "password": hasher_mot_de_passe(password),
            "publicKey": generer_trousseau(username) 
        })
        print("Inscription réussie !")
        Utilisateur.connexion_utilisateur(username, password)
        return True
    
    def connexion_utilisateur(username, password):
        print(f"Connexion de l'utilisateur : {username}")
        # Vérifier si l'utilisateur existe
        user_data = SelectQuery("Users", conditions={"username": username, "password": hasher_mot_de_passe(password)})
        print(hasher_mot_de_passe(password))
        if not user_data:
            print("Erreur : Nom d'utilisateur ou mot de passe incorrect.")
            return 0
        print("Connexion réussie !")
        return user_data[0]['userId']
    
    def get_users(current_user_id):
        users = SelectArgQuery("Users", columns=["id", "username"], conditions={"id": current_user_id}, operator="!=")
        return users
