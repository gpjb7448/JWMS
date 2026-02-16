"""
Utility Functions - Helper functions for the application
"""

import os


def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(title):
    """Print formatted header"""
    width = 60
    print("=" * width)
    print(title.center(width))
    print("=" * width)


def format_currency(amount):
    """Format number as currency"""
    return f"${amount:,.2f}"


def get_valid_input(prompt, input_type=str, validator=None):
    """
    Get validated input from user
    
    Args:
        prompt: Input prompt
        input_type: Expected type (str, int, float)
        validator: Optional validation function
    
    Returns:
        Validated input
    """
    while True:
        try:
            value = input(prompt)
            converted = input_type(value)
            
            if validator and not validator(converted):
                print("Invalid input. Please try again.")
                continue
            
            return converted
        except ValueError:
            print(f"Please enter a valid {input_type.__name__}.")
