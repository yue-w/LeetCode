
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:  
        """
        Find nodes that are not in a cycle. Topological sort.
        """
        return self.method1(graph)
        #return self.method2(graph)
        
    def method1(self, graph):
        """
        Topological sort with DFS.
        """
        def dfs(node):
            ## base case: if type == 1: visited before (dead end/ not in a cycle)
            if types[node] == 1:
                return True
            
            ## base case: if type == 2: the node is visiting
            if types[node] == 2:
                return False
            
            types[node] = 2
            
            for nxt in graph[node]:
                if not dfs(nxt):
                    return False
            
            types[node] = 1
            return True

        n = len(graph)
        ## 0: never visited.  1: visited before (dead end/ no in a cycle).   2: visiting.
        types = [0] * n
        
        rst = []
        for node in range(n):
            if dfs(node):
                rst.append(node)

        rst.sort()
        return rst
    
    def method2(self, graph):
        """
        Topological sort with BFS.
        """
        # "graph" is the adjacent list
        n = len(graph)
        # computed outdegree
        outdegree = [0] * n
        # pre is the node that points to node
        pre = [[] for _ in range(n)]
        for i in range(n):
            for node in graph[i]:
                pre[node].append(i)
                outdegree[i] += 1
        
        dq = deque()
        for i in range(n):
            if outdegree[i] == 0:
                dq.append(i)
        
        rst = []
        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                rst.append(node)
                for p in pre[node]:
                    outdegree[p] -= 1
                    if outdegree[p] == 0:
                        dq.append(p)
          
        rst.sort()
        return rst