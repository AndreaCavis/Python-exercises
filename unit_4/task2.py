def solution(num1, num2):
    i, j, carry = 0, 0, 0
    num3 = []
    
    while i < len(num1) or j < len(num1) or carry > 0:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        if n2 > n1:
            # TODO: this doesn't cover 100 - 1, 1000 - 1, etc
            difference = int(num1[i:i+2]) - n2
        else:
            difference = n1 - n2
        num3.append(str(difference))
        i += 1
        j += 1
    
    
    return "".join(num3[::-1])