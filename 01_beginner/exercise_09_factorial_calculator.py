"""
Exercise 9: Factorial Calculator
Calculate factorial using recursion and iteration
"""

def factorial_iterative(n):
    """
    Calculate factorial using iteration
    
    Args:
        n (int): Number to calculate factorial for
        
    Returns:
        int: Factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    """
    Calculate factorial using recursion
    
    Args:
        n (int): Number to calculate factorial for
        
    Returns:
        int: Factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def display_factorial_steps(n):
    """Display step-by-step factorial calculation"""
    print(f"\nCalculating {n}! step by step:")
    print("=" * 50)
    
    result = 1
    steps = []
    
    for i in range(1, n + 1):
        result *= i
        if i == 1:
            steps.append(f"{i}")
        else:
            steps.append(f"{i}")
    
    formula = " × ".join(steps)
    print(f"{n}! = {formula}")
    
    # Show intermediate results
    result = 1
    for i in range(1, n + 1):
        result *= i
        print(f"Step {i}: {' × '.join(steps[:i])} = {result}")
    
    print("=" * 50)


def factorial_range(start, end):
    """Calculate factorial for a range of numbers"""
    print(f"\nFactorials from {start} to {end}:")
    print("=" * 40)
    print(f"{'n':<5} {'n!':<20}")
    print("-" * 40)
    
    for n in range(start, end + 1):
        fact = factorial_iterative(n)
        print(f"{n:<5} {fact:<20,}")
    
    print("=" * 40)


def main():
    print("=" * 50)
    print("Factorial Calculator".center(50))
    print("=" * 50)
    
    print("\n1. Calculate factorial (iterative)")
    print("2. Calculate factorial (recursive)")
    print("3. Show step-by-step calculation")
    print("4. Factorial range")
    print("5. Exit")
    
    while True:
        choice = input("\nEnter your choice: ")
        
        if choice in ["1", "2", "3"]:
            try:
                n = int(input("Enter a number: "))
                
                if n < 0:
                    print("Factorial is not defined for negative numbers!")
                    continue
                
                if choice == "1":
                    result = factorial_iterative(n)
                    print(f"\n{n}! = {result:,} (calculated iteratively)")
                    
                elif choice == "2":
                    result = factorial_recursive(n)
                    print(f"\n{n}! = {result:,} (calculated recursively)")
                    
                elif choice == "3":
                    if n > 20:
                        print("Number too large for step-by-step display (max 20)")
                    else:
                        display_factorial_steps(n)
                        
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == "4":
            try:
                start = int(input("Start from: "))
                end = int(input("End at: "))
                
                if start < 0 or end < 0:
                    print("Please use non-negative numbers!")
                elif start > end:
                    print("Start must be less than or equal to end!")
                elif end - start > 20:
                    print("Range too large (max 20 numbers)")
                else:
                    factorial_range(start, end)
                    
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
