import customtkinter as ctk
import model.conversation as Conversation
from model.user import Utilisateur
from model.conversation import *
from model.conversation import Conversation

class Accueil(ctk.CTkFrame):
    def __init__(self, master, current_user_id, on_open_conversation=None):
        super().__init__(master)
        self.current_user_id = current_user_id
        self.current_user = Utilisateur.get_user_by_id(current_user_id)
        self.card_normal_color = "#1565C0"
        self.card_hover_color = "#1E88E5"
        self.on_open_conversation = on_open_conversation

        ctk.CTkLabel(self, text=f"Bienvenue, {self.current_user.username}!", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)
        self.afficher_utilisateurs()

    def _set_card_hover(self, card, hovered):
        card.configure(fg_color=self.card_hover_color if hovered else self.card_normal_color)

    def _ouvrir_conversation(self, utilisateur):
        conversation_id = Conversation.recherche_conversation(self.current_user_id, utilisateur.userId)
        if conversation_id == 0:
            conversation_id = Conversation.createConversation([self.current_user_id, utilisateur.userId])
        if self.on_open_conversation:
            self.on_open_conversation(conversation_id)

    def afficher_utilisateurs(self):
        utilisateurs = Utilisateur.get_users(self.current_user_id)
        for utilisateur in utilisateurs:
            card = ctk.CTkFrame(self, fg_color=self.card_normal_color, corner_radius=16)
            card.pack(fill="x", padx=12, pady=8)

            card.grid_columnconfigure(0, weight=1)
            card.grid_columnconfigure(1, weight=0)

            nom_label = ctk.CTkLabel(
                card,
                text=utilisateur.username,
                font=ctk.CTkFont(size=16, weight="bold"),
                text_color="white",
            )
            nom_label.grid(row=0, column=0, sticky="w", padx=(16, 8), pady=14)

            chatter_btn = ctk.CTkButton(
                card,
                text="chatter",
                width=110,
                fg_color="#0B3D91",
                hover_color="#082B66",
                command=lambda u=utilisateur: self._ouvrir_conversation(u),
            )
            chatter_btn.grid(row=0, column=1, sticky="e", padx=(8, 16), pady=10)

            card.bind("<Enter>", lambda e, c=card: self._set_card_hover(c, True))
            card.bind("<Leave>", lambda e, c=card: self._set_card_hover(c, False))
            nom_label.bind("<Enter>", lambda e, c=card: self._set_card_hover(c, True))
            nom_label.bind("<Leave>", lambda e, c=card: self._set_card_hover(c, False))
        

    
