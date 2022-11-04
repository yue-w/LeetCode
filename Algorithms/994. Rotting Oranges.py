from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        return self.method1(grid)
    
    def method1(self, grid):
        """
        BFS
        record the time grid[i][j] became rotten in grid
        """
        M = len(grid)
        N = len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        dq  = deque() ## enter from right, leave from left
        
        ## Add the rotten oranges into the queue
        for row in range(M):
            for col in range(N):
                if grid[row][col] == 2:
                    dq.append((row, col))
                    grid[row][col] = -1
        
        ## time it takes for the orange at grid[i][j] got rotten is -(-grid[i][j] + 1)
        ## for example grid[0][0] = -1 means grid[0][0] is rotten at the begining
        while dq:
            for _ in range(len(dq)):
                row, col = dq.popleft()
                for dr, dc in dirs:
                    ## if inside of the grid
                    if 0 <=  row + dr < M and 0 <= col + dc < N:
                        ## if no orange
                        if grid[row + dr][col + dc] == 0:
                            continue
                        ## if good orange
                        if grid[row + dr][col + dc] == 1:
                            grid[row + dr][col + dc] = grid[row][col] - 1
                            dq.append((row + dr, col + dc))
                        ## if bad orange, update the time if necessary
                        else: # grid[row + dr][col + dc] < 0
                            if grid[row + dr][col + dc] < grid[row][col] - 1:
                                grid[row + dr][col + dc] = grid[row][col] - 1
                                dq.append((row + dr, col + dc))
        rst = -1
        
        for row in range(M):
            for col in range(N):
                if grid[row][col] == 1:
                    return -1
                rst = min(rst, grid[row][col])
        return - (rst + 1)
                            
                        
if __name__ == '__main__':
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    rst = Solution().orangesRotting(grid)
    print(rst)
        