# ShadowFox Python Development Internship
# Beginner Assignment: Iteration & Loops

import random

# ==========================================
# Task 1: 6-Sided Dice Roll Simulation
# ==========================================

total_sixes = 0
total_ones = 0
consecutive_sixes = 0
last_roll_value = None

# Simulate rolling the dice 20 times
for roll_num in range(1, 21):
    current_roll = random.randint(1, 6)
    print(f"Roll {roll_num}: {current_roll}")

    # Track occurrences of 6
    if current_roll == 6:
        total_sixes += 1

    # Track occurrences of 1
    if current_roll == 1:
        total_ones += 1

    # Track back-to-back 6s
    if last_roll_value == 6 and current_roll == 6:
        consecutive_sixes += 1

    last_roll_value = current_roll

# Output the simulation breakdown
print("\n--- Simulation Results ---")
print("Total number of 6s rolled:", total_sixes)
print("Total number of 1s rolled:", total_ones)
print("Instances of back-to-back 6s:", consecutive_sixes)


# ==========================================
# Task 2: Fitness Challenge - 100 Jumping Jacks
# ==========================================

jacks_done = 0
TARGET_JACKS = 100

print("\n--- Starting Workout Challenge ---")

for set_num in range(1, 11):
    jacks_done += 10
    print(f"\nProgress Update: You have finished {jacks_done} jumping jacks.")

    # Check for workout completion
    if jacks_done == TARGET_JACKS:
        print("Fantastic job! You have fully completed the workout routine.")
        break

    # Prompt user for fatigue check
    user_fatigued = input("Are you feeling tired? (yes/y or no/n): ").strip().lower()

    if user_fatigued in ["yes", "y"]:
        stop_workout = input("Would you like to stop and skip the rest of the sets? (yes/y or no/n): ").strip().lower()
        
        if stop_workout in ["yes", "y"]:
            print(f"Workout stopped. Final score: {jacks_done} jumping jacks completed.")
            break
        else:
            jacks_left = TARGET_JACKS - jacks_done
            print(f"Keep pushing! You have {jacks_left} jumping jacks left to go.")
            
    else:
        jacks_left = TARGET_JACKS - jacks_done
        print(f"Great energy! Only {jacks_left} jumping jacks remaining.")
