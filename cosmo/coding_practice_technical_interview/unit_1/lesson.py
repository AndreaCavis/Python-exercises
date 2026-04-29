#TODO: do the practice session either today or tomorrow

def solution(arrayA, arrayB):
    indexA, indexB, max_value = 0, None, float("-inf")
    in_arrayA = True

    while True:
        if in_arrayA:
            indexB = arrayA[indexA]
            if arrayB[indexB] > max_value:
                max_value = arrayB[indexB]
        else:
            indexA = arrayB[indexB]
            if indexA == 0:
                return max_value
        in_arrayA = not in_arrayA


print(solution([2, 4, 3, 1, 6], [4, 0, 3, 2, 0])) #3
