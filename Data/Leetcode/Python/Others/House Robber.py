# https://leetcode.com/problems/house-robber/description/?envType=study-plan-v2&envId=leetcode-75

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)
            
        n = len(nums)
        dp = [0] * n
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
            
        return dp[-1]