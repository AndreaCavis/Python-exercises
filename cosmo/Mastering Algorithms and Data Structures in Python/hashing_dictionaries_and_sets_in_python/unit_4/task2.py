'''
Hey there, Space Voyager! Your mission, should you choose to accept it, involves anagrams - those fun jumbled-up words. 
You'll be given two arrays of words. Your task? 
Find the unique words in the first array that can rearrange their letters to match at least one word in the second array.
Like transforming 'cinema' into 'iceman'. Cool, right?

The input will be two lists of words; they can be of any size, and words may repeat. 
As for the output, we need a list of unique words from the first list that have anagrams in the second one. 
Make sure the spaceship does not crash into an asteroid, and check that there aren't any duplicate words in the output. 
As for edge cases, watch out for case sensitivity and one-letter words!

It's time to go where no programmer has gone before boldly. Happy coding!
'''

def find_anagram_words(list_1: list[str], list_2: list[str]) -> list[str]:
    # NOTE: tuple is needed because list are mutable and unhashable, they cannot be dict keys
    set_1_anagrams = set(tuple(sorted(word)) for word in list_1)
    set_2_anagrams = set(tuple(sorted(word)) for word in list_2)

    common_anagrams = set_1_anagrams & set_2_anagrams

    res = set()
    for word in list_1:
        if tuple(sorted(word)) in common_anagrams:
            res.add(word)

    return list(res)


print(find_anagram_words(['cinema', 'iceman'], ['iceman', 'cinema'])) # should return ['cinema', 'iceman']
print(find_anagram_words(['test', 'stet'], ['tent', 'nett'])) # should return []
print(find_anagram_words(['hello', 'world'], ['dolly', 'sir'])) # should return []