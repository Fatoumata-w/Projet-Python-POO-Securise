import customtkinter as ctk

from model.user import Utilisateur

class RegisterFrame(ctk.CTkFrame):
    def __init__(self, master, on_register_success, on_cancel):
        super().__init__(master)
        self.on_register_success = on_register_success
        self.on_cancel = on_cancel

        ctk.CTkLabel(self, text="Inscription", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)
        
        self.user_entry = ctk.CTkEntry(self, placeholder_text="Nom d'utilisateur")
        self.user_entry.pack(pady=10)
        
        self.pwd_entry = ctk.CTkEntry(self, placeholder_text="Mot de passe", show="*")
        self.pwd_entry.pack(pady=10)
        
        self.btn_register = ctk.CTkButton(self, text="S'inscrire", command=self.register_user)
        self.btn_register.pack(pady=20)

        self.btn_cancel = ctk.CTkButton(self, text="Annuler", command=self.on_cancel)
        self.btn_cancel.pack(pady=10)


    def register_user(self):
        # Ici, vous feriez votre inscription DB
        result = Utilisateur.inscrire_utilisateur(self.user_entry.get(), self.pwd_entry.get())
        if result>0:
            self.on_register_success(result)  # Passer l'ID utilisateur à la fonction de succès
        else:
            ctk.CTkLabel(self, text="Échec de l'inscription. Veuillez réessayer.", text_color="red").pack(pady=10)
