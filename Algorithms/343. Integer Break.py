

class Solution:
    def integerBreak(self, n: int) -> int:
        #return self.method1(n)
        return self.method2(n)
    
    def method1(self, n):
        """
        DFS with memo (DP top down).
        """
        def dfs(num):
            if num == 1:
                return 1    
            if num in memo:
                return memo[num]
            # if num is n, the number must be divided
            # otherwise, the number can be itself
            val = -1 if num == n else num
                
            for i in range(1, num):
                tem = dfs(i) * dfs(num - i)
                val = max(val, tem)
            memo[num] = val
            return val
                
        memo = {}
        rst = dfs(n)
        return rst
        
    def method2(self, n):
        """
        DP bottom up with table.
        dp[i]: Given an integer i, break it into the sum of k>=2 positive integers, 
        and maximize the product of those integers.
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        dp = [0 for _ in range(n + 1)]
        
        ## boundry conditions
        dp[2] = 2
        dp[3] = 3
        
        for i in range(4, n + 1):
            for j in range(2, i//2 + 1):
                dp[i] = max(dp[i], dp[j] * dp[i - j])
        
        
        return dp[n]