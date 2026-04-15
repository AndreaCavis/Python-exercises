# 1. Write a program to find HCF of two numbers by without using recursion.

# Input format: The first line contains any 2 positive numbers separated by space
# Print the HCF of given two numbers.
# Sample Input:
# 70 15
# Sample Output:
# 5

numbers = "70 15"
string1, string2 = numbers.split()
num1, num2 = int(string1), int(string2)

# x = a%b then b%x and repeat 
# calculate HCF(a,b) = HCF(b, a % b)
def HCF(a, b):
    while b!=0:
        x = a % b  
        a = b  
        b = x  
    answer = a
    return answer

print(HCF(num1, num2))