
from collections import deque
from typing import List
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        """
        Tpological sort.
        For any point its out degree is 1, and its in degree is 0 or positive number.
        """
        n = len(favorite)
        ## build in-degree
        indegree = [0] * n
        ## depth towards a 2-element circle
        depth = [1] * n
        ## whether a node has been visited
        visited = [False] * n
        
        for i in range(n):
            indegree[favorite[i]] += 1
        
        dq = deque()
        for i in range(n):
            if indegree[i] == 0:
                dq.append(i)
                visited[i] = True
        
        while dq:
            node = dq.popleft()
            nxt = favorite[node]
            ## for node's favorite person, its indegree minus 1
            indegree[nxt] -= 1
            depth[nxt] = depth[node] + 1
            if indegree[nxt] == 0:
                dq.append(nxt)
                visited[nxt] = True
            
        ## now only circle left. find the longest one
        rst = 0
        max_muti = 0
        max_2ele = 0
        for node in range(n):
            if visited[node]:
                continue
            counter = 0
            curr = node
            while not visited[curr]:
                visited[curr] = True
                counter += 1
                curr = favorite[curr]
            ## if a multi-element circle
            if counter >= 3:
                max_muti = max(max_muti, counter)
            elif counter == 2:
                max_2ele += depth[curr] + depth[favorite[curr]]
        
        return max(max_muti, max_2ele)