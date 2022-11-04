from typing import List

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        M = len(mat)
        N = len(mat[0])
        
        # top row
        for col in range(N):
            c = col
            r = 0
            tem = []
            while c < N and r < M:
                tem.append(mat[r][c])
                c += 1
                r += 1
            tem.sort()
            c = col
            r = 0
            for i in range(len(tem)):
                mat[r][c] = tem[i]
                r += 1
                c += 1
            
        # first column
        for row in range(M):
            r = row
            c = 0
            tem = []
            while r < M and c < N:
                tem.append(mat[r][c])
                r += 1
                c += 1
            tem.sort()
            r = row
            c = 0
            for i in range(len(tem)):
                mat[r][c] = tem[i]
                r += 1
                c += 1
            
        
        return mat