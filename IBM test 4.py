# Q3. Write a Program to Change Decimal Number to Binary

num = 35

def convertToBinary(num):
    numBinary = "" 
    while num >= 1:
        numBinary = str(num%2) + numBinary
        num = num // 2
    return numBinary
    
def recurseToBinary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return recurseToBinary(n // 2) + str(n % 2)

print(convertToBinary(num))
        
