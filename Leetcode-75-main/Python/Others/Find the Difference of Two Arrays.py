# https://leetcode.com/problems/find-the-difference-of-two-arrays/?envType=study-plan-v2&envId=leetcode-75

"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
	•	answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
	•	answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
"""

from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        result = [[], []]
        for n in set1:
            if n not in set2:
                result[0].append(n)
                
        for n in set2:
            if n not in set1:
                result[1].append(n)
                
        return result
    
print(Solution().findDifference([1,2,3], [2,4,6]))