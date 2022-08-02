from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        rst = []
        TOTAL = rows * cols
        steps = 0
        rst.append([rStart, cStart])
        row = rStart
        col = cStart 
        while len(rst) < TOTAL:
            ## right
            steps += 1
            for _ in range(steps):
                col += 1
                if 0 <= row < rows and 0 <= col < cols:
                    rst.append([row, col])
            ## down
            for _ in range(steps):
                row += 1
                if 0 <= row < rows and 0 <= col < cols:
                    rst.append([row, col])
            ## left
            steps += 1
            for _ in range(steps):
                col -= 1
                if 0 <= row < rows and 0 <= col < cols:
                    rst.append([row, col])
            ## up
            for _ in range(steps):
                row -= 1
                if 0 <= row < rows and 0 <= col < cols:
                    rst.append([row, col])
            
        return rst