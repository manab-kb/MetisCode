# https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75

"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        if str1 + str2 != str2 + str1:
            return ""

        def gcd(n1, n2):
            r = n1 % n2
            if r == 0:
                return n2
            else:
                return gcd(n2, r)
        
        idx = gcd(len(str1), len(str2))
        return str1[:idx]

sol = Solution()
print(sol.gcdOfStrings("ABCABC", "ABC"))
print(sol.gcdOfStrings("ABABAB", "ABAB"))
print(sol.gcdOfStrings("LEET", "CODE"))