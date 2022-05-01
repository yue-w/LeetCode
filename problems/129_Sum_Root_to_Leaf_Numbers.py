# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:26:27 2020

@author: wyue

Recursion
"""


# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
     
class Solution(object):
    def sumNumbers(self, root):
        self.total = 0
        if root == None:
            return 0
        if root.left==None and root.right==None:
            return root.val
        
        self.helper(root,'')
        return self.total
        
    def helper(self,node,pre):
        ## if leaf, return 
        if node.left == None and node.right==None:
            #nbs.append(pre+str(node.val))
            self.total += int(pre+str(node.val))
            return 
        pre += str(node.val)
        if node.left:
            self.helper(node.left, pre)
        if node.right:
            self.helper(node.right, pre)

    
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)

solu = Solution()
#solu.test()
print(solu.sumNumbers(t))

