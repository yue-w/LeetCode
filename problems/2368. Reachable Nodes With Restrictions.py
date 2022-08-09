from typing import List
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        """
        DFS
        """
        def dfs(node):
            """
            base case
            """
            if node in visited:
                return
            self.rst += 1
            visited.add(node)
            for nxt in adjlist[node]:
                dfs(nxt)
        
        ## build adjacent list
        adjlist = [[] for _ in range(n)]
        for n1, n2 in edges:
            adjlist[n1].append(n2)
            adjlist[n2].append(n1)
        
        self.rst = 0
        visited = set(restricted)
        dfs(0)
        return self.rst