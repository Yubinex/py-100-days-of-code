# Caesar Cipher
import art


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]

    
    
def caesar(plain_text, shift_amount, direction):
    output = ''
    message = f"{'Encoded' if direction == 'encode' else 'Decoded'} message: "
    for el in plain_text:
        if el in alphabet:
            index = alphabet.index(el)
            if direction == "encode":
                new_index = index + shift_amount
            elif direction == "decode":
                new_index = index - shift_amount
            else:
                print(f"{direction} is an invalid direction...")
                message = '\n'
                break
            output += alphabet[new_index]
        else:
            output += el
    print(message, output)


print(art.logo)
while True:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt, type 'q' to exit:\n")
    if direction == "q":
        print("Exiting program...")
        break
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26
    caesar(plain_text=text, shift_amount=shift, direction=direction)
