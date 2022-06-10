from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        return self.method1(grid)
        
        
    def method1(self, grid):
        """
        dfs
        """
        self.dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        ROW = len(grid)
        COL = len(grid[0])
        
        ## state matrix: 0: not reachable, 1: reachable
        state = [[0 for _ in range(COL)] for _ in range(ROW)]
        
        ## Top row:
        for col in range(COL):
            if grid[0][col]:
                self.dfs(grid, state, 0, col, ROW, COL)
        ## Bottom row:
        for col in range(COL):
            if grid[ROW - 1][col]:
                self.dfs(grid, state, ROW - 1, col, ROW, COL) 
                
        ## Left column:
        for row in range(ROW):
            if grid[row][0]:
                self.dfs(grid, state, row, 0, ROW, COL)
                
        ## Right column:
        for row in range(ROW):
            if grid[row][COL - 1]:
                self.dfs(grid, state, row, COL - 1, ROW, COL)
                
        rst = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] and state[r][c] == 0:
                    rst += 1
        return rst
        
    def dfs(self, grid, state, i, j, ROW, COL):
        ## Base case:
        if state[i][j]:
            return
        state[i][j] = 1
        for dr, dc in self.dirs:
            row = i + dr
            col = j + dc
            if 0 <= row < ROW and 0 <= col < COL and grid[row][col]:
                self.dfs(grid, state, row, col, ROW, COL)


if __name__ == '__main__':
    grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    rst = Solution().numEnclaves(grid)
    print(rst)
        