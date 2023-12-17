rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choices = [rock, paper, scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if user_input <= 2 and user_input > -1:
  user_choice = choices[user_input]
  computer_choice = random.choice(choices)
  print(f"Your Choice: {user_choice}")
  print(f"Computer Choice: {computer_choice}")
  if user_choice == computer_choice:
    print("Stalemate! Try Again")
  elif (user_choice == rock and computer_choice == scissors) or   (user_choice == paper and computer_choice == rock) or           (user_choice == scissors and computer_choice == paper):
    print("You Win!")
  elif (user_choice == rock and computer_choice == paper) or      (user_choice == scissors and computer_choice == rock) or        (user_choice == paper and computer_choice == scissors):
    print("You lose!")
else:
  print("You have inputted an invalid number")