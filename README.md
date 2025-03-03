#Calculator

## Description
This is a simple command-line calculator built using Python. It allows users to enter mathematical expressions and evaluates them safely.

## Features
- Supports basic arithmetic operations: `+`, `-`, `*`, `/`, `()`, and `.` (for decimals).
- Provides error handling for invalid inputs and division by zero.
- Ensures safe evaluation by restricting `eval()` usage.

## Usage
1. Run the script using Python:
   ```sh
   python main.py
   ```
2. Enter a mathematical expression when prompted.
3. Type `exit` to quit the calculator.

## Example
```
Welcome to the Command-Line Calculator!
Enter a mathematical expression (or type "exit" to quit): 5 + 3 * 2
Result: 11.00

Enter a mathematical expression (or type "exit" to quit): 10 / 0
Error: Cannot divide by zero!

Enter a mathematical expression (or type "exit" to quit): exit
Thank you for using the calculator!
```

## Requirements
- Python 3.x

## Notes
- The program uses regex validation to ensure only valid mathematical expressions are processed.
- The `eval()` function is used with restrictions for safety.

