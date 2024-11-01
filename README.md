# Calculator

A basic calculator application in Python that performs fundamental arithmetic operations with both command-line (CLI) and graphical user interface (GUI) options.

## Features
- Performs basic arithmetic operations:
  - **Addition**
  - **Subtraction**
  - **Multiplication**
  - **Division** (with handling for division by zero)
  - **Exponentiation**
  - **Square Root** (with handling for negative numbers)
- Two user interface options:
  - **Command-Line Interface (CLI)**
  - **Graphical User Interface (GUI)** using `tkinter`
- Supports multiple calculations in one session with an exit option.

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

### Command-Line Interface (CLI)

1. Open a terminal.
2. Navigate to the directory where `calculator.py` is located.
3. Run the calculator:
   ```bash
   python calculator.py
   ```
4. Follow the on-screen prompts to:
   - Select an operation by entering the corresponding number.
   - Input one or two numbers based on the operation.
   - View the result or continue with additional calculations.
5. To exit, select the exit option from the menu.

### Graphical User Interface (GUI)

1. Open a terminal.
2. Navigate to the directory where `calculator.py` is located.
3. Run the calculator:
   ```bash
   python calculator.py
   ```
4. In the GUI window:
   - Select an operation from the dropdown menu.
   - Enter the first number (and second number if applicable).
   - Click "Calculate" to see the result displayed.
   
## Example (CLI)

Here's an example session in the CLI:

```plaintext
Calculator
Select operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
6. Square Root
7. Exit
Enter choice (1/2/3/4/5/6/7): 1
Enter first number: 10
Enter second number: 5
Result: 15.0
```

## Code Structure

The project consists of a single Python file, `calculator.py`, which contains:

1. **Arithmetic Functions**: `add`, `subtract`, `multiply`, `divide`, `exponentiate`, and `square_root`, each performing a specific mathematical operation.
2. **Main Calculator Functions**:
   - **CLI Mode**: The `calculator()` function handles user input and operations via the command line.
   - **GUI Mode**: Uses `tkinter` to create a simple graphical interface.
3. **Execution Check**: Ensures the calculator runs when executed directly, not when imported as a module.

## Error Handling

- **Division by zero**: Displays an error message for division by zero.
- **Invalid input**: Shows a prompt for non-numeric input errors.
- **Square root of negative numbers**: Handles cases with an error message when attempting to find the square root of a negative number.

## Future Improvements

Possible additions include:
- More mathematical operations (e.g., logarithmic and trigonometric functions).
- Calculation history for each session.
- Additional customization options for the GUI.

## License
This project is open-source and available under the GPL-3.0 License.