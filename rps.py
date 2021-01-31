r = "Rock"
p = "paper"
s = "scissors"

player = "Player"
computer = "Computer"


name = input(f"Hello, {player} what is your name? ").capitalize()
game = input(f"How about a game of Rock Paper Scissors {name}? ")


if game == "no":
    quit()

elif game == "yes":
    input(f"Okay {name} choose Rock, Paper Scissors ")

    print(f"I choose {r}")
