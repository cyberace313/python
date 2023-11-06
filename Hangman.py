#Step 1
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

chosen_word = random.choice(word_list)
print(chosen_word)
num_of_letters = len(chosen_word)

blank_list = []
for i in range(0, num_of_letters):
    blank_list.append("_")

seperator = " "
blank = seperator.join(blank_list)
print(blank)

guess = input("Guess a letter: ").lower()

index = chosen_word.find(guess)
print(index)




