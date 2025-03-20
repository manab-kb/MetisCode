# https://leetcode.com/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-75

"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
"""

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                exploded = False
                
                while stack and stack[-1] > 0:
                    topAsteroid = stack.pop()
                    
                    if abs(topAsteroid) == abs(a):
                        exploded = True
                        break
                    elif abs(topAsteroid) > abs(a):
                        stack.append(topAsteroid)
                        exploded= True
                        break
                    
                if not exploded:
                    stack.append(a)
                    
        return stack