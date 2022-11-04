# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:29:48 2020

@author: wyue
"""

##Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    
    ## Method 1 BFS
    # def largestValues(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     if root == None: return []
    #     rst = []
    #     nodes = [root]
    #     while len(nodes)>0:
    #         rst.append(max([n.val for n in nodes]))
    #         nodes = [kid for node in nodes for kid in [node.left, node.right] if kid!=None ]
                
            
        # return rst

    # ## Method 2: recursion
    # def largestValues(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     rst = []
    #     self.helper(0, rst, root)
        
    #     return rst


    # def helper(self, level, rst, node):
    #     if not node:
    #         return 
        
    #     ## if this is the fist node of this level, just put this node in the list
    #     if level == len(rst):
    #         rst.append(node.val)
    #     else:
    #         rst[level] = max(rst[level], node.val)
    #     ## next level
    #     self.helper(level+1, rst, node.left)
    #     self.helper(level+1, rst, node.right)
    
    # Method 1 BFS
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        rst = []
        curr_level = [root]
        
        while curr_level:
            rst.append(-float('inf'))
            next_level = []
            
            for node in curr_level:
                if node:
                    rst[-1] = max(rst[-1], node.val)
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
            
            curr_level = next_level
        return rst
    
node = TreeNode(1)
node.left = TreeNode(3)
node.right = TreeNode(2)
node.left.left = TreeNode(5)
node.left.right = TreeNode(3)
node.right.right = TreeNode(9)

print(Solution().largestValues(node))