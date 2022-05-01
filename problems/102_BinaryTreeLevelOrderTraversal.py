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
         
def dfs(root, result, level):
    if root != None:
        if len(result)<level:
            result.append([])
        result[level-1].append(root.val)
        dfs(root.left, result, level+1)
        dfs(root.right, result, level+1)
    
    
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root == None:
            return result
        # dfs(root, result, 1)
        # return result

        return self.bfs_queue2(root)

    def bfs_queue1(self, root): 
        """
        BFS method 1.
        """   
        rst = []
        if not root:
            return rst
        queue = Queue()
        queue.put(root)
        nodes_next_level = Queue()
        nodes_current_level = []

        while not queue.empty() or not nodes_next_level.empty():
            ## if queue is not empty, add its value to nodes_current_level 
            if not queue.empty():
                while not queue.empty():
                    node = queue.get()
                    nodes_current_level.append(node.val)
                    if node.left:
                        nodes_next_level.put(node.left)
                    if node.right:
                        nodes_next_level.put(node.right)
                if nodes_current_level:
                    rst.append(nodes_current_level)
            ## if queue is empty, the current level is done, add nodes in current level (saved in nodes_current_level) to rst
            ## Add nodes of next level (saved in nodex_next_level) into queue, then clean nodex_next_level
            else:

                queue, nodes_next_level = nodes_next_level, queue
                nodes_current_level = []
 
        return rst

    def bfs_queue2(self, root):
        """
        BFS method 2
        """ 
        if not root:
            return []
        rst = []
        dq = deque()
        dq.append(root)
        while dq:
            ## Get the number of nodes in the current level, do the following:
            ## 1. Pop a node from queue. 2. Append the node to a list. 3. Add the children of the node into queue.
            num_current_level = len(dq)
            current_level = []
            for _ in range(num_current_level):
                node = dq.popleft()
                current_level.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            
            rst.append(current_level)

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