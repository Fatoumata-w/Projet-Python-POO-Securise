import customtkinter as ctk
import model.conversation as Conversation
from model.user import Utilisateur
from model.conversation import *
from model.conversation import Conversation

class Accueil(ctk.CTkFrame):
    def __init__(self, master, current_user_id):
        super().__init__(master)
        self.current_user_id = current_user_id
        ctk.CTkLabel(self, text=f"Bienvenue, Utilisateur {self.current_user_id}!", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)

    def afficher_conversations(self):
        conversations = Conversation.get_conversations_for_user(self.current_user_id)
        for conv in conversations:
            ctk.CTkLabel(self, text=f"Conversation ID: {conv['id']} - Participants: {conv['participants']}").pack(pady=5)
