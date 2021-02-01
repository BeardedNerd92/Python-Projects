
r = "Rock"
p = "paper"
s = "scissors"

player = "Player"
computer = "Computer"


name = input(f"Hello, {player} please type your name your name ").capitalize()
game = input(f"How about a game of Rock Paper Scissors {name}? ")


if game == "no":
    quit()

if game == "yes" or "okay":
    print(f"Okay I choose {r}")
    guess1 = input(f"Your turn {name} choose Rock, Paper Scissors: ")

    if guess1 == p:
        print(f"You win paper covers rock.")
    elif guess1 == r:
        print("Tie")
    elif guess1 == s:
        print(f"I win rock smashes scissors.")
