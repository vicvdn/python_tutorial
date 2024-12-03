# variables and their types

    # nom = "vic"
    # age = 23
    # taille = 1.71
    # est_etudiant = True

    # print(f"Je m'appelle {nom}, j'ai {age} ans, je mesure {taille}m. Etudiante? {est_etudiant}")
    # a = type(nom)
    # print(f"type: {a}")
    # print(f"{type(age)}")
    # print(type(taille))
    # print(type(est_etudiant))

#lists
    # fruits = ["pomme", "banane", "orange"]
    # fruits.append("kiwi")
    # print(fruits)
    # fruits[1] = "ananas"
    # print(fruits)
    # fruits.sort()
    # print(fruits)

#dictionnaries

taux_de_conversion = {}
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2
taux_de_conversion = dict()
# on a cree un dictionnaire vide, que l'on remplit ensuite
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2
print(taux_de_conversion)
# on accede a une valeur du dictionnaire via sa cle
print(f" tx conv fb: {taux_de_conversion['facebook']}")