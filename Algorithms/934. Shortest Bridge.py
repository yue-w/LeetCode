
from collections import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        Search problem.
        Shortest path -> BFS.
        """
        n = len(grid)
        """
        the state of the cell
        -1: island one, 1: island two (goal, if found, return),
        0: water (not visited), 2: water (visited) 
        """

        state = [[0 for _ in range(n)] for _ in range(n)]
        
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        
        ## define the dfs function that finds all cells of island one, mark them as -1
        def dfs(row, col):
            ## base case 1: water
            if grid[row][col] == 0 :
                return
            ## base case 2: island one:
            if state[row][col] == -1:
                return
            
            ## if island, mark it as -1
            ## explore neighbors
            state[row][col] = -1
            for dr, dc in dirs:
                if 0 <= row + dr < n and 0 <= col + dc < n:
                    dfs(row + dr, col + dc)
                    
        ## call dfs for a cell of island one
        found = False
        for row in range(n):
            if found:
                break
            for col in range(n):
                if grid[row][col] == 1:
                    dfs(row, col)
                    found = True
                    break
        
        dq = deque()
        #### add all cells from islend one into the queue
        for row in range(n):
            for col in range(n):
                if state[row][col] == -1:
                    dq.append((row, col))
                              
        rst = 0
        
        while dq:
            rst += 1
            for _ in range(len(dq)):
                row, col = dq.popleft()
                for dr, dc in dirs:
                    if 0 <= row+dr < n and 0 <= col+dc< n:
                        if state[row+dr][col+dc] == -1 or state[row+dr][col+dc] == 2:
                            continue
                        state[row+dr][col+dc] = 2
                        
                        ## if find a cell from island two, we did not have 
                        ## to flip it. rst - 1 and return
                        if grid[row+dr][col+dc] == 1:
                            return rst - 1
                        
                        dq.append((row+dr, col+dc))
        
if __name__ == '__main__':
    s = Solution()
    grid = [[0,1],[1,0]]
    #grid = [[0,1,0],[0,0,0],[0,0,1]]
    #grid = [[0,1],[1,0]]
    print(s.shortestBridge(grid))

                        
        
                        
                                
                            
                    