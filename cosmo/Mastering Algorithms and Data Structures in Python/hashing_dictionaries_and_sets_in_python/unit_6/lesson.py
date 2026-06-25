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

# alternative function with any()
def password_strenght_counter_v2(password: str) -> dict[str, bool]:
    return {
        "length":len(password) > 8,
        "digit":any(char.isdigit() for char in password),
        "lowercase": any(char.islower() for char in password),
        "uppercase": any(char.isupper() for char in password),
    }

''' The function begins by initializing a dictionary strength to hold the results of each condition. 
The keys of the dictionary are the conditions, and their corresponding values are boolean flags initialized as False, 
representing that the conditions are not met initially.

First, the function checks the length of the password. If it is 8 characters or more, the 'length' key in the dictionary is updated to True. 
The function then iterates over every character in the password, checking whether it is a digit, a lowercase letter, or an uppercase letter. 
For each character that meets a condition, the corresponding key in the strength dictionary is updated to True. 
At the end of the process, the function returns the strength dictionary, indicating which conditions the password meets and which it doesn't. '''



''' Problem 3: Bonus Calculator

As a software developer in an HR or Finance team, you might need to work on tasks related to personnel management. 
For instance, suppose your firm has just approved a new policy to give all developers a bonus equal to 10% of their salary. 
Your task is to update the database to reflect this new policy.

Naive Approach:
An initial thought might be to create a new list of dictionaries, where each dictionary contains an employee's information 
and the calculated bonus if the employee's role is 'developer'. However, creating a new list and new dictionaries would represent
an unnecessary allocation of extra memory. Besides, copying data may risk data inconsistency if the original data is updated during 
the process. Therefore, we need to find a method that doesn't involve duplicating our data.

Efficient Approach Explanation:
An efficient approach here is to add a 'bonus' field to the dictionary of each employee who is a developer, updating the ones 
we already have instead of creating new dictionaries. Therefore, we can avoid duplicating the data list.

Solution Building:
Here's how we put this strategy into action using Python code. '''

def bonus_calculator(employees):
    for employee in employees:
        bonus = 0

        if employee['role'] == 'developer':
            bonus = employee['salary'] * 0.1
        
        employee['bonus'] = bonus
    return employees

''' The function starts by iterating over the list of employees. Each employee is represented by a dictionary, and the function 
accesses the 'role' and 'salary' fields of each dictionary. If an employee is a developer, a bonus field, calculated as 10% of their salary, 
is added to their dictionary. Finally, the function returns the updated list of employees. '''



''' Lesson Summary: 

Today, we've observed Python dictionaries in action, helping solve an array of practical problems. 
From analyzing large text data to validating password strength and managing personnel data through list updates - we've seen 
how Python dictionaries offer an elegant and efficient solution in all these scenarios. We've observed how these attributes 
of Python dictionaries come in handy, especially when dealing with large datasets, where computational efficiency is vitally important.

Stay tuned! In our upcoming lessons, we will dive deeper into the systematic study of data structures, algorithms, and computational problem-solving. 
This will further equip you with the fundamentals of computer science and software engineering. Until then, happy programming! '''