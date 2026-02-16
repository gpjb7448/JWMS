"""
Exercise 2: Simple Calculator
Build a calculator with +, -, *, / operations
"""

def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract two numbers"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        return "Error: Division by zero!"
    return a / b


def main():
    print("=" * 50)
    print("Simple Calculator".center(50))
    print("=" * 50)
    
    print("\nOperations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "5":
            print("Thank you for using the calculator!")
            break
        
        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == "1":
                    result = add(num1, num2)
                    print(f"\n{num1} + {num2} = {result}")
                elif choice == "2":
                    result = subtract(num1, num2)
                    print(f"\n{num1} - {num2} = {result}")
                elif choice == "3":
                    result = multiply(num1, num2)
                    print(f"\n{num1} × {num2} = {result}")
                elif choice == "4":
                    result = divide(num1, num2)
                    print(f"\n{num1} ÷ {num2} = {result}")
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        else:
            print("Invalid choice! Please select 1-5.")


if __name__ == "__main__":
    main()
