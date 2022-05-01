# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:41:37 2020

@author: wyue
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
      
def helper(root, min_v, max_v):
    ## Base case
    if not root:
        return True
    elif root.val>=max_v or root.val<=min_v:
        return False
    else:
        return helper(root.left, min_v, root.val)\
            and helper(root.right,root.val,max_v)
        

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        valid = helper(root,float('-inf'), float('inf'))
        return valid

        return self.bfs_queue(root)
    def bfs_queue(self, root):    
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
                # while not nodes_next_level.empty():
                #     n = nodes_next_level.get()
                #     queue.put(n)
                queue, nodes_next_level = nodes_next_level, queue
                nodes_current_level = []
 
        return rst
s = Solution()
t = TreeNode(2)
t.left = TreeNode(1)
t.right = TreeNode(3)
print(s.isValidBST(t))