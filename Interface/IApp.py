import customtkinter as ctk
from Interface.ILoginFrame import LoginFrame
from Interface.IAccueil import Accueil
from Interface.IRegister import RegisterFrame


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Messagerie Instantanée")
        self.geometry("500x600")

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
        self.show_accueil()
    
    def show_registration(self):
        self.clear_frame()
        self.current_frame = RegisterFrame(self, on_register_success=self.register_callback, on_cancel=self.show_login)
        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)

    def register_callback(self):
        self.show_login()

    def show_accueil(self):
        self.clear_frame()
        self.current_frame = Accueil(self, self.current_user_id, on_open_conversation=self.show_conversation)
        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)

    def show_conversation(self, conversation_id):
        from Interface.IConversation import ConversationFrame
        self.clear_frame()
        self.current_frame = ConversationFrame(self, conversation_id=conversation_id, current_user_id=self.current_user_id, on_back=self.show_accueil)
        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)

    def clear_frame(self):
        """Détruit la vue actuelle avant d'en afficher une nouvelle"""
        if self.current_frame is not None:
            self.current_frame.destroy()