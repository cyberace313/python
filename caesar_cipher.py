
def encrypt(text, shift):
    encrypted_msg = ""
    for letter in text:
        if letter == " ":
            encrypted_msg += letter
        else:
            position = alphabet.index(letter)
            shifted_position = position + shift
            encrypted_msg += alphabet[shifted_position]
    print(f"The encoded text is {encrypted_msg}")


def decrypt(text, shift):
    decrypted_msg = ""
    for letter in text:
        if letter == " ":
            decrypted_msg += letter
        else:
            position = alphabet.index(letter)
            shifted_position = position - shift
            decrypted_msg += alphabet[shifted_position]
    print(f"The decoded text is {decrypted_msg}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
