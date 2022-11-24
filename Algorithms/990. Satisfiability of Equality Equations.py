from typing import List
from collections import defaultdict

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        """
        graph, dfs, union find
        """
        #return self.method1(equations)
        return self.method2(equations) #preferred method
    
    def method1(self, equations):
        """
        DFS
        """
        def dfs(v1):
            """
            return whether there is conflict
            """
            if v1 in visited:
                return True
            visited.add(v1)
            if v1 in cannotconnect[self.key]:
                return False
            for nxt in adjlist[v1]:
                if not dfs(nxt):
                    return False
            
            return True
 
        ## Step 1: build adjlist
        adjlist = defaultdict(set)
        for e in equations:
            v1, t1, t2, v2 = e[0], e[1], e[2], e[3]
            if t1 == '!':
                continue
            adjlist[v1].add(v2)
            adjlist[v2].add(v1)
        
        ## step 2: for each variable, build a set to check not in
        cannotconnect = defaultdict(set)
        for e in equations:
            v1, t1, t2, v2 = e[0], e[1], e[2], e[3]
            if t1 == '=':
                continue
            cannotconnect[v1].add(v2)

        ## step 3: check conflict with dfs
        for key in cannotconnect.keys():
            self.key = key
            visited = set()
            if not dfs(key):
                return False
            
        return True
    
    
    def method2(self, equations):
        """
        Union find
        """
        self.root = [i for i in range(26)]
        
        def find(x):
            ## squash the path
            if self.root[x] != x:
                self.root[x] = find(self.root[x])
            return self.root[x]
        
        def union(x, y):
            ## unify two unions
            ## squash paths
            x = find(x)
            y = find(y)
            
            if x < y:
                self.root[x] = y
            else:
                self.root[y] = x
        
        for e in equations:
            v1, t1, t2, v2 = e[0], e[1], e[2], e[3]
            if t1 == '!':
                continue
            v1 = ord(v1) - ord('a')
            v2 = ord(v2) - ord('a')
            union(v1, v2)

        for e in equations:
            v1, t1, t2, v2 = e[0], e[1], e[2], e[3]
            if t1 != '!':
                continue
            v1 = ord(v1) - ord('a')
            v2 = ord(v2) - ord('a')
            if find(v1) == find(v2):
                return False
        
        return True
        
            
"""
{a, b, c, e, f}

"""
            