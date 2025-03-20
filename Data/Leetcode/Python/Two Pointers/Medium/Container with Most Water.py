# https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75


"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        low = 0
        high = len(height) - 1
        max_water = 0

        while low < high :
            min_height = min(height[low], height[high])

            width = high - low

            max_water = max(max_water, width * min_height)

            if height[low] < height[high]:
                low += 1
            else:
                high -= 1


        return max_water
    
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))