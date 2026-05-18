'''
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2.
 Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1) additional space.

Example 1:
Input: numbers = [1,2,3,4], target = 3
Output: [1,2]

Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

https://neetcode.io/problems/two-integer-sum-ii/question?list=neetcode150
'''

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # numbers is sorted in increasing order (non decreasing).
        index1, index2= 0, len(numbers) - 1

        while index1 < index2:
            # ascending order, therefore num_right = small, num_left = big
            num_right, num_left = numbers[index1], numbers[index2]
            temp_sum = num_right + num_left

            if temp_sum == target:
                # indices must be 1-indexed.
                return [index1 + 1, index2 + 1]
            # sum too big, reduce num_left
            elif temp_sum > target:
                index2 -= 1
            # sum too small, increase num_right
            else:
                index1 += 1
        # placeholder return, the exercise guarantees one valid solution per test case
        return [0,0]
        