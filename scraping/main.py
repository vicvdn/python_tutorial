from bs4 import BeautifulSoup

with open('index.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

titre = soup.title.text
# titre = soup.title.string 
print(f"Titre de la page: {titre}")

header = soup.find('h1').string
print(f"Texte de la balise h1: {header}")

# creation d'un dictionnaire pour stocker noms, description et prix des produits
all_products = dict()
products = soup.find_all('li')
for product in products:
    name = product.find('h2').string
    price_str = product.find('p', class_="price").string
    # on cree une liste avec en pos 0 "Prix:" et en 1 le prix
    price_list = price_str.split(" ")
    all_products[name] = {"prix": price_list[1]}
    # la description est le dernier element du paragraphe
    description = product.find_all("p")[-1].string
    all_products[name]["description"] = description.split(" : ")[1]

print(f"Produits: {all_products}")

# transfo des prix en dollar
for product_name in all_products.keys():
    price_str = all_products[product_name]["prix"]
    price_value = price_str.strip("€")
    price = float(price_value)
    # price = float(price_list[1].strip("€"))
    dollar_price = price * 1.2
    all_products[product_name]["prix"] = f"{dollar_price}$"

print(f"Produits: {all_products}")