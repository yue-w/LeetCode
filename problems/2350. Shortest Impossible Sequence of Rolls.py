from typing import List
class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        """
        DFS
        State machine
        """
        if len(set(rolls)) < k:
            return 1
        
        n = len(rolls)
        rolls = [0] + rolls
        table = [[-1 for _ in range(9)] for _ in range(n + 2)]
        
        for i in range(n, 0, -1):
            table[i-1] = table[i][:]
            table[i-1][rolls[i]-1] = i 
        
        #print(table)
        self.len = 1

        def dfs(curr, num):
            if len(curr) == num:
                return exist(curr)
            
            for i in range(1, k + 1):
                curr.append(i)
                if not dfs(curr, num):
                    return False
                ## backtrakcing
                curr.pop()
            return True
        
        def exist(curr):
            tpl = tuple(curr[:-1])
            if  tpl in memo:
                idx = memo[tpl]
                idx = table[idx][curr[-1]-1]
                if idx == -1:
                    return False
            else:
                idx = 0
                for c in curr:
                    idx = table[idx][c-1]
                    if idx == -1:
                        return False
            if tpl:
                memo[tpl] = idx
            return True
            
        memo = {}
        for i in range(1, n + 1):
            if not dfs([], i):
                return i
             
        return k
            
if __name__ == '__main__':
    # rolls = [1,1,2,2,1,4,3,1,4,3,2,1,1,1,1,1,3,3,4,1,3,4,1,1,3,2,4,4,1,3,1,2,2,1,1,1,3,3,2,1,2,4,2,4,2,4,4,3,3]
    # k = 4
    rolls = [4,2,1,2,3,3,2,4,1]
    k = 4
    # rolls = [2,2,2,2,2,2,1,2,2,2,1,1,1,2,2,2,2,1,2,1,1,2,2,2,2,1,1,1,1,2,1,1,2,1,1,2,2,1,1,1,2,1,1,1,2,2,1,2,1,2,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,2,2,1,2,1,2,1,2,2,1,1,2,1,1,1,1,2,2,2,2,1,2,1,1,2,1,2,1,1,2,2,1,2,1,1,2,2,2,1,2,2,1,1,2,2,1,2,1,1,2,1,1,1,1,2,2,1,2,2,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,1,1,2,1,1,1,1,2,1,1,2,2,2,2,2,2,2,1,2,2,2,2,2,2,1,2,1,1,2,1,2,1,2,2,2,2,2,2,1,1,2,1,2,2,2,2,1,2,1,2,1,2,1,1,1,2,1,1,1,2,1,1,2,2,1,1,1,1,2,2,2,2,1,2,1,1,1,1,1,2,1,1,1,1,2,2,1,1,1,2,2,1,2,1,2,1,1,2,2,2,1,1,2,1,2,1,2,2,1,1,1,1,2,2,2,1,1,2,2,1,1,1,1,1,1,2,1,1,2,2,2,1,1,2,1,2,2,2,2,2]
    # k = 2
    rst = Solution().shortestSequence(rolls, k)
    print(rst)