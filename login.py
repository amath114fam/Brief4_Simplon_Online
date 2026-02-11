from getpass import getpass
import bcrypt
from db import get_connexion

salt = bcrypt.gensalt()  

#########################################gère la connexion#############################
connection = get_connexion()
def logine():
    cursor = connection.cursor()
    email = input("Entrer votre email : ").strip()
    while email == "" or email.isnumeric():
        print("Veiller saisir des lettres alphabétiques")
        email = input("Entrer votre email : ").strip()
    mot_de_passe = getpass("Entrer votre mot de passe : ").strip().encode("utf-8")
    while mot_de_passe == "" :
        print("Veiller saisir au moins 4 caractères")
        mot_de_passe = input("Entrer votre mot de passe : ").strip().encode("utf-8")
    query = "select id, email, mot_de_passe, role from utilisateurs where email = %s"
    cursor.execute(query, (email, ))
    user = cursor.fetchone()
    if not user:
        print("-" * 30)
        print("L'utilisateur n'existe pas")
        return None
    ids, email, mot_de_passe_hash, role = user
    hashe = mot_de_passe_hash.encode("utf-8")
    if bcrypt.checkpw(mot_de_passe, hashe):
        return {"role" : role}
    else:
        print("-" * 30)
        print("Mot de passe incorrect")

    
