from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import os
from DB.BDDScript import InsertQuery, SelectQuery


def generer_trousseau(nom_utilisateur):
    # 1. Créer la paire de clés RSA (2048 bits)
    key_pair = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # 2. Extraire la clé privée au format PEM
    private_pem = key_pair.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )

    # 3. Extraire la clé publique au format PEM
    public_pem = key_pair.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )


    # 4. Créer le dossier utilisateur puis sauvegarder la clé privée
    user_dir = os.path.join(os.path.dirname(__file__), nom_utilisateur)
    os.makedirs(user_dir, exist_ok=True)
    private_key_path = os.path.join(user_dir, f"{nom_utilisateur}_private.pem")

    with open(private_key_path, "wb") as f:
        f.write(private_pem)

    print(f"Cles generees pour {nom_utilisateur}")
    return public_pem.decode("utf-8")


