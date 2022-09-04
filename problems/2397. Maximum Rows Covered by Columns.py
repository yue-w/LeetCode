from typing import List

class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        def dfs(curr, idx):
            ## base case
            self.rst = max(self.rst, len(curr))
            if idx == mm:
                return

            
            for r in range(idx, mm):
                ## select row r
                curr.append(r)
                count = 0
                for c in range(n):
                    if selected[c] > 0:
                        count += 1
                legit = True
                cc = []
                for c in range(n):
                    if newmat[r][c] == 1:
                        if selected[c] == 0:
                            count += 1
                        selected[c] += 1
                        cc.append(c)
                        
                        if count > cols:
                            legit = False
                            break
                if legit:
                    dfs(curr, r + 1) 
                # backtracking
                curr.pop()
                for c in cc:
                    if newmat[r][c] == 1:
                        selected[c] -= 1
                

  
        m = len(mat)
        n = len(mat[0])
        newmat = []
        extra_rst = 0
        for row in range(m):
            if sum(mat[row]) == 0:
                extra_rst += 1
            else:
                newmat.append(mat[row][:])
        
        mm = len(newmat)
        curr = []
        idx = 0
    
        self.rst = 0
        selected = [0] * n
        dfs(curr, idx)
        
        return self.rst + extra_rst
        
        