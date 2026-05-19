# Description Below

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # initial check to avoid wasting time
        if sum(nums) < 0:
            return []
        
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        i, k = 0, n - 1
        res = []

        for j in range(1, n - 2, 1):
            mid_num = nums[j]

            while i < j and j < k:

        return []

'''
Given an integer array nums,
return all the triplets [nums[i], nums[j], nums[k]]
where nums[i] + nums[j] + nums[k] == 0,
and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.

The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
Input: nums = [0,1,1]
Output: []

Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]

Explanation: The only possible triplet sums up to 0.


https://neetcode.io/problems/three-integer-sum/question?list=neetcode150
'''