
from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #return self.method1(edges)
        return self.method2(edges)
        
    def method1(self, edges):
        """
        Topological sort of BFS
        find the nodes that have a degree of 2
        Time: O(n)
        Space: O(n)
        """
        
        n = len(edges)
        degree = [0] * (n + 1)
        
        adjlist = [[] for _ in range(n + 1)]
        
        for n1, n2 in edges:
            degree[n1] += 1
            degree[n2] += 1
            adjlist[n1].append(n2)
            adjlist[n2].append(n1)
        
        ## BFS. Unplug nodes with degree of 1 from the graph
        dq = deque()
        for i in range(1, n + 1):
            if degree[i] == 1:
                dq.append(i)
        
        while dq:
            for _ in range(len(dq)):
                v1 = dq.popleft()
                for v2 in adjlist[v1]:
                    degree[v2] -= 1
                    if degree[v2] == 1:
                        dq.append(v2)
        
        for n1, n2 in edges[::-1]:
            if degree[n1] > 1 and degree[n2] > 1:
                return [n1, n2]
            
    def method2(self, edges):
        """
        Unionfind.
        Time: O(n)
        Space: O(n)
        """
        n = len(edges)
        #self.father = [0] * (n + 1)
        self.father = [i for i in range(n + 1)]
        def find(i):
            """
            Find root 
            """
            if i != self.father[i]:
                self.father[i] = find(self.father[i])
            return self.father[i]
            
        def union(n1, n2):
            x1 = find(n1)
            x2 = find(n2)
            if x1 < x2:
                self.father[n1] = x2
            else:
                self.father[n2] = x1
            
        for n1, n2 in edges:
            if find(n1) != find(n2):
                union(n1, n2)
            else:
                return [n1, n2]
        
if __name__ == '__main__':
    edges = [[1,2],[1,3],[2,3]]
    rst = Solution().findRedundantConnection(edges)
    print(rst)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                    
                    
                
                