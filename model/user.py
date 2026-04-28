import datetime

from keys import generer_trousseau
from DB.BDDScript import InsertQuery, SelectArgQuery, SelectQuery, SelectData, UpdateQuery
from cryptographie import *
from model.types import ParticipantItem
from model.types import RegisterResponse

class Utilisateur:
    
    def __init__(self, username, state=False):
        self.id = None
        self.username = username
        self.cle_publique = None
        self.state = state

    def verifier_mot_de_passe(password):
        result = RegisterResponse(message="", success=False)
        # Validation du mot de passe: 8 caracteres min, 1 majuscule, 1 chiffre
        if len(password) < 8:
            result.message = "Erreur : Le mot de passe doit contenir au moins 8 caracteres."
            return result
        if not any(i.isupper() for i in password):
            result.message = "Erreur : Le mot de passe doit contenir au moins une majuscule."
            return result
        if not any(i.isdigit() for i in password):
            result.message = "Erreur : Le mot de passe doit contenir au moins un chiffre."
            return result
        result.message = "Succes"
        result.success = True
        return result
    
    def inscrire_utilisateur(username,password):
        print(f"Inscription de l'utilisateur : {username}")
        # Vérifier si l'utilisateur existe déjà
        existing_user = SelectQuery("Users", conditions={"username": username})
        if existing_user:
            return RegisterResponse(success=False, message="Erreur : Nom d'utilisateur déjà pris.")
        # Vérifier la validité du mot de passe
        password_verification = Utilisateur.verifier_mot_de_passe(password)
        if not password_verification.success:            
            return password_verification
        # Nouvelle utilisateur, générer les clés et insérer dans la base de données
        InsertQuery("Users", {
            "username": username,
            "password": hasher_mot_de_passe(password),
            "publicKey": generer_trousseau(username) 
        })
        print("Inscription réussie !")
        Utilisateur.connexion_utilisateur(username, password)
        return RegisterResponse(success=True, message="Inscription réussie !")
    
    def connexion_utilisateur(username, password):
        print(f"Connexion de l'utilisateur : {username}")
        # Vérifier si l'utilisateur existe
        user_data = SelectQuery("Users", conditions={"username": username, "password": hasher_mot_de_passe(password)})
        print(hasher_mot_de_passe(password))
        if not user_data:
            return 0
        print("Connexion réussie !")
        return user_data[0]['userId']
    
    def get_users(current_user_id):
        query = """SELECT userId, username, 
        CASE WHEN lastSeen IS NULL THEN false
        WHEN TIMESTAMPDIFF(SECOND, lastSeen, NOW()) < 20 THEN true
        ELSE false END AS isOnline
        FROM Users WHERE userId != %s;"""
        result = SelectData(query, (current_user_id,))

        return [ParticipantItem(**row) for row in result]
    
    def get_user_by_id(user_id):
        query = """SELECT userId, username, 
        CASE WHEN lastSeen IS NULL THEN false
        WHEN TIMESTAMPDIFF(SECOND, lastSeen, NOW()) < 20 THEN true
        ELSE false END AS isOnline
        FROM Users WHERE userId = %s;"""
        result = SelectData(query, (user_id,))
        if result:
            return ParticipantItem(**result[0])
        return None
    
    def update_last_seen(user_id):
        UpdateQuery("Users", data={"lastSeen": datetime.datetime.now()}, conditions={"userId": user_id})