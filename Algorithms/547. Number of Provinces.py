from collections import deque
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #return self.method1(isConnected) # DFS
        return self.method2(isConnected) # BFS
        #return self.method3(isConnected) # Union find
        
    
    def method1(self, isConnected):
        """
        DFS.
        Time: O(n^2)
        Space: O(n)
        """
        n = len(isConnected)
        ## 0: not visited. Others: group number
        group = [0] * n
        stack = []
        
        gp = 0
        for i in range(n):
            if group[i] != 0:
                continue
            stack.append(i)
            gp += 1
            while stack:
                node = stack.pop()
                if group[node] != 0:
                    continue
                group[node] = gp
                ## add all the cities connected with node into stack
                for j in range(n):
                    if node == j:
                        continue
                    if isConnected[node][j] != 0:
                        stack.append(j)

        
        ## result is the number of unique numbers in group.
        seen = set()
        for v in group:
            seen.add(v)
        return len(seen)
                    
    def method2(self, isConnected):
        """
        BFS
        """
        n = len(isConnected)
        ## 0: not visited. Others: group number
        group = [0] * n
        
        dq = deque()
        
        gp = 0
        for i in range(n):
            ## ignore if has visited, otherwise, add it into the queue
            if group[i] != 0:
                continue
            dq.append(i)
            gp += 1
            #group[i] = gp
            
            
            while dq:
                for _ in range(len(dq)):
                    node = dq.popleft()
                    if group[node] != 0:
                        continue
                    group[node] = gp
                    ## for all the cities connected with this city, add it into queue
                    for j in range(n):
                        if node == j:
                            continue
                        if group[j] != 0:
                            continue
                        if isConnected[node][j] == 1:
                            dq.append(j)
        
        ## result is the number of unique numbers in group.
        seen = set()
        for v in group:
            seen.add(v)
        return len(seen)
    
    def method3(self, isConnected):
        """
        Unionfind
        """
        N = len(isConnected)
        self.parents = [i for i in range(N)]
        ## think rank as the longest path from parents to leaf
        self.rank = [0] * N
        
        for row in range(N):
            for col in range(row + 1, N):
                if isConnected[row][col] == 0:
                    continue
                self.union(row, col)
        
        firstseen = set()
        for i in range(N):
            firstseen.add(self.find(i))
        
        return len(firstseen)
    
    def find(self, index):
        if self.parents[index] != index:
            self.parents[index] = self.find(self.parents[index])
        return self.parents[index]
    
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        ## merge the smaller one into the larger one.
        ## no need to modify rank because after merging, the longest length of the
        ## tree being merged into did not change
        if self.rank[px] < self.rank[py]:
            self.parents[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parents[py] = px
        else:
            ## equal rank, the rank (longest path from parent to child) of the 
            ## one being merged into needs to increase by 1 
            self.parents[py] = px
            self.rank[px] += 1
            
        
            
        
