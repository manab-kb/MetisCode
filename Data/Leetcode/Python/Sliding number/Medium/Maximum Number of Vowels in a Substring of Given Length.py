# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75

"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxVowelCount = 0
        currentCount = 0

        for i in range(0, k):
            currentCount += 1 if s[i] in "aeiou" else 0

        maxVowelCount = currentCount

        for i in range(k, len(s)):
            currentCount += 1 if s[i] in "aeiou" else 0

            currentCount -= 1 if s[i - k] in "aeiou" else 0

            maxVowelCount = max(maxVowelCount, currentCount)

        return maxVowelCount
