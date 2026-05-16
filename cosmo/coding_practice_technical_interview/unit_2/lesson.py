'''
Alice has devised a unique way of encoding words. She takes a word and replaces each character with the next character in the alphabetical order.
In other words, given a string word, for each character, if it's not z, she replaces it with the character that comes next alphabetically.
For the character z, she replaces it with a.

Another element of Alice's algorithm involves frequency analysis. After shifting the characters, she counts the frequency of each character in the new string.
Then, she creates an association of each character with its frequency and ASCII value. 
Each character maps to a number, which is a product of the ASCII value of the character and its frequency. 

The aim of our task is to construct a list that contains these products, sorted in descending order.

-----------------------------------
Example

For the input string "banana", the output should be [294, 222, 99].

The string "banana" will be shifted to "cbobob".

Calculating the product of frequency and ASCII value for each character:

- The ASCII value for 'c' is 99, it appears once in the string so its product is 99x1 = 99.
- The ASCII value for 'b' is 98, it appears three times in the string so its product is 98x3 = 294.
- The ASCII value for 'o' is 111, it appears twice in the string so its product is 111x2 = 222.

Collecting these products into a list gives [99, 294, 222]. Sorting this list in descending order results in [294, 222, 99].
'''

def character_frequency_encoding(word):
    next_string = ""

    for char in word:
        # next_string += "a" if char == "z" else chr(ord(char) + 1) LESSON CODE
        next_string += chr((ord(char) - ord("a") + 1) % 26 + ord("a"))

    char_frequency = dict()
    for char in next_string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    
    products = [ord(char) * freq for char, freq in char_frequency.items()]
    # products.sort(reverse=True) LESSON CODE
    # return products
    return sorted(products, reverse=True)

print(character_frequency_encoding("banana")) # [294, 222, 99]