def solution(arr1, arr2):
    # TODO: Implement this function
    result = []
    for i in arr1:
        for j in arr2:
            if calculate_perfect_square((i + j)):
                result.append((i, j))
    return result
    

def calculate_perfect_square(num):
    # this math approach returns the original value only for perfect squares (else is 23.9999 etc)
    return True if int(num**0.5)**2 == num else False


# output: [(3, 1), (16, 9)]    
print(solution([2,3,16], [1,9,10]))
print(solution([0], [0]))
print(solution([4, 13, 23], [-4, -3, -24]))
# [(4, -4), (4, -3), (13, -4)]
print(solution([4, 13, 23], [-4, -3, -24]))
# [(4, -4), (4, -3), (13, -4)]
        
print(solution([0, 1, 2, -100, 100], [-100, 100, 30, 0, -1, -2, -3]))
# [(0, 100), (0, 0), (1, 0), (1, -1), (2, -1), (2, -2), (-100, 100), (100, -100), (100, 0)

print(solution([100, 75, 36, 9, -25, -64, -100], [-1, 1, 24, 0, -1, -24]))
# [(100, 0), (36, 0), (9, 0)]

print(solution([],  [1, 2, 3, 4]))
# []
print(solution([1, 2, 3, 4], []))
# []
print(solution([], []))
# []