def caesar_cipher(text, shift, direction):
    message = ""
    shifted_position = 0
    for letter in text:
        if letter == " ":
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

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar_cipher(text, shift, direction)
