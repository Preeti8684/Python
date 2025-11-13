# calculator.py

# Function definitions for each operation(+,-,*,/)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

# The function that perform all operation 
def calculator():
    print("Welcome to Command Line Calculator!")
    print("Available operations: +  -  *  /")
    print("Type 'exit' to quit.\n")
# loop for take user all inputs one by one 
    while True:
        operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ").strip()

        if operation.lower() == 'exit':
            print("Thank you for using the calculator. Goodbye!")
            break

        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please try again.\n")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.\n")
            continue

        # Perform calculation
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)

        print(f"Result: {result}\n")

# Run the calculator
if __name__ == "__main__":
    calculator()
