
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        rst = []
        curr = []
        self.recursion(rst, curr, 0, digits)
        return rst
        
    def recursion(self, rst, curr, index, digits):
        ## Base case
        if len(curr) == len(digits):
            rst.append(''.join(curr[:]))
        
        ## recursion
        for i in range(index, len(digits)):
            chars = self.dic[digits[i]]
            for char in chars:
                curr.append(char)
                self.recursion(rst, curr, i+1, digits)
                ## Recover state
                curr.pop()
            
            
        