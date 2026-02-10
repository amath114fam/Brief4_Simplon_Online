import mysql.connector
from datetime import datetime

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "boutique_pro",
    password = "fam@2025"
)
if connection.is_connected():
    print("Connexion réussi")
"""ajouter catégorie"""
def add_categorie(nom):
    cursor = connection.cursor()
    query = "insert into categories(nom_categorie) values (%s)"
    cursor.execute(query, (nom,))
    connection.commit()
    cursor.close()
    print("-" * 10)
    print(f"La catégorie {nom} est ajoutée avec succès")
def saisie_add_categorie():
    nom = input("Entrer le nom de la catégorie : ").strip()
    while nom == "" or nom.isnumeric():
        print("Veiller saisir des lettres alphabétiques")
        nom = input("Entrer le nom de la catégorie : ").strip()
    add_categorie(nom)
"""afficher liste catégorie"""
def liste_categorie():
    cursor = connection.cursor()
    query  = "select * from categories "
    cursor.execute(query)
    rows = cursor.fetchall()
    print("-" * 10)
    print("La liste des catégories : ")
    print("-" * 5)
    for row in rows:
        print(f"{row[0]}. {row[1]}")
    cursor.close()
"""ajouter produit"""
def add_produit(nom_produit, prix, statut_stock,quantite, id_categorie):
    cursor = connection.cursor()
    query = "insert into produits(nom_produit, prix, statut_stock,quantite, id_categorie) values (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nom_produit, prix, statut_stock, quantite, id_categorie))
    connection.commit()
    print(f"Le produit {nom_produit} est ajoutée avec succès")
    print("-" * 10)
    id_produit_ancien = cursor.lastrowid
    now = datetime.now()
    querys = "insert into mouvements(quantite, date, id_produit, type_mouvement) values (%s, %s, %s, %s)"
    mouvement = "ajout"
    date = now.date()
    cursor.execute(querys, (quantite, date, id_produit_ancien, mouvement))
    connection.commit()
    cursor.close()
"""liste produit"""
def liste_produit():
    cursor = connection.cursor()
    query  = "select * from produits"
    cursor.execute(query)
    rows = cursor.fetchall()
    # now = datetime.now()
    print("La liste des produits")
    print("-" * 30)
    for row in rows:
        print(f"{row[0]}. {row[1]} {row[2]},  quantite : {row[5]}, statut : {row[3]}")
    cursor.close()
"""liste des produits avec leurs categories"""
def liste_produit_categorie():
    cursor = connection.cursor()
    query  = "select nom_produit, categories.nom_categorie from produits join categories on produits.id_categorie=categories.id_categorie"
    cursor.execute(query)
    rows = cursor.fetchall()
    print("La liste des produits avec leur catégories")
    print("-" * 10)
    for row in rows:
        print(row)
    cursor.close()
def mouvements():
    cursor = connection.cursor()
    query  = "select * from mouvements"
    cursor.execute(query)
    rows = cursor.fetchall()
    print("Les mouvements : ")
    print("-" * 10)
    for row in rows:
        print(f"{row[0]}.  quantite : {row[1]}, {row[2]}, produit : {row[3]}, {row[4]}")
    cursor.close()
"""modifier la quantité du produit"""
def modifier_quantite_produits(quantite, id_produit):
    cursor = connection.cursor()
    query = "Update produits set quantite = %s where id_produit = %s"
    cursor.execute(query, (quantite, id_produit))
    connection.commit()
    print("Le produit est modifié avec succès")
    print("-" * 10)
    now = datetime.now()
    querys = "insert into mouvements(quantite, date, id_produit, type_mouvement) values (%s, %s, %s, %s)"
    mouvement = "modifié"
    date = now.date()
    cursor.execute(querys, (quantite, date, id_produit, mouvement))
    connection.commit()
    cursor.close()
def stock_faible():
    cursor = connection.cursor()
    query = "select * from produits where quantite < 5"
    cursor.execute(query)
    rows = cursor.fetchall()
    print("La liste des produits en faible stock")
    print("-" * 30)
    for row in rows:
        print(f"{row[1]}, prix : {row[2]}, {row[5]} en stock")
    cursor.close()
"""Gère la saisie et l'appel de la fonction add_produit"""
def saisie_ajout_produit():
    nom = input("Entrer le nom du produit : ").strip()
    while nom == "" or nom.isnumeric():
        print("Veiller saisir des lettres alphabétiques")
        nom = input("Entrer le nom du produit : ").strip()
    prix = input("Entrer le prix du produit : ").strip()
    while not prix.isnumeric() or prix == "":
        print("Veillez saisir un nombre")
        prix = input("Entrer le prix du produit : ").strip()
    statut_stock = input("Entrer le statut de stock du produit(disponible ou en rupture) : ").strip()
    while statut_stock == "" or statut_stock.isnumeric():
        print("Veiller saisir des lettres alphabétiques")
        statut_stock = input("Entrer le statut de stock du produit(disponible ou en rupture) : ").strip()
    quantite = input("Entrer la quantité du stock du produit : ").strip()
    while not quantite.isnumeric() or quantite == "":
        print("Veillez saisir un nombre")
        quantite = input("Entrer la quantité de stock du produit : ").strip()
    liste_categorie()
    id_categorie = input("Choisie le numero de la catégorie exemple(1) : ").strip()
    while not id_categorie.isnumeric() or id_categorie == "":
        print("Veillez saisir un nombre")
        id_categorie = input("Choisie le numero de la catégorie exemple(1) : ").strip()
    add_produit(nom, prix, statut_stock,quantite, id_categorie)
"""modifier produit et gerer la saisie"""
def update_produit_saisie():
    quantite_modifie = input("Entrer la quantite : ")
    while not quantite_modifie.isnumeric() or quantite_modifie == "":
        print("Veillez saisir un nombre")
        quantite_modifie = input("Entrer la quantité de stock du produit : ").strip()
    iD_produit = input("Entrer l'id du produit : ").strip()
    while not iD_produit.isnumeric() or iD_produit == "":
        print("Veillez saisir un nombre")
        iD_produit = input("Choisie l'id du produit exemple(1) : ").strip()
    modifier_quantite_produits(quantite_modifie, iD_produit)
def menu():
    print("-" * 30)
    print("1. Ajouter une catégorie")
    print("2. La liste des catégories")
    print("3. Ajouter un produit")
    print("4. La liste des produits")
    print("5. Modifier un produit")
    print("6. Historique")
    print("7. La liste des produits avec leur catégorie")
    print("8. La liste des produits en faible stock")
    print("9. Quitter")
    print("-" * 30)
    question = input("Entrer un numéro du menu : ").strip()
    return question
while True:
    choix = menu()
    match choix:
        case "1":
            saisie_add_categorie()
        case "2":
            liste_categorie()
        case "3":
            print("-" * 30)
            saisie_ajout_produit()
        case "4":
            liste_produit()
        case "5":
            liste_produit()
            update_produit_saisie()
        case "6":
            try:
                mouvements()
            except Exception as e:
                print("Erreur :", e)
        case "7":
            liste_produit_categorie()
        case "8":
            stock_faible()
        case _:
            print("Erreur de saisie")
            exit()
            connection.close()

