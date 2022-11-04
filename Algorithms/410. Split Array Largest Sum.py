from typing import List

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        #return self.method1(nums, m) ## DP, TLE
        return self.method2(nums, m) ## Preferred method. Binary search.
        
    def method1(self, nums, m):
        """
        DP. TLE
        dp[i][k]: The minimimal of the largest sum for nums[0:i+1] to k groups
        transition function: dp[i][k] = min{max(dp[j][k-1], sum(nums[j:i+1]), for j = 1,2,...i}
        X X X X X [X X i]
        """
        n = len(nums)
        
        nums = [0] + nums
        
        ## check initial value
        dp = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
        
        # ## dp[i][0] = float('inf')
        # for i in range(1, n + 1):
        #     dp[i][0] = float('-inf')
        
        dp[0][0] = 0
        
        ## dp in iteration
        for i in range(1, n + 1):
            for k in range(1, min(i, m) + 1):
                cursum = 0
                for j in range(i, k - 2, -1):
                    cursum += nums[j]
                    temv = max(dp[j-1][k-1], cursum)
                    dp[i][k] = min(dp[i][k], temv)
        
        return dp[n][m]
    
    def method2(self, nums, m):
        """
        Binary search
        """
        def possible(cap):
            """
            check whether it is possible to divide nums into m 
            groups with each subgroup has a sum less than cap.
            Return True if possible.
            """
            n = len(nums)
            count = 1
            i = 0
            while count <= m:
                count += 1
                remaincap = cap
                ## if full cap is smaller than nums[i], return False
                if remaincap - nums[i] < 0:
                    return False
                while remaincap - nums[i] >= 0:
                    remaincap -= nums[i]
                    i += 1
                    if i > n - 1:
                        return True
            return False
            
            
        low = min(nums)
        high = sum(nums)
        
        while low < high:
            mid = low + (high - low) // 2
            ## if mid is possible, guess smaller value
            if possible(mid):
                high = mid
            else:
                low = mid + 1

        return low

if __name__ == '__main__':
    nums = [7,2,5,10,8]
    m = 2
    rst = Solution().splitArray(nums, m)
    print(rst)