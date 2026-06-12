'''Problem 1: Array Intersection'''

def array_intersection(list1: list, list2: list) -> list :
    intersection = set(list1) & set(list2)
    return sorted(list(intersection))


'''Problem 2: Non-Repeating Elements'''