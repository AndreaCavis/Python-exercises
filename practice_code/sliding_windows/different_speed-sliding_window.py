'''
    LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS: Find the length of the the longest unique substring (unique meaning no repeating characters).

    solution = the key to this solution is that we are looking for a SUBSTRING, meaning that the characters must be contiguous.
        we can use a sliding window to keep track of the current substring. We will have two pointers,
        LEFT and RIGHT, that will represent the start and end of the current substring.
        window will be a set() to keep track of the unique characters in the current substring. 
        we will move RIGHT to EXPAND in each for loop iteration. When encountering a duplicate char 
        When we encounter a duplicate, we will move LEFT to SHRINK the window UNTIL we remove the duplicate character from the set.
        at each step, we will update the max_length variable with the length of the current substring if it is greater than the current max_length.
'''

def longest_substring_without_repeating_characters(s):
    max_length, left = 0, 0
    window = set()

    for right in range(len(s)):
        # shrink logic
        while s[right] in window:
            window.remove(s[left])
            left += 1

        # expand logic
        window.add(s[right])
        current_length = right - left + 1
        max_length = max(max_length, current_length)

    return max_length


print(longest_substring_without_repeating_characters("abcabcbb")) # 3