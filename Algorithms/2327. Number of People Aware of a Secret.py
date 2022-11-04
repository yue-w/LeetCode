

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        #return self.method1(n, delay, forget)
        return self.method2(n, delay, forget) ## preferred method
        
    
    def method1(self, n, delay, forget):
        """
        dp[i]: number of new people were told the secret
        time: O(n^2)
        Space: O(n)
        """
        ## dp is 1 indexed. dp[0] is dummy
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n+1):
            start = max(0, i - forget + 1)
            end = max(0, i - delay)
            ## only in this time window, can the people got the secret
            ## on day j share the secret on day i
            for j in range(start, end+1):
                dp[i] += dp[j]
        
        ## check each day, if the person can still remember the secret until day n
        ## add it
        rst = 0
        for d in range(1, n+1):
            if d + forget > n:
                rst += dp[d]
        
        return rst % (10**9+7)
                
    def method2(self, n, delay, forget):
        """
        dp + sweeping ine
        dp[i]: number of new people were told the secret
        time: O(n)
        Space: O(n)
        """
        ## dp is 1 indexed. dp[0] is dummy
        dp = [0] * (n + 1)
        dp[1] = 1
        
        ## diff is the fifference betwen day i and day i - 1
        ## diff[i] = dp[i] - dp[i - 1], or dp[i] = dp[i-1] + diff[i]
        diff = [0] * (n + 1)
        diff[1] = 1
        diff[2] = -1
        
        
        for i in range(1, n+1):
            dp[i] = dp[i-1] + diff[i]
            
            ## update diff
            if i + delay <= n:
                diff[i+delay] += dp[i]
            if i + forget <= n:
                diff[i+forget] -= dp[i]
            
        
        ## check each day, if the person can still remember the secret until day n
        ## add it
        rst = 0
        for d in range(1, n+1):
            if d + forget > n:
                rst += dp[d]
        
        return rst % (10**9+7)
        
        