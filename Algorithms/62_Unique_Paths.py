# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 22:58:06 2020

@author: wyue
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        ## boundary conditions
        # last col
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][n-1] = 1
        # last row
        for i in range(n):
            dp[m-1][i] = 1
        for row in range(m-2, -1, -1):
            for col in range(n-2, -1, -1):
                dp[row][col] = dp[row+1][col] + dp[row][col+1]
        return dp[0][0]

print(Solution().uniquePaths(3,7))