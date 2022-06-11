from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        
        dp = [[0 for _ in range(2)] for _ in range(N)]
        
        dp[0][0] = 1
        dp[0][1] = 1
        
        for i in range(1, N):
            if nums[i] > nums[i - 1]:
                ## increasing sequence equals decreasing sequence plus 1
                dp[i][0] = dp[i - 1][1] + 1
                # ## decreasing sequence not change
                dp[i][1] = dp[i - 1][1]
            
            elif nums[i] < nums[i - 1]:
                ## decreasing sequence equals increasing sequense plus 1
                dp[i][1] = dp[i - 1][0] + 1
                # ## increasing not change
                dp[i][0] = dp[i - 1][0]
            else:
                dp[i][0] = dp[i - 1][0]
                dp[i][1] = dp[i - 1][1]
        
        return max(dp[N-1])
      
"""
DP
dp[i][0] count of increasing subsequence
dp[i][1] count of decreasing subsequence
"""
if __name__ == '__main__':
    nums = [1,7,4,9,2,5]
    rst = Solution().wiggleMaxLength(nums)
    print(rst)