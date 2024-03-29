from art import logo
print(logo)

def add (n1, n2):
    return n1 + n2

def subtract (n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    num1 = float(input("What is the first number? "))
    for key in operations:
        print(key)
    continue_calc = True
    while continue_calc:
        operation_symbol = input("Pick an Operation ")
        operation = operations[operation_symbol]
        num2 = float(input("What is the second number? "))
        result = operation(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        keep_going = input(
            f"Type y to continue calculation with {result}, or type 'n' to start a new calculation ")
        if keep_going == "y":
            num1 = result
        elif keep_going == "n":
            continue_calc = False
            calculator()
        else:
            print("Invalid Input")

calculator()