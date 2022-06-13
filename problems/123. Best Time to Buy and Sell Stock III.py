
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.method2(prices) 
        #return self.method1(prices)
        
    def method1(self, prices):
        """
        DP with a table.
        dp[i][j]: j = 0, 1, 2, 3
        0: hold first stock (either held the first stock bought earlier or buy it on day i)
        1: sold fist stock (either still keeping the state of sold first stock or sell it on day i)
        2: hold second stock (either held the second stock bought earlier or buy it on day i (transerred from already sold first stock))
        3: sold second stock (either still keeping the state of sold second stock or sell it on day i (transferred from already bought first stock))
        Transition functions:
        dp[i][0] = max(dp[i - 1][0], -prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] - prices[i])
        dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] + prices[i])
        """        
        N = len(prices)
        dp = [[0 for _ in range(4)] for _ in range(N)]
        
        dp[0][0] = - prices[0]
        dp[0][2] = float('-inf')
        
        for i in range(1, N):
            dp[i][0] = max(dp[i - 1][0], -prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] - prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] + prices[i])
            
        return max(dp[-1])
    
    def method2(self, prices):
        """
        Same with method1, but use smaller space:
        use 1 set of variables (keep updating it) without using an array
        """
        N = len(prices)
        dp0 = float('-inf')
        dp1 = 0
        dp2 = float('-inf')
        dp3 = 0
        
        for i in range(N):
            dp0cp = dp0
            dp1cp = dp1
            dp2cp = dp2
            dp3cp = dp3
            dp0 = max(dp0cp, -prices[i])
            dp1 = max(dp1cp, dp0cp + prices[i])
            dp2 = max(dp2cp, dp1cp - prices[i])
            dp3 = max(dp3cp, dp2cp + prices[i])
        
        ## the best return must from state of sell.
        return max(dp1, dp3)

if __name__ == "__main__":
    prices = [3,3,5,0,0,3,1,4]
    #prices = [1,2,3,4,5]
    rst = Solution().maxProfit(prices)
    print(rst)