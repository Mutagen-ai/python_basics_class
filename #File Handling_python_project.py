#File Handling
#Python Project
import math


class Calculator:

    def __init__(self):
        self.operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }

    def add_operation(self, symbol, func):
        self.operations[symbol] = func

    def calculate(self, num1, symbol, num2):
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            print("Error: Both inputs must be numbers.")
            raise TypeError("Inputs must be numbers.")

        if symbol not in self.operations:
            print(f"Error: '{symbol}' is not a recognised operation.")
            raise ValueError(f"Unknown operation: {symbol}")

        result = self.operations[symbol](num1, num2)
        return result


def exponentiation(a, b):
    return math.pow(a, b)

def square_root(a, b=None):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)

def logarithm(a, b=None):
    if a <= 0:
        raise ValueError("Logarithm undefined for zero or negative numbers.")
    return math.log(a)


def main():
    calc = Calculator()

    calc.add_operation("**", exponentiation)
    calc.add_operation("sqrt", square_root)
    calc.add_operation("log", logarithm)

    print("Welcome to the Advanced Calculator")
    print("Operations: +  -  *  /  **  sqrt  log")
    print("Type 'exit' at any prompt to quit.\n")

    while True:
        try:
            raw1 = input("Enter first number: ").strip()
            if raw1.lower() == "exit":
                break
            num1 = float(raw1)

            symbol = input("Enter operation: ").strip()
            if symbol.lower() == "exit":
                break

            if symbol in ("sqrt", "log"):
                num2 = 0
            else:
                raw2 = input("Enter second number: ").strip()
                if raw2.lower() == "exit":
                    break
                num2 = float(raw2)

            result = calc.calculate(num1, symbol, num2)
            print(f"Result: {result}\n")

        except ValueError as e:
            print(f"ValueError: {e}\n")
        except TypeError as e:
            print(f"TypeError: {e}\n")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.\n")
        except Exception as e:
            print(f"Something went wrong: {e}\n")

    print("Goodbye!")


if __name__ == "__main__":
    main()