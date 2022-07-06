# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:00:32 2020

@author: wyue
## https://leetcode.com/problems/binary-tree-level-order-traversal/
"""
from queue import Queue
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
          
    
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #return self.method1(root)
        return self.method2(root) ## preferred method
    def method1(self, root):
        """
        DFS
        """
        result = []
        if root == None:
            return result
        self.dfs(root, result, 1)
        return result

    def dfs(self, root, result, level):
        if root != None:
            if len(result)<level:
                result.append([])
            result[level-1].append(root.val)
            self.dfs(root.left, result, level+1)
            self.dfs(root.right, result, level+1)
            
    def method2(self, root):
        """
        BFS. 
        """ 
        rst = []
        dq = deque()
        if root:
            dq.append(root)
        
        while dq:
            curr = []
            for _ in range(len(dq)):
                node = dq.popleft()
                curr.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            rst.append(curr)

        
        return rst
        



 


root = TreeNode(3)
root.left = TreeNode(9)
root.left.left = TreeNode(1)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
solution = Solution()
rst = solution.levelOrder(root)
print(rst)