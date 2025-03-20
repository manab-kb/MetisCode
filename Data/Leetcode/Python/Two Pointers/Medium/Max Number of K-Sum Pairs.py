# https://leetcode.com/problems/max-number-of-k-sum-pairs/?envType=study-plan-v2&envId=leetcode-75

'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
'''

from typing import List

# Using dictionary
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dict = {}
        count = 0
        for num in nums:
            diff = k - num
            if diff in dict and dict[diff] > 0:
                count += 1
                dict[diff] -= 1
            else:
                if num not in dict:
                    dict[num] = 0
                dict[num] += 1
                
        return count
    
                
# Using two pointers
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        count = 0
        
        while left < right:
            sum = nums[left] + nums[right]
            if sum == k:
                count += 1
                left += 1
                right -= 1
            elif sum < k:
                left += 1
            else:
                right -= 1
                
        return count