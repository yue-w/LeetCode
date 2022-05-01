# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import queue
from typing import Optional
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #return self.helper(root.left, root.right)
        return self.helper_it(root)
        
        
    def helper(self, left, right):
        if left is None:
            return right is None
        elif right is None:
            return False
        else:
            if left.val != right.val:
                return False
            else:
                return self.helper(left.right, right.left) and self.helper(left.left, right.right)
    ## Iteration method    
    def helper_it(self, root):
        q = queue.Queue()
        q.put(root)
        q.put(root)
        while not q.empty():
            left = q.get()
            right = q.get()
            if (left is None) and (right is None):
                continue
            if (left is None) or (right is None):
                return False
            if left.val != right.val:
                return False
            q.put(left.left)
            q.put(right.right)
            q.put(left.right)
            q.put(right.left)
            
        return True