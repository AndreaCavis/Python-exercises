def solution(arrayA, arrayB, arrayC):
    indexA, indexB, indexC = 0, None, None
    visitedB, visitedC = set(), set()
    lengthA, lengthB, lengthC = len(arrayA), len(arrayB), len(arrayC)
    max_val_B, max_val_C = float("-inf"), float("-inf")
    
    while True:
        # step 1
        indexB = arrayA[indexA]
        if check_valid_path(indexB, lengthB, visitedB):
            max_val_B = max(max_val_B, arrayB[indexB])
        else:
            return max_val_B + max_val_C
        # step 2
        indexA = arrayB[indexB]
        if indexA >= lengthA:
            return max_val_B + max_val_C
        # step 3
        indexC = arrayA[indexA]
        if check_valid_path(indexC, lengthC, visitedC):
            max_val_C = max(max_val_C, arrayC[indexC])
        else:
            return max_val_B + max_val_C
        # step 4
        indexA = arrayC[indexC]
        if indexA >= lengthA:
            return max_val_B + max_val_C
        

def check_valid_path(index, length, visited):
    if index >= length:
        return False
    elif index in visited:
        return False
    else:
        visited.add(index)
        return True
  


arrayA = [2, 1, 3, 0]
arrayB = [1, 3, 2, 4]
arrayC = [4, 2, 5, 1]

print(solution(arrayA, arrayB, arrayC)) # 7 (being the sum of max_value_B and max_value_C)