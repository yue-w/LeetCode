class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        """
        DFS, memoization.
        """
        dirs = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2) ]
        def dfs(cur_p, row, col, cur_steps):
            ## base case:
            if cur_steps == k:
                memo[(row, col, cur_steps)] = cur_p
                return cur_p
                return
            if (row, col, cur_steps) in memo:
                return memo[(row, col, cur_steps)] 
                
            temp = 0
            for dr, dc in dirs:
                if row + dr < 0 or row + dr >=n or col + dc < 0 or col + dc >= n:
                    continue 
                temp += dfs(1/8*cur_p, row+dr, col+dc, cur_steps+1)
            memo[(row, col, cur_steps)] = temp
            return temp

        memo = {}
        return dfs(1, row, column, 0)

            