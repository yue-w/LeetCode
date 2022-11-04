# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:05:42 2020

@author: wyue
"""
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        return self.method1(graph)
        #return self.method2(graph)
    
    def method1(self, graph):
        """
        DFS
        """
        n = len(graph)
        ## group represent the state of a node: 0: not visited, 1: group 1, -1: group 2
        group = [0 for _ in range(n)]
        for node in range(n):
            if group[node] == 0:
                if not self.dfs(graph, group, node, -1):
                    return False
        
        return True
        
    def dfs(self, graph, group, node, nxt_group):
        """
        Return whther it is a Bipartite. 
        """
        ## base case
        ## if a node has been visited, check whether the 
        ## group that is supposed to assign to it conflict 
        ## with it's assigned group
        if group[node] != 0:
            return group[node] == nxt_group
        
        ## group has not been visited, set its group to nxt_group
        group[node] = nxt_group
        ## do dfs for each of node's neighbors
        for i in graph[node]:
            if not self.dfs(graph, group, i, -nxt_group):
                return False
        ## if no conflict found above, return True
        return True
        
    def method2(self, graph):
        """
        BFS
        """
        from collections import deque
        n = len(graph)
        ## group represent the state of a node: 0: not visited, 1: group 1, -1: group 2
        group = [0 for _ in range(n)]
        for node in range(n):
            if group[node] == 0:
                dq = deque()
                dq.append((node, 1))
                while dq:
                    for _ in range(len(dq)):
                        n, cur_group = dq.popleft()
                        for i in graph[n]:
                            ## check every neighbor of node. 
                            ## if a neighbor is not visted, give it a group (opposite from the 
                            ## current group) and add it to queue
                            if group[i] == 0:
                                dq.append((i, -cur_group))
                                group[i] = -cur_group
                            ## else, a neighbor has been visited before, then check whether this 
                            ## neighbor's group conflict whith the currrent node's group
                            else:
                                if cur_group == group[i]:
                                    return False                             
        return True
    
graph = [[1],[0,3],[3],[1,2]]
print(Solution().isBipartite(graph))