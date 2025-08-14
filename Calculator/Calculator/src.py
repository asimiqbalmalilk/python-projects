def calculator():
    """Simple calculator that can perform basic arithmetic operations.
    Allows continuous operations on the result or restarting with new numbers.
    """

    def add(a, b):
        return a + b

    def subt(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b

    while True:
        try:
            n1 = float(input("Enter your first number: "))
            n2 = float(input("Enter your second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        operation = input("Choose operation (+, -, *, /): ").strip()

        if operation == '+':
            result = add(n1, n2)
        elif operation == '-':
            result = subt(n1, n2)
        elif operation == '*':
            result = multiply(n1, n2)
        elif operation == '/':
            result = divide(n1, n2)
        else:
            print("Invalid operation.")
            continue

        print(f"Result: {result}")

        # Loop for continuous operations on the current result
        while True:
            ask_again = input("Use the result for another operation? (Y/N, 0 to exit): ").upper()

            if ask_again == 'Y':
                try:
                    n1 = result
                    n2 = float(input("Enter the second value: "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

                oper = input("Choose operation (+, -, *, /): ").strip()
                if oper == '+':
                    result = add(n1, n2)
                elif oper == '-':
                    result = subt(n1, n2)
                elif oper == '*':
                    result = multiply(n1, n2)
                elif oper == '/':
                    result = divide(n1, n2)
                else:
                    print("Invalid operation.")
                    continue

                print(f"Result: {result}")

            elif ask_again == 'N':
                break
            elif ask_again == '0':
                print("Exiting calculator. Goodbye!")
                return
            else:
                print("Invalid choice. Please enter Y, N, or 0.")

# Run the calculator
if __name__ == "__main__":
    calculator()
