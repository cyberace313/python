
import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list
stages = hangman_art.stages
lives = 6


######Choose a random Word#####
chosen_word = random.choice(word_list)
num_of_letters = len(chosen_word)

#####Display the blank version of the word:#####
blank_list = []
for i in range(0, num_of_letters):
    blank_list.append("_")



#####Receive input and check whether the letter matches any letter in the word#####
game_over = False
guesses = []
while game_over == False:
    guess = input("Guess a letter: ").lower()
    if guess in guesses:
        print("You guessed this letter already")
    guesses.append(guess)
    for i in range(0, len(chosen_word)):
        if chosen_word[i] == guess:
            blank_list[i] = guess

    if guess not in chosen_word:
        lives = lives - 1
        if lives == 0:
            game_over = True
            print("You Lose!")

    seperator = " "
    display = seperator.join(blank_list)
    print(display)
    if "_" not in blank_list:
        game_over = True
        print("You Win!")
    print(stages[lives])






