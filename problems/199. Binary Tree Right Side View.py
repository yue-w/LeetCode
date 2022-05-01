# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 17:48:44 2020

@author: wyue
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution(object):
    def __init__(self):
        self.rst = []
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
#         ## Method 1: BFS two queues. Best
#         ## Time: O(N)
#         ## Space: O(D), D: # of points in a level
#         if not root:
#             return []
#         current_level = collections.deque()
#         current_level.appendleft(root)
        
#         while current_level:
#             tem = []
#             next_level = collections.deque()
#             while current_level:
#                 node = current_level.pop()
#                 tem.append(node.val)
#                 if node.left:
#                     next_level.appendleft(node.left)
#                 if node.right:
#                     next_level.appendleft(node.right)
            
#             self.rst.append(tem[-1])
#             current_level = next_level     
#         return self.rst
          


#         ## Method 2: BFS one queue
#         ## Time: O(N)
#         ## Space: O(D), D: # of points in a level
#         if not root:
#             return []
#         queue = collections.deque()
#         queue.appendleft(root)
#         queue.appendleft(None)
        
#         current = root

#         while queue:
#             prev = current
#             current = queue.pop()
            
#             while current:
#                 if current.left:
#                     queue.appendleft(current.left)
#                 if current.right:
#                     queue.appendleft(current.right)
                    
#                 prev, current = current, queue.pop()
#             ## When current is None, it means prev is the last element, add it to result
#             self.rst.append(prev.val)
            
#             if queue:
#                 queue.appendleft(None)
        
#         return self.rst
            

#         ## Method 3: DFS one queue
#         ## Time: O(N)
#         ## Space: O(D), D: # of points in a level
        
        if not root:
            return []
        self.helper(root, 0)
        return self.rst
        
    def helper(self, node, level):
        if level == len(self.rst):
            self.rst.append(node.val)
        
        if node.right:
            self.helper(node.right, level+1)
        if node.left:
            self.helper(node.left, level+1)
        
    
