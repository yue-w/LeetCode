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
        # return self.recursion(nums, 0, len(nums) - 1, memo)
        return self.DP_botton_up(nums)
    
    def recursion(self, nums, i, n, memo):
        ## Base case
        if i == n:
            return nums[i]
        if i > n:
            return 0
        ## if in memo
        if i in memo:
            return memo[i]
        maxv = max(nums[i] + self.recursion(nums, i + 2, n, memo), self.recursion(nums, i + 1, n, memo))
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

nums = [2, 1, 1, 2]
print(Solution().rob(nums))
