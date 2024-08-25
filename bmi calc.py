# Function to calculate BMI
def calculate_bmi(weight_lb, height_in):
    # Calculate BMI
    bmi = (weight_lb / (height_in ** 2)) * 703
    return bmi

# Input from the user
name = input("Hello Please input your name ")
weight_lb = float(input("Enter your weight in pounds: "))
height_in = float(input("Enter your height in inches: "))

# Calculate BMI
bmi = calculate_bmi(weight_lb, height_in)

# Determine BMI category
if bmi <= 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 24.9:
    category = "Average"
elif 25 <= bmi <= 29.90:
    category = "Overweight"
else:
    category = "Big and beautiful"

# Display the results
print("Hello",name)
print(f"Your BMI is: {bmi:.3f}")
print(f"You are categorized as: {category}")
