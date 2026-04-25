def solution(num1, num2):
    i, j, carry = len(num1) - 1, len(num2) - 1, 0
    res = []
    
    while i >= 0 or j >= 0 or carry > 0:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        
        if (n1 - carry) >= n2:
            difference = n1 - carry - n2
            carry = 0
        else:
            difference = (10 + n1 - carry) - n2
            carry = 1
            
        res.append(str(difference))
        i -= 1
        j -= 1
        
        clean_res = "".join(res[::-1])
        num3 = clean_res.lstrip("0")

    return num3 if num3 else "0"