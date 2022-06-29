
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        dp[i][j]: the area of the rectangle with the bottom right at (i, j)
        Transition function: 
            if matrix[i][j] == 0, then dp[i][j] = 0
            if matrix[i][j] == 1, then dp[i][j] = min(dp[r-1][c], dp[r-1][c-1], dp[r][c-1]) + 1
        Reference: https://www.youtube.com/watch?v=eg6g6cNvsTs
        """
        
        rst = 0
        M = len(matrix)
        N = len(matrix[0])
        dp = [[0 for _ in range(N)] for _ in range(M)]
        
        ## set boundary
        for c in range(N):
            if matrix[0][c] == '1':
                dp[0][c] = 1
                rst = max(rst, dp[0][c])
        ## set boundary
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