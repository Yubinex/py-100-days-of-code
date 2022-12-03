from art import logo

# Calculator functions


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if x == 0 or y == 0:
        print("Can't divide by 0")
        return None
    return x / y


# Operator dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)

    num1: float = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol: str = input(
            "Which operations do you wish to perform? ")
        num2: float = float(input("What's the second number? "))
        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == "y":
            num1 = result
        else:
            should_continue = False
            calculator()


calculator()
