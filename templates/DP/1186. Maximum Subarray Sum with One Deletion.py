from typing import List
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        #return self.method1(arr)
        return self.method2(arr)
    
    def method1(self, arr):
        """
        dp[i][0]: max subarray ending at i, do not delete number
        dp[i][1]: max subarray ending at i, delete a number
        Transition funciton: 
        dp[i][0] = max(dp[i-1][0] + arr[i], arr[i]) ## two cases similar to Kandan algorithm
        dp[i][1] = max(dp[i-1][0], dp[i-1][1] + arr[i]) ## case 1: delete arr[i], case 2: delete some number other than arr[i]
        Time: O(n)
        Space: O(n)
        """
        N = len(arr)
        dp = [[0 for _ in range(2)] for _ in range(N)]
        dp[0][0] = arr[0]
        dp[0][1] = 0
        maxv = arr[0]
        for i in range(1, N):
            dp[i][0] = max(dp[i-1][0] + arr[i], arr[i])
            dp[i][1] = max(dp[i-1][0], dp[i-1][1] + arr[i])
            maxv = max(maxv, max(dp[i]))
            
        return maxv
            
    def method2(self, arr):
        """
        Preferred method
        Same with method1, save storage by matain two variables instead of an array.
        Time: O(n)
        Space: O(1)
        """
        N = len(arr)
        dp0 = arr[0]        
        dp1 = 0
        maxv = arr[0]
        for i in range(1, N):
            ## make a copy of dp0 and dp1
            dp0cp = dp0
            dp1cp = dp1
            dp0 = max(dp0cp + arr[i], arr[i])
            dp1 = max(dp0cp, dp1cp + arr[i])
            maxv = max(maxv, dp0, dp1)
            
        return maxv

"""

DP,
Prefix sum
"""