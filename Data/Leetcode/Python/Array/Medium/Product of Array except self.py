# https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        
        left_product = 1
        for i in range(0, n):
            result[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]


        return result

print(Solution().productExceptSelf([1,2,3,4]))