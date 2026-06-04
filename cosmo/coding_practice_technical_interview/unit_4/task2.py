'''
Assume you have a community garden composed of n different types of flowers, with n ranging from 1 to 100.
Each type is represented by a distinct number (1, 2, 3, ..., n).
The garden is depicted as a 1D array, wherein each element indicates the type of flower planted in that specific location.

Your task involves visiting each type of flower at least once, 
traversing the garden in a specific direction (either from left to right with smaller to larger indices, or from right to left). 
You can take exactly k number of steps in the chosen direction, visiting a new location.

Write a Python function, largest_step(garden, start, direction), that accepts as input the garden as an array, 
your starting position, and the direction in which you want to travel. 
This function is expected to compute and return the largest-sized step that you can take 
so that you can visit each type of flower existing in the garden at least once.

If no such value of step enables you to visit all types of flowers at least once, the function should return -1. 
The direction is given as an integer — 1 indicates moving towards larger indices (right), 
while -1 suggests moving towards smaller ones (left).
'''


# CURRENT best attempt
def largest_step(garden: list, start: int, direction: int) -> int:
    n = len(garden)
    step = 1
    max_step = -1

    FLOWERS = dict()
    for flower in garden:
        if flower not in FLOWERS:
            FLOWERS[flower] = False

    # direction -1, r to l (backwards), direction 1, l to r (normal)
    while (step * direction) + start >= 0 and (step * direction) + start <= n:
        pos = start
        visited_flowers = dict()
        flower_count, all_flowers = 0, len(FLOWERS)
        while 0 <= pos < n:
            flower = garden[pos]
            if flower not in visited_flowers:
                visited_flowers[flower] = True
                flower_count += 1
                if flower_count == all_flowers:
                    max_step = max(max_step, step)
                    break
            pos += (step * direction)

        step += 1

    return max_step


# output: 2
print(largest_step([3, 1, 2, 1, 3, 2, 1], 0, 1)) 
# output: 1
print(largest_step([1, 2, 3, 4, 5, 9, 2, 1, 3, 8, 2, 7, 1, 6], 13, -1))
# output: 1
print(largest_step([1], 0, 1))
