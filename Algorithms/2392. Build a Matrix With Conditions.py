from typing import List
from collections import deque
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def topo(conditions):
            """
            Topological sort using BFS.
            """
            adjlist = [[] for _ in range(k + 1)]
            indegree = [0] * (k + 1)
            for a, b in conditions:
                adjlist[a].append(b)
                indegree[b] += 1
                
            dq = deque()
            for i in range(1, k + 1):
                if indegree[i] == 0:
                    dq.append(i)
            vector = []
            while dq:
                for _ in range(len(dq)):
                    tem = dq.pop()
                    vector.append(tem)
                    for nxt in adjlist[tem]:
                        indegree[nxt] -= 1
                        if indegree[nxt] == 0:
                            dq.append(nxt)
                    
            return vector
        
        rows = topo(rowConditions)
        if len(rows) < k:
            return []
        cols = topo(colConditions)
        if len(cols) < k:
            return []
        coords = [[0, 0] for _ in range(k + 1)]
        for i in range(k):
            coords[rows[i]][0] = i
            coords[cols[i]][1] = i 
        
        rst = [[0 for _ in range(k)] for _ in range(k)]
        for i in range(1, k + 1):
            rst[coords[i][0]][coords[i][1]]= i
        return rst