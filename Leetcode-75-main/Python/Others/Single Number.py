# https://leetcode.com/problems/single-number/?envType=study-plan-v2&envId=leetcode-75

"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for n in nums:
            result ^= n

        return result
    
print(Solution().singleNumber([2, 2, 1]))
print(Solution().singleNumber([4,1,2,1,2]))