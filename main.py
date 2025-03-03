import re

print('Welcome to the Command-Line Calculator!')

while True:
    UserInput = input('Enter a mathematical expression (or type "exit" to quit): ').strip()

    if UserInput.lower() == 'exit':
        print("Thank you for using the calculator! ")
        break

    if not re.match(r'^[0-9+\-*/().\s]+$', UserInput):
        print("Error: Please enter a valid mathematical expression (only numbers and + - * / ( ) . allowed).")
        continue

    try:
        result = eval(UserInput, {"__builtins__": None}, {})
        print(f"Result: {result:.2f}")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except Exception as e:
        print(f"Error: {e}")
