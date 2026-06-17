import random

nombre_secret = random.randint(1, 10)

while True:
    choix = input("Devine le nombre : ")
    choix = int(choix)

    if choix == nombre_secret:
        print("Bravo !")
        break
    elif choix < nombre_secret:
        print("C'est plus grand")
    else:
        print("C'est plus petit")
        