# BMI Calculator

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

# Function to classify BMI
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25.0 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Get user input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Classify BMI
bmi_category = classify_bmi(bmi)

# Display the BMI result and category
print(f"\nYour BMI is {bmi}, which falls under the category of {bmi_category}")
