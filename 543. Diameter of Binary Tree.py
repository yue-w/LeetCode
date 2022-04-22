# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 23:08:56 2020

@author: wyue
"""

##Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ## Check input
        if not root:
            return None ## Check with interviewer 0 or None
        if not root.left and not root.right:
            return 0
        self.max = 0
        
        self.helper(root)
        return self.max
            
    def helper(self,node):
        if node.left == None:
            left_depth_max = 0
        else:
            left_depth_max = self.helper(node.left) + 1
        if node.right == None:
            right_depth_max = 0
        else:
            right_depth_max = self.helper(node.right) + 1
            
        self.max = max(left_depth_max + right_depth_max, self.max)
        return max(left_depth_max, right_depth_max)

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
t.right = TreeNode(3)
print(Solution().diameterOfBinaryTree(t))