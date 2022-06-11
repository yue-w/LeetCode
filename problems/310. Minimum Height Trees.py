
from collections import deque
from typing import List

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        Topological sort using BFS
        """
        ## edge cases: if there are only 1 or 2 points
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]

        ## Step 1: Build data structures: 
        adlist = [[] for _ in range(n)]
        degree = [0] * n
        for v1, v2 in edges:
            adlist[v1].append(v2)
            adlist[v2].append(v1)
            degree[v1] += 1
            degree[v2] += 1
        

        ## Step 2: find the points with degree 1 and add them into the queue
        q = deque() ## enter from right, leave from left
        for i in range(n):
            if degree[i] == 1:
                q.append(i)

        ## Step 3: do bfs on the points with degree 1 (peel the nodes with 
        ## degree 1 off and update its neighbors' degree)      
        count = 0
        while q:
            for _ in range(len(q)):
                v = q.popleft()
                count += 1

                for nxt in adlist[v]:
                    degree[nxt] -= 1
                    if degree[nxt] == 1:
                        q.append(nxt)
            if count == n - 1 or count == n - 2:
                break
        ## Step 4: returnthe last 1 or 2 elements in the queue is the result       
        return q
            
if __name__ == '__main__':
    s = Solution()
    n = 3
    edges = [[0,1],[0,2]]
    rst = s.findMinHeightTrees(n, edges)
    print(rst)