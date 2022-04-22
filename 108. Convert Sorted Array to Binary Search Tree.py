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
    
    ## My original solution
    # def sortedArrayToBST(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: TreeNode
    #     """
    #     if not nums:
    #         return None
    #     n = len(nums)
    #     root = TreeNode()
    #     self.helper(nums, 0, n-1, root)
        
    #     return root
        
    # def helper(self, nums, low, high, node):
    #     if low == high:
    #         node.val = nums[low]
    #         node.left = None
    #         node.right = None
    #         return 
    #     elif low == high-1:
    #         node.val = nums[high]
    #         if nums[low]>nums[high]:
    #             node.right =  TreeNode(nums[low])  
    #         else:
    #             node.left = TreeNode(nums[low])
                
    #         return
    #     else:
    #         mid = int((low+high)/2)
    #         node.val = nums[mid]
    #         node.left = TreeNode()
    #         self.helper(nums,low, mid-1,node.left)
    #         node.right = TreeNode()
    #         self.helper(nums,mid+1,high,node.right)
    
    ## A better solution.
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
        

    