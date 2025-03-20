# // https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&envId=leetcode-75

# /*
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
# */

from typing import List 

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        max_ones  = 0
        zeros = 0

        while right < len(nums):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_ones = max(max_ones, right - left + 1)

            right += 1


        return max_ones