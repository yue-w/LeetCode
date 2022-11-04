from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        """
        dp[pers][prof]: the number of schemes to use pers people to get prof profit
        iterate through group and profit, for (x, y) in zip(group, profit)
        reference: https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/879.Profitable-Schemes
        """
        M = 1e9 + 7
        dp = [[0 for _ in range(minProfit + 1)] for _ in range(n + 1)]
        dp[0][0] = 1
        
        for x, y in zip(group, profit):
            dptem = [t[:] for t in dp]
            for pers in range(0, n + 1):
                for prof in range(0, minProfit + 1):
                    if pers + x <= n:
                        pp = min(minProfit, prof + y)
                        dptem[pers + x][pp] += dp[pers][prof]
                        dptem[pers + x][pp] %= M
            dp = dptem
            
        rst = 0
        for i in range(n+1):
            rst += dp[i][minProfit]
        

        return int(rst % M)
        

if __name__ == '__main__':
    n = 5
    minProfit = 3
    group = [2,2]
    profit = [2,3]
    rst = Solution().profitableSchemes(n, minProfit, group, profit)
    print(rst)