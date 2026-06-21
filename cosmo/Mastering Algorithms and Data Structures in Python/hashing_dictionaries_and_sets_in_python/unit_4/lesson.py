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



''' Problem 2: Anagram Pairs in Two Lists
Consider a cryptology scenario. You've intercepted two separate messages,
each consisting of a list of coded words. You suspect that there might be some connection between the two messages - specifically, 
that some words from one list are anagrams of words in the other list.
Your goal is to find these pairs of anagram words to decipher the code. '''

def solution(list_1: list, list_2: list):
    # Convert every word in sorted(tuple(word)) (aka, Anagram) for a unified form of all anagrams
    sorted_tuples_1 = set(tuple(sorted(word)) for word in list_1)
    # NOTE: tuples are needed to avoid TypeError on keys since list are mutable and unhashable
    sorted_tuples_2 = set(tuple(sorted(word)) for word in list_2)
    
    # Find the common_tuples between the 2 sets, representing the anagrams
    common_tuples = sorted_tuples_1 & sorted_tuples_2
    
    # Create filtered lists by iterating again through the original lists and 
    # store 'word' in their respective list if Anagram belongs in common_tuples
    list_1_output = [word for word in list_1 if tuple(sorted(word)) in common_tuples]
    list_2_output = [word for word in list_2 if tuple(sorted(word)) in common_tuples]
    
    # Finally, return a list(tuple()) where tuple = anagram pair from list_1_output and list_2_output
    output = []
    for word1 in list_1_output:
        for word2 in list_2_output:
            # traversing every word pair in filtered lists
            if tuple(sorted(word1)) == tuple(sorted(word2)):
                output.append((word1, word2))

    return output

print(solution(['cinema', 'iceman'], ['iceman', 'cinema']))



''' Problem 2: Solution with Dictionaries (Optional) '''
from collections import defaultdict

def solution_dictionary(list_1, list_2):
    # Create mapping for `list_1`
    mapping_1 = defaultdict(list)
    # mapping_1 stores (sorted anagram) -> list[anagrams] mapping for `list_1`
    for word in list_1:
        sorted_tuple = tuple(sorted(word)) # unique identifier of the anagram
        mapping_1[sorted_tuple].append(word)
        # `mapping_1[sorted_tuple]` stores all anagrams under the same identifier for `list_1`

    # Create mapping for `list_2`
    mapping_2 = defaultdict(list)
    # mapping_2 stores (sorted anagram) -> list[anagrams] mapping for `list_2`
    for word in list_2:
        sorted_tuple = tuple(sorted(word)) # unique identifier of the anagram
        mapping_2[sorted_tuple].append(word)
        # `mapping_2[sorted_tuple]` stores all anagrams under the same identifier for `list_2`

    # Intersect keys from mapping_1 and mapping_2 to get common sorted tuples
    # Every element in `common_tuples` is an anagram identifier that exists in both lists
    common_tuples = set(mapping_1.keys()) & set(mapping_2.keys())

    output = []
    for anagram_tuple in common_tuples:
        for word1 in mapping_1[anagram_tuple]:
            for word2 in mapping_2[anagram_tuple]:
                # Both word1 and word2 have the same anagram identifier, so are anagrams
                output.append((word1, word2))

    return output

print(solution_dictionary(['cinema', 'iceman'], ['iceman', 'cinema']))
