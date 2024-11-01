# calculator.py

import tkinter as tk
from tkinter import messagebox

# Function to handle button press and update the expression
def press_button(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(value))

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression in the input field
def calculate():
    try:
        # Get the expression from the entry field
        expression = entry.get()
        result = eval(expression)  # Evaluate the expression
        entry.delete(0, tk.END)  # Clear the entry field
        entry.insert(tk.END, str(result))  # Display the result
    except Exception:
        messagebox.showerror("Error", "Invalid input")
        entry.delete(0, tk.END)

# Initialize the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget for displaying the input and result
entry = tk.Entry(root, width=25, font=("Arial", 16), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons for digits, operators, and parentheses in the specified layout
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '(', ')', '+',
    '=', '.', 'clear'
]

# Place buttons in a grid layout
row = 1
col = 0
for button_text in buttons:
    if button_text == '=':
        tk.Button(root, text=button_text, width=5, height=2, command=calculate).grid(row=row, column=col, padx=5, pady=5)
    elif button_text == 'clear':
        tk.Button(root, text=button_text, width=5, height=2, command=clear).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=button_text, width=5, height=2, command=lambda value=button_text: press_button(value)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:  # Move to the next row after every 4 columns
        col = 0
        row += 1

# Start the main GUI loop
root.mainloop()
