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
    def hasPathSum(self, root, targetSum):
        return self.method1(root, targetSum)
    
    def method1(self, root, targetSum):
        if not root:
            return False
        
        def dfs(node, cur):
            # base case
            # if leaf
            if (not node.left) and (not node.right):
                return cur == node.val
            cur -= node.val

            if node.left and dfs(node.left, cur):
                return True
            if node.right and dfs(node.right, cur):
                return True
            return False

        return dfs(root, targetSum)
    
    def method2(self, root, targetSum):
        
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