# ShadowFox Python Development Internship
# Beginner Assignment: List Manipulation and Methods

# Initial roster of the Justice League
heroes_roster = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]

# ==========================================
# Task 1: Roster Size Verification
# ==========================================
print(f"Task 1 - Current Team Count: {len(heroes_roster)}")


# ==========================================
# Task 2: Recruiting New Members
# ==========================================
heroes_roster.append("Batgirl")
heroes_roster.append("Nightwing")
print(f"Task 2 - Roster after recruitment: {heroes_roster}")


# ==========================================
# Task 3: Leadership Realignment
# ==========================================
# Elevating Wonder Woman to the top position (index 0)
heroes_roster.remove("Wonder Woman")
heroes_roster.insert(0, "Wonder Woman")

print("\nTask 3 - Roster with Wonder Woman leading at index 0:")
print(heroes_roster)


# ==========================================
# Task 4: Conflict Resolution (Separating Flash & Aquaman)
# ==========================================
# Isolating them by positioning Green Lantern directly between them
heroes_roster.remove("Aquaman")
heroes_roster.remove("Green Lantern")

# Locating Flash to accurately anchor the placement
target_index = heroes_roster.index("Flash")

heroes_roster.insert(target_index, "Aquaman")
heroes_roster.insert(target_index + 1, "Green Lantern")

print("\nTask 4 - Roster after placing Green Lantern between Aquaman and Flash:")
print(heroes_roster)


# ==========================================
# Task 5: Roster Confirmation Display
# ==========================================
print(f"\nTask 5 - Current Working Roster:\n{heroes_roster}")


# ==========================================
# Task 6: Alphabetical Sorting & New Command Structure
# ==========================================
# Sorting the array alphabetically
heroes_roster.sort()

print("\nTask 6 - Alphabetically Organized Roster:")
print(heroes_roster)
print(f"Newly Appointed Leader (Index 0): {heroes_roster[0]}")
