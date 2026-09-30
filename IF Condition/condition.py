# ShadowFox Python Development Internship
# Beginner Assignment: Conditional Decision Making

# ==========================================
# Task 1: Health Metrics (BMI Evaluator)
# ==========================================
print("--- Part 1: Body Mass Index (BMI) Assessment ---")

try:
    # Gathering user measurements
    user_weight = float(input("Enter weight in kilograms (kg): "))
    user_height = float(input("Enter height in meters (m): "))

    # Calculating BMI value
    calculated_bmi = user_weight / (user_height ** 2)
    print(f"Your calculated BMI is: {calculated_bmi:.2f}")

    # Determining weight classification status
    if calculated_bmi >= 30:
        health_status = "Obesity"
    elif calculated_bmi >= 25:
        health_status = "Overweight"
    elif calculated_bmi >= 18.5:
        health_status = "Normal weight"
    else:
        health_status = "Underweight"

    print(f"Health Category Classification: {health_status}")

except ValueError:
    print("Invalid numeric entry. Skipping BMI calculation evaluation.")


# ==========================================
# Task 2: Geographic & Location Matching
# ==========================================
print("\n--- Part 2: Regional Location Analysis ---")

# Database mapping primary cities to their respective nations
regional_map = {
    "Mumbai": "India",
    "Delhi": "India",
    "Kolkata": "India",
    "New York": "USA",
    "Los Angeles": "USA",
    "Chicago": "USA",
    "London": "UK",
    "Manchester": "UK",
    "Birmingham": "UK"
}

# 2.1 Identify the country of a specific city
target_city = input("Enter a city name to look up its country: ").strip().title()

if target_city in regional_map:
    corresponding_nation = regional_map[target_city]
    print(f"Result: The city of {target_city} is located in {corresponding_nation}.")
else:
    print(f"Result: Sorry, {target_city} is not present in our current regional database.")


# 2.2 Compare two cities to check if they share a country
print("\n--- Part 3: City Location Comparison ---")
first_city = input("Enter the first city name: ").strip().title()
second_city = input("Enter the second city name: ").strip().title()

# Verify both entries exist inside our dataset map
if first_city in regional_map and second_city in regional_map:
    nation_one = regional_map[first_city]
    nation_two = regional_map[second_city]
    
    # Conditional logic execution checking equality
    if nation_one == nation_two:
        print(f"Success! Both {first_city} and {second_city} belong to the same country ({nation_one}).")
    else:
        print(f"Notice: These cities are in different countries. {first_city} is in {nation_one} and {second_city} is in {nation_two}.")
else:
    print("Error: One or both of the entered cities could not be found in our records to make a comparison.")
