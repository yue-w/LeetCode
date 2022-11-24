

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
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