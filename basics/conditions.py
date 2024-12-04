#exo conditions

while True:
    input_gauche = input("enter left number : ")
    try:
        nombre_a_gauche = int(input_gauche)
        break
    except ValueError :
        print("Please enter a valid number :) ")

while True:
    input_droite = input("enter right number : ")
    try:
        nombre_a_droite = int(input_droite)
        break
    except ValueError :
        print("Please enter a valid number :) ")


if not isinstance(nombre_a_droite, int) or not isinstance(nombre_a_gauche, int):
    print("we aint an int")
    raise SystemExit("End of the program")

operator = input("enter operator + or - or * or / : ")

if operator not in ['+', '-', '*', '/']:
    print("operator is invalid")
    raise SystemExit("End of the program")

match operator:
    case '+':
        print("we add things")
        result = nombre_a_gauche + nombre_a_droite
    case '-':
        print("we substract things")
        result = nombre_a_gauche - nombre_a_droite
    case '*':
        print("we multiply things")
        result = nombre_a_gauche * nombre_a_droite
    case '/':
        print("we divide things")
        if nombre_a_droite == 0:
            print("but not by 0!")
            raise SystemExit("End of the program")
        else :
            result = nombre_a_gauche / nombre_a_droite

print(f"the result is {result}")