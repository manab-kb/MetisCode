# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=study-plan-v2&envId=leetcode-75

"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
"""

from typing import List 

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right, max_len, zeros = 0, 0, 0, 0
        
        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
                
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
                
            max_len = max(max_len, right - left)
            right += 1
            
        return max_len