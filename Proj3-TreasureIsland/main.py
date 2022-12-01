print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************

''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
choice1 = input("You're at a cross road. Where to you want to go? Type \"left\" or \"right\"\n").lower()
if choice1 == "right":
    choice2 = input("Now you stand before a large river. How do you want to continue? Type \"swim\" or \"bridge\"\n").lower()
    if choice2 == "bridge":
        choice3 = input("You now stumble upon a ginormous lake with a small island in the middle. What will you do? Type \"swim\" \"boat\" \"tunnel\"\n").lower()
        if choice3 == "tunnel":
            choice4 = input("You made it on the island. Where could the treasure be I wonder? Type \"tower\" \"cave\" \"x\"\n").lower()
            if choice4 == "tower":
                print("YEAAAAH BABYYYY! THAT'S WHAT I'VE BEEN WAITING FOOOR! THE TREASURE!!")
            elif choice4 == "cave":
                print("It's a monster cave... you dead...")
            elif choice4 == "x":
                print("It's a trap. There was a hidden bomb. You dead...")
            else:
                print("You gave up... and died during the journey back...")
        elif choice3 == "swim":
            print("You drowned my guy...")
        elif choice3 == "boat":
            print("You capsized... in short... you drowned...")
        else:
            print("You died of old age by not deciding on anything...")
    else:
        print("You drowned...")
else:
    print("You died LOL...")
