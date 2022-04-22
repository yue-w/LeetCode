from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Thoughts: usge dynamic programming, use back tracking?
        """

        memo = {}
        rst = self.recursion(coins, amount, memo)
        return rst

    
    def recursion(self, coins, remain, memo):
        ## Base cases
        if remain == 0:
            memo[0] = 0
            return 0
        if remain < 0:
            memo[remain] = -1
            return -1 
        min_sum = -1
        for coin in coins:
            if remain - coin not in memo:
                running_sum =  self.recursion(coins, remain-coin, memo)
                memo[remain-coin] = running_sum

            else:
                running_sum = memo[remain-coin]
            if running_sum > -1:
                running_sum += 1
                if min_sum == -1 or min_sum > running_sum:
                    min_sum = running_sum

        return min_sum


if __name__ == '__main__':
    solution = Solution()
    coins = [2,5,10,1]
    amount = 27
    rst = solution.coinChange(coins, amount)
    print(rst)