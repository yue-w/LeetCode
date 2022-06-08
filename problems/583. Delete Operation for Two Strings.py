
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        
        ## append a token to word1 and word2 to make 1 indexed.
        word1 = '*' + word1
        word2 = '%' + word2
        

        
        dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        return len1 + len2 - dp[len1][len2] * 2
        
        
"""
Clarification:
same as find the longest common string. Then subtract it from the length of both strings
return len(word1) + len(word2) - dp[i][j] * 2
dp[i][j]: The longest common subsequence of word1[0][i] and word2[0][j].
The transition function: 
    if word1[i] == word2[j], then dp[i][j] = dp[i-1][j-1] + 1
    else, dp[i][j] = max(dp[i][j-1], dp[i-1][j])
""" 
