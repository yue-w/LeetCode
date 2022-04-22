# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:41:37 2020

@author: wyue
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
      
def helper(root, min_v, max_v):
    ## Base case
    if not root:
        return True
    elif root.val>=max_v or root.val<=min_v:
        return False
    else:
        return helper(root.left, min_v, root.val)\
            and helper(root.right,root.val,max_v)
        

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        valid = helper(root,float('-inf'), float('inf'))
        return valid

s = Solution()
t = TreeNode(2)
t.left = TreeNode(1)
t.right = TreeNode(3)
print(s.isValidBST(t))