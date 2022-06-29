
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        dp[i][j]: minimum number of operations to convert word1[:i+1] 
        to word2[:j+1]
        """
        n1 = len(word1)
        n2 = len(word2)
        
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        
        ## edge conditions
        for i in range(n1 + 1):
            dp[i][0] = i
        for j in range(n2 + 1):
            dp[0][j] = j
        
        ## make 1 indexed 
        word1 = '*' + word1
        word2 = '*' + word2
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i-1][j] + 1, dp[i][j-1] + 1) 
        
        return dp[n1][n2]
        
if __name__ == '__main__':
    # word1 = 'horse'
    # word2 = 'ros'
    word1 = "intention"
    word2 = "execution"
    rst = Solution().minDistance(word1, word2)
    print(rst)