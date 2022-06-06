
from collections import deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        ## if only one or two nodes, they are the answer
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]
        adlist = [[] for _ in range(n)]
        degree = [0] * n
        for v1, v2 in edges:
            adlist[v1].append(v2)
            adlist[v2].append(v1)
            degree[v1] += 1
            degree[v2] += 1
        
        q = deque() ## enter from right, leave from left
        visited = [0] * n
        for i in range(n):
            if degree[i] == 1:
                q.append(i)
        count = 0
        while q:
            for _ in range(len(q)):
                v = q.popleft()
                visited[v] = 1
                count += 1

                for nxt in adlist[v]:
                    degree[nxt] -= 1
                    if degree[nxt] == 1:
                        q.append(nxt)
            if count == n - 1 or count == n - 2:
                break
        rst = []
        for i, val in enumerate(visited):
            if val == 0:
                rst.append(i)
                
        return rst

        # ## Topological sort
        # ## edge cases: if there are only 1 or 2 points
        # if n == 1:
        #     return [0]
        # if n == 2:
        #     return [0, 1]
        
        # ## Step 1: Build data structures: 
        # ##        (1) build an adjancent list (2) record degree of each node 
        # adlist = [[] for _ in range(n)]
        # degree = [0] * n
        # for e in edges:
        #     a, b = e[0], e[1]
        #     adlist[a].append(b)
        #     adlist[b].append(a)
        #     degree[a] += 1
        #     degree[b] += 1
        
        # ## Step 2: find the points with degree 1 and add them into the queue
        # dq = deque() ## enter from the right and leave from the left
        # for i in range(n):
        #     if degree[i] == 1:
        #         dq.append(i)
        
        # ## Step 3: do bfs on the points with degree 1 (peel the nodes with degree 1 off and update degree)
        # visited = [0] * n
        # counter = n ## in the end, there will be either 1 or 2 points left, use counter to record the process
        # rst = []
        # while dq:
        #     nq = len(dq)
        #     for _ in range(nq):
        #         node = dq.popleft()
        #         visited[node] = 1
        #         counter -= 1
        #         ## decrease the degree of adjance point of node
        #         for v in adlist[node]:
        #             degree[v] -= 1
        #             if degree[v] == 1:
        #                 dq.append(v)
                        
        #     if counter == 1 or counter == 2:
        #         break
        # ## Step 4: find the one or two points that has not been visited, they are the inner point, return
        # for i in range(n):
        #     if visited[i] == 0:
        #         rst.append(i)
        # return rst
            
if __name__ == '__main__':
    s = Solution()
    n = 3
    edges = [[0,1],[0,2]]
    rst = s.findMinHeightTrees(n, edges)
    print(rst)