# https://leetcode.com/problems/number-of-provinces/?envType=study-plan-v2&envId=leetcode-75

"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        def dfs(city: int):
            visited[city] = True
            for neighbor, is_connected in enumerate(isConnected[city]):
                if is_connected and not visited[neighbor]:
                    dfs(neighbor)

        province_count = 0
        n = len(isConnected)
        visited = [False] * n

        for city in range(n):
            if not visited[city]:
                province_count += 1
                dfs(city)
        
        return province_count