import customtkinter as ctk
import random
from datetime import datetime
from model.conversation import *




class ConversationFrame(ctk.CTkFrame):
    def __init__(self, parent, controller, conversation_id=None, current_user_id = None):
        super().__init__(parent, fg_color="transparent")
        self.conversation_id = conversation_id
        self.current_user_id = current_user_id
        self.envoyeur = None
        self.receveur = None
        self.timer_call = False    
        self.recherche_interlocuteurs()


        self.label_title = ctk.CTkLabel(self, text=f"Chat avec {self.receveur.username}", font=("Roboto", 18, "bold"))
        self.label_title.pack(pady=10)

        self.chat_display = ctk.CTkScrollableFrame(self, width=450, height=300)
        self.chat_display.pack(expand=True, fill="both", padx=10, pady=10)

        self.input_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.input_frame.pack(fill="x", padx=10, pady=10)

        self.entry_message = ctk.CTkEntry(self.input_frame, placeholder_text=f"Écrire un message pour {self.receveur.username}...")
        self.entry_message.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.btn_send = ctk.CTkButton(self.input_frame, text="Ajouter", width=80, command=self.ajouter_message)
        self.btn_send.pack(side="right")

        self.charger_messages()

        self.lancer_timer()

    def lancer_timer(self):
        if self.timer_call:
            self.rafraichir_messages()
        self.timer_call = True
        self.timer_id = self.after(30000, self.lancer_timer)

    def rafraichir_messages(self):        

        

        
        items = len(self.ma_liste_de_conversations)

        self.ma_liste_de_conversations.append(Conversation.readConversation(self.conversation_id, self.current_user_id))
        
        if (items < len(self.ma_liste_de_conversations)):
            for item in self.ma_liste_de_conversations[items:]:
                self.creer_bulle_message(item)        
        self.chat_display._parent_canvas.yview_moveto(1.0)



    def recherche_interlocuteurs(self):
        # ICI IL FAUT ALLER CHERCHER EN BASE LES PARTICIPANTS
        mes_participants = [
            ParticipantMock(
                userId= 10,
                username= "Alice"
            ),
            ParticipantMock(
                userId= 11,
                username= "Bob"
            )
        ]

        # On ne récupère que le participant qui n'est pas l'utilisateur en cours
        for item in mes_participants:
            if item.userId != self.current_user_id:
                self.receveur = item
            else:
                self.envoyeur = item

    def charger_messages(self):
        # On vide l'affichage actuel (si nécessaire)
        for widget in self.chat_display.winfo_children():
            widget.destroy()

        self.ma_liste_de_conversations = [
            ConversationMock(
                content = "Salut ! Comment ça va ?", 
                date = "2023-10-27 10:00", 
                username = "Alice",
                role = "envoyeur",
                userId = 10
            ),                        
            ConversationMock(
                content = "Hello ! Très bien et toi ?", 
                date = "2023-10-27 10:05", 
                username = "Bob",
                role = "receveur",
                userId = 11
            ),
            ConversationMock(
                content = "Je teste mon application Python.", 
                date = "2023-10-27 10:10", 
                username = "Alice",
                role = "envoyeur",
                userId = 10
            )
        ]

        for item in self.ma_liste_de_conversations:
            self.creer_bulle_message(item)
        self.chat_display._parent_canvas.yview_moveto(1.0)

    def creer_bulle_message(self, item):
        if item.userId == self.current_user_id:
            alignement = "e"       # Droite (East)
            couleur_bulle = "#1f538d" # Bleu
            texte_couleur = "white"
        else:
            alignement = "w"       # Gauche (West)
            couleur_bulle = "#3d3d3d" # Gris foncé
            texte_couleur = "white"

        # Cadre pour la bulle
        bulle = ctk.CTkFrame(self.chat_display, fg_color=couleur_bulle, corner_radius=10)
        bulle.pack(padx=10, pady=5, anchor=alignement)

        # Texte du message à l'intérieur
        lbl = ctk.CTkLabel(
            bulle, 
            text=f"{item.content}\n\n{item.date}", 
            text_color=texte_couleur,
            font=("Roboto", 12),
            justify="left",
            padx=10,
            pady=5
        )
        lbl.pack()


    def ajouter_message(self):
        texte = self.entry_message.get()
        if texte.strip() != "":
            
            nouveau_item = ConversationMock(
                content=texte,
                date=datetime.now().strftime("%H:%M"),
                username= self.envoyeur.username,
                userId = self.envoyeur.userId,
                role="envoyeur"
            )
            
            # ICI : il faut l'ajouter dans la base de données !
            # APPEL DANS LA BASE DE DONNEES

            # APRES : je l'ajoute à mon objet global
            self.ma_liste_de_conversations.append(nouveau_item)
            
            # Ajout d'une nouvelle bulle de message
            self.creer_bulle_message(nouveau_item)
            
            # On efface la zone de saise
            self.entry_message.delete(0, "end")
            self.chat_display._parent_canvas.yview_moveto(1.0)

    def destroy(self):
            if hasattr(self, 'timer_id'):
                self.after_cancel(self.timer_id)
            super().destroy()