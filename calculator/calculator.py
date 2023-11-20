from art import logo
print(logo)

#Operations:
def add(a, b):
    """Performs addition between two given numbers"""
    return a + b
def subtract(a, b):
    """Performs subtractions between two given numbers"""
    return a - b
def multiply(a, b):
    """Performs multiplication between two given numbers"""
    return a * b
def divide(a, b):
    """Performs division between two given numbers"""
    return a / b

a = int(input("What is the first number? "))

operation = input("""
+
-
*
/
Pick and Operation """)
b = int(input("What is the second number? "))

result = 0
if operation == "+":
    result = add(a, b)
elif operation == "-":
    result = subtract(a, b)
elif operation == "*":
    result = multiply(a, b)
elif operation == "/":
    result = divide(a, b)

print(result)