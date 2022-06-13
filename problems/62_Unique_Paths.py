# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 22:58:06 2020

@author: wyue
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 or n==1:
            return 1

        table = [[0 for _ in range(n)] for _ in range(m)]
        
        ## The last row has only 1 method: move right
        table[m-1][:] = [1] * n
        
        ## The last column has only 1 method: movre down
        for i in range(m):
            table[i][n-1] = 1
        
        ## Botton up
        for r in range(2, m+1):
            for c in range(2, n+1):
                table[-r][-c] = table[-r+1][-c] + table[-r][-c+1]
        
        
        
        return table[0][0]

print(Solution().uniquePaths(3,7))