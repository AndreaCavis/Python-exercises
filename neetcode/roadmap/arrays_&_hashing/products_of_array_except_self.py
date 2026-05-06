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

# ----------------------- Naive Solution (division) -----------------------
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        products_list = []
        total_prod = 1
        # calculate total product from which we will deduct nums[i]
        for num in nums:
            total_prod *= num

        for num in nums:
            total_without_current_num = total_prod // num
            products_list.append(total_without_current_num)

        return products_list


nums=[1,2,4,6]
print(Solution().productExceptSelf(nums))
