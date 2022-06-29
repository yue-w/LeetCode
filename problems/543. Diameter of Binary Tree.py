# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 23:08:56 2020

@author: wyue
"""
from typing import Optional
##Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_v = 0
        self.dfs(root)
        
        return self.max_v
    
    def dfs(self, node):
        ## Base case
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.max_v = max(self.max_v, left + right)
        return 1 + max(left, right)

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
t.right = TreeNode(3)
print(Solution().diameterOfBinaryTree(t))