from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.method1(prices)
        #return self.method2(prices)
    
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

    def method2(self, prices):
        """
        Preferred method.
        Similar to method 1. But save some space. (keep updating 3 values instead of two arrays.)
        held: held stock on day i (either held a stock bought before or buy a stock on day i)
        sell: sell stock on day i (sell it today)
        cooled: sold stock more than 1 day ago (either sold stock yesterday (sell) or sold more than 2 days ago)
        Transition functions:
        held = max(held, coold - price[i])
        sell = held + price[i]
        cooled = max(sell, cooled)
        """
        N = len(prices)
        
        held = float('-inf')
        sell = 0
        cooled = 0
        
        for i in range(N):
            ## back up
            held2 = held
            sell2 = sell
            cooled2 = cooled
            
            ## update
            held = max(held2, cooled2 - prices[i])
            sell = held2 + prices[i]
            cooled = max(sell2, cooled2)
            
        return max(sell, cooled)