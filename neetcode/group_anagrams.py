class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        n = len(strs)
        # letter key for multiple non anagram words
        x = "a"

        for i in range(n):
            word = strs[i]
            word_length = len(word)

            if word_length not in anagrams:
                anagrams[word_length] = []
                anagrams[word_length].append(word)    
            elif isAnagram(word, anagrams[word_length][0]):
                anagrams[word_length].append(word)
            else:
                # initialise new list and append new value
                anagrams[x] = []
                anagrams[x].append(word)
                x = chr(ord(x) + 1)

        clean_data = filter(isEmpty, anagrams.values())
        
        result = [x for x in clean_data]
        result += [x for x in anagrams.values() if x is str]

        print(result)
            

        return result

def isAnagram(word1, word2):
    return sorted(word1) == sorted(word2)

def isEmpty(array):
    return None if not array else array
        