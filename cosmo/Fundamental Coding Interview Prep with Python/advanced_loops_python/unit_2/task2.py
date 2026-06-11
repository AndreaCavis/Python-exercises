'''
You are given a string of n words, with n ranging from 1 to 100, inclusive. The words are separated by a single space in the string.
Your task is to return the most frequently occurring character in each word that has an odd number of characters.
The resulting characters should be concatenated into a string with their occurrences in the sentence.

Please note:
Each word's character count ranges from 1 to 500, inclusive. The string contains lowercase and uppercase alphanumeric characters, spaces, and punctuation.
For instance, if the input string is "Hello world this is a demo string", your function should return "lwa".
In this string, 'Hello', 'world', and 'a' have an odd number of characters. The most frequently occurring character in these words are 'l', 'w', and 'a' respectively.
When concatenated, they form "lwa".

In case of a tie in character frequency, return the character that appears first in the word. In the example above, we took 'w' from the word 'world'.
The function should be case insensitive. The lowercase and uppercase characters should be counted as the same character.
The output should only contain lowercase characters. 

For example: "Hhi" should return "h" because "h" appears twice in the string even though one is uppercase and one is lowercase.

If there are no words with an odd number of characters in the input string, your function should return an empty string.
The input string will always be at least one character long, and it cannot be just a single whitespace.
Having a good understanding of string operations and the use of nested loops is very useful in solving this task.
'''

# neater function but less efficient O(W * n^2)
def solution(sentence):
    words = [word.lower() for word in sentence.split()]
    result = ""
    
    for word in words:
        if len(word) % 2 != 0:
            # count goes through the entire word for each character, so it is O(n^2)
            char = max(word, key=word.count) 
            result += char

    return result


# more verbose but more efficient O(W * n)
def best_solution(sentence):
    words = [word.lower() for word in sentence.split()]
    result = ""
    
    for word in words:
        if len(word) % 2 != 0:
            max_occurence = 0
            recurring_chars = {}
    
            for i in range(len(word)):
                char = word[i]

                if char in recurring_chars:
                    recurring_chars[char] += 1
                else:
                    recurring_chars[char] = 1

                char_count = recurring_chars[char]
                
                if char_count > max_occurence:
                        max_occurence = char_count
                        
            for char in recurring_chars:
                if char_count == max_occurence:
                    result += char
                    break

    return result