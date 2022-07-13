from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return self.method1(k, n) ## DFS. Preferred method
        #return self.method2(k, n) ## Bit.
    
    def method1(self, k, n):
        """
        DFS
        Time: O(C(9, k))
        Space:  O(C(9, k))
        """
        rst = []
        curr = []
        self.dfs(rst, curr, 0, k, 0, n)
        return rst
    
    def dfs(self, rst, curr, currsum, k, i, n):
        ## base case
        if len(curr) == k and currsum == n:
            rst.append(curr[:])
            return
        if len(curr) > k or currsum > n:
            return
        
        for index in range(i + 1, 10):
            curr.append(index)
            currsum += index
            self.dfs(rst, curr, currsum, k, index, n)
            
            ## bracktracing
            curr.pop()
            currsum -= index
            
    def method2(self, k, n):
        """
        Bit.
        Time: O(2^9)
        Space:  O(C(9, k))
        """
        rst = []
        up_lim = 1 << 9
        for v in range(up_lim):
            curr = []
            acc = 0
            for i in range(1, 10):
                if v & (1 << (i - 1)):
                    acc += i
                    curr.append(i)
            if len(curr) == k and acc == n:
                rst.append(curr)
                
                
            
        return rst
        
        
            
        
        
        
        
"""
Ideas: 
DFS with memo
Two/three pointers (only suitable for k<=3)

"""