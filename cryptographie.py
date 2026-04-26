import base64

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

def hasher_mot_de_passe(mot_de_passe):
    # 1. Générer un sel unique 
    salt_bytes = "fgdzlaamvjhla35fdac".encode("utf-8")
    mot_de_passe_bytes = mot_de_passe.encode("utf-8")

    # 2. Configurer PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32, # On veut un hash de 32 octets
        salt=salt_bytes,
        iterations=600000, # Nombre de répétitions pour ralentir les attaques brute-force
    )
    
    # 3. Générer le hash
    hash_genere = kdf.derive(mot_de_passe_bytes)
    
    return base64.b64encode(hash_genere).decode("utf-8")


