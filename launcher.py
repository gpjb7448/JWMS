"""
Python Learning Examples - Master Launcher
===========================================

Navigate and run all exercises and projects from one convenient interface.

This launcher provides:
- Quick access to all 15 beginner exercises
- Direct links to Phase 1 project
- Exercise descriptions and learning objectives
- Easy navigation through your learning journey
"""

import os
import sys
import subprocess

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Exercise catalog
EXERCISES = {
    "Beginner Level": [
        {
            "num": 1,
            "name": "Temperature Converter",
            "file": "01_beginner/exercise_01_temperature_converter.py",
            "concepts": "Functions, I/O, Math operations"
        },
        {
            "num": 2,
            "name": "Simple Calculator",
            "file": "01_beginner/exercise_02_simple_calculator.py",
            "concepts": "Functions, Loops, Error handling"
        },
        {
            "num": 3,
            "name": "User Greeting",
            "file": "01_beginner/exercise_03_user_greeting.py",
            "concepts": "String formatting, Conditionals"
        },
        {
            "num": 4,
            "name": "Even/Odd Checker",
            "file": "01_beginner/exercise_04_even_odd_checker.py",
            "concepts": "Modulo operator, List comprehensions"
        },
        {
            "num": 5,
            "name": "BMI Calculator",
            "file": "01_beginner/exercise_05_bmi_calculator.py",
            "concepts": "Math operations, Validation"
        },
        {
            "num": 6,
            "name": "Number Guessing Game",
            "file": "01_beginner/exercise_06_number_guessing_game.py",
            "concepts": "Random module, Game logic"
        },
        {
            "num": 7,
            "name": "Multiplication Table",
            "file": "01_beginner/exercise_07_multiplication_table.py",
            "concepts": "Loops, Range, Formatting"
        },
        {
            "num": 8,
            "name": "Password Validator",
            "file": "01_beginner/exercise_08_password_validator.py",
            "concepts": "String methods, Validation"
        },
        {
            "num": 9,
            "name": "Factorial Calculator",
            "file": "01_beginner/exercise_09_factorial_calculator.py",
            "concepts": "Recursion, Iteration"
        },
        {
            "num": 10,
            "name": "Prime Number Checker",
            "file": "01_beginner/exercise_10_prime_checker.py",
            "concepts": "Algorithms, Math logic"
        },
        {
            "num": 11,
            "name": "Shopping List Manager",
            "file": "01_beginner/exercise_11_shopping_list.py",
            "concepts": "Lists, CRUD operations"
        },
        {
            "num": 12,
            "name": "Student Grade Calculator",
            "file": "01_beginner/exercise_12_grade_calculator.py",
            "concepts": "Lists, Statistics"
        },
        {
            "num": 13,
            "name": "Random Lottery Generator",
            "file": "01_beginner/exercise_13_lottery_generator.py",
            "concepts": "Random module, No duplicates"
        },
        {
            "num": 14,
            "name": "Simple Todo List",
            "file": "01_beginner/exercise_14_todo_list.py",
            "concepts": "Data structures, Dictionaries"
        },
        {
            "num": 15,
            "name": "Math Quiz Game",
            "file": "01_beginner/exercise_15_math_quiz.py",
            "concepts": "Game logic, Score tracking"
        }
    ],
    "Projects": [
        {
            "num": 1,
            "name": "Personal Finance Tracker",
            "file": "04_projects/phase1_personal_finance_tracker/main.py",
            "concepts": "OOP, File I/O, CRUD, Reports"
        }
    ]
}


def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(title):
    """Print formatted header"""
    width = 80
    print("\n" + "=" * width)
    print(title.center(width))
    print("=" * width)


def display_main_menu():
    """Display the main menu"""
    clear_screen()
    print_header("🐍 PYTHON LEARNING EXAMPLES - MASTER LAUNCHER")
    
    print("\n📚 What would you like to do?")
    print("\n" + "-" * 80)
    print("1. 🌱 Browse Beginner Exercises (1-15)")
    print("2. 🎯 Launch Phase 1 Project (Personal Finance Tracker)")
    print("3. 📖 View Documentation (README)")
    print("4. 🗂️  View Master Index")
    print("5. 📂 Open Project Folder")
    print("6. 🚪 Exit")
    print("-" * 80)


def display_exercise_menu(category):
    """Display exercises in a category"""
    clear_screen()
    print_header(f"📚 {category.upper()}")
    
    exercises = EXERCISES[category]
    
    print(f"\n{'#':<4} {'Name':<30} {'Concepts':<40}")
    print("-" * 80)
    
    for ex in exercises:
        print(f"{ex['num']:<4} {ex['name']:<30} {ex['concepts']:<40}")
    
    print("-" * 80)
    print(f"Total: {len(exercises)} {'exercises' if category == 'Beginner Level' else 'projects'}")
    print("\nEnter exercise number to run, or 0 to go back")


def run_exercise(file_path):
    """Run a Python exercise"""
    full_path = os.path.join(BASE_DIR, file_path)
    
    if not os.path.exists(full_path):
        print(f"\n❌ Error: File not found: {file_path}")
        input("\nPress Enter to continue...")
        return
    
    print(f"\n{'=' * 80}")
    print(f"🚀 Launching: {os.path.basename(file_path)}")
    print(f"{'=' * 80}\n")
    
    try:
        # Run the exercise
        subprocess.run([sys.executable, full_path], cwd=os.path.dirname(full_path))
    except KeyboardInterrupt:
        print("\n\n⚠️ Program interrupted by user")
    except Exception as e:
        print(f"\n❌ Error running exercise: {e}")
    
    print(f"\n{'=' * 80}")
    input("\nPress Enter to continue...")


def view_file(file_path):
    """View a file in the default editor or browser"""
    full_path = os.path.join(BASE_DIR, file_path)
    
    if not os.path.exists(full_path):
        print(f"\n❌ Error: File not found: {file_path}")
        input("\nPress Enter to continue...")
        return
    
    try:
        if os.name == 'nt':  # Windows
            os.startfile(full_path)
        else:  # Mac/Linux
            subprocess.run(['open' if sys.platform == 'darwin' else 'xdg-open', full_path])
        print(f"\n✅ Opened: {file_path}")
    except Exception as e:
        print(f"\n❌ Error opening file: {e}")
    
    input("\nPress Enter to continue...")


def open_project_folder():
    """Open the project folder in file explorer"""
    try:
        if os.name == 'nt':  # Windows
            os.startfile(BASE_DIR)
        else:  # Mac/Linux
            subprocess.run(['open' if sys.platform == 'darwin' else 'xdg-open', BASE_DIR])
        print(f"\n✅ Opened project folder in file explorer")
    except Exception as e:
        print(f"\n❌ Error opening folder: {e}")
    
    input("\nPress Enter to continue...")


def browse_exercises(category):
    """Browse and run exercises in a category"""
    while True:
        display_exercise_menu(category)
        
        choice = input("\nYour choice: ").strip()
        
        if choice == '0':
            break
        
        try:
            num = int(choice)
            exercises = EXERCISES[category]
            
            # Find exercise by number
            exercise = next((ex for ex in exercises if ex['num'] == num), None)
            
            if exercise:
                run_exercise(exercise['file'])
            else:
                print(f"\n❌ Exercise {num} not found!")
                input("\nPress Enter to continue...")
        except ValueError:
            print("\n❌ Invalid input! Please enter a number.")
            input("\nPress Enter to continue...")


def main():
    """Main launcher loop"""
    while True:
        display_main_menu()
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            browse_exercises("Beginner Level")
        elif choice == '2':
            browse_exercises("Projects")
        elif choice == '3':
            view_file("README.md")
        elif choice == '4':
            view_file("MASTER_INDEX.md")
        elif choice == '5':
            open_project_folder()
        elif choice == '6':
            clear_screen()
            print("\n" + "=" * 80)
            print("👋 Thank you for learning Python!".center(80))
            print("Keep coding and keep learning! 🐍✨".center(80))
            print("=" * 80 + "\n")
            sys.exit(0)
        else:
            print("\n❌ Invalid choice! Please select 1-6.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    """
    MASTER LAUNCHER
    
    Run this file to access all exercises and projects from one place.
    
    Usage:
        python launcher.py
    """
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print("\n\n👋 Goodbye! Keep learning! 🐍✨\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please report this issue.")
        input("\nPress Enter to exit...")
        sys.exit(1)
