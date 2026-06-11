'''
Welcome to the first practice of this course!

Let's start by making sure you know enough Python to progress through the rest of the course successfully!
Fill in the missing chunk of the code to make sure this code runs correctly.
'''

def print_dict_elements(dct):
    for key, value in dct.items():
        print(f"{key}: {value}")

# Dictionary containing information about rockets
rocket_info = {
    "Falcon 1": "First privately developed liquid-fueled rocket",
    "Atlas V": "Launch vehicle for Mars Rovers",
    "Saturn V": "Rocket that took humans to the Moon",
    "Space Shuttle": "First reusable spacecraft"
}

print_dict_elements(rocket_info)

# Expected Output:
# Falcon 1: First privately developed liquid-fueled rocket
# Atlas V: Launch vehicle for Mars Rovers
# Saturn V: Rocket that took humans to the Moon
# Space Shuttle: First reusable spacecraft