# Import des bibliothèques nécessaires
from selenium import webdriver
import re
from bs4 import BeautifulSoup
import csv
import requests
import time
import ent as et

# Initialisation du dictionnaire pour stocker les entreprises
Entreprises = {}

# Lecture du fichier 'liste.txt' contenant les noms d'entreprises
with open('liste.txt', "r", encoding="utf-8-sig") as file:
    lines = file.readlines()
    for line in lines:
        ListeEn = line.strip()
        Entreprises[ListeEn] = None

# Affiche la taille du dictionnaire
print(len(Entreprises))

# Message de début
print("debut")

# Initialisation du pilote Chrome
driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")
x = 1

# Ouverture du fichier CSV pour écrire les résultats
with open('resultats.csv', mode='w', newline='', encoding='utf-8-sig') as file:
    fieldnames = ['Entreprises', 'Email']
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')

    # Boucle à travers les entreprises
    for Entreprise in Entreprises:

        # Appel de la fonction 'facebookS' du module 'etab' avec les paramètres nécessaires
        url = et.facebookS(ListeEn, requests, BeautifulSoup, time)

        # Vérification si l'URL est valide
        if not (url == None):
            driver.get(url)

            # Attendre 30 secondes pour que l'utilisateur puisse mettre les logs de connexion de sa page facebook (uniquement pour la première itération)
            if x == 1:
                time.sleep(30)
                x = 10

            # Récupération du code source de la page
            page_source = driver.page_source

            # Analyse HTML avec BeautifulSoup
            soup = BeautifulSoup(page_source, 'html.parser')

            # Recherche des adresses e-mail
            email_matches = soup.find_all(
                "span", text=re.compile(r"[\w\.-]+@[\w\.-]+"))
            
            # Si une adresse e-mail est trouvée, la récupérer
            if email_matches:
                email = email_matches[0].get_text()
            else:
                email = "N/A"
            # Afficher l'adresse e-mail
            print(email)
        else:
            # Si l'URL n'est pas valide, marquer comme 'N/A'
            email = "N/A"

        # Écrire les résultats dans le fichier CSV
        writer.writerow({'Entreprises': Entreprise, 'Email': email})

# Fermeture du pilote Chrome
driver.quit()
