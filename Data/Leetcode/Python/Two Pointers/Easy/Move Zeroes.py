# https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75

"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nonZeroIdx = 0

        for currIdx in range(len(nums)):
            if nums[currIdx] != 0:
                nums[currIdx], nums[nonZeroIdx] = nums[nonZeroIdx], nums[currIdx]
                nonZeroIdx += 1

sol = Solution()
nums = [0,1,0,3,12]
sol.moveZeroes(nums)
print(nums)