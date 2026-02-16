"""
Exercise 8: Password Validator
Check password strength (length, characters, etc.)
"""

import re


def check_length(password, min_length=8):
    """Check if password meets minimum length"""
    return len(password) >= min_length


def has_uppercase(password):
    """Check if password contains uppercase letters"""
    return any(char.isupper() for char in password)


def has_lowercase(password):
    """Check if password contains lowercase letters"""
    return any(char.islower() for char in password)


def has_digit(password):
    """Check if password contains digits"""
    return any(char.isdigit() for char in password)


def has_special_char(password):
    """Check if password contains special characters"""
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    return any(char in special_chars for char in password)


def validate_password(password):
    """
    Validate password strength
    
    Returns:
        tuple: (strength_score, feedback_list, is_strong)
    """
    feedback = []
    score = 0
    
    # Check length
    if check_length(password):
        score += 20
        feedback.append("✓ Length requirement met (8+ characters)")
    else:
        feedback.append("✗ Too short (minimum 8 characters required)")
    
    # Check uppercase
    if has_uppercase(password):
        score += 20
        feedback.append("✓ Contains uppercase letters")
    else:
        feedback.append("✗ Missing uppercase letters")
    
    # Check lowercase
    if has_lowercase(password):
        score += 20
        feedback.append("✓ Contains lowercase letters")
    else:
        feedback.append("✗ Missing lowercase letters")
    
    # Check digits
    if has_digit(password):
        score += 20
        feedback.append("✓ Contains numbers")
    else:
        feedback.append("✗ Missing numbers")
    
    # Check special characters
    if has_special_char(password):
        score += 20
        feedback.append("✓ Contains special characters")
    else:
        feedback.append("✗ Missing special characters")
    
    # Bonus for length
    if len(password) >= 12:
        score += 10
        feedback.append("✓ Bonus: Extra long password!")
    
    # Check for common patterns
    if password.lower() in ['password', '12345678', 'qwerty', 'abc123']:
        score = 0
        feedback.append("⚠️ WARNING: Common password detected!")
    
    is_strong = score >= 80
    
    return score, feedback, is_strong


def get_strength_label(score):
    """Get strength label based on score"""
    if score >= 80:
        return "STRONG 🟢", "green"
    elif score >= 60:
        return "MODERATE 🟡", "yellow"
    elif score >= 40:
        return "WEAK 🟠", "orange"
    else:
        return "VERY WEAK 🔴", "red"


def main():
    print("=" * 60)
    print("Password Strength Validator".center(60))
    print("=" * 60)
    
    print("\nPassword Requirements:")
    print("• Minimum 8 characters")
    print("• At least one uppercase letter")
    print("• At least one lowercase letter")
    print("• At least one number")
    print("• At least one special character (!@#$%^&*...)")
    print()
    
    while True:
        password = input("Enter password to validate (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("Goodbye!")
            break
        
        if not password:
            print("Password cannot be empty!\n")
            continue
        
        score, feedback, is_strong = validate_password(password)
        strength, color = get_strength_label(score)
        
        print("\n" + "=" * 60)
        print(f"Password Strength: {strength}")
        print(f"Score: {score}/100")
        print("=" * 60)
        
        print("\nDetailed Feedback:")
        for item in feedback:
            print(f"  {item}")
        
        print("\n" + "=" * 60)
        
        if is_strong:
            print("✅ This is a strong password!")
        else:
            print("⚠️ Consider making your password stronger.")
        
        print()


if __name__ == "__main__":
    main()
