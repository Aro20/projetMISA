#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Création d'une base de données pour créer un répertoire de contacts


import sqlite3
import sys, re

nom_base='Data.sq3'	# Nom de la base de données
# Pour l'affichage des couleurs
ROUGE = '\033[00;31m'
BLEU = '\033[00;36m'
NORM = '\033[00m'

# Fonction affichant un menu
def menu():
	print("\t\t\t\t - Menu -")
	print("[ 1 ] - Ajouter un contact -")
	print("[ 2 ] - Rechercher un contact -")
	print("[ 3 ] - Afficher la liste de contact -")
	print("[ 4 ] - Quitter -")
	choix = input(" $ ")

	if choix == '1':
		ajout()
	if choix == '2':
		recherche()
	if choix == '3':
		afficher()
	if choix == '4':
		print("Sortie de la base de données", nom_base)
		connexion.close()
		sys.exit(0)
	else:
		menu()

# Fonction d'ajout de contact
def ajout():
	print("\t\t\t -- Ajouter un nouveau contact -- ")
	while 1:
		nom = input("Nom > ")
		if nom == '':
			break;
		prenom = input("Prénom > ")
		date_naiss = input("Date de naissance > ")
		tel = input("Téléphone >  ")
		adresse = input("Adresse postale > ")
		mail = input("Adresse email > ")
		req = "INSERT INTO contacts(nom, prenom, date_naiss, tel, adresse, mail) VALUES(?, ?, ?, ? ,?, ?)"
		curseur.execute(req, (nom, prenom, date_naiss, tel, adresse, mail))

	print("---- Nouveau contact enregistrer ----------------> [ OK ]")
	# Transfert effectif des enregistrements dans la BDD
	connexion.commit()


# Fonction d'affichage de la liste de contacts
def afficher():
	nbContact=0
	curseur.execute("select * from contacts")
	for enreg in curseur:	# Boucler sur les enregistrements et les affichés au format sqlite3
		print(ROUGE,'Nom: {}\nPrénom: {}\nDate de naissance: {}\nTéléphone: {}\nAdresse: {}\nEmail: {}\n'.format(*enreg),NORM)
		nbContact = nbContact + 1

	print("Nombre de contact(s):", nbContact)
	print("\t\t\t** Fin des enregistrements **\n")

# Fonction de recherche d'un contact
def recherche():
	print("\t\t\t-- Recherche de contact --")
	nom = input("Nom a rechercher: ")
	curseur.execute("select * from contacts")
	for enreg in curseur:
		match = re.search('{}'.format(*enreg), nom, re.IGNORECASE)
		if match != None:
			print(ROUGE,'Nom: {}\nPrénom: {}\nDate de naissance: {}\nTéléphone: {}\nAdresse: {}\nEmail: {}\n'.format(*enreg),NORM)
			menu()
	print(ROUGE,"- Contact", nom, " inconnu -",NORM)


# Bandeau d'acceuil
print(BLEU,"\t\t\t=============================")
print("\t\t\t       Base de données")
print("\t\t\t=============================",NORM)

# Connexion a la base de données - création du curseur
connexion = sqlite3.connect(nom_base)
curseur = connexion.cursor()

# Création des tables, L'utilisation de try/except permet de réutiliser
# le script indéfiniment, même si la base de donnée existe déja.
try:
	req = "CREATE TABLE contacts(nom TEXT, prenom TEXT, date_naiss INTEGER, tel INTEGER, adresse TEXT, mail TEXT)"
	curseur.execute(req)
except:
	pass
	
# Appeller la fonction menu()
menu()
