# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75

"""
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
"""


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []

        maxNum = max(candies)

        for c in candies:
            if c + extraCandies >= maxNum:
                result.append(True)
            else:
                result.append(False)

        return result

sol = Solution()
print(sol.kidsWithCandies([2,3,5,1,3], 3))
print(sol.kidsWithCandies([4,2,1,1,2], 1))
