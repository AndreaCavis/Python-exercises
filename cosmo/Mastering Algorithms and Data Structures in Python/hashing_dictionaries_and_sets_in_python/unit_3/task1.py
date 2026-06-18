'''
Hold onto your tail, Voyager! We're in the midst of an integers war, separated into two integer lists!
We have to find the common integers in both lists. Remember, we only need the unique ones.
Your mission is to compute a new set of common_integers with those common “heroes”, in a descending honor roll.

No number repeats nor resists the gravitational pull! Make sure you deliver in the right format:

- Each set can contain up to 10^4 integers, ranging from -10^6 to 10^6 inclusive.
- Output should be a list of unique integers existing in both sets in descending order.

Let's go, Cosmonaut! Leave no Integer behind!
'''

def intersecting_elements(set1: set, set2: set) -> list:
    common_integers = sorted(list(set1 & set2), reverse=True)
    return common_integers

print(intersecting_elements({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}))
# Expected output: [10, 9, 8, 7, 6, 5]

print(intersecting_elements({-1, -2, -3, -4, -5}, {-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5}))
# Expected output: [-1, -2, -3, -4, -5]

print(intersecting_elements({1, 3, 5, 7, 9}, {2, 4, 6, 8, 10}))
# Expected output: []