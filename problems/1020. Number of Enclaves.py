from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        #return self.method1(grid)
        return self.method2(grid)
        
    def method1(self, grid):
        """
        DFS.
        Mark cell with value 1 and reachable from borders to -1.
        After BFS, the cells with value 1 are rst.
        """
        def dfs(row, col):
            ## base case 1:
            if row < 0 or row == m or col < 0 or col == n:
                return

            ## base case 2:
            if grid[row][col] == 0 or grid[row][col] == -1:
                return
            
            grid[row][col] = -1
            for dr, dc in dirs:
                 dfs(row+dr, col+dc)
            
        m = len(grid)
        n = len(grid[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        
        ## top row and bottom row
        for col in range(n):
            if grid[0][col] == 1:
                dfs(0, col)
            if grid[m-1][col] == 1:
                dfs(m-1, col)
        ## first and last column
        for row in range(m):
            if grid[row][0] == 1:
                dfs(row, 0)
            if grid[row][n-1] == 1:
                dfs(row, n-1)
        rst = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    rst +=  1  

        return rst
    
    def method2(self, grid):
        """
        BFS. Mark cell with value 1 and reachable from borders to -1.
        After BFS, the cells with value 1 are rst.
        """
        from collections import deque
        m = len(grid)
        n = len(grid[0])
        dq = deque()
        ## add island at the border to the queue
        ## first row and last row
        for col in range(n):
            if grid[0][col] == 1:
                dq.append((0, col))
                grid[0][col] = -1
            if grid[m-1][col] == 1:
                dq.append((m-1, col))
                grid[m-1][col] = -1
        ## first column and last column
        for row in range(m):
            if grid[row][0] == 1:
                dq.append((row, 0))
                grid[row][0] = -1
            if grid[row][n-1] == 1:
                dq.append((row, n-1))
                grid[row][n-1] = -1
        
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        while dq:
            for _ in range(len(dq)):
                row, col = dq.popleft()
                for dr, dc in dirs:
                    if 0 <= row + dr < m and 0 <= col + dc < n:
                        if grid[row+dr][col+dc] == 1:
                            ## make sure to change the label here, because this cell may
                            ## be multiple nodes' neighbor so it may be added into the
                            ## queue multiple times.
                            grid[row+dr][col+dc] = -1
                            dq.append((row+dr, col+dc))
                    
        rst = 0 
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    rst += 1
        return rst
        
        
        

if __name__ == '__main__':
    grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    rst = Solution().numEnclaves(grid)
    print(rst)
        