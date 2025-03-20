# https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75

"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1
        vowels = set('aeiouAEIOU')

        while left < right:
            left_vowel = s[left] in vowels
            right_vowel = s[right] in vowels

            if left_vowel and right_vowel:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif left_vowel:
                right -= 1
            elif right_vowel:
                left += 1
            else:
                left += 1
                right -= 1

        return ''.join(s)

sol = Solution()
print(sol.reverseVowels("hello"))
print(sol.reverseVowels("leetcode"))