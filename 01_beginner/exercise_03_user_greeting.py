"""
Exercise 3: User Greeting
Take user's name and age, display personalized message
"""

def get_user_info():
    """Get user information"""
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    return name, age


def generate_greeting(name, age):
    """Generate personalized greeting"""
    current_year = 2026
    birth_year = current_year - age
    
    greeting = f"\nHello, {name}! 👋\n"
    greeting += f"You are {age} years old.\n"
    greeting += f"You were born around {birth_year}.\n"
    
    # Age-based messages
    if age < 13:
        greeting += "You're a kid! Enjoy your childhood! 🎈"
    elif age < 20:
        greeting += "You're a teenager! Exciting times ahead! 🎓"
    elif age < 30:
        greeting += "You're in your twenties! Make the most of it! 🚀"
    elif age < 60:
        greeting += "You're an adult! Hope you're living your best life! ✨"
    else:
        greeting += "You're a senior! Wisdom comes with age! 🌟"
    
    return greeting


def main():
    print("=" * 50)
    print("User Greeting System".center(50))
    print("=" * 50)
    
    try:
        name, age = get_user_info()
        greeting = generate_greeting(name, age)
        print(greeting)
        
        # Additional info
        print(f"\nFun fact: In 10 years, you'll be {age + 10} years old!")
        
    except ValueError:
        print("Error: Please enter a valid age (number)!")


if __name__ == "__main__":
    main()
