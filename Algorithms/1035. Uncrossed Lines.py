from typing import List
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """
        dp[i][j]: maximum number of connecting lines we can draw with between nums1[0: i + 1] and nums[0: j + 1]
        """
        n1 = len(nums1)
        n2 = len(nums2)
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        nums1 = [0] + nums1
        nums2 = [0] + nums2
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        
        return dp[n1][n2]
        
        
        
        
