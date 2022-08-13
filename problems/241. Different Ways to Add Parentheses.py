
"""
Reference: https://youtu.be/r2wZUlt2wJo
"""
from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        def dfs(left, right):
            ## base case:
            if left == right:
                dp[left][right] = [digt[left]]
                return
            ## if encountered before
            if dp[left][right]:
                return 
            
            ## recurseion
            for i in range(left, right):
                dfs(left, i)
                dfs(i+1, right)
                leftnum = dp[left][i]
                rightnum = dp[i+1][right]
                for lef in leftnum:
                    for rig in rightnum:
                        op = oper[i]
                        if op == '+':
                            dp[left][right].append(lef + rig)
                        elif op == '-':
                            dp[left][right].append(lef - rig)
                        else: #'*'
                            dp[left][right].append(lef * rig)
        
        
        ## split expression into numbers and operators
        ## Do it again using regular expression
        i = 0
        digt = []
        oper = []
        n = len(expression)
        while i < n:
            j = i
            while j < n and expression[j].isdigit():
                j += 1
            digt.append(int(expression[i:j]))
            if j < n:
                oper.append(expression[j])
            i = j + 1

        ## dp[i][j]: list of results between expression[i][j]
        dp = [[[] for _ in range(n)] for _ in range(n)]
        dfs(0, len(digt)-1)

        return dp[0][len(digt)-1]
            
        
if __name__ == '__main__':
    expression = "2-1-1" #"2*3-4*5"
    rst = Solution().diffWaysToCompute(expression)
    print(rst)