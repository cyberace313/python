#Step 1
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

######Choose a random Word#####
chosen_word = random.choice(word_list)
num_of_letters = len(chosen_word)

#####Display the blank version of the word:#####
blank_list = []
for i in range(0, num_of_letters):
    blank_list.append("_")



#####Receive input and check whether the letter matches any letter in the word#####
game_over = False
while game_over == False:
    guess = input("Guess a letter: ").lower()
    for i in range(0, len(chosen_word)):
        if chosen_word[i] == guess:
            blank_list[i] = guess
    seperator = " "
    display = seperator.join(blank_list)
    print(display)
    if "_" not in blank_list:
        game_over = True
        print("You Win!")







