# https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75


"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""


"""
# runtime: 19ms
def mergeAlternately(word1, word2):
    result = ""

    i = 0
    j = 0

    while i < len(word1) or j < len(word2):
        if i < len(word1):
            result += word1[i]
            i += 1
        
        if j < len(word2):
            result += word2[j]
            j += 1

    return result
"""



# runtime: 10ms
def mergeAlternately(word1, word2):
    result = []
    i, j = 0, 0

    while i < len(word1) or j < len(word2):
        if i < len(word1):
            result.append(word1[i])
            i += 1
        
        if j < len(word2):
            result.append(word2[j])
            j += 1

    return ''.join(result)

print(mergeAlternately("abc", "pqr"))
print(mergeAlternately("ab", "pqrs"))
