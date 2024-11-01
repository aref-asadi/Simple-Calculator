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

# Configure the grid to be responsive
root.rowconfigure(0, weight=1)  # Entry row
for i in range(1, 6):           # Button rows (5 rows total with buttons)
    root.rowconfigure(i, weight=1)
for j in range(4):               # 4 columns for buttons
    root.columnconfigure(j, weight=1)

# Entry widget for displaying the input and result
entry = tk.Entry(root, font=("Arial", 16), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

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
        btn = tk.Button(root, text=button_text, command=calculate)
    elif button_text == 'clear':
        btn = tk.Button(root, text=button_text, command=clear)
    else:
        btn = tk.Button(root, text=button_text, command=lambda value=button_text: press_button(value))
    
    # Make buttons expand to fill their grid cells
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    
    col += 1
    if col > 3:  # Move to the next row after every 4 columns
        col = 0
        row += 1

# Start the main GUI loop
root.mainloop()
