
from typing import List

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        """
        dp[i][k]:  the maximum score you can achieve for at most k partitions
        for nums[0:i + 1].
        Transition function dp[i][k] = max{dp[0:j][k-1] + helper(s[j:i+1]) for j = 0, ..., i}

        """
        n = len(nums)
        nums = [0] + nums
        
        ## think about the initial values
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        
        ## initial values for the corner cases dp[0][1]
        for i in range(1, n + 1):
            dp[i][0] = float('-inf')#sum(nums[0:i + 1])
        
            
        for i in range(1, n + 1):
            for kk in range(1, min(i, k) + 1):
                cursum = 0
                for j in range(i, kk-1, -1):
                    cursum += nums[j]
                    dp[i][kk] = max(dp[i][kk], dp[j-1][kk - 1] + cursum/(i - j + 1))
        rst = 0
        for k in range(1, k + 1):
            rst = max(rst, dp[n][k])
        return rst
        
         
        
        
