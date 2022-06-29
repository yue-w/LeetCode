
class Solution:
    def numberOfWays(self, s: str) -> int:
        return self.method2(s)
    
    def method1(self, s):
        """
        DP with table
        TLE
        """
        n = len(s)
        
        s = '*' + s
        
        ## dp[i][j][k]: ith string, have selected j strings, with the last selectged string being k
        dp = [[[0 for _ in range(2)] for _ in range(4)] for _ in range(n + 1)]
        
        dp[0][0][0] = 1
        dp[0][0][1] = 1
        
        for i in range(1, n + 1):
            for j in range(4):
                for k in range(2):
                    dp[i][j][k] = dp[i-1][j][k]
                    if j - 1 >= 0 and int(s[i]) == (1 - k):
                        dp[i][j][k] += dp[i-1][j-1][1-k]
                        
        return dp[n][3][0] + dp[n][3][1] 
    
    def method2(self, s):
        """
        DP
        """
        dp = {"0": 0, "1": 0, "01": 0, "10": 0, "010": 0, "101": 0}
        for i in range(len(s)):
            if s[i] == "0":
                dp["0"] += 1
                dp["10"] += dp["1"]
                dp["010"] += dp["01"]
            if s[i] == "1":
                dp["1"] += 1
                dp["01"] += dp["0"]
                dp["101"] += dp["10"]
                
        return dp["010"] + dp["101"]
        
        