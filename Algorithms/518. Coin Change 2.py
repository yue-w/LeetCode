
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.method1(amount, coins)

    def method1(self, amount, coins):
        """
        recursion and memoization
        """
        def dfs(need, idx):
            ## base case 1
            if need == 0:
                return 1
            ## base case 2
            if need < 0:
                return 0
            ## base case 3
            if (need, idx) in memo:
                return memo[(need, idx)]
            count = 0
            for i in range(idx, len(coins)):
                count += dfs(need - coins[i], i)
            memo[(need, idx)] = count
            return count
        coins.sort(reverse=True)
        memo = {}
        rst = dfs(amount, 0)
        return rst

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