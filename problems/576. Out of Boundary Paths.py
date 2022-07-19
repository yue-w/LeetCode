

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        return self.method1(m, n, maxMove, startRow, startColumn)
    
    
    def method1(self, m, n, maxMove, startRow, startColumn):
        """
        DFS. Memo.
        """
        if maxMove == 0:
            return 0
        self.rst = 0
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        memo = {}
        
        def dfs(row, col, moves):
            ## base case
            if row == -1 or row == m or col == -1 or col == n:
                self.rst += 1
                return 1
            if moves == 0:
                return 0
            if (row, col, moves) in memo:
                return memo[(row, col, moves)]



            tem = 0
            for dr, dc in dirs:
                tem += dfs(row+dr, col+dc, moves - 1)
            memo[row, col, moves] = tem
            return tem
                    
        dfs(startRow, startColumn, maxMove)
        return memo[(startRow, startColumn, maxMove)]
     
                

if __name__ == '__main__':
    m = 7
    n = 6
    maxMove = 13
    startRow = 0
    startColumn = 2

    # m = 1
    # n = 3
    # maxMove = 3
    # startRow = 0
    # startColumn = 1
    rst = Solution().findPaths(m, n, maxMove, startRow, startColumn)
    print(rst)