import customtkinter as ctk

from model.user import Utilisateur

class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, on_login_success, on_register):
        super().__init__(master)
        self.on_login_success = on_login_success
        self.on_register = on_register

        ctk.CTkLabel(self, text="Connexion", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)
        
        self.user_entry = ctk.CTkEntry(self, placeholder_text="Nom d'utilisateur")
        self.user_entry.pack(pady=10)
        
        self.pwd_entry = ctk.CTkEntry(self, placeholder_text="Mot de passe", show="*")
        self.pwd_entry.pack(pady=10)
        
        self.btn_login = ctk.CTkButton(self, text="Se connecter", command=self.check_auth)
        self.btn_login.pack(pady=20)

        self.btn_register = ctk.CTkButton(self, text="S'inscrire", command=self.show_registration)
        self.btn_register.pack(pady=10)


    def show_registration(self):
        self.on_register()  # Appeler la fonction de redirection vers l'inscription
        
    def check_auth(self):
        # Ici, vous feriez votre vérification DB
        result = Utilisateur.connexion_utilisateur(self.user_entry.get(), self.pwd_entry.get())
        if result>0:
            self.on_login_success(result)  # Passer l'ID utilisateur à la fonction de succès
        else:
            ctk.CTkLabel(self, text="Échec de la connexion. Veuillez réessayer.", text_color="red").pack(pady=10)