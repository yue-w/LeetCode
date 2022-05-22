

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Thoughts: brute force: O(n^2)
        
        """
        M = len(text1)
        N = len(text2)
        txt1 = '*' + text1
        txt2 = '*' + text2
        dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if txt1[i] == txt2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[M][N]
                