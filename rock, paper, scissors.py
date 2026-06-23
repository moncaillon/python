import random

choices = ["rock", "paper", "scissors"]
games_played = 0
wins = 0
losses = 0
draws = 0

while True:
    players_choice = input("Choose rock, paper or scissors: ").lower()
    games_played += 1
    computer_choice = random.choice(choices)

    if players_choice == computer_choice:
        print("Draw")
        draws += 1
    elif players_choice == "rock":
        if computer_choice == "scissors":
            print("you win")
            wins += 1
        else:
            print("you fail")
            losses += 1
    elif players_choice == "paper":

        if computer_choice == "rock":
            print("you win")
            wins += 1
        else:
            print("you fail")
            losses += 1
    elif players_choice == "scissors":
        if computer_choice == "paper":
            print("you win")
            wins += 1
        else:
            print("you lose")
            losses += 1

    print("Games played:", games_played)
    print("Win percentage:", wins / games_played * 100, "%")
    print("Loss percentage:", losses / games_played * 100, "%")
    print("Draw percentage:", draws / games_played * 100, "%")
