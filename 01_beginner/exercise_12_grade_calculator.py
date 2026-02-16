"""
Exercise 12: Student Grade Calculator
Calculate average from list of grades

STEP-BY-STEP GUIDE:
===================
1. Store student grades in a list
2. Calculate the sum of all grades
3. Divide by the number of grades to get average
4. Determine letter grade based on average
5. Display results with statistics
"""

def calculate_average(grades):
    """
    Calculate the average of grades
    
    STEP 1: Sum all grades
    STEP 2: Divide by count of grades
    
    Args:
        grades (list): List of numerical grades
        
    Returns:
        float: Average grade
    """
    if not grades:
        return 0
    return sum(grades) / len(grades)


def get_letter_grade(average):
    """
    Convert numerical average to letter grade
    
    GRADING SCALE:
    - A: 90-100
    - B: 80-89
    - C: 70-79
    - D: 60-69
    - F: Below 60
    
    Args:
        average (float): Numerical average
        
    Returns:
        str: Letter grade
    """
    if average >= 90:
        return 'A', '🌟'
    elif average >= 80:
        return 'B', '😊'
    elif average >= 70:
        return 'C', '😐'
    elif average >= 60:
        return 'D', '😕'
    else:
        return 'F', '😢'


def get_statistics(grades):
    """
    Calculate grade statistics
    
    Returns:
        dict: Dictionary containing statistical measures
    """
    return {
        'highest': max(grades),
        'lowest': min(grades),
        'average': calculate_average(grades),
        'total': len(grades)
    }


def display_grade_report(student_name, grades):
    """
    Display comprehensive grade report
    
    STEP 1: Calculate statistics
    STEP 2: Determine letter grade
    STEP 3: Format and display report
    """
    print("\n" + "=" * 60)
    print(f"Grade Report for {student_name}".center(60))
    print("=" * 60)
    
    # Display all grades
    print("\nIndividual Grades:")
    print("-" * 60)
    for idx, grade in enumerate(grades, 1):
        print(f"Assignment {idx:2d}: {grade:5.1f}")
    
    # Calculate and display statistics
    stats = get_statistics(grades)
    average = stats['average']
    letter, emoji = get_letter_grade(average)
    
    print("\n" + "=" * 60)
    print("Summary Statistics:")
    print("-" * 60)
    print(f"Total Assignments: {stats['total']}")
    print(f"Highest Grade    : {stats['highest']:.1f}")
    print(f"Lowest Grade     : {stats['lowest']:.1f}")
    print(f"Average Grade    : {average:.2f}")
    print(f"Letter Grade     : {letter} {emoji}")
    print("=" * 60)


def main():
    """
    MAIN PROGRAM FLOW:
    ==================
    1. Get student name
    2. Collect grades from user
    3. Calculate statistics
    4. Display grade report
    5. Offer to calculate for another student
    """
    print("=" * 60)
    print("Student Grade Calculator".center(60))
    print("=" * 60)
    
    while True:
        # STEP 1: Get student information
        student_name = input("\nEnter student name (or 'quit' to exit): ").strip()
        
        if student_name.lower() == 'quit':
            print("Goodbye!")
            break
        
        if not student_name:
            print("Name cannot be empty!")
            continue
        
        # STEP 2: Collect grades
        grades = []
        print(f"\nEnter grades for {student_name}")
        print("(Enter 'done' when finished)")
        
        assignment_num = 1
        while True:
            grade_input = input(f"Assignment {assignment_num}: ").strip()
            
            if grade_input.lower() == 'done':
                if not grades:
                    print("Please enter at least one grade!")
                    continue
                break
            
            try:
                # STEP 3: Validate grade input
                grade = float(grade_input)
                
                if grade < 0 or grade > 100:
                    print("Grade must be between 0 and 100!")
                    continue
                
                grades.append(grade)
                assignment_num += 1
                
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        # STEP 4: Display comprehensive report
        display_grade_report(student_name, grades)
        
        # STEP 5: Ask to continue
        print()


if __name__ == "__main__":
    """
    PROGRAM ENTRY POINT
    
    When this script is run directly (not imported),
    the main() function is executed.
    """
    main()
