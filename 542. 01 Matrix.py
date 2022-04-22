# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:47:07 2020

@author: wyue
"""

class Solution:
    def updateMatrix(self, matrix):
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
        
matrix = [[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]

print(Solution().updateMatrix(matrix))