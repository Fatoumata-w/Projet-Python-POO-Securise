import mysql.connector

#Connexion a la base de données MySQL
try:
    # Configuration de la connexion
    db = mysql.connector.connect(
        host="localhost",
        user="root",        
        password="",       
        database="messageriesecurisee"
    )

    if db.is_connected():
        print("Connexion réussie à la base de données !")
        
except mysql.connector.Error as err:
    print(f"Erreur lors de la connexion : {err}")

finally:
    if 'db' in locals() and db.is_connected():
        db.close()


def InsertQuery(table, data):
    try:
        # Reconnexion à la base de données
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="messageriesecurisee"
        )
        cursor = db.cursor()
        # Construction de la requête d'insertion
        placeholders = ', '.join(['%s'] * len(data))
        columns = ', '.join(data.keys())
        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        cursor.execute(sql, list(data.values()))
        db.commit()
        return cursor.lastrowid
    except mysql.connector.Error as err:
        print(f"Erreur lors de l'insertion : {err}")
        return None
    finally:
        if 'db' in locals() and db.is_connected():
            db.close()

def SelectQuery(table, conditions=None):
    try:
        # Reconnexion à la base de données
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="messageriesecurisee"
        )
        cursor = db.cursor(dictionary=True)
        # Construction de la requête de sélection
        sql = f"SELECT * FROM {table}"
        if conditions:
            placeholders = ' AND '.join([f"{key} = %s" for key in conditions.keys()])
            sql += f" WHERE {placeholders}"
            cursor.execute(sql, list(conditions.values()))
        else:
            cursor.execute(sql)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Erreur lors de la sélection : {err}")
        return None
    finally:
        if 'db' in locals() and db.is_connected():
            db.close()
            