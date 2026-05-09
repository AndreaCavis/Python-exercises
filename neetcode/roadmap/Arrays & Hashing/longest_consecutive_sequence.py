'''
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

https://neetcode.io/problems/longest-consecutive-sequence/history?list=neetcode150&submissionIndex=3
'''

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        num_sequences = dict()

        for num in sorted(nums):
            if (num - 1) in num_sequences:
                if num in num_sequences[num-1]:
                    continue
                else:
                    num_sequences[num-1].append(num)
                    num_sequences[num] = num_sequences[num-1]
            else:
                num_sequences[num] = [num]

        # the result of max() in this case is a tuple, e.g.: (1, [1,2,3]) 
        # so 2 variables must be assigned to access max_sequence
        index, max_sequence = max(num_sequences.items(), key=lambda item: len(item[1]))

        return len(max_sequence)
    

nums = [2,20,4,10,3,4,5]
print(Solution().longestConsecutive(nums))
    

