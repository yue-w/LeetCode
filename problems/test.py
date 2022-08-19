
#%%
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        def dfs(row, col):
            ## base case: if already visited
            if memo[row][col]:
                return 
            memo[row][col] = 1
            
            maxnxt = 0
            for dr, dc in dirs:
                newrow = row + dr
                newcol = col + dc
                if 0 <= newrow < M and 0 <= newcol < N:
                    if matrix[newrow][newcol] > matrix[row][col]:

                        dfs(newrow, newcol)
                        maxnxt = max(maxnxt, memo[newrow][newcol])
            memo[row][col] += maxnxt
            
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        
        M = len(matrix)
        N = len(matrix[0])
        memo = [[0 for _ in range(N)] for _ in range(M)]
        for row in range(M):
            for col in range(N):
                dfs(row, col)
        
        rst = max(max(memo[r]) for r in range(M))
        print(memo)
        
        return rst

matrix = [[9,9,4],[6,6,8],[2,1,1]]
rst = Solution().longestIncreasingPath(matrix)
print(rst)