def solution(arrayA, arrayB, arrayC):
    indexA, indexB, indexC = 0, None, None
    visitedB, visitedC = set(), set()
    lengthA, lengthB, lengthC = len(arrayA), len(arrayB), len(arrayC) 
    max_val_B, max_val_C = float("-inf"), float("-inf")
    
    while True:
        indexB = arrayA[indexA]
        if indexB >= lengthB:
            return max_val_B + max_val_C
        elif indexB not in visitedB:
            visitedB.add(indexB)
        else:
            return max_val_B + max_val_C
        
        max_val_B = max(max_val_B, arrayB[indexB])
            
        indexA = arrayB[indexB]
        if indexA >= lengthA:
            return max_val_B + max_val_C
        
        indexC = arrayA[indexA]
        if indexC >= lengthC:
            return max_val_B + max_val_C
        elif indexC not in visitedC:
            visitedC.add(indexC)
        else:
            return max_val_B + max_val_C
            
        max_val_C = max(max_val_C, arrayC[indexC])
        
        indexA = arrayC[indexC]
        if indexA >= lengthA:
            return max_val_B + max_val_C
  


arrayA = [2, 1, 3, 0]
arrayB = [1, 3, 2, 4]
arrayC = [4, 2, 5, 1]

print(solution(arrayA, arrayB, arrayC)) # 7 (being the sum of max_value_B and max_value_C)