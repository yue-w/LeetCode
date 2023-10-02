# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:05:42 2020

@author: wyue
"""
from typing import List
import collections

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #return self.method1(graph)
        #return self.method2(graph)
        return self.method3(graph)

    def method1(self, graph):
        """
        DFS
        """
        def dfs(idx):
            ## Base case
            #?
            for nxt in graph[idx]:
                if not groups[nxt]:
                    groups[nxt] = -groups[idx]
                    if not dfs(nxt):
                        return False
                else:
                    if groups[nxt] == groups[idx]:
                        return False
            return True

        n = len(graph)
        groups = [0 for _ in range(n)]
        for i in range(n):
            if not groups[i]:
                groups[i] = 1
                if not dfs(i):
                    return False
        return True

    def method2(self, graph):
        """
        BFS
        """
        n = len(graph)
        groups = [0 for _ in range(n)]
        for i in range(n):
            if not groups[i]:
                groups[i] = 1
                dq = collections.deque([i])
                while dq:
                    for _ in range(len(dq)):
                        node = dq.popleft()
                        for nxt in graph[node]:
                            if not groups[nxt]:
                                groups[nxt] = - groups[node]
                                dq.append(nxt)
                            elif groups[nxt] == groups[node]:
                                return False

        return True

    def method3(self, graph):
        """
        UnionFind
        """
        n = len(graph)
        rank = [1] * n
        root = [i for i in range(n)]
        
        def find_root(idx):
            if idx != root[idx]:
                root[idx] = find_root(root[idx])
            return root[idx]
        
        def union(x, y):
            root_x = find_root(x)
            root_y = find_root(y)

            if rank[x] < rank[y]:
                root[x] = root_y
            elif rank[x] > rank[y]:
                root[y] = find_root(x)
            else:
                root[x] = root_y
                rank[x] += 1
        
        for i in range(n):
            for nxt in graph[i]:
                if find_root(i) == find_root(nxt):
                    return False
                union(graph[i][0], nxt)
        return True

    
graph = [[1],[0,3],[3],[1,2]]
print(Solution().isBipartite(graph))