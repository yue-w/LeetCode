from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        Define dp[i][j]: maximum coins you can collect by bursting the balloons nums[i:j+1]
        Transition function:
        define k as the last ballon you burst in nums[i:j+1]
        ... i xxxxxxx k xxxxxx j...
        reference: https://www.youtube.com/watch?v=BBdHB2jjNUA
        """

        n = len(nums)
        
        dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
        
        ## On both side, add an extra bollon. Becaues "If i - 1 or i + 1 
        ## goes out of bounds of the array, then treat it as if there is 
        ## a balloon with a 1 painted on it."
        nums = [1] + nums + [1]
        
        for length in range(1, n + 1):
            ## j = i + length - 1, j <= n => i <= n - length + 1
            for i in range(1, n - length + 2):
                j = i + length - 1
                for k in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], dp[i][k-1] + nums[i - 1] * nums[k] * nums[j + 1] + dp[k+1][j])
                    
        return dp[1][n]
                
        
        

                
        
        
