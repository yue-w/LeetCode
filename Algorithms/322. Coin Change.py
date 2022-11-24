from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Thoughts: dfs with memo.
        """
        def dfs(val):
            if val == 0:
                return 0
            if val < 0:
                memo[val] = -1
                return -1

            min_sum = -1
            for c in coins:
                if val - c in memo:
                    tem = memo[val - c]
                else:
                    tem = dfs(val - c)
                    memo[val-c] = tem
                if tem != -1:
                    if min_sum == -1 or min_sum > tem:
                        min_sum = tem + 1
            
            return min_sum
        
        ## remove duplicates 
        coins = list(set(coins))
        
        coins.sort(reverse=True)
        memo = {}
        return dfs(amount)


if __name__ == '__main__':
    solution = Solution()
    coins = [2,5,10,1]
    amount = 27
    rst = solution.coinChange(coins, amount)
    print(rst)