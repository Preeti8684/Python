⚙️ Features
     Perform +, -, *, / operations
     Handles invalid inputs gracefully
     Prevents division by zero
     Allows continuous use with an exit option
     Fully function-based structure for clarity and modularity
  Code Explanation
def add(a, b):
    return a + b

# Explanation
 *Adds two numbers and returns the result.

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b


* Prevents division by zero error and safely returns a message if it occurs.

while True:
    operation = input("Enter operation or 'exit' to quit: ")


* Keeps the calculator running until the user enters “exit”.

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input! Please enter numeric values.")


* Handles incorrect inputs gracefully (like entering letters instead of numbers).

🧑‍💻 How to Run the Project

Open the terminal or command prompt.

Navigate to the folder containing calculator.py.

*Run the command:

python calculator.py


🧰 Tools Used

Language: Python

Editor: VS Code / Any text editor

Environment: Command Line / Terminal

🧾 Project Outcome

A well-structured, modular Python CLI calculator demonstrating core programming concepts that are essential for beginners and developers.

Name: Preeti
Internship: Python Developer Internship - Elevate Labs x WESE
Date: November 2025
