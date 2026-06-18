'''Problem 1: Array Intersection'''

def array_intersection(list1: list, list2: list) -> list :
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1 & set2
    return sorted(list(intersection))

def array_intersection_optimised(list1: list, list2: list) -> list :
    intersection = set(list1) & set(list2)
    return sorted(list(intersection))

# output: [0,20,40,60,80]
print(array_intersection([x for x in range(0,100,10) if x % 20 == 0], [x*10 for x in range(10)]))

'''Problem 2: Non-Repeating Elements'''