
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rst = 0
        M = len(matrix)
        N = len(matrix[0])
        dp = [[0 for _ in range(N)] for _ in range(M)]
        
        for c in range(N):
            if matrix[0][c] == '1':
                dp[0][c] = 1
                rst = max(rst, dp[0][c])
        
        for r in range(M):
            if matrix[r][0] == '1':
                dp[r][0] = 1
                rst = max(rst, dp[r][0])  
        
        
        for r in range(1, M):
            for c in range(1, N):
                if matrix[r][c] == '1':
                    dp[r][c] = min(dp[r-1][c], dp[r-1][c-1], dp[r][c-1]) + 1
                    rst = max(rst, dp[r][c])
        
        
        return rst * rst

"""
Memorize the equation (trick)
dp[r][c] = min(dp[r-1][c], dp[r-1][c-1], dp[r][c-1]) + 1
"""