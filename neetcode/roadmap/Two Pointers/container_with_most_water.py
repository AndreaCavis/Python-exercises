# I already know this problem is thought, probably have to inform myself about it. 
# I remember seeing the execution of this algorithm on python alchemist. Yeah, here it is:
# https://www.pythonalchemist.com/blog/trapping-rain-water
#  ok, let's dig it

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

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        n = len(heights) - 1
        l, r = 0, n
        max_area = float("-inf")

        while l < r:
            height = min(height[l], height[r])
            length = r - l
            curr_area = height * length
            max_area = max(curr_area, max_area)



        return 0