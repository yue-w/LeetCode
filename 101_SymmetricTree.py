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

class Solution(object):
    
    ## Recursion
    # def isSymmetric(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     if root == None: return True
    #     return self.helper(root.left, root.right)
        
    # def helper(self, left, right):
    #     if left==None or right==None:
    #         return left == right
    #     if left.val != right.val:
    #         return False
    #     ## left child's left child equals right child's right child, left child's right child equals right child's left child
    #     return self.helper(left.left, right.right) and self.helper(left.right, right.left)

    
    ## Iteration
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = queue.Queue()
        q.put(root)
        q.put(root)
        
        while not q.empty():
            left = q.get()
            right = q.get()
            if left == None and right == None:
                continue
            if left==None or right == None:
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