import copy
from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        M = len(matrix)
        N = len(matrix[0])
        dirs = [(1, -1), (1, 0), (1, 1)]
        #dp = [[0 for _ in range(N)] for _ in range(M)]
        dp = copy.deepcopy(matrix)
        ## If there is only one row
        if M == 1:
            return max(matrix[0])
        for r in range(M-2, -1, -1):
            for c in range(0, N):
                minv = float('inf')
                for d in dirs:
                    dr, dc = d
                    if self.isvalid(r + dr, c + dc, M, N):
                        tem = dp[r + dr][c + dc] + matrix[r][c]
                    else:
                        tem = float('inf')
                    minv = min(minv, tem)
                dp[r][c] = minv
                    
        
        
        print(dp)
        return min(dp[0])
    
    def isvalid(self, r, c, M, N):
        if 0 <= r < M and 0 <= c < N:
            return True
        else:
            return False