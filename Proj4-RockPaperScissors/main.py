import random


ASCII_ART = [
"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n> "))
computer_choice = random.randint(0,2)

res = ""
if player_choice >= 3 or player_choice < 0:
    print("Invalid input! ...")
elif player_choice == 0 and computer_choice == 2:
    res = "Player won!"
elif computer_choice == 0 and player_choice == 2:
    res = "Computer won!"
elif player_choice > computer_choice:
    res = "Player won!"
elif computer_choice > player_choice:
    res = "Computer won!"
elif player_choice == computer_choice:
    res = "It's a draw!"

print(f"You chose:\n{ASCII_ART[player_choice]}")
print(f"Computer chose:\n{ASCII_ART[computer_choice]}")
print(f"\n-> {res}\n")
