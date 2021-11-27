# Calculator
from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for op in operations:
        print(op)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        loop = input(
            f"Type 'y' to continue calculating with {answer}, 'n' to start a new calculation, or 'q' to quit: ").lower()
        if loop == 'y':
            num1 = answer
        elif loop == 'n':
            should_continue = False
            calculator()
        elif loop == 'q':
            should_continue = False
            print("Goodbye!")
        else:
            should_continue = False
            print("Invalid input. Terminating program.")


calculator()
