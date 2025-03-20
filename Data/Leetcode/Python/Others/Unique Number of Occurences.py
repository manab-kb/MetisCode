# https://leetcode.com/problems/unique-number-of-occurrences/?envType=study-plan-v2&envId=leetcode-75

"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
"""

from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = {}

        for a in arr:
            if a in dict:
                dict[a] += 1
            else:
                dict[a] = 1

        return len(dict.values()) == len(set(dict.values()))
        

print(Solution().uniqueOccurrences([1,2,2,1,1,3]))