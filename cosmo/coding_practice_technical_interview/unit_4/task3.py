'''
Prepare to challenge your array manipulation skills! Consider two arrays, array1 and array2, each consisting of n non-negative integers.
The values of n range from 1 to 500 inclusive.
Each integer in the arrays is at most 10^3.

Your task is to discover a rotation of array1 that minimizes the Manhattan distance with array2. 
The Manhattan distance between two arrays, a and b, of size n, is defined by:

D(A, B) = (n ∑ i=1) |Ai - Bi|

where Ai and Bi denote the i-th elements of arrays a and b, respectively, and n represents the size of the arrays.

A rotation of an array refers to taking one or more elements from the end and moving these elements to the beginning,
maintaining their original order in the process.

You need to return the smallest possible Manhattan distance obtained through this operation.

Let's say that you find multiple rotations of array1 that yield the same smallest Manhattan distance with array2.
In this case, you should return the rotated array that, when converted into an integer number by concatenating all of its digits (from left to right),
would be the smallest.

Consider the array as periodic; that is, after the last element, the first one follows.

Keep in mind that the size of the two arrays is always the same, and the arrays are not necessarily sorted at the beginning.

If array1 is exactly the same as array2 from the beginning, output the original array1 and the Manhattan distance 0.

Remember, the ultimate goal is to minimize the Manhattan distance between array1 and array2 through the least alterations possible to array1.
Let's see how small you can get!
'''


def solution(array1: list[int], array2: list[int]) -> tuple[list[int], int]:
    # both arrays have the same len() as per exercise
    n = len(array1)
    distances_dict = dict()
    shift = 1

    if calculate_manhattan_distance(array1, array2) == 0:
        return (array1, 0)

    while shift < n:
        curr_array = array1[shift:] + array1[:shift]
        curr_dist = calculate_manhattan_distance(curr_array, array2)

        if curr_dist in distances_dict:
            distances_dict[curr_dist] += [curr_array]
        else:
           distances_dict[curr_dist] = [curr_array]
        
        shift += 1

    # calculate min manhattan distance
    min_shift = min(distances_dict)
    # dict() to handle multiple array with same manhattan distance
    stringified_min_result = dict()
    for x in distances_dict[min_shift]:
        stringified_min_result[stringify_array(x)] = x

    min_str_array = min(stringified_min_result)
    min_array = stringified_min_result[min_str_array]

    return (min_array, min_shift)


def calculate_manhattan_distance(arr1: list[int], arr2: list[int]) -> int:
    return sum([abs(a - b) for a, b in zip(arr1, arr2)])


def stringify_array(arr: list[int]) -> str:
    return "".join(f"{x}" for x in arr)


# output: ([3, 4, 5, 1, 2], 6)
print(solution([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))

# output: ([2, 1], 0))
print(solution([1, 2], [2, 1]))

# output: ([10, 1, 2, 3, 4, 5, 6, 7, 8, 9], 45)
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

