def salaire_mensuel(salaire_annuel):
    return (salaire_annuel / 12)

def salaire_hebdomadaire(salaire_mensuel):
    return (salaire_mensuel / 4)

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    if heures_travaillees <= 0 :
        print("pas de salaire horaire si pas d'horaires")
        raise SystemExit("End of program")
    else:
        return (salaire_hebdomadaire / heures_travaillees)

while True:
    salaire_annuel = input("Donnez votre salaire annuel : \n")
    try:
        salaire_annuel = float(salaire_annuel)
        break
    except ValueError:
        print("please enter a valid number")

while True:
    heures_travaillees = input("Donnez votre nombre d'heures travailles par semaine : \n")
    try:
        heures_travaillees = float(heures_travaillees)
        break
    except ValueError:
        print("please enter a valid number")

if heures_travaillees <= 0:
    raise SystemExit("EOP")

mens = salaire_mensuel(salaire_annuel)
heb = salaire_hebdomadaire(mens)
result = heb / heures_travaillees
print(f"Votre salaire horaire est de {result} euros")