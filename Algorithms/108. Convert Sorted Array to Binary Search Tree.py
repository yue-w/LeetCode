# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 22:56:36 2020

@author: wyue
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        n = len(nums)
        return self.helper(nums, 0, n-1)
    
    def helper(self, nums, low, high):
        if low>high:
            return None
        mid = int((low+high)/2)
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, low, mid-1)
        node.right = self.helper(nums, mid+1, high)
        
        return node
        

    