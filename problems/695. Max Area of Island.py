
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.rst = 0
        
        visited = [[False for _ in range(n)] for _ in range(m)]
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(row, col):
            ## base case: visited
            if visited[row][col]:
                return
            visited[row][col] = True
            
            self.cur += 1
            self.rst = max(self.rst, self.cur)
            
            for dr, dc in dirs:
                if 0 <= row + dr < m and 0 <= col + dc < n:
                    if grid[row+dr][col+dc] == 1:
                        dfs(row+dr, col+dc)
        
        
        for row in range(m):
            for col in range(n):
                if grid[row][col]:
                    self.cur = 0
                    dfs(row, col)

        return self.rst

if __name__ == "__main__":
    grid = [[1,0,1],[1,1,1],[0,0,1]]
    rst = Solution().maxAreaOfIsland(grid)
    print(rst)
