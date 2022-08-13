
from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:        
        def dfs(node):
            ## base case 0: visited before
            if types[node] == -2:
                types[node] = 2
                return 2
            ## base case 1: visited before
            if types[node] != -1:
                return types[node]
            ## base case 2: terminal node
            if not graph[node]:
                types[node] = 0
                return 0
            types[node] = -2         
            for nxt in graph[node]:
                tp = dfs(nxt)
                if tp == 2:
                    types[node] = 2
                    return 2
            types[node] = 1
            return 1
        

        n = len(graph)
        ## -2: visited second time (circle). -1:not visited. 0:terminal node. 1:safe node. 2:normal node 
        types = [-1] * n
        for node in range(n):
            dfs(node)
        rst = []
        for i, t in enumerate(types):
            if t == 0 or t == 1:
                rst.append(i)
        rst.sort()
        return rst