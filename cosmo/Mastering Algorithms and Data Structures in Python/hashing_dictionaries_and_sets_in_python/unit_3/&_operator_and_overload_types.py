'''
In Python, the & operator is the bitwise AND operator.
It compares the bits of two integers and returns a new integer whose bits are set to 1 only where both operands have 1.

Example:'''
a = 12      # binary: 1100
b = 10      # binary: 1010

result = a & b
print(f"bitwise AND operator: {bin(a)[2:]} & {bin(b)[2:]}. Result: {result}")  # 8
'''
Why?
  1100   (12)
& 1010   (10)
------
  1000   (8)
'''

''' # Common use cases
1. Bit masking 
Check whether a specific bit is set
'''
flags = 0b1010

if flags & 0b0010:
    print(f"Since 0b1010 & 0b0010 returns {0b1010 & 0b0010}, the bit is set (because {0b1010 & 0b0010} != 0)")
'''
2. Set Intersection (The studying case in this unit)
For python SETS, & means intersection:'''
a = {1, 2, 3}
b = {2, 3, 4}

print(f"a & b is the intersection between {1, 2, 3} & {2, 3, 4}, returning {a & b}")  # {2, 3}
'''
3. Boolean values
Since True and False are integers (1 and 0), & works on them. # print(True & False) returns False, etc

However, for LOGICAL CONDITIONS, prefer 'and' because 'and' short-circuits, meanwhile '&' evaluates both sides.
'''
x = 0

# Logical AND
if x != 0 and 10 / x > 1:
    pass  # safe 

# Bitwise AND
try:
    if (x != 0) & (10 / x > 1):
        pass # raises ZeroDivisionError
except Exception as error:
    print(f"{error}. & evaluates the second condition instead of stopping like and and avoiding the error")



