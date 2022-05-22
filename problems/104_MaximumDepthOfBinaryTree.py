# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 23:28:39 2020

@author: wyue
"""
from collections import deque

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.recursion(root)

    ## Method 1: recersion
    def recursion(self, root):
        ## Base case
        if root is None: return 0
        return 1 + max(self.recursion(root.left), self.recursion(root.right))
    
    ## Method 2: stack
    def stack_method(self, root):
        stack = []
        if root is not None:
            stack.append((root,0))
        max_depth = 0
        
        while len(stack)>0:
            root,depth = stack.pop()
            if max_depth<depth:
                max_depth = depth
            if root is not None:
                stack.append((root.left, depth+1))
                stack.append((root.right, depth+1))
        return max_depth
    

    ## Method 3: BFS
    def bfs(self, root):
        rst = 0
        dq = deque() ## Keep entering from right and leaving from left
        if root:
            dq.append(root)
            
        while dq:
            num_cur = len(dq)
            ## for every node in current level
            if num_cur > 0:
                rst += 1
            for _ in range(num_cur):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        
        return rst

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution=Solution()
print(solution.maxDepth(root))