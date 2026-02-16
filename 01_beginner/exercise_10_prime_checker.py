"""
Exercise 10: Prime Number Checker
Determine if a number is prime
"""

import math


def is_prime(n):
    """
    Check if a number is prime
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def find_primes_in_range(start, end):
    """Find all prime numbers in a range"""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def get_prime_factors(n):
    """Get prime factors of a number"""
    factors = []
    
    # Check for 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check for odd factors
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    
    # If n is still greater than 1, it's a prime factor
    if n > 1:
        factors.append(n)
    
    return factors


def nth_prime(n):
    """Find the nth prime number"""
    count = 0
    num = 2
    
    while count < n:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1
    
    return None


def main():
    print("=" * 60)
    print("Prime Number Checker".center(60))
    print("=" * 60)
    
    print("\n1. Check if a number is prime")
    print("2. Find primes in a range")
    print("3. Get prime factors")
    print("4. Find nth prime number")
    print("5. First N primes")
    print("6. Exit")
    
    while True:
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            try:
                num = int(input("Enter a number: "))
                if is_prime(num):
                    print(f"\n✅ {num} is a PRIME number!")
                else:
                    print(f"\n❌ {num} is NOT a prime number.")
            except ValueError:
                print("Invalid input! Please enter a number.")
                
        elif choice == "2":
            try:
                start = int(input("Start from: "))
                end = int(input("End at: "))
                
                if start > end:
                    print("Start must be less than or equal to end!")
                    continue
                
                primes = find_primes_in_range(start, end)
                
                print(f"\nPrime numbers between {start} and {end}:")
                print("=" * 60)
                
                if primes:
                    # Display in rows of 10
                    for i in range(0, len(primes), 10):
                        row = primes[i:i+10]
                        print("  ".join(f"{p:5d}" for p in row))
                    print(f"\nTotal: {len(primes)} prime numbers")
                else:
                    print("No prime numbers found in this range.")
                    
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                
        elif choice == "3":
            try:
                num = int(input("Enter a number: "))
                
                if num < 2:
                    print("Prime factorization is only for numbers >= 2")
                    continue
                
                factors = get_prime_factors(num)
                
                print(f"\nPrime factorization of {num}:")
                print("=" * 60)
                print(f"{num} = {' × '.join(map(str, factors))}")
                
                # Count occurrences
                from collections import Counter
                factor_counts = Counter(factors)
                
                print("\nFactor breakdown:")
                for factor, count in sorted(factor_counts.items()):
                    if count == 1:
                        print(f"  {factor}")
                    else:
                        print(f"  {factor}^{count}")
                        
            except ValueError:
                print("Invalid input! Please enter a number.")
                
        elif choice == "4":
            try:
                n = int(input("Enter n (find nth prime): "))
                
                if n < 1:
                    print("n must be positive!")
                    continue
                
                if n > 10000:
                    print("n is too large (max 10000)")
                    continue
                
                prime = nth_prime(n)
                print(f"\nThe {n}th prime number is: {prime}")
                
            except ValueError:
                print("Invalid input! Please enter a number.")
                
        elif choice == "5":
            try:
                n = int(input("How many primes to find? "))
                
                if n < 1:
                    print("Please enter a positive number!")
                    continue
                
                if n > 100:
                    print("Too many primes requested (max 100)")
                    continue
                
                print(f"\nFirst {n} prime numbers:")
                print("=" * 60)
                
                primes = []
                for i in range(1, n + 1):
                    primes.append(nth_prime(i))
                
                # Display in rows of 10
                for i in range(0, len(primes), 10):
                    row = primes[i:i+10]
                    print("  ".join(f"{p:5d}" for p in row))
                    
            except ValueError:
                print("Invalid input! Please enter a number.")
                
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
