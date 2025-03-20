# https://leetcode.com/problems/non-overlapping-intervals/?envType=study-plan-v2&envId=leetcode-75

"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum
number of intervals you need to remove to make the rest of the intervals non-overlapping.
"""

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        
        end = intervals[0][1]
        counter = 0
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                counter += 1
            else:
                end = intervals[i][1]
                
        return counter