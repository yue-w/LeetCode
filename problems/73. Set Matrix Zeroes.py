from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M = len(matrix)
        N = len(matrix[0])
        r0 = 1
        for r in range(M):
            for c in range(N):
                if matrix[r][c] == 0:
                    if r == 0:
                        matrix[0][c] = 0
                        r0 = 0
                    else:
                        matrix[0][c] = 0
                        matrix[r][0] = 0
        
        ## zero out the columns other than the first column
        for c in range(1, N):
            if matrix[0][c] == 0:
                for r in range(M):
                    matrix[r][c] = 0
        
        ## zero out the rows other than the first column
        for r in range(1, M):
            if matrix[r][0] == 0:
                for c in range(N):
                    matrix[r][c] = 0
                    
        ## Back up fist element
        tem = matrix[0][0]
        ## First row 
        if r0 == 0:
            for c in range(N):
                matrix[0][c] = 0
        
        ## First column
        if tem == 0:
            for r in range(M):
                matrix[r][0] = 0