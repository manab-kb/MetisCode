# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        s = list(s)
        t = list(t)
        
        for c in t:
            if i == len(s):
                break

            if s[i] == c:
                i += 1

        return i == len(s)
    
print(Solution().isSubsequence("abc", "ahbgdc"))
print(Solution().isSubsequence("axc", "ahbgdc"))