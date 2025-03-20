# https://leetcode.com/problems/increasing-triplet-subsequence/?envType=study-plan-v2&envId=leetcode-75

"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
"""

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = float('inf')
        j = float('inf')

        for n in nums:
            if i >= n:
                i = n
            elif j >= n:
                j = n
            else:
                return True

        return False
