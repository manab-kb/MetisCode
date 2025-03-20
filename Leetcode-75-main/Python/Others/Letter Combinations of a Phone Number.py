# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=leetcode-75

"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dict = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        
        result = []
        
        for digit in digits:
            dInt = int(digit)
            
            if not result:
                result = dict[dInt]
            else:
                temp = []
                
                for c in dict[dInt]:
                    for str in result:
                        temp.append(str + c)
                    
                
                result = temp
            
        return result