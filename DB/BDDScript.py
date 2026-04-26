import mysql.connector

def get_connection():
    try:
        # Configuration de la connexion
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="messageriesecurisee"
        )
        return db
    except mysql.connector.Error as err:
        print(f"Erreur lors de la connexion : {err}")
        return None
    finally:
        if 'db' in locals() and db.is_connected():
            db.close()
        
def SelectData(query, variables):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="messageriesecurisee"
        )
        cursor = db.cursor(dictionary=True)
        cursor.execute(query, variables)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Erreur lors de la sélection : {err}")
        return None
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
            
def SelectArgQuery(table, columns, conditions=None):
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
        cols = ', '.join(columns)
        sql = f"SELECT {cols} FROM {table}"
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
    
    