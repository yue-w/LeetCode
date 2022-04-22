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
        if nums == []: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        scores = [-1] * len(nums)
        scores[-1] = nums[-1]
        self.helper(nums, scores, 0)
        return scores[0]

    def helper(self,nums, scores, index):    
        ## Base case of recursion
        if len(nums)==0: 
            return 0
        if len(nums)==1:
            return scores[-1] 
        if len(nums) ==2:
            """
            value = nums[-2]
            scores[-2] = value
            """
            return max(nums)
            
        first = nums[0]
        if scores[index+2] != -1:
            sol1 = first + scores[index+2] 
        else:
            sol1 = first + self.helper(nums[2:], scores, index+2)
        if scores[index+1] != -1:
            sol2 = scores[index+1]
        else:
            sol2 = self.helper(nums[1:],scores, index+1)
        value = max(sol1, sol2)
        ## momization
        scores[index] = value
        return value

nums = [2,1,1,2]
print(Solution().rob(nums))
