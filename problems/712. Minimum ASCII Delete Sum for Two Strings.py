
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        dp[i][j]: the lowest ASCII sum of deleted characters to make s1[0 : i + 1] and s2[0 : j + 1] equal.
        """
        n1 = len(s1)
        n2 = len(s2)
        
        s1 = '*' + s1
        s2 = '*' + s2
        
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        
        for i in range(1, n1 + 1):
            ## delete all characters in s2
            dp[i][0] = sum([ord(s1[k]) for k in range(1, i + 1)])
        
        for j in range(1, n2 + 1):
            ### delete all characters in s1
            dp[0][j] = sum([ord(s2[k]) for k in range(1, j + 1)])
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + ord(s1[i]) + ord(s2[j]), dp[i - 1][j] + ord(s1[i]), dp[i][j - 1] + ord(s2[j]))
                    
        return dp[n1][n2]
        
        
        
        
