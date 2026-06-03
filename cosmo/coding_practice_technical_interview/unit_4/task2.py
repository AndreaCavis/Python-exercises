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
    jump = 1
    n = len(garden)
    res = []

    FLOWERS = set()
    for flower in garden:
        FLOWERS.add(flower)

    all_flowers = len(FLOWERS)
    while (jump * direction) + start >= 0 and (jump * direction) + start <= n:
        pos = start
        flowers, steps = 0, 0
        while pos >= 0 and pos < n:
            flower = garden[pos]
            if flower in FLOWERS:
                flowers += 1
                if flowers == all_flowers:
                    return jump
            pos += direction * jump
            steps += 1
        jump += 1
    return -1


# output: 2
print(largest_step([3, 1, 2, 1, 3, 2, 1], 0, 1)) 
# output: 1
print(largest_step([1, 2, 3, 4, 5, 9, 2, 1, 3, 8, 2, 7, 1, 6], 13, -1))


#             ------------------ WIP ----------------------                         
def largest_step_WIP(garden: list, start: int, direction: int) -> int:
    jump = 1
    n = len(garden)
    res = []

    flowers = dict()
    for flower in garden:
        flowers[flower] = False
    total_flowers = len(flowers)
    
    while (jump * direction) + start >= 0 and (jump * direction) + start <= n:
        pos = start
        flower_count = 0
        flowers = reset_flowers(flowers)
        while pos >= 0 and pos < n:
            flower = garden[pos]
            if flower in flowers:
                if flowers[flower] == False:
                    flowers[flower] = True
                    flower_count += 1
                    if flower_count == total_flowers:
                        res.append(jump)
            pos += jump * direction
        else:
            res.append(jump)

        jump += 1

    return max(res)


def reset_flowers(flowers: dict) -> dict:
    for flower in flowers:
        flowers[flower] = False
    return flowers

# output: 2
print(largest_step_WIP([3, 1, 2, 1, 3, 2, 1], 0, 1)) 
# output: 1
print(largest_step_WIP([1, 2, 3, 4, 5, 9, 2, 1, 3, 8, 2, 7, 1, 6], 13, -1))
