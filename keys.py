from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import os
from BDD import InsertQuery


def generer_trousseau(nom_utilisateur):
    # 1. Créer la paire de clés (Mathématiques)
    # 2048 bits est le standard actuel pour RSA
    key_pair = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # 2. Extraire la clé privée et la formater en texte (PEM)
    private_pem = key_pair.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption() # On ne met pas de mot de passe pour simplifier ton projet
    )

    # 3. Extraire la clé publique et la formater en texte (PEM)
    public_pem = key_pair.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # 4. Enregistrer dans les fichiers respectifs
    # La clé privée va dans le dossier de l'utilisateur
    with open(f"{nom_utilisateur}/{nom_utilisateur}_private.pem", "wb") as f:
        f.write(private_pem)


    print(f"✅ Clés générées pour {nom_utilisateur}")

# --- EXECUTION ---
# Assure-toi que tes dossiers existent avant de lancer le script
for dossier in ["dylan", "mael", "public_keys"]:
    if not os.path.exists(dossier):
        os.makedirs(dossier)
