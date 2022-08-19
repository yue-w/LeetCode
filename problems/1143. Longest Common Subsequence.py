

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Reference
        https://www.youtube.com/watch?v=CEnb7Ho7TYc&t=545s

        dp[i][j]: The longest common subsequence of text1[0][i] and text2[0][j].
        The transition function: 
            if text1[i] == text2[j], then dp[i][j] = dp[i-1][j-1] + 1
            else, text1[i][j] = max(dp[i][j-1], dp[i-1][j])
        """
        M = len(text1)
        N = len(text2)

        ## append a token to word1 and word2 to make 1 indexed, to avoid
        ##  dealing with dp[-1] and dp[-1] below.
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

