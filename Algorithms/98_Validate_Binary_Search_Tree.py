# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:41:37 2020

@author: wyue
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
      
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Recursion
        """
        #return self.recursion(root, float('-inf'), float('inf'))
        #return self.iteration(root)
        
    def recursion(self, root, minv, maxv):
        ## Base case:
        if not root:
            return True
        if root.val <= minv or root.val >= maxv:
            return False
        return self.recursion(root.left, minv, root.val) and self.recursion(root.right,root.val, maxv)
        
    
    def iteration(self, root):
        if not root:
            return True
        stack = []
        stack.append((root, float('-inf'), float('inf')))
        
        while stack:
            curr = stack.pop()
            
            if not curr[0]:
                continue
                
            if curr[0].val <= curr[1] or curr[0].val >= curr[2]:
                return False
            
            if curr[0].left:
                stack.append((curr[0].left, curr[1], curr[0].val))
            if curr[0].right:
                stack.append((curr[0].right, curr[0].val, curr[2]))
        
        return True
s = Solution()
t = TreeNode(2)
t.left = TreeNode(1)
t.right = TreeNode(3)
print(s.isValidBST(t))