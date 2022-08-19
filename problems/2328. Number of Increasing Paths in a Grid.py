

from typing import List

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        """
        DFS + memo
        Time: O(MN)
        """
        def dfs(currow, curcol):
            if count[currow][curcol]:
                return
            count[currow][curcol] = 1
            
            for dr, dc in dirs:
                row = currow + dr
                col = curcol + dc
                if 0 <= row < M and 0 <= col < N:
                    if grid[row][col] > grid[currow][curcol]:
                        dfs(row, col)
                        count[currow][curcol] += count[row][col]
            
        
        M = len(grid)
        N = len(grid[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        count = [[0 for _ in range(N)] for _ in range(M)]
        
        for row in range(M):
            for col in range(N):
                dfs(row, col)
        rst = sum(sum(count[i]) for i in range(M))
        return rst % (10**9+7)