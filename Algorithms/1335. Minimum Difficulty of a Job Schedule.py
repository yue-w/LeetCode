
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """
        dp[i][k]:  the minimum difficulty of a job schedule 
        for assigning jobDifficulty[0: i + 1] to k groups

        Transition function: dp[i][k] = min{dp[0:j][k-1] + max(jobDifficulty[j:i+1]), for j = 0, 1, .... i}
        Time: O(n*n*d)
        """
        
        if len(jobDifficulty) < d:
            return -1
        
        n = len(jobDifficulty)
        
        dp = [[float('inf') for _ in range(d + 1)] for _ in range(n + 1)]
        
        ## make it 1 indexed to make it earsier to set boundary values
        jobDifficulty = [-1] + jobDifficulty
        
        ## set boundary values of dp, e.g. dp[i][0]
        dp[0][0] = 0
        
        for i in range(1, n + 1):
            for k in range(1, min(i, d) + 1):
                maxd = jobDifficulty[i]
                for j in range(i, k - 2, -1):
                    maxd = max(maxd, jobDifficulty[j])
                    temv = dp[j - 1][k - 1] + maxd
                    dp[i][k] = min(dp[i][k], temv)
                    
                    
        return dp[n][d]
                
        
        
        
