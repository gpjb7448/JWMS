"""
Exercise 6: Number Guessing Game
Random number game with limited attempts
"""

import random


def play_game():
    """Play the number guessing game"""
    # Generate random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("I'm thinking of a number between 1 and 100...")
    print(f"You have {max_attempts} attempts to guess it!\n")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100!")
                attempts -= 1
                continue
            
            if guess == secret_number:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
                return True
            elif guess < secret_number:
                print("Too low! Try a higher number. ⬆️")
            else:
                print("Too high! Try a lower number. ⬇️")
                
            # Give hints
            if attempts == max_attempts - 2:
                print(f"💡 Hint: The number is {'even' if secret_number % 2 == 0 else 'odd'}")
                
        except ValueError:
            print("Invalid input! Please enter a number.")
            attempts -= 1
    
    print(f"\n❌ Game Over! The number was {secret_number}")
    return False


def main():
    print("=" * 50)
    print("Number Guessing Game".center(50))
    print("=" * 50)
    print()
    
    wins = 0
    games = 0
    
    while True:
        if play_game():
            wins += 1
        games += 1
        
        print(f"\nScore: {wins}/{games} wins")
        
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print(f"\nFinal Score: {wins}/{games} wins")
            print("Thanks for playing! 👋")
            break
        print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()
