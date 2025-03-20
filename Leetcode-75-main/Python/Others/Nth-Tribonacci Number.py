# https://leetcode.com/problems/n-th-tribonacci-number/description/?envType=study-plan-v2&envId=leetcode-75

"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        
        t0, t1, t2 = 0, 1, 1
        
        for i in range(0, n - 2):
            tn =  t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = tn
            
        return t2