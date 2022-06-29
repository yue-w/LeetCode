class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        dp[i][j]: the number of distinct subsequences of s[:i+1] that
        equals t[:j+1].
        if s[i] == t[j]: dp[i][j] equals dp[i-1][j-1] plus the number of distinct 
        subsequences of s[:i] and t[:j+1] because s[i-1] may also equals t[j], 
        i.e. the subsequences of s[:i] may also equals t[:j+1]
        """
        n1 = len(s)
        n2 = len(t)
        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        s = '*' + s
        t = '*' + t
        
        ## base cases 
        ## if t is '', then s has 1 way to form a subsequence that 
        ## equals t (by selecting nothing from t).
        ## if s is '' but t is not '', there is no way a subsequence of s
        ## equals t.  
        for i in range(n1 + 1):
            dp[i][0] = 1

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s[i] == t[j]:
                    ## don't forget the dp[i-1][j] term
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

                else:
                    dp[i][j] += dp[i-1][j]

        return dp[n1][n2]
     
        
if __name__ == '__main__':
    s = "rabbbit" 
    t = "rabbit"
    rst = Solution().numDistinct(s, t)
    print(rst)

        
"""
dp[i][j]: the number of distinct subsequences of s[:i+1] which equals t[:j+1].
if s[i] == t[j]:
    dp[i][j] = dp[i-1][j-1]
else:
    dp[i][j] = dp[i-1][j]
"""