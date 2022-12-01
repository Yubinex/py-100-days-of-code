import random


print("Welcome to Bill Gamble!")
str_input = input("Enter every person's name, seperated by a ','\n")
people_list = str_input.split(',')
rand = random.randint(0, len(people_list) - 1)
print(f"{people_list[rand]} was chosen! Damn bro, that's rough...")
