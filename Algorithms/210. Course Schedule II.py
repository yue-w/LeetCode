

from typing import List

from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        return self.method1(numCourses, prerequisites)
        #return self.method1(numCourses, prerequisites)
    
    
    def method1(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Topological sort by DFS
        """
        
        self.rst = []
        
        # 0: not visited. 1: visiting (in stack) --> detecting cycle. 2: visited.
        self.state = [0 for _ in range(numCourses)]
        
        ## Build an adjacent list
        self.adlist = [[] for _ in range(numCourses)]        
        for c1, c2 in prerequisites:
            self.adlist[c2].append(c1)
        
        for c in range(numCourses):
            if not self.dfs(c):
                return []
        self.rst.reverse()
        return self.rst
        
    def dfs(self, course):
        """
        Return True if no cycle exists, Return False otherwise
        """
        ## Base case 1: the node (course) in in stack, detect cycle, return False
        if self.state[course] == 1:
            return False
        ## Base case 2: the node has been visited (not in stack), return True
        if self.state[course] == 2:
            return True
        
        ## Change state of course to 1 (visiting)
        self.state[course] = 1
        
        for c in self.adlist[course]:
            ## if detect cycle, return False
            if not self.dfs(c):
                return False
        
        ## If not return false at this stage, 
        ## There is no cycle starting from this node. 
        ## Change state of course to 2 (visited)
        self.state[course] = 2
        ## Add the course to rst
        self.rst.append(course)
        return True
        

    def method2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Topological sort by BFS
        """
        rst = []
        
        ## Build adjacent list
        self.adlist = [[] for _ in range(numCourses)]
        ## In degree of each node
        self.in_degree = [0] * numCourses
        for c1, c2 in prerequisites:
            self.adlist[c2].append(c1)
            self.in_degree[c1] += 1

        q = deque() ## enter from right, leave from left
        for node in range(numCourses):
            if self.in_degree[node] == 0:
                q.append(node)
                rst.append(node)

        while q:
            node = q.popleft()
            for c in self.adlist[node]:
                self.in_degree[c] -= 1
                if self.in_degree[c] == 0:
                    q.append(c)
                    rst.append(c)
    
    
    
        if len(rst) == numCourses:
            return rst
        else:
            return []

        
        
        
        
        
        
        
        
        
        
        
        
        

    
    
        

