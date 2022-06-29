import queue
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # return self.method1(isConnected) # DFS
        # return self.method2(isConnected) # BFS
        return self.method3(isConnected) # Union find
        
    
    def method1(self, isConnected):
        ## DFS
        m = len(isConnected)
        stack = []
        seen = set()
        rst_list = []
        for i in range(m):
            if i in seen:
                continue
            stack.append(i)
            while stack:
                head = stack.pop()
                connected, index = self.in_list(rst_list, head)
                if connected:
                    self.add_tails(head, isConnected, stack, seen, rst_list, index)
                    
                else:
                    rst_list.append({head})
                    index = len(rst_list) - 1
                    self.add_tails(head, isConnected, stack, seen, rst_list, index)
                    
                    
        return len(rst_list)

            
    def in_list(self, rst_list, city):
        ## if city is in a set of rst_list, return True, and the index of the set
        ## otherwise, return False and -1
        for index, ele in enumerate(rst_list):
            if city in ele:
                return True, index
            
        return False, -1        

    def add_tails(self, head, isConnected, stack, seen, rst_list, index):
        m = len(isConnected)
        for tail in range(m):
            if (tail != head) and tail not in seen:
                if isConnected[head][tail] == 1:
                    seen.add(tail)
                    stack.append(tail)
                    rst_list[index].add(tail)
                    
    def method2(self, isConnected):
        ## BFS
        m = len(isConnected)
        rst_list = []
        seen = set()
        q = queue.Queue()
        for i in range(m):
            if i in seen:
                continue
            q.put(i)
            while not q.empty():
                head = q.get()
                connected, index = self.in_list2(rst_list, head)
                if connected:
                    self.add_tails2(head, isConnected, q, seen, rst_list, index)
                else:
                    rst_list.append({head})
                    index = len(rst_list) - 1
                    self.add_tails2(head, isConnected, q, seen, rst_list, index)
                    
        return len(rst_list)
        
    
    def in_list2(self, rst_list, city):
        ## if city is in a set of rst_list, return True, and the index of the set
        ## otherwise, return False and -1
        for index, ele in enumerate(rst_list):
            if city in ele:
                return True, index
            
        return False, -1
    
        
    def add_tails2(self, head, isConnected, q, seen, rst_list, index):
        m = len(isConnected)
        for tail in range(m):
            if (tail != head) and tail not in seen:
                if isConnected[head][tail] == 1:
                    seen.add(tail)
                    q.put(tail)
                    rst_list[index].add(tail)
    
    def method3(self, isConnected):
        """
        Unionfind
        """
        N = len(isConnected)
        self.parents = [i for i in range(N)]
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
        if self.rank[px] < self.rank[py]:
            self.parents[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parents[py] = px
        else:
            self.parents[py] = px
            self.rank[px] += 1
            
        
