
from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        Find the node with an out-degree of 0 and an in-degree of n-1
        """
        
        indegree = [0] * n
        outdegree = [0] * n
        
        for p1, p2 in trust:
            indegree[p2 - 1] += 1
            outdegree[p1 - 1] += 1
            
        for i in range(n):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i + 1
        
        return -1
        