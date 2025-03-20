# https://leetcode.com/problems/equal-row-and-column-pairs/?envType=study-plan-v2&envId=leetcode-75

"""Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
"""

from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        equal_pairs = 0
        
        for i in range(n):
            for j in range(n):
                
                is_equal = True
                for k in range(n):
                    if grid[i][k] != grid[k][j]:
                        is_equal = False
                        break
                    
                if is_equal:
                    equal_pairs += 1
                    
        return equal_pairs