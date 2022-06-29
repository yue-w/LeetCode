# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:48:28 2020

@author: wyue
"""
from collections import deque
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #return self.method1(graph) ## preferred method.
        return self.method2(graph)

    
    def method1(self, graph):
        """
        dfs
        dfs is preferred.
        """
        n = len(graph)
        curr = [0]
        rst = []
        
        self.dfs(graph, rst, curr, 0)
        
        return rst
    
    def dfs(self, graph, rst, curr, node):
        ## base cases
        if node == len(graph) - 1:
            rst.append(curr[:])
            return 
        
        for n in graph[node]:
            curr.append(n)
            self.dfs(graph, rst, curr, n)
            ## backing track
            curr.pop()
    
    def method2(self, graph):
        """
        BFS
        """
        dq = deque() ## enter from right, leave from left
        rst = []
        
        dq.append([0])
        while dq:
            curr = dq.popleft()
            if curr[-1] == len(graph) - 1:
                rst.append(curr[:])
            for n in graph[curr[-1]]:
                newcurr = curr[:]
                newcurr.append(n)
                dq.append(newcurr)
                
        return rst
            
if __name__ == "__main__":
    #graph = [[1,2],[3],[3],[]]
    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    print(Solution().allPathsSourceTarget(graph))