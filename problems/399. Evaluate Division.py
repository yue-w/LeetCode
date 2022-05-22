

from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        if two points are not connected return -1?
        """
        self.adlist = defaultdict(list)
        ## Build adjacent list
        for e, val in zip(equations, values):
            v1, v2 = e
            self.adlist[v1].append((v2, val))
            self.adlist[v2].append((v1, 1/val))
        
        ans = []
        
        for q in queries:
            seen = set()
            v1, v2 = q
            if not v1 in self.adlist or not v2 in self.adlist:
                ans.append(-1)
            # elif v1 == v2:
            #     ans.append(1)
            else:
                value = self.dfs(v1, v2, seen)
                if not value:
                    ans.append(-1)
                else:
                    ans.append(value)
                
        
        return ans
    
    def dfs(self, v1, v2, seen):
        ## Base case
        if v1 in seen:
            return None
        if v1 == v2:
            return 1
        seen.add(v1)
        for e in self.adlist[v1]:
            node, val = e
            
            tem = self.dfs(node, v2, seen)
            if tem:
                return val * tem
        return None
        
if __name__ == '__main__':
    s = Solution()

    equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
    values = [3.0,4.0,5.0,6.0]
    queries = [["x2","x4"]]
    rst = s.calcEquation(equations, values, queries)
    print(rst)  
