

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        #return self.method1(low, high, zero, one)
        return self.method2(low, high, zero, one)
        
    def method1(self, low, high, zero, one):
        """
        DFS with memo
        """
        def dfs(cur_len):
            if cur_len in memo:
                return memo[cur_len]
            if cur_len > high:
                return 0

            tem = 0
            if low <= cur_len <= high:
                tem += 1
                
            zeros =  dfs(cur_len + zero) % self.M
            ones = dfs(cur_len + one) % self.M
            
            memo[cur_len] = tem + zeros + ones
            return (tem + zeros + ones) % self.M 
        
        memo = {}
        self.M = int(10**9+7)
        return dfs(0) % self.M
    
    
    def method2(self, low, high, zero, one):
        M = int(10**9+7)
        
        DP = [0] * (high + 1)
        DP[0] = 1
        
        for i in range(1, high + 1):
            if i - zero >= 0:
                DP[i] += DP[i - zero] 
            if i - one >= 0:
                DP[i] += DP[i - one] 

        rst = sum(DP[i] for i in range(low, high + 1))
        return rst % M