'''
Our mission for today is to generate a unique encoded message for a book club. Here's the fun part:
to create a cryptic message, we will process a string and an array of numbers simultaneously and stop once a given condition is satisfied.

For the string, our task is to replace each letter with the next alphabetical letter and then reverse the entire updated string.
For the array of numbers, our task is to divide each number by 2, round the result, and accumulate the rounded numbers until their total exceeds 20.

When the accumulated total exceeds 20, we immediately stop the process and 
return the updated string and the as yet unprocessed numbers in their original order.

----------------------------------------------
Example

Consider the input string "books" and array [10, 20, 30, 50, 100].

We start our process with an empty string and a sum of 0.

- For the first character 'b' in 'books', we replace it with the next alphabet 'c'. 
  For the corresponding number 10 in the array, we divide it by 2 and round it. The result is 5.
  The sum after first operation is 5 which is less than 20, so we continue to the next character.
- For the next character 'o', we replace it with 'p'. And for the corresponding number 20 in the array, half and rounded is 10.
  The sum after the second operation is 15 (5 + 10). The sum still doesn't exceed 20, so we move to third character.
- For the next character 'o', we replace it with 'p'. And for the corresponding number 30 in the array, half and rounded is 15.
  When we add this '15' to our previously calculated sum 15, it totals to 30 which is more than 20.
  So, we stop the process here.
- We have processed 'b', 'o', and 'o' from the word 'books' and replaced them with 'c', 'p', and 'p' respectively to get "cpp".
  After reversing, we get "ppc".
- For the array, we exclude any numbers that we have processed. Hence, we exclude the first three numbers and the array becomes [50, 100].

So the output should be ('ppc', [50, 100]).
'''

# NOTE
'''
Why using round() and instead of // ?
// represents FLOOR division, meaning each result is rounded down to the nearest whole number.
For example, 5 // 2 would yield 2, and -5 // 2 would yield -3.

round() rounds to the nearest whole number following the banker's rounding rule (when half, round to the nearest even number).
For example, round(5 / 2) would yield 2, and round(-5 / 2) would yield -2.
'''

# 2 versions of the solution, one is the original and one is mine, the difference is that I operate by removing numbers from the original array,
# the original takes advantage of the index i to return the unprocessed list
def solution(inputString, numbers):
    result = ""
    sum_so_far = 0
    i = 0

    while i < len(inputString) and sum_so_far <= 20:
        result += chr((ord(inputString[i]) - ord("a") + 1) % 26 + ord("a"))
        sum_so_far += round(numbers[i] / 2)
        i += 1
    
    return (result[::-1], numbers[i:])

# ----------------------------------------------------------------------------
def Mysolution(inputString, numbers):
    result = ''
    sum_so_far = 0
    i = 0

    while i < len(inputString) and sum_so_far <= 20:
        result += chr((ord(inputString[i]) - ord("a") + 1) % 26 + ord("a"))
        # the difference is here, I remove from the beginning of list as opposed to simply copying the value from the given position
        sum_so_far += round(numbers.pop(0) / 2)
        i += 1

    return (result[::-1], numbers)


inputString = "books"
array = [10, 20, 30, 50, 100]

print(solution(inputString, array))  # Output: ('ppc', [50, 100])
print(Mysolution(inputString, array))  # Output: ('ppc', [50, 100])

print()
print(f"round( 5 / 2):  {round(5 / 2)}") 
print(f"round( 7 / 2):  {round(7 / 2)}") 
print(f"round(-5 / 2): {round(-5 / 2)}") 
print(f" 5 // 2:  {5 // 2}")
print(f" 7 // 2:  {7 // 2}")
print(f"-5 // 2: {-5 // 2}")
