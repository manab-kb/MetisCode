# https://leetcode.com/problems/counting-bits/?envType=study-plan-v2&envId=leetcode-75

"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        result = [0] * (n+1)

        for i in range(1, n+1):
            if i % 2 == 0:
                result[i] = result[i >> 1]
            else:
                result[i] = result[i - 1] + 1

        return result

print(Solution().countBits(2))
print(Solution().countBits(5))