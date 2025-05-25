# I change that not you ;)
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

# Change from RosenCodes20
def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            print("Result:", add(num1, num2))
        elif op == '-':
            print("Result:", subtract(num1, num2))
        elif op == '*':
            print("Result:", multiply(num1, num2))
        elif op == '/':
            print("Result:", divide(num1, num2))
        else:
            print("Invalid operator.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()
