# position-value notation
def solution(num1, num2):
    # two pointers initialised to the end of each string (len() - 1 due to 0 indexing)
    i, j = len(num1) - 1, len(num2) - 1
    # carry is needed to hold carryovers from each addition
    carry, res = 0, []

    while i >= 0 or j >= 0 or carry > 0:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        total = n1 + n2 + carry
        carry = total // 10
        res.append(str(total % 10))
        i -= 1
        j -= 1

    return "".join(res[::-1])




print(solution("111111111111111", "222222222222222"))