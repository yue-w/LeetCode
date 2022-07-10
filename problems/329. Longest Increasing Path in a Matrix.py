from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        return self.method1(matrix)
    
    def method1(self, matrix):
        """
        DFS with memo
        """
        self.rst = 1
        M = len(matrix)
        N = len(matrix[0])
        memo = [[None for _ in range(N)] for _ in range(M)]
        for row in range(M):
            for col in range(N):
                self.dfs(matrix, row, col, memo,M,N)
        return self.rst
        
    def dfs(self, matrix, row, col, memo,M,N):
        ## base case: no neighbour is larger than this cell
        if not self.has_larger(matrix, row, col):
            memo[row][col] = 1
            return 1
        if memo[row][col] is not None:
            return memo[row][col]
        temv = float('-inf')
        for dr, dc in [(-1, 0),(1, 0),(0, -1),(0, 1)]:
            if 0 <= row + dr < M and 0 <= col + dc < N:
                if matrix[row+dr][col+dc] > matrix[row][col]:
                    nxt_temv = self.dfs(matrix, row+dr, col+dc, memo,M,N)
                    temv = max(temv, nxt_temv) 
        memo[row][col] = 1 + temv
        self.rst = max(self.rst, 1 + temv)
        return 1 + temv
        
        
    def has_larger(self, matrix, row, col):
        M = len(matrix)
        N = len(matrix[0])
        for dr, dc in [(-1, 0),(1, 0),(0, -1),(0, 1)]:
            if 0 <= row + dr < M and 0 <= col + dc < N:
                if matrix[row][col] < matrix[row + dr][col + dc]:
                    return True
            
        return False
        
if __name__ == '__main__':
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    #matrix = [[3,4,5],[3,2,6],[2,2,1]]
    rst = Solution().longestIncreasingPath(matrix)
    print(rst)