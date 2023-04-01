# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 12:38:42 2020

@author: wyue
https://leetcode.com/problems/symmetric-tree/
101. Symmetric Tree
"""

##Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import queue
from typing import Optional
class Solution(object):
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #return self.method1(root.left, root.right)
        return self.method2(root)
        
        
    def method1(self, root):

        def dfs(left, right):
            if left is None:
                return right is None
            elif right is None:
                return False
            else:
                if left.val != right.val:
                    return False
                else:
                    return dfs(left.right, right.left) and dfs(left.left, right.right)

        return dfs(root.left, root.right)
            
    ## Iteration method    
    def method2(self, root):
        q = queue.Queue()
        q.put(root)
        q.put(root)
        while not q.empty():
            left = q.get()
            right = q.get()
            if (left is None) and (right is None):
                continue
            if (left is None) or (right is None):
                return False
            if left.val != right.val:
                return False
            q.put(left.left)
            q.put(right.right)
            q.put(left.right)
            q.put(right.left)
            
        return True
            

node = TreeNode(1)
node.left = TreeNode(3)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right.left = TreeNode(5)
node.right.right = TreeNode(4)

print(Solution().isSymmetric(node))