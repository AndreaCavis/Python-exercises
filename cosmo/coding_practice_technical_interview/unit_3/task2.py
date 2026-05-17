# Task description at the bottom 

def solution(inputString, numbers):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    new_string = ""
    sum_so_far, i = 0, 0
    n = min(len(inputString), len(numbers))

    while i < n and sum_so_far < 100:
        char = inputString[i]
        if char in vowels:
            # string.index() returns the index of the first occurrence of the specified value in the string
            new_string += vowels[(vowels.index(char) + 1) % len(vowels)]
        else:
            new_string += consonants[(consonants.index(char) + 1) % len(consonants)]
            
        sum_so_far += numbers[i] * 3
        i += 1

    return (new_string, numbers[i:])


inputString = "examplestring"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(solution(inputString, numbers))  # Output: ('iyenqmit', [9, 10])

input_string = 'zero'
array = [0, 0, 0]
print(solution(input_string, array)) # Output: ('bis', [])




'''
You are given a string of length at most 100 and an array of at most 100 integers.
The task requires you to process both the string and the array simultaneously from their first elements, 
and continue as long as certain condition on the array is satisfied.
Return the modified string and certain portion of the original array.

For the string, your goal is to replace every occurrence of a vowel with the next vowel in the sequence, wrapping around from 'u' to 'a'.
If the character is a consonant, it should be replaced with the next consonant in alphabetical order, wrapping around from 'z' to 'b'.

Meanwhile, for the array of integers, you are instructed to multiply each integer by 3 
and add the result to a total until that total reaches or exceeds 100.
Each integer in the array can range from -50 to 50, inclusive.

Finally, return the modified string and any unprocessed integers from the array in their original order.

Stop processing when the total sum, restricted to 100, is met or when all elements have been processed.
In other words, process both the string and the array while the condition holds true.

If you process all elements in the array and the string, and the total sum still has not reached 100, simply return the processed string and an empty list.

Consider using Python's built-in functions such as ord(), chr(), and round() to aid in achieving this.

The final return format should be a tuple containing the modified string and the list of unprocessed integers.

-----------------------------------------------
Example:

Input:
- String: "examplestring"
- Array: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

Start processing both the string and the array:

1. Character 'e' and Number 1:
   - 'e' is a vowel, so it is replaced with the next vowel 'i'.
   - The array calculation: 1 · 3 = 3, total = 3.

2. Character 'x' and Number 2:
   - 'x' is a consonant, so it is replaced with the next consonant 'y'.
   - The array calculation: 2 · 3 = 6, total = 9.

3. Character 'a' and Number 3:
   - 'a' is a vowel, so it is replaced with the next vowel 'e'.
   - The array calculation: 3 · 3 = 9, total = 18.

4. Character 'm' and Number 4:
   - 'm' is a consonant, so it is replaced with the next consonant 'n'.
   - The array calculation: 4 · 3 = 12, total = 30.

5. Character 'p' and Number 5:
   - 'p' is a consonant, so it is replaced with the next consonant 'q'.
   - The array calculation: 5 · 3 = 15, total = 45.

6. Character 'l' and Number 6:
   - 'l' is a consonant, so it is replaced with the next consonant 'm'.
   - The array calculation: 6 · 3 = 18, total = 63.

7. Character 'e' and Number 7:
   - 'e' is a vowel, so it is replaced with the next vowel 'i'.
   - The array calculation: 7 · 3 = 21, total = 84.

8. Character 's' and Number 8:
   - 's' is a consonant, so it is replaced with the next consonant 't'.
   - The array calculation: 8 · 3 = 24, total = 108 (stop, as total reached over 100).

The rest of the string and array processing stops since the total has exceeded 100.

Output:
- Resulting string: "iyenqmit"
- Remaining array: {9, 10}

In conclusion:
- Processed String: The string "examplestring" becomes "iyenqmit".
- Processed Array: With multiplications and additions up to the total exceeding 100,
  the processed numbers are [1, 2, 3, 4, 5, 6, 7, 8] and the remaining array is {9, 10}.
'''