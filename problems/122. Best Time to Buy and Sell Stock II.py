from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #return self.method1(prices)
        return self.method2(prices)
    
    def method1(self, prices):
        """
        dp[i][0]: Max total money of 'helding a stock' on day i (either held a stock bought earlier or buy it on day i)
        dp[i][1]: Max total money of 'no stock' on day i (either keep the state of no stock or sell a stock on day i)
        transition function:
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        """
        N = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(N)]
        ## income on first day of having stock is -prices[0]
        dp[0][0] = -prices[0] 
        for i in range(1, N):
            ## no stock
            dp[i][1] = max(dp[i-1][1], dp[i - 1][0] + prices[i])
            ## have stock
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
        
        
        return dp[N-1][1]
    
    def method2(self, prices):
        """
        Same with method1, but save space by updating two variables instead of an array
        """
        N = len(prices)
        ## income on first day of having stock is -prices[0]
        stk = -prices[0] 
        nostk = 0
        
        for i in range(1, N):
            ## backup 
            stk_cp = stk
            nostk_cp = nostk
            
            ## no stock
            nostk = max(nostk_cp, stk_cp + prices[i])
            ## have stock
            stk = max(stk_cp, nostk_cp - prices[i])
            
        return nostk

