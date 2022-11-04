class Solution:
    def climbStairs(self, n: int) -> int:
        # ## DP with recursion
        # memo = {}
        # rst = self.recursion(n, memo)
        # return rst
        
        ## DP with tabular
        #return self.tabular(n)
        return self.tabular2(n)
    def recursion(self, n, memo):
        # Base case:
        if n == 0 or n == 1:
            return 1
        if n - 1 not in memo:
            one_step = self.recursion(n-1, memo) 
            memo[n - 1] = one_step
        else:
            one_step = memo[n - 1]
        if n - 2 not in memo:
            two_step = self.recursion(n-2, memo)
            memo[n - 2] = two_step
        else:
            two_step = memo[n - 2]
        memo[n] = one_step + two_step
        return one_step + two_step
        
        
    def tabular(self, n):
        if n == 1:
            return 1
        table = [0] * n
        table[0] = 1
        table[1] = 2
        for i in range(2, n):
            table[i] = table[i - 1] + table[i - 2]
            
        return table[-1]
    
    def tabular2(self, n):
        """
        Same with tabular, but use two variables instead of two arrays
        """
        if n == 1:
            return 1

        t1 = 1
        t2 = 2
        for i in range(2, n):
            #table[i] = table[i - 1] + table[i - 2]
            t1c = t1
            t2c = t2
            t2 = t1c + t2c
            t1 = t2c
            
        return t2
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        