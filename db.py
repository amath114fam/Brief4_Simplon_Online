import mysql.connector
def get_connexion():
    return mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "boutique_pro",
    password = "fam@2025"
    )
connection = get_connexion()
if connection.is_connected():
    print("Connexion réussi")
