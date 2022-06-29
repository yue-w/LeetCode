
from collections import Counter
from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:  
        """
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

if __name__ == '__main__':
    strs = ["10","0001","111001","1","0"] 
    m = 4
    n = 3
    rst = Solution().findMaxForm(strs, m, n)
    print(rst)