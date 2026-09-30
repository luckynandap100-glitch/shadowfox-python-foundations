# # hadowFox Python Development Internship
# Beginner Assignment: Numeric Computations and Formatting

# ==========================================
# Task 1: Custom Base Number Formatting
# ==========================================
def convert_numeric_base(val, base_format):
    """Converts a given number into a specified format representation."""
    return format(val, base_format)

# Formatting 145 into its octal ('o') equivalent value
octal_output = convert_numeric_base(145, 'o')
print(f"Task 1 - Octal base representation: {octal_output}")


# ==========================================
# Task 2: Geometric & Environmental Analysis
# ==========================================
pond_radius = 84
PI_VALUE = 3.14

# Computing the surface area of the circular layout
pond_surface_area = PI_VALUE * (pond_radius ** 2)
print(f"Task 2 - Surface area of the pond: {pond_surface_area} sq meters")

# Bonus: Environmental impact analysis (1.4 liters of water per sq meter)
liters_per_sq_meter = 1.4
aggregate_water_volume = pond_surface_area * liters_per_sq_meter

# Presenting final volume as a truncated whole integer
print(f"Bonus  - Total projected water capacity: {int(aggregate_water_volume)} liters")


# ==========================================
# Task 3: Kinematic Speed Evaluation
# ==========================================
travel_distance_meters = 490
duration_minutes = 7

# Transforming the timeline from minutes into runtime seconds
duration_seconds = duration_minutes * 60

# Calculating the rate of speed in meters per second (m/s)
velocity_mps = travel_distance_meters / duration_seconds
print(f"Task 3 - Calculated velocity: {int(velocity_mps)} m/s")
