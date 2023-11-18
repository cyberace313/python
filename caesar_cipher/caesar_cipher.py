import art
print(art.logo)
def caesar_cipher(text, shift, direction):
    message = ""
    shifted_position = 0
    if shift > 26:
        shift = shift % 26
    for letter in text:
        if letter == " " or letter not in alphabet:
            message += letter
        else:
            position = alphabet.index(letter)
            if direction == "decode":
                shifted_position = position - shift
            elif direction == "encode":
                shifted_position = position + shift
            message += alphabet[shifted_position]
    print(f"The {direction}d text is {message}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

run = True

while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar_cipher(text, shift, direction)
    run_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if run_again == "no":
        run = False