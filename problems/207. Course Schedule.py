from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return self.method1(numCourses, prerequisites)
        #return self.method2(numCourses, prerequisites)
    
    def method1(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Topological sort by DFS
        """
        self.rst = []
        
        ## 0: not visited. 1: visiting (in stack) 2: visited (not in stack).
        self.state = [0] * numCourses
        
        self.adlist = [[] for _ in range(numCourses)]
        
        for c1, c2 in prerequisites:
            self.adlist[c2].append(c1)
        
        for c in range(numCourses):
            if not self.dfs(c):
                return False
        
        return True
    
    def dfs(self, course):
        """
        Return True if no cycle exist, otherwise return False
        """
        if self.state[course] == 1:
            return False
        if self.state[course] == 2:
            return True
        self.state[course] = 1
        
        ## Return False if any of the folloing courses find a cycle
        for c in self.adlist[course]:
            if not self.dfs(c):
                return False

        ## Backing track, if no cycle after this node, mark it as visited
        self.state[course] = 2
        return True
        
    
    def method2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Topological sort by BFS
        """
        ## the number of nodes have been visited
        count = 0
        ## Build adjacent list
        self.adlist = [[] for _ in range(numCourses)]
        ## In degree of each node
        self.in_degree = [0] * numCourses
        for c1, c2 in prerequisites:
            self.adlist[c2].append(c1)
            self.in_degree[c1] += 1

        ## add nodes with 0 degree into the queue (those are course OK to take now)
        q = deque() ## enter from right, leave from left
        for node in range(numCourses):
            if self.in_degree[node] == 0:
                q.append(node)
                count += 1

        while q:
            node = q.popleft()
            for c in self.adlist[node]:
                self.in_degree[c] -= 1
                if self.in_degree[c] == 0:
                    q.append(c)
                    count += 1

        return count == numCourses

if __name__ == '__main__':
    s = Solution()
    numCourses = 2
    prerequisites = [[1,0]]
    rst = s.canFinish(numCourses, prerequisites)
    print(rst)