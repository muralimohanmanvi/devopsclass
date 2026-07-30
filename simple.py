def calculator(a, b, operator):

    if operator == "+":
        print("Sum =", a + b)

    elif operator == "-":
        print("Difference =", a - b)

    elif operator == "*":
        print("Multiplication =", a * b)

    elif operator == "/":
        print("Division =", a / b)

    else:
        print("Invalid Operator")

# User Input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

calculator(num1, num2, op)
