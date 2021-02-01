rock = "Rock"
paper = "paper"
scissors = "scissors"

player = "Player"
computer = "Computer"


name = input(f"Hello, {player} please type your name ").capitalize()
game = input(f"How about a game of Rock Paper Scissors {name}? ")


if game == "no":
    quit()

elif game == "yes" or "okay":
    print(f"Okay I choose {rock}")
    guess1 = input(f"Your turn {name}: ")

    if guess1 == paper:
        print(f"You win paper covers rock.")

    elif guess1 == rock:
        print("Tie")

    elif guess1 == scissors:
        print(f"I win rock smashes scissors.")
