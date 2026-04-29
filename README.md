# 📖 Messagerie Sécurisée en Python

## 📝 Description

Ce projet est une application de **messagerie instantanée sécurisée** développée en **Python**, basée sur la **Programmation Orientée Objet (POO)**. Il a été réalisé en réponse aux consignes initiales, avec une attention particulière portée à la **confidentialité**, à l'**intégrité** et à l'**authenticité** des messages échangés.

L'application permet à des utilisateurs de s'inscrire, de se connecter, et d'échanger des messages **chiffrés de bout en bout** grâce à un système de clés **RSA**. Chaque message est chiffré deux fois : une fois pour le destinataire, une fois pour l'émetteur — permettant à chacun de relire sa propre conversation.

Pour la fonctionnalité supplémentaire demandée par le TechLead, nous avons choisi d'implémenter un **système de présence en temps réel** : chaque utilisateur peut voir si ses interlocuteurs sont **en ligne ou hors ligne**, avec une mise à jour automatique toutes les 10 secondes.

---

## ⚙️ Fonctionnalités Principales

### 🔐 Chiffrement de Bout en Bout (E2EE)
- Chaque utilisateur possède une **paire de clés RSA 2048 bits** générée à l'inscription.
- La **clé publique** est stockée en base de données.
- La **clé privée** est sauvegardée localement dans le dossier `privateKey/`.
- À l'envoi d'un message, celui-ci est **chiffré avec la clé publique du destinataire** (pour qu'il puisse le lire) et **chiffré une deuxième fois avec la clé publique de l'émetteur** (pour que l'émetteur puisse relire ses propres messages).
- Le déchiffrement se fait côté client via la **clé privée locale**.
- L'algorithme utilisé est **RSA-OAEP avec SHA-256**.

### 🔑 Authentification des Utilisateurs
- Système d'**inscription** avec validation du mot de passe (8 caractères minimum, 1 majuscule, 1 chiffre).
- Le mot de passe est **haché via PBKDF2-HMAC-SHA256** avec 600 000 itérations avant d'être stocké en base de données.
- Lors de la connexion, le mot de passe saisi est haché et comparé au hash stocké — le mot de passe en clair n'est jamais conservé.

### 💬 Conversations
- Création automatique d'une **conversation** entre deux utilisateurs si elle n'existe pas encore.
- Affichage des messages sous forme de **bulles** alignées selon le rôle (émetteur à droite, destinataire à gauche).
- Les messages sont **déchiffrés à la volée** lors du chargement de la conversation.

### 🟢 Présence en Temps Réel *(Fonctionnalité Supplémentaire)*
- Chaque utilisateur dispose d'un champ `lastSeen` mis à jour régulièrement.
- Un utilisateur est considéré **En ligne** si son `lastSeen` date de moins de **20 secondes**.
- La liste des utilisateurs et le titre de la conversation se **rafraîchissent automatiquement toutes les 10 secondes**.

---

## 🏗️ Infrastructure

### Architecture du projet

```
ProjetAissatouFatoumataDylan/
│
├── main.py                  → Point d'entrée, lance l'application
├── cryptographie.py         → Hachage des mots de passe (PBKDF2)
├── keys.py                  → Génération des paires de clés RSA
│
├── Interface/               → Couche présentation (CustomTkinter)
│   ├── IApp.py              → Fenêtre principale, gestion de la navigation
│   ├── ILoginFrame.py       → Vue de connexion
│   ├── IRegister.py         → Vue d'inscription
│   ├── IAccueil.py          → Liste des utilisateurs, statut en ligne
│   └── IConversation.py     → Affichage et envoi des messages
│
├── model/                   → Couche logique métier (POO)
│   ├── user.py              → Classe Utilisateur (inscription, connexion, présence)
│   ├── message.py           → Classe Message (chiffrement, sauvegarde)
│   ├── conversation.py      → Classe Conversation (création, lecture, déchiffrement)
│   └── types.py             → Dataclasses partagées (ParticipantItem, ConversationItem, RegisterResponse)
│
├── DB/                      → Couche accès aux données
│   ├── BDDScript.py         → Helpers SQL génériques (Select, Insert, Update)
│   └── messageriesecurisee_Dump.sql → Script de création et données de la base
│
└── privateKey/              → Clés privées RSA stockées localement par utilisateur
    └── {username}_private.pem
```

### Base de données

La base de données `messageriesecurisee` repose sur **4 tables relationnelles** sous **MariaDB**.

#### Schéma et liaisons

```
┌─────────────────────────────┐
│           Users             │
├─────────────────────────────┤
│ PK  userId       INT AI     │
│     username     VARCHAR    │
│     password     VARCHAR    │  ← Hash PBKDF2-HMAC-SHA256
│     publicKey    TEXT       │  ← Clé RSA publique
│     lastSeen     DATETIME   │  ← Statut en ligne
└────────────┬────────────────┘
             │ 1
             │
             │ N
┌────────────┴──────────────────────────┐
│        ConversationParticipants       │
├───────────────────────────────────────┤
│ PK,FK  conversationId   INT          │──────┐
│ PK,FK  userId           INT          │      │
└───────────────────────────────────────┘      │ N
                                               │
                                               │ 1
                               ┌───────────────┴──────────┐
                               │       Conversations       │
                               ├──────────────────────────┤
                               │ PK  ConversationId  INT  │
                               │     date       DATETIME  │
                               └───────────────┬──────────┘
                                               │ 1
                                               │
                                               │ N
┌─────────────────────────────┐               │
│           Users             │    ┌───────────┴──────────────────────┐
│  userId (FK) ───────────────┼────│            Messages              │
└─────────────────────────────┘    ├──────────────────────────────────┤
                                   │ PK  messageId       INT AI       │
                                   │ FK  conversationId  INT          │
                                   │ FK  userId          INT          │  ← Émetteur
                                   │     content         TEXT         │  ← Chiffré destinataire
                                   │     envoyeurContent TEXT         │  ← Chiffré émetteur
                                   │     date            DATETIME     │
                                   │     state           TINYINT      │
                                   └──────────────────────────────────┘
```

#### Détail des relations

| Relation | Type | Description |
|---|---|---|
| `Users` → `ConversationParticipants` | 1-N | Un utilisateur peut participer à plusieurs conversations |
| `Conversations` → `ConversationParticipants` | 1-N | Une conversation a au moins 2 participants |
| `Conversations` → `Messages` | 1-N | Une conversation contient plusieurs messages |
| `Users` → `Messages` | 1-N | Un utilisateur peut envoyer plusieurs messages |

### Technologies utilisées

| Technologie | Rôle |
|---|---|
| Python 3.13 | Langage principal |
| CustomTkinter | Interface graphique |
| `cryptography` | RSA-OAEP, PBKDF2-HMAC |
| mysql-connector-python | Accès à la base de données |
| MariaDB | Stockage des données |

---

## 🔐 Gestion des Mots de Passe Utilisateur

### Règles de validation
Lors de l'inscription, le mot de passe doit respecter les critères suivants :
- Au moins **8 caractères**
- Au moins **1 lettre majuscule**
- Au moins **1 chiffre**

### Hachage et salage
Le mot de passe n'est jamais stocké en clair. Voici le processus appliqué :

```python
def hasher_mot_de_passe(mot_de_passe):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt_bytes,
        iterations=600000,
    )
    hash_genere = kdf.derive(mot_de_passe_bytes)
    return base64.b64encode(hash_genere).decode("utf-8")
```

- **Algorithme** : PBKDF2-HMAC-SHA256
- **Itérations** : 600 000 (recommandation NIST 2023) — ralentit les attaques brute-force
- **Résultat** : hash de 32 octets encodé en base64, stocké en base de données

À la connexion, le mot de passe saisi est haché de la même façon et comparé au hash stocké — aucun déchiffrement n'est possible.

---

## 🟢 Fonctionnalité Supplémentaire — Statut En ligne / Hors ligne

### Principe
Pour enrichir l'expérience utilisateur tout en restant dans une logique sécurisée, nous avons implémenté un **système de présence en temps réel**.

### Fonctionnement
- À chaque action (ouverture de la liste des utilisateurs, envoi d'un message), le champ `lastSeen` de l'utilisateur est mis à jour avec l'heure courante.
- Un utilisateur est affiché **En ligne** si son `lastSeen` date de moins de **20 secondes** (calculé côté SQL avec `TIMESTAMPDIFF`).
- Un rafraîchissement automatique s'effectue **toutes les 10 secondes** dans la vue d'accueil et dans la conversation.

```sql
CASE 
  WHEN TIMESTAMPDIFF(SECOND, lastSeen, NOW()) < 20 THEN true
  ELSE false 
END AS isOnline
```

### Affichage
- Dans la liste des utilisateurs : `Dylan (En ligne)` ou `Dylan (Hors ligne)`
- Dans le titre de la conversation : `Chat avec Dylan (En ligne)`
- Le titre se met à jour automatiquement sans rechargement de la page.

---

## 🚀 Installation et Exécution

### Prérequis
- Python 3.10+
- MariaDB / WAMP en local
- Base de données `messageriesecurisee` créée à partir du dump SQL

### 1. Cloner le dépôt
```sh
git clone <url-du-repo>
cd ProjetAissatouFatoumataDylan
```

### 2. Installer les dépendances
```sh
pip install customtkinter cryptography mysql-connector-python
```

### 3. Importer la base de données
```sh
mysql -u root -p messageriesecurisee < DB/messageriesecurisee_Dump.sql
```

### 4. Lancer l'application
```sh
python main.py
```

---

## 👥 Comptes Utilisateurs de Test

Les utilisateurs suivants sont déjà enregistrés en base de données et peuvent être utilisés pour tester l'application :

| Nom d'utilisateur | Mot de passe |
|---|---|
| dylan | Dylan12345 |
| fatou | Fatou12345 |
| isham | Isham12345 |
| laura | Laura12345 |
| mael | Mael12345 |
| thomas | Thomas12345 |


---
# Projet de groupe par Thomas,Fatoumata et Aissatou 

