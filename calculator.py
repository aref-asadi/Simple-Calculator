# calculator.py
import os, platform


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
    else:
        return "Unknown system."


# Define a function to perform addition
def add(x, y):
    return x + y  # Returns the sum of x and y


# Define a function to perform subtraction
def subtract(x, y):
    return x - y  # Returns the difference between x and y


# Define a function to perform multiplication
def multiply(x, y):
    return x * y  # Returns the product of x and y


# Define a function to perform division
def divide(x, y):
    # Check for division by zero
    if y == 0:
        return "Error: Division by zero"  # Return error message if y is zero
    return x / y  # Returns the division of x by y

def exponentiate(x, y):
     return x ** y  # Returns the exponentiate of x by y   

def square_root(n, tolerance=1e-10):
    if n < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    if n == 0:
        return 0

    x = n  # Initial guess
    while True:
        new_x = 0.5 * (x + n / x)
        if abs(new_x - x) < tolerance:
            return new_x
        x = new_x

# Main calculator function to handle user input and perform operations
def calculator():
    # Display the calculator menu
    print("Calculator")
    print("Select operation:\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Other\n")

    # Get the user's choice of operation
    choice = input("Enter your choice (1/2/3/4/5): ")

    # Check if the choice is valid (1, 2, 3, or 4)
    if choice in ("1", "2", "3", "4"):
        try:
            # Prompt the user to enter two numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform the selected operation based on the user's choice
            if choice == "1":
                print(
                    f"Result: {add(num1, num2)}"
                )  # Calls add function and displays result
            elif choice == "2":
                print(
                    f"Result: {subtract(num1, num2)}"
                )  # Calls subtract function and displays result
            elif choice == "3":
                print(
                    f"Result: {multiply(num1, num2)}"
                )  # Calls multiply function and displays result
            elif choice == "4":
                print(
                    f"Result: {divide(num1, num2)}"
                )  # Calls divide function and displays result
        except ValueError:
            # Handle the case where the input is not a number
            print("Invalid input. Please enter a number.")
    elif choice == "5":
        clear_screen()
        print("Calculator")
        print("Select operation:\n")
        print("1. Square root")
        print("2. Exponentiation\n")

        choice = input("Enter your choice (1/2): ")
        if choice in ("1", "2"):
            try:
                if choice == "1":
                    # Prompt the user to enter number
                    num = float(input("Enter number: "))
                    print(f"Result: {square_root(num)}")  # Calls divide function and displays result  
                elif choice == "2":
                    # Prompt the user to enter two numbers
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    print(f"Result: {exponentiate(num1, num2)}")  # Calls divide function and displays result  
            except ValueError:
                print("Invalid input. Please enter a number.")
    else:
        # Handle the case where an invalid operation choice is entered
        print("Invalid choice. Please select a valid operation.")


# Ensure the calculator function only runs if the script is executed directly
if __name__ == "__main__":
    calculator()  # Call the main calculator function
