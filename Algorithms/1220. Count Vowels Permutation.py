

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        return self.method1(n)
        #return self.method2(n) ## preferred method
    
    def method1(self, n):
        """
        Recursion + memo
        """
        def dfs(cur_ch, cur_idx):
            """
            add 1 to result if len(curr) = n, otherwise, recurse (only if curr satisfies the rule). 
            """
            ## base case
            if cur_idx == n:
                memo[cur_ch][cur_idx] = 1
                return 1
            
            if cur_idx in memo[cur_ch]:
                return memo[cur_ch][cur_idx]
            
            tem = 0
            for j in range(5):
                if cur_ch == a:
                    if j == e:
                        tem += dfs(j, cur_idx + 1)
                elif cur_ch == e:
                    if j == a or j == i:
                        tem += dfs(j, cur_idx + 1)
                elif cur_ch == i:
                    if j != i:
                        tem += dfs(j, cur_idx + 1)
                elif cur_ch == o:
                    if j == i or j == u:
                        tem += dfs(j, cur_idx + 1)
                else: #u
                    if j == a:
                        tem += dfs(j, cur_idx + 1)
            memo[cur_ch][cur_idx] = tem    
            return tem
            
        self.rst = 0
        #vowel = ('a', 'e', 'i', 'o', 'u')
        a, e, i, o, u = 0, 1, 2, 3, 4
        memo = [{} for _ in range(5)]
        rst = 0
        for k in range(5):
            rst += dfs(k, 1)
        M = int(1e9+7)
        return rst % M          
                
    def method2(self, n):
        """
        DP.
        dp[i][0]: count of strings of s[i:n] can be formed if s[i] == 'a'
        dp[i][1]: count of strings of s[i:n] can be formed if s[i] == 'e'
        ...
        """
        a, e, i, o, u = 0, 1, 2, 3, 4
        dp = [1] * 5
        for _ in range(n-2, -1, -1): ## note that token i has been used.
            dp_cp = dp[:]
            dp[a] = dp_cp[e]
            dp[e] = dp_cp[a] + dp_cp[i]
            dp[i] = dp_cp[a] + dp_cp[e] + dp_cp[o] + dp_cp[u]  
            dp[o] = dp_cp[i] + dp_cp[u]
            dp[u] = dp_cp[a]
        
        M = 10**9+7
        return sum(dp) % M
                    
if __name__ == '__main__':
    n = 144
    rst = Solution().countVowelPermutation(n)
    print(rst)
            
            
            
        