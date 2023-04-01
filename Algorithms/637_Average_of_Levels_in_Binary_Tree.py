# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 08:44:43 2020

@author: wyue
"""
import numpy as np
from typing import Optional, List
import collections

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right



class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        #return self.method1(root)
        return self.method2(root)

    def method1(self, root):
        """
        BFS
        """
        rst = []
        dq = collections.deque([root])
        while dq:
            cur = 0
            n = len(dq)
            for _ in range(n):
                node = dq.popleft()
                cur += node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            rst.append(cur/n)

        return rst

    def method2(self, root):
        """
        DFS
        """
        def dfs(node, level):
            ## Base case
            if not node:
                return
            ## Add node to sums, count++
            if level == len(sums):
                sums.append(node.val)
                counts.append(1)
            else:
                sums[level] += node.val
                counts[level] += 1
            ## children
            dfs(node.left, level+1)
            dfs(node.right, level+1)


        sums = []
        counts = []
        dfs(root, 0)
        rst = []
        for sumv, c in zip(sums, counts):
            rst.append(float(sumv)/c)
        return rst





root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(15)
root.left.right = TreeNode(7)

"""
root = TreeNode(4)
root.left = TreeNode(7)
root.right = TreeNode(9)
root.left.left = TreeNode(10)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(6)
root.left.right.right.left = TreeNode(2)
root.right.right = TreeNode(6)
"""
print(Solution().averageOfLevels(root))

