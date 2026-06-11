'''
Excellent job! Let's make it slightly more challenging. 
Can you finish this function so it prints all key/value pairs in the given dictionary?
'''

def print_space_elements(space_dict):
    for key, value in space_dict.items():
        print(f"{key}: {value}")

# Example usage
space_data = {
    "Mercury": "The smallest planet",
    "Venus": "The hottest planet",
    "Earth": "Our home",
    "Mars": "The Red Planet",
    "Jupiter": "The largest planet",
    "Saturn": "Known for its rings",
    "Uranus": "An ice giant",
    "Neptune": "The farthest planet",
    "Pluto": "A dwarf planet"
}

print_space_elements(space_data)