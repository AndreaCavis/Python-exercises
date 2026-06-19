# https://codesignal.com/learn/course/10/unit/3

''' Problem 1: Array Intersection
Our journey begins with the challenge of identifying the intersection of two arrays. 
In other words, we aim to pinpoint the elements that appear in both of the given lists. 
It's important to note that we're interested in locating unique common elements
- even if an element appears more than once in both lists,
it should only feature once in our output. '''

def array_intersection(list1: list, list2: list) -> list :
    set1, set2 = set(list1), set(list2)
    intersection = set1 & set2
    return sorted(list(intersection))

def array_intersection_optimised(list1: list, list2: list) -> list :
    intersection = set(list1) & set(list2)
    return sorted(list(intersection))

# output: [0,20,40,60,80]
print(array_intersection([x for x in range(0,100,10) if x % 20 == 0], [x*10 for x in range(10)]))


''' Problem 2: Non-Repeating Elements 
Our next issue is slightly more complex. We must determine all elements in a given list that appear only once,
meaning they don't have any duplicates in the same list. '''

def non_repeating_elements(nums: list) -> list:
    seen, repeated = set(), set()

    for num in nums:
        if num in seen:
            repeated.add(num)
        else:
            seen.add(num)

    return list(seen - repeated)


''' Problem 3: Unique Elements 
The third problem compels us to find elements unique to each of the two given lists, i.e. given two lists, list1 and list2, 
we need to find elements that exist only in list1 and elements that exist only in list2, respectively.

Such a task might be beneficial if you possess two lists of employees from different company departments
and you wish to identify the employees unique to each department. '''

def unique_elements(list1: list, list2: list) -> tuple[list, list]:
    set1, set2 = set(list1), set(list2)
    unique_to_1 = list(sorted(set1 - set2))
    unique_to_2 = list(sorted(set2 - set1))
    return (unique_to_1, unique_to_2)
    