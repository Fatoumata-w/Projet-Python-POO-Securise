import customtkinter as ctk

from model.user import Utilisateur
from model.types import RegisterResponse

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

        self.pwd_entry_confirm = ctk.CTkEntry(self, placeholder_text="Confirmer le mot de passe", show="*")
        self.pwd_entry_confirm.pack(pady=10)
        
        self.btn_register = ctk.CTkButton(self, text="S'inscrire", command=self.register_user)
        self.btn_register.pack(pady=20)

        self.btn_cancel = ctk.CTkButton(self, text="Annuler", command=self.on_cancel)
        self.btn_cancel.pack(pady=10)

        self.error_label = ctk.CTkLabel(self, text="", text_color="red")
        self.error_label.pack()


    def register_user(self):
        if self.pwd_entry.get() != self.pwd_entry_confirm.get():
            self.error_label.configure(text="Les mots de passe ne correspondent pas.")
            return

        result = Utilisateur.inscrire_utilisateur(self.user_entry.get(), self.pwd_entry.get())
        if result.success:
            self.on_register_success()  
        else:
            self.error_label.configure(text=result.message)
