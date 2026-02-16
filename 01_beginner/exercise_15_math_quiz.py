"""
Exercise 15: Math Quiz Game
Generate random math problems using math module

STEP-BY-STEP GUIDE:
===================
1. Import random and math modules
2. Generate random math problems
3. Get user's answer
4. Check if answer is correct
5. Keep score and display results
6. Offer different difficulty levels

LEARNING OBJECTIVES:
- Using random module for problem generation
- User input validation
- Score tracking
- Conditional logic
- String formatting
"""

import random
import math


def generate_problem(difficulty):
    """
    Generate a random math problem based on difficulty
    
    STEP 1: Choose operation based on difficulty
    STEP 2: Generate random numbers
    STEP 3: Calculate correct answer
    STEP 4: Return problem string and answer
    
    Args:
        difficulty (str): 'easy', 'medium', or 'hard'
        
    Returns:
        tuple: (problem_string, correct_answer)
    """
    if difficulty == 'easy':
        # EASY: Addition and subtraction with numbers 1-20
        operation = random.choice(['+', '-'])
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        
        # Ensure positive result for subtraction
        if operation == '-' and num1 < num2:
            num1, num2 = num2, num1
        
        problem = f"{num1} {operation} {num2}"
        answer = eval(problem)
        
    elif difficulty == 'medium':
        # MEDIUM: All basic operations with numbers 1-50
        operation = random.choice(['+', '-', '*', '/'])
        
        if operation == '/':
            # Generate division that results in whole number
            num2 = random.randint(1, 12)
            answer = random.randint(1, 12)
            num1 = num2 * answer
        else:
            num1 = random.randint(1, 50)
            num2 = random.randint(1, 50)
            
            if operation == '-' and num1 < num2:
                num1, num2 = num2, num1
        
        problem = f"{num1} {operation} {num2}"
        if operation != '/':
            answer = eval(problem)
        
    else:  # hard
        # HARD: Complex operations, including powers and roots
        problem_type = random.choice(['power', 'sqrt', 'multi_op'])
        
        if problem_type == 'power':
            base = random.randint(2, 10)
            exponent = random.randint(2, 3)
            problem = f"{base}^{exponent}"
            answer = base ** exponent
            
        elif problem_type == 'sqrt':
            # Perfect square root
            num = random.randint(1, 12)
            square = num * num
            problem = f"√{square}"
            answer = num
            
        else:  # multi_op
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 10)
            num3 = random.randint(1, 10)
            operation1 = random.choice(['+', '-', '*'])
            operation2 = random.choice(['+', '-'])
            
            if operation1 == '*':
                problem = f"({num1} {operation2} {num2}) {operation1} {num3}"
            else:
                problem = f"{num1} {operation1} {num2} {operation2} {num3}"
            
            answer = eval(problem.replace('^', '**').replace('√', 'math.sqrt'))
    
    return problem, int(answer) if isinstance(answer, float) and answer.is_integer() else answer


def play_quiz(difficulty, num_questions):
    """
    Play a math quiz
    
    STEP 1: Initialize score
    STEP 2: Loop through questions
    STEP 3: Generate problem
    STEP 4: Get and validate user answer
    STEP 5: Check answer and update score
    STEP 6: Display results
    
    Args:
        difficulty (str): Difficulty level
        num_questions (int): Number of questions
        
    Returns:
        tuple: (score, total_questions)
    """
    score = 0
    questions_asked = []
    
    print("\n" + "=" * 60)
    print(f"MATH QUIZ - {difficulty.upper()} LEVEL".center(60))
    print("=" * 60)
    print(f"\nYou will answer {num_questions} questions. Good luck!\n")
    
    # STEP: Loop through questions
    for question_num in range(1, num_questions + 1):
        # STEP: Generate problem
        problem, correct_answer = generate_problem(difficulty)
        
        print(f"\nQuestion {question_num}/{num_questions}:")
        print(f"  {problem} = ?")
        
        # STEP: Get user answer with validation
        try:
            user_answer = input("  Your answer: ").strip()
            
            # Allow user to skip
            if user_answer.lower() == 'skip':
                print(f"  ⏭️  Skipped! (Correct answer: {correct_answer})")
                questions_asked.append({
                    'problem': problem,
                    'correct': correct_answer,
                    'user': 'skipped',
                    'is_correct': False
                })
                continue
            
            user_answer = float(user_answer)
            
            # STEP: Check answer (allow small floating point differences)
            if abs(user_answer - correct_answer) < 0.01:
                print(f"  ✅ Correct!")
                score += 1
                is_correct = True
            else:
                print(f"  ❌ Wrong! Correct answer: {correct_answer}")
                is_correct = False
            
            # STEP: Record question
            questions_asked.append({
                'problem': problem,
                'correct': correct_answer,
                'user': user_answer,
                'is_correct': is_correct
            })
            
        except ValueError:
            print(f"  ❌ Invalid input! Correct answer: {correct_answer}")
            questions_asked.append({
                'problem': problem,
                'correct': correct_answer,
                'user': 'invalid',
                'is_correct': False
            })
    
    # STEP: Display final results
    display_results(score, num_questions, questions_asked, difficulty)
    
    return score, num_questions


def display_results(score, total, questions, difficulty):
    """
    Display quiz results
    
    STEP 1: Calculate percentage
    STEP 2: Determine grade
    STEP 3: Display summary
    STEP 4: Show question review
    """
    print("\n" + "=" * 60)
    print("QUIZ RESULTS".center(60))
    print("=" * 60)
    
    # STEP 1: Calculate statistics
    percentage = (score / total) * 100
    
    # STEP 2: Determine grade and message
    if percentage >= 90:
        grade = "A"
        message = "Outstanding! 🌟"
        emoji = "🏆"
    elif percentage >= 80:
        grade = "B"
        message = "Great job! 😊"
        emoji = "🎉"
    elif percentage >= 70:
        grade = "C"
        message = "Good effort! 👍"
        emoji = "😊"
    elif percentage >= 60:
        grade = "D"
        message = "Keep practicing! 📚"
        emoji = "😐"
    else:
        grade = "F"
        message = "Don't give up! 💪"
        emoji = "😕"
    
    # STEP 3: Display summary
    print(f"\nDifficulty: {difficulty.upper()}")
    print(f"Score: {score}/{total} ({percentage:.1f}%)")
    print(f"Grade: {grade} {emoji}")
    print(f"Message: {message}")
    
    # STEP 4: Show question review
    print("\n" + "=" * 60)
    print("Question Review:")
    print("-" * 60)
    
    for idx, q in enumerate(questions, 1):
        status = "✅" if q['is_correct'] else "❌"
        user_ans = q['user'] if isinstance(q['user'], str) else f"{q['user']:.2f}"
        print(f"{idx}. {q['problem']} = {q['correct']}")
        print(f"   {status} Your answer: {user_ans}")
        print()
    
    print("=" * 60)


def get_difficulty():
    """
    Get difficulty level from user
    
    STEP 1: Display difficulty options
    STEP 2: Get user choice
    STEP 3: Validate and return
    """
    print("\n" + "=" * 60)
    print("Select Difficulty Level:")
    print("-" * 60)
    print("1. Easy   - Addition, Subtraction (1-20)")
    print("2. Medium - All operations (1-50)")
    print("3. Hard   - Powers, roots, complex operations")
    print("=" * 60)
    
    while True:
        choice = input("\nEnter choice (1-3): ")
        
        difficulty_map = {
            '1': 'easy',
            '2': 'medium',
            '3': 'hard'
        }
        
        if choice in difficulty_map:
            return difficulty_map[choice]
        else:
            print("Invalid choice! Please select 1-3.")


def main():
    """
    MAIN PROGRAM FLOW:
    ==================
    1. Display welcome message
    2. Get difficulty level
    3. Get number of questions
    4. Start quiz
    5. Display results
    6. Ask to play again
    
    PROGRAM FEATURES:
    - Multiple difficulty levels
    - Score tracking
    - Question review
    - Replay option
    """
    print("=" * 60)
    print("MATH QUIZ GAME".center(60))
    print("=" * 60)
    print("\nTest your math skills with randomly generated problems!")
    print("Type 'skip' to skip a question.")
    
    # Statistics tracking
    total_score = 0
    total_questions = 0
    games_played = 0
    
    while True:
        # STEP 1: Get difficulty
        difficulty = get_difficulty()
        
        # STEP 2: Get number of questions
        while True:
            try:
                num_q = int(input("\nHow many questions? (1-50): "))
                if 1 <= num_q <= 50:
                    break
                else:
                    print("Please enter a number between 1 and 50.")
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        # STEP 3: Play quiz
        score, total = play_quiz(difficulty, num_q)
        
        # STEP 4: Update statistics
        total_score += score
        total_questions += total
        games_played += 1
        
        # STEP 5: Display overall statistics
        print("\n" + "=" * 60)
        print("Overall Statistics:")
        print("-" * 60)
        print(f"Games Played: {games_played}")
        print(f"Total Score: {total_score}/{total_questions}")
        print(f"Overall Percentage: {(total_score/total_questions*100):.1f}%")
        print("=" * 60)
        
        # STEP 6: Play again?
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("\n🎓 Thanks for playing! Keep practicing your math skills!")
            break


if __name__ == "__main__":
    """
    PROGRAM ENTRY POINT
    
    EXECUTION FLOW:
    1. Check if script is run directly (__name__ == "__main__")
    2. If yes, execute main() function
    3. If imported, don't auto-execute (allows module reuse)
    
    WHY THIS MATTERS:
    - Allows code reuse through imports
    - Separates module definition from execution
    - Python best practice
    """
    main()
