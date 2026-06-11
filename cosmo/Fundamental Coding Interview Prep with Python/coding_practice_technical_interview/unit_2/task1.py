'''
Mike is fascinated by numbers and operations, having devised a unique number encoding scheme.
Given an array numbers consisting of n integers, where n ranges from 1 to 100 inclusive, Mike undertakes the following operations:

1. For each number in the array that is not a multiple of 10, he increases it by 1.
2. For each number that is a multiple of 10, he assigns it a value of 1.

Following these operations, Mike calculates the frequency of each number in the new array. Subsequently, he establishes an association between each number and its frequency.
This association maps the number to a product, defined as the multiplication of the number itself by its frequency.

Your task is to generate a list that encompasses these products, organized in ascending order.
Each number in the array numbers spans from -100 to 100, inclusive.

For example, given the input array numbers = [5, 10, 15, 10, 5, 15],
after applying Mike's operations, we have a resulting array of [6, 1, 16, 1, 6, 16]. 
The frequency of each number is 6: 2, 1: 2, 16: 2. 
The corresponding products (number * frequency) are 6*2 = 12, 1*2 = 2, and 16*2 = 32. 
Therefore, the output is [2, 12, 32], sorted in ascending order.
'''

def solution(numbers):
    next_numbers = []
    for num in numbers:
        if num % 10 == 0:
            next_numbers.append(1)
        else:
            next_numbers.append(num + 1)
    
    num_frequency = dict()
    for num in next_numbers:
        if num in num_frequency:
            num_frequency[num] += 1
        else:
            num_frequency[num] = 1
            
    result = [num * freq for num, freq in num_frequency.items()]
    
    return sorted(result)