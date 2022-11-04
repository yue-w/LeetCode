

from collections import deque
from typing import List
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        """
        Topological sort
        Time: O(n)
        Space: O(n), where n is the number of nodes
        """
        
        ## Step 1: get in-degree info
        indegree = [0] * len(edges)
        for i, e in enumerate(edges):
            if e == -1:
                continue
            indegree[e] += 1
        
        dq = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                dq.append(i)
        
        ## Step 2: remove all nodes with 0 in degree
        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                if edges[node] == -1:
                    continue
                indegree[edges[node]] -= 1
                if indegree[edges[node]] == 0:
                    dq.append(edges[node])

        ## Step 3: 
        ##  if all nodes now has 0 indegree, return -1
        ##  if there are nodes have in-degree of 1, it's part of a cycle
        ##  there may be multiple cycles, find the longest one.
        if sum(indegree) == 0:
            return -1
        
        rst = 0
        ## iterate all cycles, find the longest one
        ## avoid visited nodes to avoid duplication
        seen = set()
        cur_len = 0
        for i in range(len(indegree)):
            if indegree[i] == 0:
                continue
            if i in seen:
                continue
            while not i in seen:
                seen.add(i)
                cur_len += 1
                i = edges[i]
            rst = max(rst, cur_len)
            cur_len = 0
        
        return rst
            