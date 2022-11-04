# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 16:32:22 2020

@author: wyue
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # memo = {}
        # return self.DP_recursion(nums, 0, len(nums) - 1, memo)
        # return self.DP_botton_up(nums)
        return self.dp_table(nums)
    def DP_recursion(self, nums, i, n, memo):
        ## Base case
        if i == n:
            return nums[i]
        if i >= n:
            return 0
        ## if in memo
        if i in memo:
            return memo[i]
        maxv = max(nums[i] + self.DP_recursion(nums, i + 2, n, memo), self.DP_recursion(nums, i + 1, n, memo))
        memo[i] = maxv
        return maxv
    
    def DP_botton_up(self, nums):
        if nums == []: 
            return 0
        if len(nums) == 1: 
            return nums[0]
        if len(nums) == 2: 
            return max(nums)
        prepre = nums[0]
        pre = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            cur = max(prepre + nums[i], pre) 
            prepre = pre
            pre = cur  
        return pre
    
    def dp_table(self, nums):
        """
        This is the preferred method.
        Reference: https://www.youtube.com/watch?v=IcEX9Oi_tao
        dp_rob[i]: max amount if rob house i. dp_rob[i]
                  dp_rob[i] = max(dp_not[i-1] + nums[i])
        dp_notrob[i]: max amount if not rob house i. dp_notrob[i]. 
                  dp_notrob[i] = max(dp_rob[i-1], dp_notrob[i-1])
        """
        if not nums:
            return 0
        
        rob = nums[0]
        norob = 0
        
        for i in range(1, len(nums)):
            norob_tmp = norob
            norob = max(rob, norob)
            rob = norob_tmp + nums[i]
        
        return max(rob, norob)

nums = [2, 1, 1, 2]
print(Solution().rob(nums))
