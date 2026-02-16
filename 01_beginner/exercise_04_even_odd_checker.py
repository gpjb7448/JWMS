"""
Exercise 4: Even/Odd Checker
Check if a number is even or odd
"""

def is_even(number):
    """
    Check if a number is even
    
    Args:
        number (int): Number to check
        
    Returns:
        bool: True if even, False if odd
    """
    return number % 2 == 0


def check_multiple_numbers():
    """Check multiple numbers for even/odd"""
    numbers = input("Enter numbers separated by spaces: ")
    number_list = [int(num) for num in numbers.split()]
    
    print("\nResults:")
    print("-" * 30)
    for num in number_list:
        status = "EVEN" if is_even(num) else "ODD"
        print(f"{num:5d} -> {status}")


def main():
    print("=" * 50)
    print("Even/Odd Checker".center(50))
    print("=" * 50)
    
    print("\n1. Check single number")
    print("2. Check multiple numbers")
    print("3. Exit")
    
    while True:
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            try:
                number = int(input("Enter a number: "))
                if is_even(number):
                    print(f"\n{number} is EVEN ✓")
                else:
                    print(f"\n{number} is ODD ✗")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                
        elif choice == "2":
            try:
                check_multiple_numbers()
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
                
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
