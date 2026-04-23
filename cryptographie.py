from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

def hasher_mot_de_passe(mot_de_passe):
    # 1. Générer un sel unique de 16 octets
    sel = os.urandom(16)
    
    # 2. Configurer PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32, # On veut un hash de 32 octets
        salt=sel,
        iterations=600000, # Nombre de répétitions pour ralentir les attaques brute-force
    )
    
    # 3. Générer le hash
    hash_genere = kdf.derive(mot_de_passe.encode())
    
    return hash_genere


