from art import logo
print(logo)

def calculate(a, b):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b

calc = True
while calc:
    first_num = float(input("What is the first number? "))
    operation = input("""
    +
    -
    *
    /
    Pick and Operation """)
    second_num = float(input("What is the second number? "))
    result = calculate(first_num, second_num)
    print(f"{first_num} {operation} {second_num} = {result}")
    continue_calc = True
    while continue_calc:
        keep_going = input(f"Type y to continue calculation with {result}, or type 'n' to start a new calculation or type 'e' to exit the calculator ")
        if keep_going == "y":
            first_num = result
            operation = input("""
              +
              -
              *
              /
              Pick and Operation """)
            second_num = float(input("What is the second number? "))
            result = calculate(first_num, second_num)
            print(f"{first_num} {operation} {second_num} = {result}")
        elif keep_going == "n":
            continue_calc = False
        elif keep_going == "e":
            continue_calc = False
            calc = False
        else:
            print("Invalid Input")
