
class Solution:
    def countHousePlacements(self, n: int) -> int:
        """
        DP. 
        dp[i]: ways to place house from 1 to i.
        dp[i] = (do not put ith house) + (put ith house) = dp[i - 2] + dp[i - 1]
        """
        dp = [0 for _ in range(n + 2)]
        dp[1] = 2
        dp[2] = 3
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        
        M = int(1e9 + 7)
        return (dp[n] * dp[n]) % M