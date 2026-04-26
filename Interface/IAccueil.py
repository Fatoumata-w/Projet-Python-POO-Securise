import customtkinter as ctk
import model.conversation as Conversation
from model.user import Utilisateur

class Accueil(ctk.CTk):
    def __init__(self, current_user_id):
        super().__init__()
        self.title("Messagerie Sécurisée - Accueil")
        self.geometry("600x600")
        self.resizable(True, True)
        self.current_user_id = current_user_id
        self.conversations = Conversation.Conversation.getConversationIdByParticipant(current_user_id)
        self.create_widgets()

    def liste_conversations(self):
        for widget in self.winfo_children():
            widget.destroy()
        ctk.CTkLabel(self, text="Conversations", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)
        for conversation in self.conversations:
            ctk.CTkButton(self, text=f"Conversation avec {conversation['username']} - Dernier message : {conversation['content']}", command=lambda c=conversation: self.ouvrir_conversation(c)).pack(pady=10)
        