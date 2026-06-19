'''
Alright, Space Voyager! Now that we're done with arrays and strings let's fuse them together in a real-time scenario. Here's your scenario:

Suppose you've got a list of words, let's say ['apple', 'banana', 'apple', 'mango', 'banana']. 
Each word could be repeated an arbitrary number of times. Think of this list as a conveyor belt in a space-age fruit factory. 
Now, your task is to identify the last unique fruit on the belt, i.e., the one that didn't repeat. 
If all the fruits are repeating, then there ain't any unique fruit, and your function should return an empty string ('').

Your function should take a list of strings (the conveyor belt of fruits) as input. 
Now, a string can be any word, not just a fruit name, and the list can have any number of strings. 
There could also be an edge case where the list has no strings at all (Empty conveyor belt, eh?). 
For output, your function should return the last unique string in the list or an empty string if there are not any of them.

To solve this task, you are expected to use sets. Sets are efficient for tracking seen and duplicate elements due to their fast membership testing capability.

Think you can deal with this, Space Voyager? Onwards!
'''

def find_unique_string(words: list[str]) -> str:
    if not words:
        return ""
    
    seen, duplicates = set(), set()

    for word in words:
        if word in seen:
            duplicates.add(word)
        seen.add(word)

    for word in reversed(words):
        if word not in duplicates:
            return word
        
    return ""

print(find_unique_string(['apple', 'banana', 'apple', 'mango', 'banana']))  # It should print: 'mango'
print(find_unique_string(['hello', 'world', 'hello', 'world']))  # It should print: ''
print(find_unique_string(['hello', 'world', 'hello']))  # It should print: 'world'
print(find_unique_string([]))  # It should print: ''