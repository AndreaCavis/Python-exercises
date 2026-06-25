# Created text variable to test the function described below
text = ''' Problem 1: Frequent Words Finder

Let's start with an interesting task. Imagine being asked to construct a simple word frequency analyzer. 
Given a large body of text, we need to identify the three most frequently occurring words. 
Imagine working with large documents, such as news articles, thesis manuscripts, or even books. 
Identifying the most common words could give us an overview of the main themes or topics in the text.

Naive Approach:
An initial thought might be to iterate over the entire set of words, count each word's occurrences, and then compare the counts. 
However, this method would involve repetitive and redundant operations and is, therefore, inefficient. 
If we think back to the theory of computational complexity from our earlier lessons, 
this 'brute force' approach is known to have a time complexity of O(n^2), where n is the total number of words. 
That's not very appealing, right? Hence, we need to find an alternative approach that's more time-efficient.

Efficient Approach Explanation:
This is where Python dictionaries shine. A Python dictionary allows us to store data in key-value pairs. 
In this case, we can use each unique word in the text as a key and the frequency of the word as its corresponding value. 
As we traverse the document once, we can record the count of each word on the go, avoiding the need for multiple full-document checks. 
Hence, using a dictionary would drastically reduce our algorithm's time complexity and boost its efficiency. 

Solution Building:
Now, let's put this efficient approach into effect with some Python code and dive into its step-by-step explanation. '''

def frequent_words_finder(text: str) -> list:
    from collections import defaultdict

    text = text.lower()
    word_counts = defaultdict(int)
    word_list = text.split()

    for word in word_list:
        word_counts[word] += 1

    top_three = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:3]

    return top_three # [x[0]for x in top_three] for words only

print(frequent_words_finder(text))

''' The function begins by converting the entire text to lowercase. This standardizes the text and ensures that words are not treated as different due to case sensitivity.
Next, the function uses the defaultdict from the collections module to store each word's frequency. 
A defaultdict is a dictionary that provides a default value for a key that does not exist.
Instead of raising a KeyError, it provides a default value, making it perfect for our use case. For the int type, the default value will be 0.

After splitting the text into individual words, the function then iterates over the list of words, 
adding each word to the defaultdict and incrementing the count at every occurrence. 
Finally, using the sorted function on the dictionary entries, it returns a list of the three words with the highest frequency.

The time complexity of this solution is O(N), which is much better than the naive approach we discussed at the beginning. '''



''' Problem 2: Password Strength Counter

As an application developer, ensuring the security of user data is pivotal. A common measure to ensure robust security is testing the strength of passwords. 
A 'strong' password is usually defined as one that is long (at least 8 characters) and includes a mix of uppercase characters, lowercase characters, and digits.

Naive Approach:
Initially, you might think of checking each condition separately. For example, you could use four separate 'for' loops to iterate over the password string to check for each condition, 
i.e., length and the presence of digits, lowercase letters, and uppercase letters. But we know that this approach doesn't scale well. 
Imagine having a password that's hundreds of characters long. Iterating over it four times is unnecessary and, therefore, inefficient.

Efficient Approach Explanation:
A more polished and less time-consuming solution would be to traverse the password string just once while checking for all conditions. 
As we check each character, we can update a dictionary where each condition is a key, 
and its fulfillment (True or False) is the corresponding value. This approach enables us to keep the code both elegant and efficient, 
making the best use of Python dictionaries.

Solution Building:
Now, it's time to implement this efficient solution with some Python code.
'''

def password_strenght_counter(password: str) -> dict[str, bool]:
    strength = {
        'length': False,
        'digit': False,
        'lowercase': False,
        'uppercase': False,
    }

    if len(password) > 8:
        strength['length'] = True

    for char in password:
        if char.isdigit():
            strength['digit'] = True
        if char.islower():
            strength['lowercase'] = True
        if char.isupper():
            strength['uppercase'] = True
        

    return strength
