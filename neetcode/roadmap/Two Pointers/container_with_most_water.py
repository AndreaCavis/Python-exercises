'''
You are given an integer array heights where heights[i] represents the height of the i(th) bar.
You may choose any two bars to form a container. 
Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,7,2,5,4,7,3,6]
Output: 36

Example 2:
Input: height = [2,2,2]
Output: 4

https://neetcode.io/problems/max-water-container/question?list=neetcode150
'''

# Ok, so the task asks me the max_area I can produce with n bars where n is the len(heights)
# min(height[l], height[r]) is the height of the bar (1st dimension) and 
# the distance between the indices 'l' and 'r' (2nd dimension) multiplied will produce curr_area.
# I need to evaluate each area I can form and select the max(max_area, curr_area)

# NOTE: Naive Solution, needs refactoring
class Solution:
    def maxArea(self, heights: list[int]) -> int:
        n = len(heights) - 1
        max_area = 0
        
        # Brute Force approach. O(n)2
        for l in range(n):
            r = n
            while l < r:
                height = min(heights[l], heights[r])
                length = r - l
                curr_area = height * length if length != 0 else 1
                max_area = max(curr_area, max_area)
                r -= 1

        return max_area


height=[1,7,2,5,4,7,3,6]
height2 = [1,2]
height3 = [1,7,2,5,12,3,500,500,7,8,4,7,3,6]

# print(Solution().maxArea(height)) # 36
# print(Solution().maxArea(height2)) # 1
print(Solution().maxArea(height3)) # 500
