"""
Exercise 5: BMI Calculator
Calculate Body Mass Index from height and weight
Formula: BMI = weight(kg) / (height(m) × height(m))
"""

def calculate_bmi(weight, height):
    """
    Calculate BMI
    
    Args:
        weight (float): Weight in kg
        height (float): Height in meters
        
    Returns:
        float: BMI value
    """
    bmi = weight / (height ** 2)
    return bmi


def get_bmi_category(bmi):
    """
    Get BMI category
    
    Args:
        bmi (float): BMI value
        
    Returns:
        str: BMI category
    """
    if bmi < 18.5:
        return "Underweight", "🔵"
    elif 18.5 <= bmi < 25:
        return "Normal weight", "🟢"
    elif 25 <= bmi < 30:
        return "Overweight", "🟡"
    else:
        return "Obese", "🔴"


def main():
    print("=" * 50)
    print("BMI Calculator".center(50))
    print("=" * 50)
    
    try:
        print("\nEnter your details:")
        weight = float(input("Weight (kg): "))
        height = float(input("Height (meters): "))
        
        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive!")
            return
        
        bmi = calculate_bmi(weight, height)
        category, emoji = get_bmi_category(bmi)
        
        print("\n" + "=" * 50)
        print(f"Your BMI: {bmi:.2f}")
        print(f"Category: {category} {emoji}")
        print("=" * 50)
        
        # Display BMI chart
        print("\nBMI Categories:")
        print("-" * 50)
        print("Underweight  : BMI < 18.5")
        print("Normal       : 18.5 ≤ BMI < 25")
        print("Overweight   : 25 ≤ BMI < 30")
        print("Obese        : BMI ≥ 30")
        
        # Health recommendation
        print("\n💡 Health Tip:")
        if bmi < 18.5:
            print("Consider consulting a nutritionist for a healthy weight gain plan.")
        elif 18.5 <= bmi < 25:
            print("Great! Maintain your healthy lifestyle!")
        elif 25 <= bmi < 30:
            print("Consider regular exercise and a balanced diet.")
        else:
            print("Consult a healthcare professional for guidance.")
            
    except ValueError:
        print("Error: Please enter valid numbers!")


if __name__ == "__main__":
    main()
