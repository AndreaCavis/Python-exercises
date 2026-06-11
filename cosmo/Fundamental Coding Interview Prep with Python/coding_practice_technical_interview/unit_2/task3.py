'''
Bob, Alice's friend, is also interested in string manipulations. Inspired by Alice's technique, he has devised his own string encoding scheme.
He takes a sentence, which is a string of n alphanumeric characters (ranging from a-z, A-Z, 0-9), 
including spaces and punctuation marks, with n ranging from 1 to 500, inclusive. 

His encoding technique consists of the following steps:
- He replaces each alphanumeric character with the previous character in their respective sequence, i.e., for alphabets,
  he moves in the alphabetical order, and for numbers, he moves in the ordinal sequence.
  - For instance, given a string word, for each character, if it's not a or A or 0, he replaces it with the character that precedes it in the sequence.
  - For the character a or A, he replaces it with z or Z, respectively.
  - For the number 0, he replaces it with 9.

- Another important aspect of Bob's algorithm involves frequency analysis. 
  After shifting the characters, he counts the frequency of each alphanumeric character in the new string.
  Then, he creates an association between each alphanumeric character and its frequency and ASCII value.
  Each character maps to a number, which is the difference between the ASCII value of the character and its frequency.
  Once this is done, he computes the absolute value of each of these differences.

The task is to help Bob generate a list of these absolute differences, sorted in ascending order.
'''

def solution(sentence):
    next_sentence = "".join(shift_char(char) for char in sentence)
    
    char_frequency = dict()
    for char in next_sentence:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    
    value_differences = {char: ord(char) - freq for char, freq in char_frequency.items()}
    result = [abs(value) for key, value in value_differences.items()]
    
    return sorted(result)
    
    
def shift_char(char):
    # isalnum() checks for alphanumeric characters. isalnum() = isalpha() or isdigit()
    if not char.isalnum():
        return ""

    if char == "a":
        return "z"
    elif char == "A":
        return "Z"
    elif char == "0":
        return "9"
    else:
        return chr(ord(char) - 1)
        