
from collections import Counter
from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:  
        #return self.method1(strs, m, n)
        #return self.method2(strs, m, n)
        return self.method3(strs, m, n)
    def method1(self, strs, m, n):
        """
        dp with table. 0-1 Knapsack
        dp[i][j]: use i '1' and j '0', the size of the largest subset of strs 
        such that there are at most m 0's and n 1's in the subset.
        """

        N = len(strs)
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)] 
        
        for k in range(N):
            c = Counter(strs[k])
            zeros = c['0']
            ones = c['1']
            ## backup the result of the previous round
            dp_tem = [x[:] for x in dp]
            for i in range(zeros, m + 1):
                for j in range(ones, n + 1):
                    ## case 1: do not use the current string (kth string)
                    case1 = dp_tem[i][j]
                    ## case 2: use the current string (kth string)
                    case2 = dp_tem[i-zeros][j-ones] + 1
                    dp[i][j] = max(case1, case2)

        return dp[m][n]
    
    def method2(self, strs, m, n):
        """
        DFS with memo
        """

        # preprocess to count 0 and 1 for each element in strs
        zeros = [0] * len(strs)
        ones = [0] * len(strs)
        for i in range(len(strs)):
            count = Counter(strs[i])
            zeros[i] = count['0']
            ones[i] = count['1']
        
        def dfs(curr, idx, remain_zeros, remain_ones):
            # base case
            if idx == len(strs):
                self.rst = max(self.rst, curr)
                return self.rst
            # memo
            if (curr, idx, remain_zeros, remain_ones) in memo:
                return 
            # use strs[idx]
            if remain_zeros >= zeros[idx] and remain_ones >= ones[idx]:
                dfs(curr+1, idx+1, remain_zeros-zeros[idx], remain_ones-ones[idx])
            # do not use strs[idx]
            dfs(curr, idx+1, remain_zeros, remain_ones)
            memo.add((curr, idx, remain_zeros, remain_ones))
            
        memo = set()
        self.rst = 0
        dfs(0, 0, m, n)
        return self.rst
    
    def method3(self, strs, m, n):
        """
        DFS with memo
        """
        from collections import Counter
        # preprocess to count 0 and 1 for each element in strs
        zeros = [0] * len(strs)
        ones = [0] * len(strs)
        for i in range(len(strs)):
            count = Counter(strs[i])
            zeros[i] = count['0']
            ones[i] = count['1']
        
        def dfs2(idx, remain_zeros, remain_ones):
            # base case
            if idx == len(strs):
                return 0
            # memo
            if (idx, remain_zeros, remain_ones) in memo:
                return memo[(idx, remain_zeros, remain_ones)]
            
            best = 0
            # use strs[idx]
            if remain_zeros >= zeros[idx] and remain_ones >= ones[idx]:
                use = dfs2(idx+1, remain_zeros-zeros[idx], remain_ones-ones[idx])
                best = max(best, use + 1) 
            # do not use strs[idx]
            not_use = dfs2(idx+1, remain_zeros, remain_ones)
            best = max(best, not_use)
            memo[(idx, remain_zeros, remain_ones)] = best
            return best
            
        memo = {}
        rst = dfs2(0, m, n)
        return rst


if __name__ == '__main__':
    strs = ["10","0001","111001","1","0"] 
    m = 4
    n = 3
    rst = Solution().findMaxForm(strs, m, n)
    print(rst)