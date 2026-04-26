import customtkinter as ctk
from model.user import Utilisateur
import IAccueil as Accueil

class ConnexionInscription(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Messagerie Sécurisée - Connexion/Inscription")
        self.geometry("600x600")
        self.resizable(True, True)
        
    
    def inscription(self):
        ctk.CTkLabel(self, text="Inscription", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)
        
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Nom d'utilisateur")
        self.username_entry.pack(pady=10)
        
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Mot de passe", show="*")
        self.password_entry.pack(pady=10)
        
        ctk.CTkButton(self, text="S'inscrire", command=lambda: Utilisateur.inscrire_utilisateur(self.username_entry.get(), self.password_entry.get())).pack(pady=20)
        

    
        
        