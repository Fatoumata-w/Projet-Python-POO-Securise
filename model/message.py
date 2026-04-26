from xmlrpc.client import DateTime
from datetime import datetime
from DB.BDDScript import InsertQuery, SelectArgQuery, SelectData, get_connection
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

class Message:

    def __init__(self, conversationId, currentUserId, destinataireId, content):
        self.conversationId = conversationId
        self.content = content
        self.state = False
        self.role = "envoyeur"
        self.userId = currentUserId
        self.contentChiffre(destinataireId)


    def contentChiffre(self, destinataireId):
        public_key = SelectArgQuery("Users", ["publicKey"], conditions={"userId": destinataireId})[0]['publicKey']  
        key = serialization.load_pem_public_key(public_key.encode("utf-8"))

        receveurContent = key.encrypt(
            self.content.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        receveurContent = base64.b64encode(receveurContent).decode("utf-8")

        public_key = SelectArgQuery("Users", ["publicKey"], conditions={"userId": self.userId})[0]['publicKey']  
        key = serialization.load_pem_public_key(public_key.encode("utf-8"))

        envoyeurContent = key.encrypt(
            self.content.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        envoyeurContent = base64.b64encode(envoyeurContent).decode("utf-8")
        self.content = receveurContent
        self.envoyeurContent = envoyeurContent
        return True
    
    def saveMessage(self):
        get_connection()
        InsertQuery("Messages", {
            "conversationId": self.conversationId,
            "content": self.content,
            "userId": self.userId, # Id de l'émetteur
            "date": datetime.now(),
            "state": self.state,
            "envoyeurContent": self.envoyeurContent
        })

    def getMessagesByConversationId(conversationId, current_user_id):
        query = """SELECT M.conversationId, M.`messageId`, U.userId,U.username, M.`date`, M.content, M.state,
        CASE 
        WHEN M.`userId`=%s THEN 'envoyeur'  
        ELSE 'receveur'
        END AS role
        FROM Conversations C
        JOIN Messages M ON C.ConversationId = M.conversationId
        JOIN Users U ON M.userId = U.userId
        WHERE C.`ConversationId` = %s
        ORDER BY M.`date` ASC;"""
        return SelectData(query, (current_user_id, conversationId))
