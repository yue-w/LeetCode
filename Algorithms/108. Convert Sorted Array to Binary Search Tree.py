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
        def dfs(le, ri):
            ## base case
            if le > ri:
                return None

            mid = le + (ri - le) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(le, mid - 1)
            root.right = dfs(mid + 1, ri)
            return root

        root = dfs(0, len(nums) - 1)
        return root
        

    