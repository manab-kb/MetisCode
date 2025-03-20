# https://leetcode.com/problems/decode-string/?envType=study-plan-v2&envId=leetcode-75

"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105
"""

class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        
        curr_num = 0
        curr_str = ""
        
        for c in s:
            if c == '[':
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif c == ']':
                s, n = stack.pop()
                
                curr_str = s + n * curr_str
            elif c.isdigit():
                curr_num = curr_num * 10 + int(c)
            else:
                curr_str += c
                
        return curr_str