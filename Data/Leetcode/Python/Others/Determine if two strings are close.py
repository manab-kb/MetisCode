# https://leetcode.com/problems/determine-if-two-strings-are-close/?envType=study-plan-v2&envId=leetcode-75

"""
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
"""

# Using dictionary

from typing import List

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1 = {}
        dict2 = {}

        for char in word1:
            if char not in dict1:
                dict1[char] = 1
            else:
                dict1[char] += 1

        for char in word2:
            if char not in dict2:
                dict2[char] = 1
            else:
                dict2[char] += 1

        if dict1.keys() != dict2.keys():
            return False
        
        if sorted(dict1.values()) == sorted(dict2.values()):
            return True
        
        return False
    

# Using Counter

from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)

        return set(count1.keys()) == set(count2.keys()) and sorted(count1.values()) == sorted(count2.values())

    

solution = Solution()
print(solution.closeStrings("abc", "bca"));  # True
print(solution.closeStrings("abc", "bac"));   # Frue
print(solution.closeStrings("aabbcc", "ccbbdd"));  # False