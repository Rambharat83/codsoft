def calculator():
    print("Choose operation: +, -, *, /, ^")
    op = input("Enter operation: ")
    try:
        f1 = float(input("Enter first number: "))
        s1 = float(input("Enter second number: "))

        if op == '+':
            res = f1 + s1
        elif op == '-':
            res = f1 - s1
        elif op == '*':
            res = f1 * s1
        elif op == '/':
            res = f1 / s1 if s1 != 0 else "Error! Division by zero!"
        elif op == '^':
            res = f1 ** s1
        else:
            print("Invalid operation.")
            calculator()

        print("Result:", res)
        another = input("would you like to continue (yes/no): ").strip().lower()
        if another != 'yes':
            print("Thankyou")
        else:
            calculator()
        return
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        calculator()

calculator()
