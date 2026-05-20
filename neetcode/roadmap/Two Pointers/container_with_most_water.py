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

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        return 0