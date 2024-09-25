# Validate_input.py

def yes_no_check(prompt):
    """Validates yes/no input from the user."""
    while True:
        response = input(prompt).lower()
        if response == "yes" or response == "no":
            return response
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
