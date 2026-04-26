import os
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from model.message import Message
import base64
from DB.BDDScript import InsertQuery, SelectData, SelectQuery, get_connection, SelectArgQuery
from datetime import datetime

class Conversation:
    def __init__(self, participants : list):
        self.participants = participants

    def createConversation(participants):
        conversationId = InsertQuery("Conversations", {"date": datetime.now()})
        for participant in participants:
            InsertQuery("ConversationParticipants", {
                "conversationId": conversationId,
                "userId": participant
            })
        return conversationId

    def getConversationIdByParticipant(current_user_id):
        query = """SELECT subquery.`conversationId`, M.`date`, M.content, U.publicKey
        FROM (
        SELECT C.`ConversationId`, MAX(M.`messageId`) as last_message_id
        FROM conversations as `C`
        JOIN ConversationParticipants as `CP` ON C.ConversationId = CP.conversationId
        JOIN messages as `M` ON C.ConversationId = M.conversationId
        WHERE CP.userId = %s
        GROUP BY C.`ConversationId`
        ) AS subquery
        JOIN messages M ON subquery.last_message_id = M.messageId
        JOIN Users U ON M.userId = U.userId
        ORDER BY M.`date` DESC;"""
        return SelectData(query, (current_user_id,))
    
    def contentDechiffre(contentChiffre, current_user_id):
        username = SelectArgQuery("Users", ["username"], conditions={"userId": current_user_id})[0]['username']
        private_key_path = os.path.join(os.path.dirname(__file__), "..", "privateKey", f"{username}_private.pem")
        print(private_key_path)
        with open(private_key_path, "rb") as f:
            private_key = serialization.load_pem_private_key(f.read(), password=None)
        decrypted_content = private_key.decrypt(
            base64.b64decode(contentChiffre),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_content.decode("utf-8")
    
    def readConversation(conversationId, current_user_id):
        query = """SELECT M.conversationId, M.`messageId`, U.userId,U.username, M.`date`, M.content, M.state, M.envoyeurContent,
        CASE 
        WHEN M.`userId`=%s THEN 'envoyeur'  
        ELSE 'receveur'
        END AS role
        FROM Conversations C
        JOIN Messages M ON C.ConversationId = M.conversationId
        JOIN Users U ON M.userId = U.userId
        WHERE C.`ConversationId` = %s
        ORDER BY M.`date` ASC;"""
        messages = SelectData(query, (current_user_id, conversationId))
        print(messages)
        for message in messages:
            if message['role'] == 'receveur':
                message['content'] = Conversation.contentDechiffre(message['content'], current_user_id)
                message['envoyeurContent'] = ""
            else:
                message['content'] = Conversation.contentDechiffre(message['envoyeurContent'], current_user_id)
                message['envoyeurContent'] = ""
        print(messages)
        return messages
    
                
        

    
            