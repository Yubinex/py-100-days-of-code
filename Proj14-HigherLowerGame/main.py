from game_data import data
from art import logo, vs
import random
import os
import platform
import sys

# implement clear() function
PLATFORM = platform.system()
if PLATFORM == "Linux":
    def clear(): return os.system('clear')
elif PLATFORM == "Windows":
    def clear(): return os.system('cls')
else:
    print(f"{PLATFORM} is not supported...")
    def clear(): return os.system('cls')
    os.abort


def get_random_data():
    return random.choice(data)


def get_display_string(data, char):
    string = f"{data['name']}, a {data['description']}, from {data['country']}"
    if char == 'A':
        return f"Compare A: {string}."
    else:
        return f"Against B: {string}."


def check_guess(followers_a, followers_b, user_guess):
    if followers_a > followers_b and user_guess == 'a':
        return True
    elif followers_a < followers_b and user_guess == 'b':
        return True
    else:
        return False
    

def run():
    clear()
    
    score = 0
    running = True

    print(logo)
    while running:

        data_a = get_random_data()
        data_b = get_random_data()
        while data_a == data_b:
            data_a = get_random_data()
            data_b = get_random_data()

        print(get_display_string(data=data_a, char='A'))
        print(vs)
        print(get_display_string(data=data_b, char='B'))
        
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        clear()
        print(logo)
        if check_guess(data_a["follower_count"], data_b["follower_count"], guess):
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            running = False
            print(f"You're wrong! Final score: {score}")
            
    while input("Play again? y/n ").lower() == "y":
        run()
    print("Program finished...")
    sys.exit()  #? Don't know if this is needed...
    
run()
