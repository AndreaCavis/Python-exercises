def solution(num1, num2):
    if len(num1) > len(num2):
        return 1
    elif len(num1) < len(num2):
        return -1
    else:
        i, j = 0, 0
         
        while i < len(num1) or j < len(num2):
            if num1[i] > num2[j]:
                return 1
            elif num1[i] < num2[j]:
                return -1
            i += 1
            j += 1
    
    return 0