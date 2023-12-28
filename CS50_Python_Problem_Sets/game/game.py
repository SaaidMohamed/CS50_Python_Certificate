from random import randint
from sys import exit

def main():
    get_level_guess()


def check_guess(n):
    while True:
        guess = input("guess: ").strip()

        if guess.isalpha():
            pass
        else:
            guess = int(guess)
            random_number = randint(0,n)

            if guess == random_number:
                print("Just right!")
                exit()
            elif guess < random_number:
                print("Too small!")
            elif guess > random_number:
                print("Too large!")
            else:
                pass


def get_level_guess():
    while True:
        level = input("Level: ").strip()
        if level.isalpha():
            pass
        elif level.isnumeric():
            level = int(level)
            check_guess(level)

main()
