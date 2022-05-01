# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 22:06:47 2020

@author: wyue
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
                nums[i] = 0
        
        for k in range(index,len(nums)):
            nums[k] = 0