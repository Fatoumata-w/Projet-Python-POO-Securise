import customtkinter as ctk
from Interface.ILoginFrame import LoginFrame
from Interface.IAccueil import Accueil
from Interface.IRegister import RegisterFrame


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Mon App Pro")
        self.geometry("500x400")

        self.current_user_id = None
        self.current_frame = None

        self.show_login()

    def show_login(self):
        self.clear_frame()
        self.current_frame = LoginFrame(self, on_login_success=self.login_callback, on_register=self.show_registration)
        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)

    def login_callback(self, user_id):
        """Cette fonction est appelée quand la connexion réussit"""
        self.current_user_id = user_id
        print(f"Utilisateur {user_id} connecté. Redirection...")
        self.show_dashboard()
    
    def show_registration(self):
        self.clear_frame()
        self.current_frame = RegisterFrame(self, on_register_success=self.register_callback, on_cancel=self.show_login)
        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)

    def register_callback(self, user_id):
        """Cette fonction est appelée quand l'inscription réussit"""
        self.current_user_id = user_id
        print(f"Utilisateur {user_id} inscrit et connecté. Redirection...")
        self.show_login()

    def show_dashboard(self):
        self.clear_frame()
        self.current_frame = Accueil(self, self.current_user_id)
        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)

    def clear_frame(self):
        """Détruit la vue actuelle avant d'en afficher une nouvelle"""
        if self.current_frame is not None:
            self.current_frame.destroy()