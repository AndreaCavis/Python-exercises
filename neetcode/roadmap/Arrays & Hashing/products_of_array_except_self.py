'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]

Constraints:
2 <= nums.length <= 1000
-20 <= nums[i] <= 20
'''

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        l, r = 0, n - 1
        # lists of len(nums) filled with 1 placeholders
        prefix, suffix = [1] * n, [1] * n
        prod_left, prod_right = 1, 1

        while l < n or r >= 0:
            # assigning values to indices before multiplication excludes current i
            prefix[l] = prod_left
            suffix[r] = prod_right
            # perform multiplication for next round of indices
            prod_left *= nums[l]
            prod_right *= nums[r]
            l += 1
            r -= 1

        res = []
        # fill res with the multiplications using prefix and suffix
        for i in range(n):
            res += [prefix[i] * suffix[i]]

        return res


nums = [1,2,4,6]
nums2 = [-1,0,1,2,3]
print(Solution().productExceptSelf(nums))
print(Solution().productExceptSelf(nums2))
