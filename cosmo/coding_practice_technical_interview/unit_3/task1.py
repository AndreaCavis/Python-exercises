'''
As an aspiring musician, you are given a chance to create a unique encrypted song.
The song's lyrics will be encoded based on specific rules applied to an array of integers and a string.

You are provided with an array of n integers, where n is between 1 to 500, inclusive.
Each integer in the array ranges from -100 to 100, inclusive. Accompanying this, you are presented with a string comprising n lowercase alphabetical characters.

Here are your tasks:

1. For the array, calculate the absolute value of each number and multiply it by 2.
   Accumulate these results until the total exceeds 100.

2. For the string, your task is to replace each letter with the preceding alphabetical character and then concatenate these characters in the order they were processed.
   However, if the current character in the string is a vowel (i.e., 'a', 'e', 'i', 'o', 'u'), it should not be processed, and you should stop the process immediately.

When the accumulated total exceeds 100, or if the next character is a vowel, halt the process and return the transformed string and the remainder of the array in their original order.

Your main challenge here is to process the given string and integer array according to the stated rules but stopping when a certain condition is met.
The final output should be a tuple with the transformed string as the first element and the remaining, unprocessed part of the array as the second element.
'''

def solution(strings, numbers):
    sum_so_far = 0
    new_string = ""
    i = 0
    n = min(len(strings), len(numbers))
    
    while i < n and sum_so_far <= 100:
        sum_so_far += abs(numbers[i]) * 2
        if strings[i] in "aeiou":
            break
        else:
            new_string += chr(ord(strings[i]) - 1)
        i += 1
        
    return (new_string, numbers[i:])


print(solution('abcdef', [10, 20, 30, 40, 50, 60])) # ('', [10, 20, 30, 40, 50, 60]))

print(solution('z', [50])) # ('y', []))




