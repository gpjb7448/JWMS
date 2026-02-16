"""
Exercise 1: Temperature Converter
Create a program that converts Celsius to Fahrenheit
Formula: F = (C × 9/5) + 32
"""

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit
    
    Args:
        celsius (float): Temperature in Celsius
        
    Returns:
        float: Temperature in Fahrenheit
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
        
    Returns:
        float: Temperature in Celsius
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def main():
    print("=" * 50)
    print("Temperature Converter".center(50))
    print("=" * 50)
    
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("\nEnter your choice (1 or 2): ")
    
    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"\n{celsius}°C = {fahrenheit:.2f}°F")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"\n{fahrenheit}°F = {celsius:.2f}°C")
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
