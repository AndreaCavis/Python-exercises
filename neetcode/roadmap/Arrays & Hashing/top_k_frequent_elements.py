'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

https://neetcode.io/problems/top-k-elements-in-list/question
'''

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        seen = {}
        # res = set()

        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        
        # sort dictionary by values(represented by item[1]) in descending order to find the most frequent elements
        sorted_seen = sorted(seen.items(), key=lambda item: item[1], reverse=True)
        # extract keys sorted by frequency
        res = [num[0] for num in sorted_seen]
        # return only the most k frequent
        return res[:k]
    

solution = Solution()

print(solution.topKFrequent([1,2,2,3,3,3], 2))