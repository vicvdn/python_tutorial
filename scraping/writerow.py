import requests
from bs4 import BeautifulSoup
import csv

# lien de la page à scrapper
url = "https://www.gov.uk/search/news-and-communications"
reponse = requests.get(url)
page = reponse.content

# transforme (parse) le HTML en objet BeautifulSoup
soup = BeautifulSoup(page, "html.parser")

# récupération de tous les éléments
elements = soup.find_all("li", class_="gem-c-document-list__item")

resultats = []

for element in elements:
    titre = element.find("a", class_="govuk-link")
    description = element.find("p", class_="gem-c-document-list__item-description")
    donnee = (titre.string, description.string)
    resultats.append(donnee)

# création du fichier data.csv
en_tete = ["titre", "description"]
with open("data.csv", "w", newline="") as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=",")
    writer.writerow(en_tete)
    # zip permet d'itérer sur deux listes à la fois
    for donnee in resultats:
        writer.writerow(donnee)


# The code above repeats itself so we want to create functions instead

# Here, we will create a function to extract the elements from the page into a list
def extract(url):
    response = requests.get(url)
    page = response.content

    #then we want to parse into a BeautifulSoup object
    soup = BeautifulSoup(page, 'html.parser')
    elements = soup.find_all('li', class_="gem-c-document-list__item")
    return elements

def transform(element):
    titre = element.find("a", class_="govuk-link")
    description = element.find('p', class_="gem-c-document-list__item-description")
    return (titre.string, description.string)

def charger(donnees):
    en_tete = ["titre", "description"]
    with open(("data.csv"), "w", newline="") as fichier_csv:
        writer = csv.writer(fichier_csv, delimiter=",")
        writer.writerow(en_tete)

        for donnee in donnees:
            writer.writerow(donnee)

def etl(url):
    elements = extract(url)
    resultats = []
    for element in elements:
        resultats.append(transform(element))
    charger(resultats)