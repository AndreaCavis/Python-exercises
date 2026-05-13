'''
You are given two exceedingly large positive decimal numbers, num1 and num2, both represented as strings. 
The length of these strings can range anywhere from 1 to 500 characters. 
The challenge here is to subtract num2 from num1 without directly converting the strings into integers.

Create a Python function that performs this operation and returns the resultant string, referred to as num3.

Please note that the subtraction will not result in a negative number, as num1 will always be greater than or equal to num2.
'''

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