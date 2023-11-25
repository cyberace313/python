import random
import math

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

computer_cards = []
user_cards = []

computer_cards.append(random.choice(cards))
computer_cards.append(random.choice(cards))
user_cards.append(random.choice(cards))
user_cards.append(random.choice(cards))
current_score = sum(user_cards)
print(f"Your cards {user_cards} , current score: {current_score}")
print(f"Computer's first card: {computer_cards[0]}")

if sum(user_cards) < 12:
    user_cards.append(random.choice(cards))
    print(user_cards)




print(computer_cards)