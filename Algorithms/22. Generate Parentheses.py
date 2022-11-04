
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        rst = []
        curr = []
        self.dfs(0, 0, n, rst, curr)
        
        return rst
    
    def dfs(self, left, right, n, rst, curr):
        """
        left: number of "(" has been used
        right: number of ")" has been used
        """
        ## Base case
        if left == n and right == n:
            rst.append(''.join(curr))
            return
        
        ## add "("
        if left < n:
            curr.append('(') 
            self.dfs(left + 1, right, n, rst, curr)
            ## recover state
            curr.pop()
        
        ## add ")"
        if right < left:
            curr.append(')')
            self.dfs(left, right + 1, n, rst, curr)
            ## recover state
            curr.pop()
            
            
if __name__ == '__main__':
    s = Solution()
    n = 3

    print(s.generateParenthesis(n))