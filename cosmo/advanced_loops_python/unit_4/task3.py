def solution(num1: str, num2: str) -> str:
    unit_first_num1 = num1[::-1]
    result = "0"
    
    for j in range(len(unit_first_num1)):
        current_digit = unit_first_num1[j]
        current_product = multiply_strings(num2, current_digit) + ("0" * j)
        result = add_strings(result, current_product)
   
    return result.lstrip("0") or "0"


def multiply_strings(num1: str, current_digit: str) -> str:
    digit, carry = int(current_digit), 0
    res = []
    for i in num1[::-1]:
        n1 = int(i)
        total = (n1 * digit) + carry
        carry = total // 10
        res.append(str(total % 10))
    if carry > 0:
        res.append(str(carry))
    return "".join(res[::-1])
    

def add_strings(string1: str, string2: str) -> str:
    i, j, carry = len(string1) - 1, len(string2) - 1, 0
    string3 = ""
    while i >= 0 or j >= 0 or carry > 0:
        digit1 = int(string1[i]) if i >= 0 else 0
        digit2 = int(string2[j]) if j >= 0 else 0
        total = digit1 + digit2 + carry
        carry = total // 10
        string3 = str(total % 10) + string3
        i -= 1
        j -= 1
    return string3

print(multiply_strings("99425", "9"))        

print(add_strings("12345", "54321"))

print(solution("123", "456"))
