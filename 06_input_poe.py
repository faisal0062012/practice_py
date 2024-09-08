# BMI formula
def calculate_bmi(weight, height):
    """
    Calculates the body mass index (BMI) given the weight and height.
    
    Args:
        weight (float): The weight in kilograms (kg).
        height (float): The height in meters (m).
    
    Returns:
        float: The calculated BMI.
    """
    bmi = weight / (height ** 2)
    return bmi

# Example usage
weight = 70  # kg
height = 1.75  # m
bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")