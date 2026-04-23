from BDD import *
from keys import generer_trousseau

def inscrire_utilisateur(username, password):
    # Vérifier si l'utilisateur existe déjà
    passeword 
    existing_user = SelectQuery("Users", conditions={"username": username})
    if existing_user:
        print("Erreur : Nom d'utilisateur déjà pris.")
        return False
    
    # Insérer le nouvel utilisateur dans la base de données
    InsertQuery("Users", {
        "username": username,
        "password": password,
        "publicKey": generer_trousseau(username) 
    })
    
    print("Inscription réussie !")
    return True

def connexion_utilisateur(username, password):
    # Vérifier les informations d'identification de l'utilisateur
    user = SelectQuery("Users", conditions={"username": username, "password": password})
    if user:
        print("Connexion réussie !")
        return True
    else:
        print("Erreur : Nom d'utilisateur ou mot de passe incorrect.")
        return False

inscrire_utilisateur("dylan")