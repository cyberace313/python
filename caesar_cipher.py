
def encrypt(text, shift):
    text_list = list(text)
    shifted_list = []
    for letter in text_list:
        letter_index = alphabet.index(letter)
        shifted_index = letter_index + shift
        shifted_list += alphabet[shifted_index]
    encrypted_msg = "".join(shifted_list)
    print(encrypted_msg)


def decrypt(text, shift):
    text_list = list(text)
    shifted_list = []
    for letter in text_list:
        letter_index = alphabet.index(letter)
        shifted_index = letter_index - shift
        shifted_list += alphabet[shifted_index]
    decrypted_msg = "".join(shifted_list)
    print(decrypted_msg)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

correct_input = False
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

while correct_input == False:
    print("Please choose from the two given options with exact spelling")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode" or direction == "decode":
        correct_input = True


text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)




    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.