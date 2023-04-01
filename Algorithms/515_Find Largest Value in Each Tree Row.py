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
    

    def largestValues(self, root):
        return self.method1(root)
        #return self.method2(root)
    
    def method1(self, root):
        """
        BFS
        """
        from collections import deque
        if not root:
            return []
        rst = []
        dq = deque([root])
        while dq:
            # Enter from right, exist from left
            maxv = float('-inf')
            for _ in range(len(dq)):
                node = dq.popleft()
                maxv = max(maxv, node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            rst.append(maxv)
        return rst
    
    def method2(self, root):
        """
        DFS
        """
        def dfs(level, rst, node):
            if not node:
                return 
            
            ## if this is the fist node of this level, just put this node in the list
            if level == len(rst):
                rst.append(node.val)
            else:
                rst[level] = max(rst[level], node.val)
            ## next level
            dfs(level+1, rst, node.left)
            dfs(level+1, rst, node.right)
        
        rst = []
        dfs(0, rst, root)
        return rst
        


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
    

    
node = TreeNode(1)
node.left = TreeNode(3)
node.right = TreeNode(2)
node.left.left = TreeNode(5)
node.left.right = TreeNode(3)
node.right.right = TreeNode(9)

print(Solution().largestValues(node))