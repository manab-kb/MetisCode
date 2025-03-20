# https://leetcode.com/problems/longest-common-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

""" 
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        gridDP = [[0 for _ in range(len(text2) + 1)]
                  for _ in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    gridDP[i][j] = 1 + gridDP[i-1][j-1]
                else:
                    gridDP[i][j] = max(gridDP[i][j-1], gridDP[i-1][j])

        return gridDP[-1][-1]
