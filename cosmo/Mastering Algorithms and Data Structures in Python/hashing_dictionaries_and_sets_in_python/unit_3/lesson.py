'''Problem 1: Array Intersection'''

def array_intersection(list1: list, list2: list) -> list :
    intersection = set(list1) & set(list2)
    return sorted(list(intersection))


# output: [2, 3]
print(array_intersection([1,2,3], [60,20,3,4,7,2]))

# output: [1,5,9]
print(array_intersection([x for x in range(10)], [1,20,5,9,11]))

# output: [10,20,30]
print(array_intersection([x for x in range(0,100,10)], [10,20,30,456,7,8,99]))

'''Problem 2: Non-Repeating Elements'''