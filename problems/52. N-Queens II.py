
"""
Same solution as 51.
"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(row):
            """
            only call this function if row, col are valid
            """
            ## base case
            if row == n:
                self.rst += 1
                return
            
            for c in range(n):
                if canput(row, c, curr):
                    curr[row][c] = 'Q'
                    dfs(row+1)
                    ## backtracking
                    curr[row][c] = '.'
        
        
        def canput(row, col, curr):
            """
            Return whether you can put a queen at row, col with curr position
            """
            ## check row
            for c in range(n):
                if c != col and curr[row][c] == 'Q':
                    return False
            ## check col
            for r in range(n):
                if r != row and curr[r][col] == 'Q':
                    return False
            ## check diagnal: upper left 
            ## go up
            r = row - 1
            c = col - 1
            while r >= 0 and c >= 0:
                if curr[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1
            
                
            ## check diagnal: upper right 
            ## go up
            r = row - 1
            c = col + 1
            while r >= 0 and c < n:
                if curr[r][c] == 'Q':
                    return False
                r -= 1
                c += 1
            
            return True
        
        self.rst = 0
        curr = [['.' for _ in range(n)] for _ in range(n)]
        dfs(0)
            
        return self.rst