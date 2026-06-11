'''
You are tasked with writing a Python function to multiply two extremely large positive integers. 
These are not your regular-sized large numbers; they are represented as strings potentially up to 500 digits long.

Your function should take two string parameters, representing the two large integers to be multiplied, 
and return the product as a string. 
The challenging part is that you should perform the multiplication without converting the entire strings into integers.

Keep in mind that the elements of the string are digits in the range from 0 to 9, inclusive.

Furthermore, bear in mind that when multiplying numbers manually, 
we align the numbers vertically and multiply each digit of the first number with each digit of the second number, starting from the rightmost digits,
and add the results after shifting appropriately.

Please solve this problem using similar, decision-based string manipulations 
instead of merely converting strings into integers, multiplying them, and converting the result back to a string. 
This approach is imperative as direct multiplication would not be feasible for very large numbers.

Challenge yourself, and Happy Coding!
'''

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
