import pandas

nato_df = pandas.read_csv("Proj25-NATO_Alphabet/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

def generate_phonetic():
    user_input = input("Enter a word: ").strip().upper()
    try:
        phonetic_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()
