

from collections import deque

class Solution(object):

    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.island = set() #[[False for _ in N] for _ in M]
        self.find_island(grid)
        return self.bfs(grid)
    
    def bfs(self, grid):
        dq = deque() ## Enter from right and leve from left
        for node in self.island:
            dq.append(node)
            

        water_seen = set()
        rst = 0
        
        while dq:
            num = len(dq)
            for _ in range(num):
                node = dq.popleft()
                i = node[0]
                j = node[1]
                
                for dir in self.dirs:
                    di = dir[0]
                    dj = dir[1]
                    new_i = i + di
                    new_j = j + dj
                    
                    if self.valid(grid, new_i, new_j):
                        if grid[new_i][new_j] == 1 and (new_i, new_j) not in self.island:
                            return rst
                        else:
                            if (new_i, new_j) not in water_seen:
                                dq.append((new_i, new_j))
                                water_seen.add((new_i, new_j))
                            
       
            rst += 1
            
        return rst
        
        
        
    def find_island(self, grid):
        """
        use dfs to find an island
        """
        
        M = len(grid)
        N = len(grid[0])
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)
                    #print(self.island)
                    return
                    
    def dfs(self, grid, row, col):
        ## Base case
        valid = self.valid(grid, row, col)
        if not valid or grid[row][col] == 0 or (row, col) in self.island:
            return
        
        self.island.add((row, col))
        
        for dir in self.dirs:
            self.dfs(grid, row+dir[0], col+dir[1])
        
    
    def valid(self, grid, row, col):
        M = len(grid)
        N = len(grid[0])
        return row >=0 and row < M and col >=0 and col < N
        
if __name__ == '__main__':
    s = Solution()
    grid = [[0,1,0],[0,0,0],[0,0,1]]
    #grid = [[0,1],[1,0]]
    print(s.shortestBridge(grid))

                        
        
                        
                                
                            
                    