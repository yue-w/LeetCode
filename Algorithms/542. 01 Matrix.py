# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:47:07 2020

@author: wyue
"""
from collections import deque
class Solution:
    def updateMatrix(self, mat):


        return self.bfs(mat)
    
    
    def bfs(self, matrix):
        """
        Time: O(mn)
        Space: O(mn)
        """
        m = len(matrix)
        n = len(matrix[0])
        rst = [[float('inf') for _ in range(n)] for _ in range(m)]
        seen = [[False for _ in range(n)] for _ in range(m)]
        dq = deque() ## Always enter from right and leave from left
        ## find a cell with 0 value

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rst[i][j] = 0
                    dq.append((i, j))
                    seen[i][j] = True


        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                row, col = node
                
                if matrix[row][col] == 0:
                    rst[row][col] = 0
                
                ## Add neighbors into queue, also compare value
                for dir in dirs:
                    row_new = row + dir[0]
                    col_new = col + dir[1]
                ## if within the boundary
                    if row_new >= 0 and row_new < m and col_new >=0 and col_new < n:
                        rst[row][col] = min(rst[row][col], rst[row_new][col_new] + 1)
                        if not seen[row_new][col_new]:
                            dq.append((row_new, col_new))
                            seen[row_new][col_new] = True
                
                
        return rst


        ## DP
        #visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        rst = [[float('inf') for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        ## Set distance = 0 for all the zeros
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rst[i][j] = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                #self.helper_leftup(rst, i,j, len(matrix), len(matrix[0]))
                if i==0:
                    up = float('inf')
                else:
                    up = 1 + rst[i-1][j]
                if j == 0:
                    left = float('inf')
                else:
                    left = 1 + rst[i][j-1]
                rst[i][j] = min([up, left, rst[i][j]])

        m = len(matrix)
        n = len(matrix[0])
        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix[0])-1, -1, -1):
                #self.helper_rightdown(rst, i,j, len(matrix), len(matrix[0]))
                if i==m-1:
                    down = float('inf')
                else:
                    down = 1 + rst[i+1][j]
        
                if j == n-1:
                    right = float('inf')
                else:
                    right = 1 + rst[i][j+1] 
                rst[i][j] = min([right, down, rst[i][j]])
        return rst
        
#matrix = [[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]
matrix = [[0,0,0],[0,1,0],[0,0,0]]
print(Solution().updateMatrix(matrix))