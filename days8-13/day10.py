def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator():
    def calculate(n1, n2, operation):
        function = operations[operation]
        result = function(n1, n2)
        return result

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    num1 = float(input("What's the first number? "))

    continue_calc = True

    while continue_calc:
        for key in operations:
            print(key)
        operation_symbol = input("Pick an operation from listed above: ")
        num2 = float(input("What's the second number? "))

        answer = calculate(num1, num2, operation_symbol)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input("Do you want to perform another operation? y or n: ") == "y":
            num1 = answer
        else:
            continue_calc = False
            calculator()


calculator()
