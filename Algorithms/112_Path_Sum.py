# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 18:17:38 2020

@author: wyue
"""
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
    #     ## Mehtod 1: Recursion
    #     v = 0
        
    #     self.rst = False
    #     if not root: return False
    #     self.helper(root,sum,v)
        
    #     return self.rst
    
    # def helper(self,root,sum, v):
    #     if self.rst == True: return 
    #     if root.left ==None and root.right == None:
    #         if v+root.val == sum:
    #             self.rst = True
    #             return 
        
    #     v += root.val
    #     if root.left:
    #         self.helper(root.left, sum, v)
    #     if root.right:
    #         self.helper(root.right, sum,v)
        
        ## Method 2: Iteration.
        if not root:
            return False
        
        stack = []
        stack.append((root,sum-root.val))
        while stack:
            node,sum = stack.pop()
            if (not node.left) and (not node.right) and sum==0:
                return True
            if node.left:
                stack.append((node.left, sum-node.left.val))
            if node.right:
                stack.append((node.right, sum-node.right.val))
            
        return False




t = TreeNode(1)
t.left = TreeNode(2)
t.left.left = TreeNode(3)
t.left.right = TreeNode(0)
t.right = TreeNode(0)
t.right.left = TreeNode(0)
t.right.right = TreeNode(0)

print(Solution().hasPathSum(t,6))