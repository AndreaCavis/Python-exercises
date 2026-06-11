'''
In today's task, we'll step into the world of large numbers, where, specifically, we are given two exceedingly large positive integers.
However, these aren't your average, everyday large numbers. They are so vast they're represented as strings that can be up to 10,000 digits long!

Accepting our mission means writing a Python function that binds these two "string-numbers" together. 
The challenge is to perform the addition without converting the entire strings into integers.

Finally, our function should return the resulting sum, represented as a string. 
While it might seem daunting at first, don't worry -- we'll break it down step by step, mimicking how we manually add numbers.

# -------------------------------------#

Before we start coding, let's consider the strategy we're going to adopt. 
You may recall that each digit in a number has a value, and the position of the digit determines its influence on the total value of the number.

*This system is called place-value notation.*
'''


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