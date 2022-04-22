# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:48:28 2020

@author: wyue
"""
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        ## Mehtod 1:DFS
        rst = []
        n = len(graph)
        path = []
        path.append(0)
        self.helper(0,n,graph,path,rst)
        return rst
        
    def helper(self,i,n,graph,path, rst):
        for j in graph[i]:
            
            temPath = path[:]
            temPath.append(j)
            if j == n-1:
                rst.append(temPath) 
            
            else:
                self.helper(j,n,graph,temPath, rst)
                  
        #return rst
graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(Solution().allPathsSourceTarget(graph))