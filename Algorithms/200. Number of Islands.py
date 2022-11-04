

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        rst = 0
        if not grid:
            return rst
        
        M = len(grid)
        N = len(grid[0])

        self.visited = [[False for _ in range(N)] for _ in range(M)]
        
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for i in range(M):
            for j in range(N):
                if not self.visited[i][j]:
                    if grid[i][j] == '1':
                        self.dfs(grid, i, j)
                        rst += 1
                        self.visited[i][j] = True
        
        return rst
                
        
    def dfs(self, grid, row, col):
        """
        find all the 1 that are reachable from grid[row][col], mark them as visited
        """
        ## Base case 0 or out of matrix
        if not self.valid(grid, row, col) or grid[row][col] == '0'  or self.visited[row][col]:
            return 
        
        ## Mark the node as visited
        if grid[row][col] == '1':
            self.visited[row][col] = 1
        ## search dfs
        for dir in self.dirs:
            self.dfs(grid, row + dir[0], col + dir[1])
        
        
    def valid(self, grid, row, col):
        M = len(grid)
        N = len(grid[0])
        return row >= 0 and row < M and col >= 0 and col < N 



if __name__ == '__main__':

    s = Solution()

    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    print(s.numIslands(grid))