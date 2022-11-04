from typing import List
from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """
        Time: O(n*(2^n))
        Space: O(n*(2^n))
        Reference: https://youtu.be/wA_eIZFhpIc
        """
        n = len(graph)
        
        
        target = (1 << n) - 1
        
        ## state compression
        ## state is the current node being visited and all the nodes that have been visited
        visited = [[False for _ in range(1 << n)] for _ in range(n)]
        
        dq = deque()
        
        ## add all nodes into queue
        for i in range(n):
            dq.append((i, (1<<i)))
        
        steps = -1
        while dq:
            steps += 1
            for _ in range(len(dq)):
                node, state = dq.popleft()
                if visited[node][state]:
                    continue
                visited[node][state | 1 << node] = True
                
                for i in graph[node]:
                    if state  == target:
                        return steps   
                    dq.append((i, state | 1 << i))
                    
        return 0