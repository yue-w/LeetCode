

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        """
        dp[i][k]: the minimumal number of characters need to 
        change to divide s[0: i+1] into k non-empty disjoint 
        substrings such that each substring is a palindrome.
        dp[i][k] = min(dp[0:j+1][k-1] + helper(s[j:i+1])) 
        for j = 0, 1, ... i, where helper(s[j:i+1]) return
        the number of characters need to change to make 
        s[j:i+1] parlindrom.
        """        
        
        n = len(s)
        
        dp = [[float('inf') for _ in range(k + 1)] for _ in range(n + 1)]
        
        s = '*' + s
        
        
        ## initialize corner values
        dp[0][0] = 0
        
        ## helper is called to compute a cache of the min count of change needed to make s[i:j+1] to parlindrome
        self.helper(s, n)
        
        for i in range(1, n + 1):
            for kk in range(1, min(i, k) + 1):
                for j in range(kk-1, i+1):
                    ## to calculate the count of deletion in s[j:i+1],
                    ## we can use DP to calculate a cach and look up
                    ## or we can call a helper function to compute it 
                    ## every time
                    ## method 1: use DP to compute a cache
                    temv = dp[j-1][kk-1] + self.count[j][i]
                    ## method 2: compute it every time
                    #temv = dp[j-1][kk-1] + self.helper(s, j, i)
                    dp[i][kk] = min(dp[i][kk], temv)
        
        return dp[n][k]
    
        
    def helper(self, s, n):
        ## compute a cache of the min count of change needed to make s[i:j+1] to parlindrome
        self.count = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        
        
        for length in range(2, n + 1):
            for i in range(1, n + 2 - length):
                j = i + length - 1
                if s[i] == s[j]:
                    self.count[i][j] = self.count[i+1][j-1]
                else:
                    self.count[i][j] = self.count[i+1][j-1] + 1
        


        

