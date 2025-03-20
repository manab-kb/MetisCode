# https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75

"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
"""

# Sliding window approach

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        n = len(nums)

        for i in range(n - k):
            window_sum = window_sum - nums[i] + nums[i + k]
            max_sum = max(window_sum, max_sum)

        return max_sum / k

print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))
print(Solution().findMaxAverage([5], 1))