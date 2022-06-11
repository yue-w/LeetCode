from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #return self.method1(prices)
        return self.method2(prices)
    
    def method1(self, prices):
        """
        DP
        dp[i][0]: 'Held stock' on day i (either held a stock bought earlier or buy it on day i)
        dp[i][1]: 'No stock' on day i (either keep the state of no stock or sell it on day i)

        transition function:
        dp[i][0] = max(dp[i - 1][0], dp[i - 2][1] - prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        """
        N = len(prices)
        
        if N == 1:
            return 0
        
        dp = [[0 for _ in range(2)] for _ in range(N)]
        
        dp[0][0] = - prices[0]
        dp[0][1] = 0
        dp[1][0] = max(-prices[0], -prices[1])
        dp[1][1] = max(0, prices[1] - prices[0])
        
        for i in range(2, N):
            dp[i][0] = max(dp[i - 1][0], dp[i - 2][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            
        return max(dp[N-1])