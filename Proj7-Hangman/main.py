import random
from ascii_art import stages, logo
from words import word_list


chosen_word = random.choice(word_list)
print(f"Pssst, the solution is {chosen_word}")

display = ['_'] * len(chosen_word)
word_length = len(chosen_word)

lives = 6
flag = False
print(logo)
while not flag:
    print(f"Lives: {lives}")
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}!")
    for index in range(word_length):
        letter = chosen_word[index]
        if letter == guess:
            display[index] = letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print(f"\nLives: {lives}\nYou lost!\n")
            flag = True
    print(f"{''.join(display)}\n")
    if '_' not in display:
        print("\nYou won!\n")
        flag = True
    print(stages[lives])
