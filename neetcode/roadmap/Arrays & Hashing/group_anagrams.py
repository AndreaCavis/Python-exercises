'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

https://neetcode.io/problems/anagram-groups/question?list=neetcode150
'''


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}

        for word in strs:
            clean_word = "".join(sorted(word))
            if clean_word in anagrams:
                anagrams[clean_word].append(word)
            else:
                anagrams[clean_word] = [word]

        result = [x for x in anagrams.values()]

        return result