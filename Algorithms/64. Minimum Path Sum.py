from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        dp[m - 1][n - 1] = grid[m - 1][n - 1]
        
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row == m - 1 and col == n - 1:
                    continue
                if col + 1 < n:
                    right = dp[row][col + 1]
                else:
                    right = float('inf')
                if row + 1 < m:
                    below = dp[row + 1][col]
                else:
                    below = float('inf')
                dp[row][col] = grid[row][col] + min(below, right)
                
        return dp[0][0]
