# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 22:58:06 2020

@author: wyue
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==1 or n==1:
            return 1
        row = [0]*n
        table = [row]*m
        
        table[m-1][:] = [1] * n
        for i in range(m):
            table[i][n-1] = 1
        
        for r in range(2, m+1):
            for c in range(2, n+1):
                table[-r][-c] = table[-r+1][-c] + table[-r][-c+1]
        
        
        
        return table[0][0]

print(Solution().uniquePaths(3,7))