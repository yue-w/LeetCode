# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 11:12:06 2020

@author: wyue
https://leetcode.com/problems/maximal-network-rank/
"""

import heapq
class Solution(object):
    def maximalNetworkRank(self, n, roads):
        return self.method1(n, roads)
    def method1(self, n, roads):
        """
        preferred method.
        Time: O(n^2)
        Space: O(n^2)
        Clarification: the two city under consideration may not be connected.
        Matrix.
        """
        ## for each node count the edges connect to it.
        count = [0] * n
        ## use a matrix[i][j] to represent whether i and j are connected
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        for c1, c2 in roads:
            count[c1] += 1
            count[c2] += 1
            matrix[c1][c2] = 1
            matrix[c2][c1] = 1
        
        rst = 0
        
        for c1 in range(n):
            for c2 in range(c1 + 1, n):
                tem = count[c1] + count[c2] - matrix[c1][c2]
                rst = max(rst, tem)
        return rst

    def method2(self, n, roads):
        """
        Same ideas with method 1, but using adjacent list.
        """
        adjlist = [set() for _ in range(n)]
        for c1, c2 in roads:
            adjlist[c1].add(c2)
            adjlist[c2].add(c1)
        
        rst = 0
        for c1 in range(n - 1):
            for c2 in range(c1+1, n):
                tem = len(adjlist[c1]) + len(adjlist[c2]) - (c1 in adjlist[c2])
                rst = max(rst, tem)

        return rst

        

n = 8
roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
"""
n = 5
roads = [[2,3],[0,3],[0,4],[4,1]]
"""
print(Solution().maximalNetworkRank(n,roads))
