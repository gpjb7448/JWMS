"""
Exercise 13: Random Number Generator
Use random module to create lottery numbers

STEP-BY-STEP GUIDE:
===================
1. Import the random module
2. Generate random numbers within a range
3. Ensure no duplicate numbers
4. Display results in a formatted way
5. Offer different lottery game types
"""

import random


def generate_lottery_numbers(count, min_num, max_num, allow_duplicates=False):
    """
    Generate lottery numbers
    
    STEP 1: Create empty list for numbers
    STEP 2: Generate random numbers
    STEP 3: Check for duplicates if needed
    STEP 4: Return the list
    
    Args:
        count (int): How many numbers to generate
        min_num (int): Minimum number (inclusive)
        max_num (int): Maximum number (inclusive)
        allow_duplicates (bool): Allow duplicate numbers
        
    Returns:
        list: List of lottery numbers
    """
    if allow_duplicates:
        # STEP: Generate with possible duplicates
        return [random.randint(min_num, max_num) for _ in range(count)]
    else:
        # STEP: Generate unique numbers using random.sample
        if count > (max_num - min_num + 1):
            raise ValueError("Cannot generate more unique numbers than available range!")
        return sorted(random.sample(range(min_num, max_num + 1), count))


def powerball():
    """
    Powerball lottery: 5 numbers (1-69) + 1 powerball (1-26)
    
    STEP 1: Generate 5 main numbers
    STEP 2: Generate 1 powerball number
    STEP 3: Display formatted results
    """
    print("\n" + "=" * 60)
    print("POWERBALL LOTTERY NUMBERS".center(60))
    print("=" * 60)
    
    # STEP 1: Generate main numbers (no duplicates)
    main_numbers = generate_lottery_numbers(5, 1, 69, allow_duplicates=False)
    
    # STEP 2: Generate powerball (separate from main numbers)
    powerball = random.randint(1, 26)
    
    # STEP 3: Display results
    print("\nMain Numbers: ", end="")
    print(" - ".join(f"{num:02d}" for num in main_numbers))
    print(f"Powerball   : {powerball:02d} 🔴")
    print("=" * 60)


def mega_millions():
    """
    Mega Millions: 5 numbers (1-70) + 1 mega ball (1-25)
    
    STEP 1: Generate 5 main numbers
    STEP 2: Generate 1 mega ball
    STEP 3: Display formatted results
    """
    print("\n" + "=" * 60)
    print("MEGA MILLIONS LOTTERY NUMBERS".center(60))
    print("=" * 60)
    
    main_numbers = generate_lottery_numbers(5, 1, 70, allow_duplicates=False)
    mega_ball = random.randint(1, 25)
    
    print("\nMain Numbers: ", end="")
    print(" - ".join(f"{num:02d}" for num in main_numbers))
    print(f"Mega Ball   : {mega_ball:02d} 🟡")
    print("=" * 60)


def lotto_649():
    """
    Lotto 6/49: 6 numbers from 1-49
    
    STEP 1: Generate 6 unique numbers
    STEP 2: Sort them for easy reading
    STEP 3: Display formatted results
    """
    print("\n" + "=" * 60)
    print("LOTTO 6/49 NUMBERS".center(60))
    print("=" * 60)
    
    numbers = generate_lottery_numbers(6, 1, 49, allow_duplicates=False)
    
    print("\nYour Numbers: ", end="")
    print(" - ".join(f"{num:02d}" for num in numbers))
    print("=" * 60)


def custom_lottery():
    """
    Custom lottery: User defines parameters
    
    STEP 1: Get user input for parameters
    STEP 2: Validate inputs
    STEP 3: Generate numbers
    STEP 4: Display results
    """
    print("\n" + "=" * 60)
    print("CUSTOM LOTTERY".center(60))
    print("=" * 60)
    
    try:
        # STEP 1: Get parameters from user
        count = int(input("\nHow many numbers to generate? "))
        min_num = int(input("Minimum number: "))
        max_num = int(input("Maximum number: "))
        
        # STEP 2: Validate inputs
        if count <= 0:
            print("Count must be positive!")
            return
        
        if min_num >= max_num:
            print("Minimum must be less than maximum!")
            return
        
        allow_dup = input("Allow duplicates? (y/n): ").lower() == 'y'
        
        # STEP 3: Generate numbers
        numbers = generate_lottery_numbers(count, min_num, max_num, allow_dup)
        
        # STEP 4: Display results
        print("\n" + "=" * 60)
        print(f"Your {count} numbers ({min_num}-{max_num}):")
        print(" - ".join(f"{num:02d}" for num in numbers))
        print("=" * 60)
        
    except ValueError as e:
        print(f"Error: {e}")


def generate_multiple_tickets(game_type, num_tickets):
    """
    Generate multiple lottery tickets
    
    STEP 1: Loop for specified number of tickets
    STEP 2: Generate each ticket
    STEP 3: Display all tickets
    """
    print(f"\n{'=' * 60}")
    print(f"Generating {num_tickets} tickets...".center(60))
    print('=' * 60)
    
    for i in range(num_tickets):
        print(f"\nTicket #{i + 1}:")
        if game_type == '1':
            main = generate_lottery_numbers(5, 1, 69, False)
            pb = random.randint(1, 26)
            print(f"  Main: {' - '.join(f'{n:02d}' for n in main)}")
            print(f"  PB: {pb:02d}")
        elif game_type == '2':
            main = generate_lottery_numbers(5, 1, 70, False)
            mb = random.randint(1, 25)
            print(f"  Main: {' - '.join(f'{n:02d}' for n in main)}")
            print(f"  MB: {mb:02d}")
        elif game_type == '3':
            numbers = generate_lottery_numbers(6, 1, 49, False)
            print(f"  Numbers: {' - '.join(f'{n:02d}' for n in numbers)}")


def main():
    """
    MAIN PROGRAM FLOW:
    ==================
    1. Display menu of lottery types
    2. Get user choice
    3. Generate lottery numbers based on choice
    4. Display results
    5. Repeat or exit
    """
    print("=" * 60)
    print("Random Lottery Number Generator".center(60))
    print("=" * 60)
    
    while True:
        print("\nSelect Lottery Type:")
        print("1. Powerball (5 numbers 1-69 + Powerball 1-26)")
        print("2. Mega Millions (5 numbers 1-70 + Mega Ball 1-25)")
        print("3. Lotto 6/49 (6 numbers 1-49)")
        print("4. Custom Lottery")
        print("5. Generate Multiple Tickets")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            powerball()
        elif choice == "2":
            mega_millions()
        elif choice == "3":
            lotto_649()
        elif choice == "4":
            custom_lottery()
        elif choice == "5":
            print("\n1. Powerball")
            print("2. Mega Millions")
            print("3. Lotto 6/49")
            game = input("Select game: ")
            
            try:
                num = int(input("How many tickets? "))
                if num > 0:
                    generate_multiple_tickets(game, num)
                else:
                    print("Number must be positive!")
            except ValueError:
                print("Invalid input!")
        elif choice == "6":
            print("\n🍀 Good luck! Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    """
    PROGRAM ENTRY POINT
    
    WHAT HAPPENS:
    1. Python checks if this file is being run directly
    2. If yes (__name__ == "__main__"), execute main()
    3. If imported as module, main() is not auto-executed
    """
    main()
