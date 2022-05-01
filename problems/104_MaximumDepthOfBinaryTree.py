# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 23:28:39 2020

@author: wyue
"""
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    ## Method 1: recersion
    def maxDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ## Base case
        if root is None: return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
    
    
    ## Method 2: stack
    def maxDepth(self, root):
        stack = []
        if root is not None:
            stack.append((root,0))
        maxDepth = 0
        while len(stack)>0:
            root,depth = stack.pop()
            if maxDepth<depth:
                maxDepth = depth
            if root is not None:
                stack.append((root.left, depth+1))
                stack.append((root.right, depth+1))
        return maxDepth
    

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution=Solution()
print(solution.maxDepth(root))