import sys

# Check if two arguments are provided
if len(sys.argv) != 3:
    print("Usage: python bmi_calculator.py <weight_kg> <height_m>")
    sys.exit(1)

# Read command-line arguments
weight = float(sys.argv[1])
height = float(sys.argv[2])

# Calculate BMI
bmi = weight / (height * height)

# Display output
print("Weight (kg):", weight)
print("Height (m):", height)
print("Your BMI is:", round(bmi, 2))
