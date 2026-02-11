from db import get_connexion
import bcrypt

# génération du sel
salt = bcrypt.gensalt()  # s

"""Authentification"""
connection = get_connexion()
##################################Créer un utilisateur################################
def create_admin():
    print("#" * 80)
    print("Bienvenu dans la boutique".center(80))
    print("#" * 80)
    email = input("Entrer votre email : ").strip()
    mot_de_passe = input("Entrer votre mot de passe : ").strip().encode("utf-8")
    cursor = connection.cursor()
    query = "insert into utilisateurs(email, mot_de_passe, role) values (%s, %s, 'admin')"
    cursor.execute(query, (email, bcrypt.hashpw(mot_de_passe, salt)))
    connection.commit()
    cursor.close()
    print("Admin crée avec succès")
###############################################Create utilisateurs###############################################""
def create_user():
    print("#" * 80)
    print("Bienvenu dans la boutique".center(80))
    print("#" * 80)
    email = input("Entrer votre email : ").strip()
    while email == "" or email.isnumeric():
        print("Veiller saisir des lettres alphabétiques")
        email = input("Entrer votre email : ").strip()
    mot_de_passe = input("Entrer votre mot de passe : ").strip().encode("utf-8")
    while mot_de_passe == "" or len(mot_de_passe) < 4:
        print("Veiller saisir au moins 4 caractères")
        mot_de_passe = input("Entrer votre mot de passe : ").strip().encode("utf-8")
    role = "user"
    cursor = connection.cursor()
    query = "insert into utilisateurs(email, mot_de_passe, role) values (%s, %s, %s)"
    cursor.execute(query, (email, bcrypt.hashpw(mot_de_passe, salt), role ))
    connection.commit()
    cursor.close()
    print("Utilisateur crée avec succès") 
"""Menu connexion"""
