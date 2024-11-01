# Calculator

A basic calculator application in Python that performs fundamental arithmetic operations with a graphical user interface (GUI) designed to resemble a typical calculator. This version includes a responsive grid layout, making the interface adaptable to different window sizes.

## Features
- Performs basic arithmetic operations:
  - **Addition**
  - **Subtraction**
  - **Multiplication**
  - **Division** (with handling for division by zero)
  - **Parentheses** for complex expressions
- User-friendly graphical interface with responsive grid layout, making it adaptable to different screen sizes.
- Clear button to reset the input.

## Requirements
- Python 3.x
- `tkinter` (included with standard Python installations)

## Installation

1. Clone this repository or download the code:
   ```bash
   git clone https://github.com/aref-asadi/calculator.git
   cd calculator
   ```

2. Ensure you have Python 3 installed. You can check your Python version with:
   ```bash
   python --version
   ```

## Usage

1. Open a terminal.
2. Navigate to the directory where `calculator.py` is located.
3. Run the calculator:
   ```bash
   python calculator.py
   ```
4. In the GUI window:
   - Click on buttons to build a mathematical expression.
   - Press `=` to calculate and display the result.
   - Use `clear` to reset the input field for a new calculation.

## Button Layout

The button layout in the GUI resembles a typical calculator, with each button performing the following functions:

| Button | Function               |
|--------|-------------------------|
| 0–9    | Enters digits          |
| +, -, *, / | Performs basic operations |
| ( , )  | Allows grouping with parentheses |
| =      | Evaluates the expression and displays the result |
| .      | Adds a decimal point    |
| clear  | Clears the input field |

The layout in the GUI is as follows:

```plaintext
7    8    9    /
4    5    6    *
1    2    3    -
0    (    )    +
=    .    clear
```

## Code Structure

The project consists of a single Python file, `calculator.py`, which contains:
1. **Arithmetic Functionality**: Handles the expression-building and calculation using Python’s `eval()` function.
2. **GUI Design**: Created using `tkinter` with buttons laid out in a grid pattern to resemble a calculator.
3. **Responsive Grid Layout**: The grid layout is responsive, allowing the calculator to adapt its button sizes based on the window size.
4. **Error Handling**: Displays an error message for invalid inputs.

## Error Handling

- **Division by zero**: Displays an error message for division by zero.
- **Invalid input**: Shows an error message for improperly formatted expressions.

## License
This project is open-source and available under the GPL-3.0 License.