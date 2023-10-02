from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Method 1: DFS
        """
        def dfs(row, col):
            """
            grid[row, col] is 1. Starting form here,
            flip all the connected island to -1.
            """
            if grid[row][col] != '1':
                return
            grid[row][col] = '-1'
            for dr, dc in dirs:
                if 0 <= row + dr < m and 0 <= col + dc < n:
                    dfs(row+dr, col+dc)

        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        m = len(grid)
        n = len(grid[0])
        rst = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    rst += 1
                    dfs(r, c) 

        return rst
        """
        Method 2: Stack
        """
        m = len(grid)
        n = len(grid[0])
        stack = []
        rst = 0
        found = False
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    rst += 1
                    stack.append((r, c))
                    while stack:
                        row, col = stack.pop()
                        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                            if 0 <= row+dr < m and 0 <= col + dc < n and grid[row+dr][col+dc] == '1':
                                grid[row+dr][col+dc] = '-1'
                                stack.append((row+dr, col+dc))

        return rst


if __name__ == '__main__':

    s = Solution()

    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    print(s.numIslands(grid))