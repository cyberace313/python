import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

computer_cards = []
user_cards = []

computer_cards.append(random.choice(cards))
computer_cards.append(random.choice(cards))
user_cards.append(random.choice(cards))
user_cards.append(random.choice(cards))


current_score = sum(user_cards)
computer_score = sum(computer_cards)
print(f"Your cards {user_cards} , current score: {current_score}")
print(f"Computer's first card: {computer_cards[0]}")
get_another = input("Type 'y' to get another card, type 'n' to pass ")


if get_another == "y":
    user_cards.append(random.choice(cards))
    current_score = sum(user_cards)
    print(f"Your cards: {user_cards}, score: {current_score}")
    print(f"Computer cards: {computer_cards}, score {computer_score}")
    if current_score > computer_score:
        print(f"You win! your score is {current_score} and the computer score is {computer_score}")
    elif current_score < computer_score:
        print(f"You lose! your is {current_score} and the computer is {computer_score}")
elif get_another == "n":
    if current_score > computer_score:
        print(f"You win! your score is {current_score} and the computer score is {computer_score}")
    elif current_score < computer_score:
        print(f"You lose! your is {current_score} and the computer is {computer_score}")
