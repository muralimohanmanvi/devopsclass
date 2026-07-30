def calculate(a, b, operator):

    if operator == "+":
        print("Sum =", a + b)

    elif operator == "-":
        print("Difference =", a - b)

    elif operator == "*":
        print("Multiplication =", a * b)

    elif operator == "/":
        print("Division =", a / b)

    else:
        print("Invalid operator")


op = input("Enter operator (+, -, *, /): ")

calculate(5, 8, op)
