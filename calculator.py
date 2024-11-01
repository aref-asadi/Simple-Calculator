# calculator.py

import tkinter as tk  # Import tkinter for GUI
from tkinter import messagebox  # Import messagebox for error dialogs
import math  # Import math for square root function

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

# Define a function for exponentiation
def exponentiate(base, exponent):
    return base ** exponent  # Returns base raised to the power of exponent

# Define a function for square root
def square_root(x):
    # Check for negative input
    if x < 0:
        return "Error: Square root of a negative number is not defined"  # Handle negative input
    return math.sqrt(x)  # Returns the square root of x

# Function to perform the selected operation and display the result
def calculate():
    try:
        # Retrieve the first input number
        num1 = float(entry1.get())
        # For square root, only one number is required; set num2 to 0 if operation is square root
        num2 = float(entry2.get()) if operation.get() != "Square Root" else 0
        
        # Perform calculation based on selected operation
        if operation.get() == "Addition":
            result = add(num1, num2)
        elif operation.get() == "Subtraction":
            result = subtract(num1, num2)
        elif operation.get() == "Multiplication":
            result = multiply(num1, num2)
        elif operation.get() == "Division":
            result = divide(num1, num2)
        elif operation.get() == "Exponentiation":
            result = exponentiate(num1, num2)
        elif operation.get() == "Square Root":
            result = square_root(num1)
        
        # Display result in the result label
        result_label.config(text=f"Result: {result}")
    except ValueError:
        # Show error message if the input is not valid
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# GUI setup
root = tk.Tk()  # Create the main application window
root.title("Simple Calculator")  # Set the window title

# Operation selection dropdown
operation = tk.StringVar(value="Addition")  # Store the selected operation
tk.Label(root, text="Select Operation:").pack()  # Label for operation selection
# Dropdown menu for selecting operation
operations = ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation", "Square Root"]
tk.OptionMenu(root, operation, *operations).pack()

# Input field for the first number
tk.Label(root, text="Enter first number:").pack()  # Label for first number
entry1 = tk.Entry(root)  # Entry widget for first number input
entry1.pack()

# Input field for the second number
tk.Label(root, text="Enter second number (if applicable):").pack()  # Label for second number
entry2 = tk.Entry(root)  # Entry widget for second number input
entry2.pack()

# Button to perform calculation
tk.Button(root, text="Calculate", command=calculate).pack()  # Button to trigger calculation

# Label to display the result
result_label = tk.Label(root, text="Result: ")  # Label to show result
result_label.pack()

# Run the GUI application
root.mainloop()  # Starts the tkinter event loop, keeping the window open
