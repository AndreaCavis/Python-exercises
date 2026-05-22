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
        n = len(heights) - 1
        max_area = 0
        l, r = 0, n

        while l < r:
            height = min(heights[l], heights[r])
            length = r - l
            curr_area = height * length
            max_area = max(curr_area, max_area)
            # I KNEW THIS WAS THE APPROACH BUT I SECOND GUESSED MYSELF
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area



height = [1,7,2,5,4,7,3,6]
height2 = [1,2]
height3 = [1,7,2,5,12,3,500,500,7,8,4,7,3,6]

print(Solution().maxArea(height)) # 36
print(Solution().maxArea(height2)) # 1
print(Solution().maxArea(height3)) # 500