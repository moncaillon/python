import random


questions = [
    {
        "question": "Quelle est la capitale de la France ? ",
        "reponse": "paris",
    },
    {
        "question": "Combien y a-t-il de continents sur Terre ? ",
        "reponse": "7",
    },
    {
        "question": "Quel est le plus grand ocean du monde ? ",
        "reponse": "pacifique",
    },
    {
        "question": "Qui a peint la Joconde ? ",
        "reponse": "leonard de vinci",
    },
    {
        "question": "Quelle planete est surnommee la planete rouge ? ",
        "reponse": "mars",
    },
    {
        "question": "Combien y a-t-il de jours dans une annee bissextile ? ",
        "reponse": "366",
    },
    {
        "question": "Dans quel pays se trouve la ville de Rome ? ",
        "reponse": "italie",
    },
    {
        "question": "Quel animal est le roi de la jungle ? ",
        "reponse": "lion",
    },
    {
        "question": "Quelle est la monnaie utilisee au Japon ? ",
        "reponse": "yen",
    },
    {
        "question": "Quel est le plus long fleuve du monde ? ",
        "reponse": "nil",
    },
    {
        "question": "Combien font 9 x 8 ? ",
        "reponse": "72",
    },
    {
        "question": "Quel sport se joue avec une raquette et un volant ? ",
        "reponse": "badminton",
    },
    {
        "question": "Quel est le symbole chimique de l'eau ? ",
        "reponse": "h2o",
    },
    {
        "question": "Dans quelle galaxie se trouve la Terre ? ",
        "reponse": "voie lactee",
    },
    {
        "question": "Qui a ecrit Les Miserables ? ",
        "reponse": "victor hugo",
    },
]


score = 0
nombre_questions = 10

questions_choisies = random.sample(questions, nombre_questions)

print("Bienvenue dans le quiz de culture generale !")
print("Reponds aux questions avec des mots simples.")
print()

for element in questions_choisies:
    reponse_utilisateur = input(element["question"]).lower().strip()

    if reponse_utilisateur == element["reponse"]:
        print("Bonne reponse !")
        score = score + 1
    else:
        print("Mauvaise reponse.")
        print("La bonne reponse etait :", element["reponse"])

    print()

print("Quiz termine !")
print("Ton score est de", score, "/", nombre_questions)

if score == nombre_questions:
    print("Excellent, tu as tout juste !")
elif score >= 7:
    print("Tres bon score !")
elif score >= 4:
    print("Pas mal, continue comme ca.")
else:
    print("Tu peux reessayer pour progresser.")
