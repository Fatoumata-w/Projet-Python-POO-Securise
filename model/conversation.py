import os
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from model.message import Message
import base64
from DB.BDDScript import InsertQuery, SelectData, SelectQuery, get_connection, SelectArgQuery
from datetime import datetime
from model.types import ParticipantItem, ConversationItem

class Conversation:
    def __init__(self, participants : list):
        self.participants = participants

    def recherche_conversation(current_user_id, user_id):
        query = """SELECT CP.ConversationId
        FROM ConversationParticipants CP
        JOIN ConversationParticipants CP2 ON CP.conversationId = CP2.conversationId AND CP2.userId = %s
        WHERE CP.userId = %s"""
        result = SelectData(query, (user_id, current_user_id))
        if result:
            return result[0]['ConversationId']
        return 0
    
    def createConversation(participants):
        conversationId = InsertQuery("Conversations", {"date": datetime.now()})
        for participant in participants:
            InsertQuery("ConversationParticipants", {
                "conversationId": conversationId,
                "userId": participant
            })
        return conversationId

    def getParticipantsByConversationId(conversationId):
        query = """SELECT U.userId, U.username, CASE WHEN U.lastSeen IS NULL THEN false
        WHEN TIMESTAMPDIFF(SECOND, U.lastSeen, NOW()) < 20 THEN
        true ELSE false END AS isOnline
        FROM ConversationParticipants CP
        JOIN Users U ON CP.userId = U.userId
        WHERE CP.conversationId = %s;"""
        result = SelectData(query, (conversationId,))
        for i in range(len(result)):
            result[i] = ParticipantItem(**result[i])
        return result

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
        result = []
        for message in messages:
            if message['role'] == 'receveur':
                message['content'] = Conversation.contentDechiffre(message['content'], current_user_id)
                message['envoyeurContent'] = ""
            else:
                message['content'] = Conversation.contentDechiffre(message['envoyeurContent'], current_user_id)
                message['envoyeurContent'] = ""
            msg = ConversationItem( content=message['content'], date=message['date'], username=message['username'], userId=message['userId'], role=message['role'])
            result.append(msg)
        return result
                
        

    
            