"""
Exercise 7: Multiplication Table
Generate multiplication table for any number
"""

def generate_table(number, up_to=10):
    """
    Generate multiplication table
    
    Args:
        number (int): Number for which to generate table
        up_to (int): Generate table up to this value
        
    Returns:
        list: List of tuples (multiplier, result)
    """
    table = []
    for i in range(1, up_to + 1):
        table.append((i, number * i))
    return table


def display_table(number, table):
    """Display multiplication table in formatted way"""
    print(f"\n{'=' * 40}")
    print(f"Multiplication Table of {number}".center(40))
    print('=' * 40)
    
    for multiplier, result in table:
        print(f"{number:3d} × {multiplier:2d} = {result:4d}")
    
    print('=' * 40)


def generate_range_tables(start, end):
    """Generate tables for a range of numbers"""
    for num in range(start, end + 1):
        table = generate_table(num, 10)
        display_table(num, table)
        print()


def main():
    print("=" * 50)
    print("Multiplication Table Generator".center(50))
    print("=" * 50)
    
    print("\n1. Generate table for a single number")
    print("2. Generate tables for a range")
    print("3. Custom table (choose range)")
    print("4. Exit")
    
    while True:
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            try:
                number = int(input("Enter a number: "))
                up_to = int(input("Generate up to (default 10): ") or "10")
                table = generate_table(number, up_to)
                display_table(number, table)
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                
        elif choice == "2":
            try:
                start = int(input("Start from: "))
                end = int(input("End at: "))
                generate_range_tables(start, end)
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                
        elif choice == "3":
            try:
                number = int(input("Enter number: "))
                start = int(input("Start multiplier from: "))
                end = int(input("End multiplier at: "))
                
                print(f"\n{'=' * 40}")
                print(f"Table of {number} ({start} to {end})".center(40))
                print('=' * 40)
                
                for i in range(start, end + 1):
                    print(f"{number:3d} × {i:2d} = {number * i:4d}")
                print('=' * 40)
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
