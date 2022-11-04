from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights)
        COL = len(heights[0])
        ## A table to store whether can visit Pac
        pac = [[False for _ in range(COL)] for _ in range(ROW)]
        ## A table to stor whether can visit Alt
        alt = [[False for _ in range(COL)] for _ in range(ROW)]
        
        ## DFS for pacific ocean
        for c in range(COL):
            ## Search staring form first row (Pacific)
            self.dfs(heights, pac, heights[0][c], 0, c, ROW, COL)
            ## Search from last row (Altanic)
            self.dfs(heights, alt, heights[ROW - 1][c], ROW - 1, c, ROW, COL)

    
        ## DFS for Altanic ocean
        for r in range(ROW):
            ## Search starting from first column (Pacific)
            self.dfs(heights, pac, heights[r][0], r, 0, ROW, COL)
            ## Search from last column (Altanic)
            self.dfs(heights, alt, heights[r][COL - 1], r, COL - 1, ROW, COL)

        
        rst = []
        for r in range(ROW):
            for c in range(COL):
                if pac[r][c] and alt[r][c]:
                    rst.append([r, c])
                    
        return rst
        
        
    def dfs(self, heights, can_visit, pri_hei, r, c, ROW, COL):
        ## Base cases: can visit, height is lower, or index out of boundary 
        if r < 0 or r >= ROW or c < 0 or c >= COL or can_visit[r][c] or pri_hei > heights[r][c]:
            return
        
        ## this cell can be visited
        can_visit[r][c] = True
        
        ## Visit neighbors
        self.dfs(heights, can_visit, heights[r][c], r - 1, c, ROW, COL)
        self.dfs(heights, can_visit, heights[r][c], r + 1, c, ROW, COL)
        self.dfs(heights, can_visit, heights[r][c], r, c - 1, ROW, COL)
        self.dfs(heights, can_visit, heights[r][c], r, c + 1, ROW, COL)
        

if __name__ == '__main__':
    s = Solution()
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]


    print(s.pacificAtlantic(heights))