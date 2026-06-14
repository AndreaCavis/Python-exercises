'''Problem 1: Array Intersection'''

def array_intersection(list1: list, list2: list) -> list :
    intersection = set(list1) & set(list2)
    return sorted(list(intersection))


# output: [2, 3]
print(array_intersection([1,2,3], [60,20,3,4,7,2]))
# output: []
print(array_intersection([1,2,3], [4,5,6]))


'''Problem 2: Non-Repeating Elements'''