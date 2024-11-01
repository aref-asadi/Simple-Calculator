# calculator

A basic calculator application in Python that performs fundamental arithmetic operations using a command-line interface (CLI).

## Features
- Performs basic arithmetic operations:
  - **Addition**
  - **Subtraction**
  - **Multiplication**
  - **Division** (with handling for division by zero)
- User-friendly command-line interface

## Requirements
- Python 3.x

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
4. Follow the on-screen prompts to:
   - Select an operation by entering the corresponding number.
   - Input two numbers for the operation.
5. The calculator will display the result of your chosen operation.

## Example

Here's an example session:

```plaintext
Calculator
Select operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter choice (1/2/3/4): 1
Enter first number: 10
Enter second number: 5
Result: 15.0
```

## Code Structure

The project consists of a single Python file `calculator.py`, which contains:

1. **Arithmetic Functions**: `add`, `subtract`, `multiply`, and `divide`, each performing a specific mathematical operation.
2. **Main Calculator Function**: The `calculator()` function serves as the main interface, prompting the user for an operation choice and inputs, then displaying the result.
3. **Execution Check**: Ensures that the calculator only runs when the script is executed directly, not when imported as a module.

## Error Handling

- Division by zero: If a user tries to divide by zero, the calculator will display an error message.
- Invalid input: If non-numeric input is entered, an error message will prompt the user to enter valid numbers.

## Future Improvements

Possible additions include:
- Additional operations (e.g., exponentiation, square root).
- Option to handle multiple calculations in one session.
- GUI implementation for a more visual experience.

## License
This project is open-source and available under the MIT License.