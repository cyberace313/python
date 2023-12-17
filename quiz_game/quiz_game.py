
print("Welcome to Quiz Game")

score = 0
questions = [
     "What is the capital of Russia? ",
     "What is the largest big cat? ",
     "What planet is the largest in the solar system? ",
     "Which planet is known as the red plane? ",
     "What animal is called the king of the jungle? ",
]

choices = [
    "A. Moscow \nB. London \nC. Berlin \nD. Paris",
    "A. Leopard \nB. Tiger \nC. Lion \nD. Cheetah",
    "A. Uranus \nB. Earth \nC. Neptune \nD. Jupiter",
    "A. Mars \nB. Mercury \nC. Venus \nD. Pluto",
    "A. Elephant \nB. Polar Bear \nC. Lion \nD. Tiger",
]

answers = [
    "A", "B", "D", "A", "C"
]
question_num = len(questions)

for i in range(0, question_num):
    print(f"{i + 1}. {questions[i]}")
    print(choices[i])
    user_input = input("Choose one of the options. Type 'A', 'B', 'C', or 'D' ").upper()
    if user_input == answers[i]:
        score += 1

print(f"You score is {score} out of 5")
