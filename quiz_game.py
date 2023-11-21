
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
    "A. Moscow B. London C. Berlin D. Paris",
    "A. Leopard B. Tiger C. Lion D. Cheetah",
    "A. Uranus B. Earth C. Neptune D. Jupiter",
    "A. Mars B. Mercury C. Venus D. Pluto",
    "A. Elephant B. Polar Bear C. Lion D. Tiger",
]

answers = [
    "A", "B", "D", "A", "C"
]
question_num = len(questions)
print(question_num)

for i in range(0, question_num):
    print(questions[i])
    print(choices[i])
    user_input = input("Choose one of the options. Type 'A', 'B', 'C', or 'D' ").upper()
    if user_input == answers[i]:
        score += 1

print(f"You score is {score} out of 5")
