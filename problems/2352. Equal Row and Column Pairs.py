from typing import List     
import collections
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = collections.defaultdict(int)
        n = len(grid)
        rst = 0
        for r in range(n):
            counter[tuple(grid[r])] += 1
        
        col = [0] * n
        for c in range(n):
            for r in range(n):
                col[r] = grid[r][c]
            
            rst += counter[tuple(col)]
        return rst