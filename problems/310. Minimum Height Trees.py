
from collections import deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        ## Topological sort
        ## edge cases: if there are only 1 or 2 points
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]
        
        ## Step 1: Build data structures: 
        ##        (1) build an adjancent list (2) record degree of each node 
        adlist = [[] for _ in range(n)]
        degree = [0] * n
        for e in edges:
            a, b = e[0], e[1]
            adlist[a].append(b)
            adlist[b].append(a)
            degree[a] += 1
            degree[b] += 1
        
        ## Step 2: find the points with degree 1 and add them into the queue
        dq = deque() ## enter from the right and leave from the left
        for i in range(n):
            if degree[i] == 1:
                dq.append(i)
        
        ## Step 3: do bfs on the points with degree 1 (peel the nodes with degree 1 off and update degree)
        visited = [0] * n
        counter = n ## in the end, there will be either 1 or 2 points left, use counter to record the process
        rst = []
        while dq:
            nq = len(dq)
            for _ in range(nq):
                node = dq.popleft()
                visited[node] = 1
                counter -= 1
                ## decrease the degree of adjance point of node
                for v in adlist[node]:
                    degree[v] -= 1
                    if degree[v] == 1:
                        dq.append(v)
                        
            if counter == 1 or counter == 2:
                break
        ## Step 4: find the one or two points that has not been visited, they are the inner point, return
        for i in range(n):
            if visited[i] == 0:
                rst.append(i)
        return rst
            
            