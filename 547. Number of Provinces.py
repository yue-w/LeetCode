import queue
from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ## BFS
        m = len(isConnected)
        rst_list = []
        ## Breadth first search
        seen = set()
        q = queue.Queue()
        for i in range(m):
            if i in seen:
                continue
            q.put(i)
            while not q.empty():
                head = q.get()
                connected, index = self.in_list(rst_list, head)
                if connected:
                    self.add_tails(head, isConnected, q, seen, rst_list, index)
                else:
                    rst_list.append({head})
                    index = len(rst_list) - 1
                    self.add_tails(head, isConnected, q, seen, rst_list, index)
                    
        return len(rst_list)
        
    
    def in_list(self, rst_list, city):
        ## if city is in a set of rst_list, return True, and the index of the set
        ## otherwise, return False and -1
        for index, ele in enumerate(rst_list):
            if city in ele:
                return True, index
            
        return False, -1
    
        
    def add_tails(self, head, isConnected, q, seen, rst_list, index):
        m = len(isConnected)
        for tail in range(m):
            if (tail != head) and tail not in seen:
                if isConnected[head][tail] == 1:
                    seen.add(tail)
                    q.put(tail)
                    rst_list[index].add(tail)
                    
                    
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
