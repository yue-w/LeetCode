
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        """
        dp[i][j]: the minimum amount of money you need to guarantee a win for guessing number 
        between i and j (inclusive).
        Transition function:
        dp[i][j] = max{dp[i][k-1], dp[k+1][j]} for k in range i and j (inclusive)
        """
        dp = [[float('inf') for _ in range(n + 3)] for _ in range(n + 3)]         
        
        ## boundary values
        for i in range(n + 2):
            dp[i][0] = 0
            dp[0][i] = 0
            dp[i][i] = 0
            
        for length in range(2, n + 1):
            # j <= n
            for i in range(1, n - length + 2):
                j = length + i - 1
                #dp[i][j] = float('inf')
                for k in range(i, j + 1):
                    tem = k + max(dp[i][k-1], dp[k+1][j])
                    dp[i][j] = min(dp[i][j], tem)         
                    
        return dp[1][n]
   
if __name__ == '__main__':
    n = 10
    rst = Solution().getMoneyAmount(n)
    print(rst)    
