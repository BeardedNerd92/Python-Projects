import random

name = input('Please enter your name: ').capitalize()
computer = input(f'Hello {name}, I am thinking of a number between 1 and 75... (Please press enter to continue)')
user_input = input('Do you want to try guessing the number... (Enter y/n)? ')

computer_input = random.randint(70,72)

def secret_num():
    while True:
        if user_input.lower() == 'y':
            guess = int(input(f'Input a number {name}: '))
        elif user_input == 'n':
            print(f'Okay {name}, thanks for playing')
            print('Now signing off...')
        if guess > computer_input:
            print(f'Sorry {name}, the number {guess} is less than the one chosen.')
        elif guess < computer_input:
            print(f'Sorry {name}, the number {guess} is greater than the one chosen.')
        elif guess == computer_input:
            print(F'NICE! {name}, {guess} is the number I am looking for.')

        try_again = input(f'Would you like another shot {name} (Enter y/n): ')
        if try_again.lower() != 'y':
            print(f'Thanks for playing {name}.')
            break 
secret_num()