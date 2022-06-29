
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.method1(amount, coins)

    def method1(self, amount, coins):
        """
        recursion and memoization
        """
        memo = {}
        return self.dfs(coins, amount, 0, memo)
        
    
    def dfs(self, coins, remain, index, memo):
        """
        index = 0 to len(coins) - 1, whether to use ith coin
        """
        ## base cases
        if remain == 0:
            return 1
        if remain < 0:
            return 0
        if index >= len(coins):
            return 0
        ## if already in memo
        if (index, remain) in memo:
            return memo[(index, remain)]
        
        use_index = self.dfs(coins, remain - coins[index], index, memo)
        not_index = self.dfs(coins, remain, index + 1, memo)
        total = use_index + not_index
        memo[(index, remain)] = total
        return total
    def method2(self, amount, coins):
        ## TODO
#         """
#         DP using table
#         dp[i][j]: count of ways to sum to i using coins[0: j + 1]
#         dp[i][j] = count of ways to sum to i using coin[j] plus ways to sum to i not using coin[j]
#         """
        
#         n = len(coins)
#         coins = [0] + coins
        
#         dp = [[0 for _ in range(n + 1)] for _ in range(amount + 1)]
        
#         ## dp[0][:] = 1 when using 0 coins for amount 0, there is 1 way.
#         for c in range(n + 1):
#             dp[0][c] = 1
        
#         for amt in range(1, amount + 1):
#             for c in range(n + 1):
#                 ## use coins[c]
#                 if amt + coins[c] <= amount:
#                     use = dp[amt - coins[c]][c]
#                 else:
#                     use = 0
#                 ##  not use coins[c]
#                 if c + 1 <= n:
#                     not_use = dp[amt][c + 1]
#                 else:
#                     not_use = 0
#                 dp[amt][c] = use + not_use
        
#         return dp[-1][-1]
#  
if __name__ == '__main__':
    amount = 5
    coins = [1,2,5]
    rst = Solution().change(amount, coins)
    print(rst)