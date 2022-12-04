import random
from art import logo


def get_random_number():
    return random.randint(1, 100)


def run_game():
    print(logo)

    random_number: int = get_random_number()
    attemps: int = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        difficulty: str = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == "easy":
            attemps = 10
            break
        elif difficulty == "hard":
            attemps = 5
            break
        else:
            print("Not a valid option...")

    while attemps > 0:
        print(f"You have {attemps} attemps remaining to guess the number.")
        guess: int = int(input("Make a guess: "))
        if guess == random_number:
            print(f"You got it! The answer was {random_number}")
            break
        elif guess > random_number:
            print("Too high.\nGuess again.")
            attemps -= 1
        elif guess < random_number:
            print("Too low.\nGuess again.")
            attemps -= 1
        else:
            print("You lost! No more attempts left.")
            break

    while input("Play again? y/n ") == 'y':
        run_game()


run_game()
