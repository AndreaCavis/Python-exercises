def solution(arrayA, arrayB):
    indexA, indexB = 0, None
    in_arrayA = True
    visited_arrayA = {0}
    arrayB_path = []
    # values inside arrays are 1-based, not 0 based like indices
    while True:
        if in_arrayA:
            indexB = arrayA[indexA] - 1
            arrayB_path.append(indexB + 1)
        else:
            indexA = arrayB[indexB] - 1
            if indexA not in visited_arrayA:
                visited_arrayA.add(indexA)
            else:
                return arrayB_path
                
        in_arrayA = not in_arrayA


arrayA = [1, 3, 2, 5, 4]
arrayB = [5, 4, 3, 2, 1]

print(solution(arrayA, arrayB)) #  [1, 4, 3, 2, 5]