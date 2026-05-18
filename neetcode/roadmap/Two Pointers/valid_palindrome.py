'''
Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward.
It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

https://neetcode.io/problems/is-palindrome/question?list=neetcode150
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        working_str = "".join(s.split())
        # isalnum() = isalpha() or isdigit()
        clean_str = "".join([ch.lower() for ch in working_str if ch.isalnum()]) 
        n = len(clean_str)
        l, r = 0, n - 1

        while l < r:
            if clean_str[l] != clean_str[r]:
                return False
            l += 1
            r -= 1

        return True
    

s = "Was it a car or a cat I saw?"
s2= "0P"
print(Solution().isPalindrome(s))
print(Solution().isPalindrome(s2))