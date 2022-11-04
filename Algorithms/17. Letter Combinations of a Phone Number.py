
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
        def dfs(index):
            ## base case
            if index == len(digits):
                rst.append(''.join(curr))
                return
            for char in self.dic[digits[index]]:
                curr.append(char)
                dfs(index+1)
                ## backtracking
                curr.pop()
            
        dfs(0)
        
        return rst
            
            
        