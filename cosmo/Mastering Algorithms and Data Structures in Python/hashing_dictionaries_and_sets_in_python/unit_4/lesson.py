# https://codesignal.com/learn/course/10/unit/4

''' Problem 1: Unique String in the List

Our first problem revolves around identifying the first unique string from a list. 
Imagine you're working on a text analyzing tool that needs to identify the first unique word in a piece of text. 
This problem simulates such a real-world scenario. '''

def find_unique_string(words: list[str]) -> str:
    seen, duplicates = set(), set()

    for word in words:
        if word in seen:
            duplicates.add(word)
        seen.add(word)

    for word in words:
        if word not in duplicates:
            return word
        
    return ""

print(find_unique_string(["lol", "lol", "lol", "lol", "Nakama", "lol", "lol", "lol"]))