# https://codesignal.com/learn/course/10/unit/4

''' Problem 1: Unique String in the List

Our first problem revolves around identifying the first unique string from a list. 
Imagine you're working on a text analyzing tool that needs to identify the first unique word in a piece of text. 
This problem simulates such a real-world scenario.

Naive Approach:
At first glance, a naive approach would be to iterate over the list of words and, for each word, scan the entire list again to count its occurrences. 
This method of double-pass scanning the list results in an unsightly time complexity of O(n^2) as each word incurs another full traverse. 
As the list grows in size, the time taken by this approach grows exponentially, making it impractical for larger datasets.

Efficient Approach Explanation:
Let's introduce Python sets to the stage! The defining property of a set is that it contains unique elements, making it a perfect fit for our current predicament.

Our strategy consists of two parts, each tailored to leverage the capabilities of sets:
1. We scan through the words, keeping track of the previously encountered words in a set called seen. A crucial aspect of our solution comes from an inherent feature of sets:
   if a word is already in seen, adding it again does not change the set. Keeping this in mind, we create a second set, duplicates, consisting only of words that we have previously seen.
2. Once we know which words are duplicates, it becomes elementary to find the first word in our original list that isn't a duplicate.
   We make another pass over the list, checking each word to see if it's in the duplicates set. The first word we find that isn't a duplicate is our answer.

By focusing our solution around sets, we've reduced the problem to two single-pass traversals, 
giving our solution a linear time complexity of O(2N), a significant improvement over the naive approach.

Solution Building:
1. In the initial iteration over words, if a word already exists in the seen set, we identify it as a duplicate and add it to duplicates. If not, the word is added to seen.
    (This code creates two sets. seen contains all words we've come across, and duplicates contains words that have appeared more than once. 
    To visualize it, consider words as 'apple', 'banana', 'apple'. After the above block of code, we'd have seen as 'apple', 'banana', and duplicates as 'apple'.)
2. In the next phase of our solution, we iterate over words again, checking if a word is in duplicates. 
   The first word that is not in duplicates is our answer as it's the first unique string in the list. If we don't find any unique string, we return an empty string. '''

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

''' Thanks to two simple traversals, we've efficiently solved a problem that initially seemed complex. '''



''' Problem 2: Anagram Pairs in Two Lists

Consider a cryptology scenario. You've intercepted two separate messages,
each consisting of a list of coded words. You suspect that there might be some connection between the two messages - specifically, 
that some words from one list are anagrams of words in the other list.
Your goal is to find these pairs of anagram words to decipher the code. 

Naive Approach:
The most straightforward approach to this problem would involve checking each word from the first list against each word from the second list to find anagrams. 
While this would provide correct results, it's an inefficient method with a time complexity of O(n⋅m⋅w),
where n is the size of the first list of words, m is the size of the second list of words, and w is the average word length. 
As you can see, it gets impractically slow for larger inputs.

Efficient Approach Explanation:
We can achieve a more efficient solution by representing each word from both lists as a sorted tuple of characters. 
This gives us a unified form for each set of anagram words, making them easy to compare. If the sorted tuples of characters for two words are the same, 
then those words are anagrams. Once we have these sorted tuples, we can use Python's set methods to find pairs of words that are anagrams of each other.

Solution Building:
Here's how we fulfill the task:

- We first convert every word from both lists to a sorted tuple of its characters to have a unified form for all anagram words.
- Now, those sets themselves have unique character tuples. We find the common tuples between the two, which represent the anagram words.
- For the final output, we iterate over the words in the original lists again, and for each word, if its sorted character tuple is present in common_tuples set, we add it to the respective output list.
- Finally, we return a list of tuples, where each tuple is an anagram pair from list_1_output and list_2_output.

'''

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

''' The time complexity of this method is O((n+m)⋅wlogw + a⋅b⋅wlogw), 
where n and m are sizes of list1 and list2, respectively, w is the average word length, and a and b are the sizes of list_1_output and list_2_output.
In the worst case where most words are anagrams, this becomes O(n⋅m⋅wlogw). 
While this is still potentially quadratic in terms of list sizes, it's much more efficient than the naive approach in typical cases where only a subset of words have anagrams. '''



''' Problem 2: Solution with Dictionaries (Optional) 

While this course didn't cover Python dictionaries yet, they are essentially a very powerful tool that can make the solution here even more effective. 
We are going to dig into Python dictionaries later in this course, but take a moment to go through and try to understand the solution for this problem 
if dictionaries would be possible to use. This is totally optional; no worries if you don't understand the solution yet; we will learn dictionaries later in this course. '''

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

''' This solution will only traverse pairs that are actually anagrams, so the complexity will be O((n+m)⋅wlogw+P), 
where n and m are sizes of list1 and list2, respectively, w is the average word length and P is the number of anagram pairs in the output. 
This is significantly better than the previous approach because we avoid redundant sorting operations and only iterate through actual anagram pairs. 
Note that if you only need to calculate the number of anagram pairs, 
the time complexity remains O((n+m)⋅wlogw) as you can simply count pairs without iterating through them. '''