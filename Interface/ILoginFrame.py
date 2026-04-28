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
        
        self.error_label = ctk.CTkLabel(self, text="", text_color="red")
        self.error_label.pack()

        self.btn_register = ctk.CTkLabel(self, text="Pas encore de compte ? S'inscrire", text_color="#1E88E5", cursor="hand2", font=ctk.CTkFont(size=13, underline=True))
        self.btn_register.pack(pady=10)
        self.btn_register.bind("<Button-1>", lambda e: self.show_registration())


    def show_registration(self):
        self.on_register()  
        
    def check_auth(self):
        result = Utilisateur.connexion_utilisateur(self.user_entry.get(), self.pwd_entry.get())
        if result>0:
            self.on_login_success(result)  
        else:
            self.error_label.configure(text="Nom d'utilisateur ou mot de passe incorrect.")