# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:00:32 2020

@author: wyue
## https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
def helper(root, result, level):
    if root != None:
        if len(result)<level:
            result.append([])
        result[level-1].append(root.val)
        helper(root.left, result, level+1)
        helper(root.right, result, level+1)
    
    
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root == None:
            return result
        helper(root, result, 1)
        
        return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
solution = Solution()
rst = solution.levelOrder(root)
print(rst)