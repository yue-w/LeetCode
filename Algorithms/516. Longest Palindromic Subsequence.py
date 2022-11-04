class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        #return self.method1(s)
        return self.method2(s)
        
        
    def method1(self, s):
        """
        DP with recursion and memoization
        """
        memo = {}
        return self.recursion(s, 0, len(s) - 1, memo)
        
    def recursion(self, s, left, right, memo):
        ## Base case 1: two pointers meet
        if left == right:
            return 1
        ## Base case 2: two pointers cross
        if left > right:
            return 0
        ## Base case 3: calculated before
        if (left, right) in memo:
            return memo[(left, right)]
        
        
        if s[left] == s[right]:
            return 2 + self.recursion(s, left + 1, right - 1, memo)
        else:
            leftv = self.recursion(s, left, right - 1, memo)
            rightv = self.recursion(s, left + 1, right, memo)
            maxv = max(leftv, rightv)
            memo[(left, right)] = maxv
            return maxv
        
        
    def method2(self, s):
        """
        DP with table.
        dp[i][j]: the longest palindromic subsequence's length in s[i:j+1].
        Time: O()
        """
        n = len(s)
        
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        
        ## add a special token to make it 1 indexed
        s = '*' + s
        
        ## boundary values
        for i in range(1, n + 1):
            dp[i][i] = 1
        
        
        ## loop length of the substring. Start from at least 2 characters so that i + 1 <= j - 1
        ## in the transition function below.
        for length in range(2, n + 1):
            # loop the starging point of the substring
            ## the upper bound of i is computed by setting j <= n (j = i + length - 1)
            for i in range(1, n - length + 2):
                j = i + length - 1
                ## transotion function
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
   
                
        return dp[1][n]
        
        
            