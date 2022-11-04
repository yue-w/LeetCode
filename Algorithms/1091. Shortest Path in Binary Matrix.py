
from collections import deque
from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        steps = 0
        
        dq = deque()
        dq.append((0,0))
        visited = [[False for _ in range(n)] for _ in range(n)]
        while dq:
            steps += 1
            for _ in range(len(dq)):
                r, c = dq.popleft()
                visited[r][c] = True
                if r == n - 1 and c == n - 1:
                    return steps
                for dr, dc in dirs:
                    ## in the grid
                    if 0 <= r + dr < n and 0 <= c + dc < n and not visited[r + dr][c + dc]:
                        if grid[r+dr][c+dc] == 0:
                            dq.append((r+dr, c+dc))
                
        
        return -1

if __name__ == '__main__':
    grid = [[0,1,1,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],
    [0,0,0,1,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]]
    rst = Solution().shortestPathBinaryMatrix(grid)
    print(rst)