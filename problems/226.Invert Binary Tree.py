from queue import Queue
from typing import Optional

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #self.dfs_recursion(root)
        #self.dfs_iteration(root)
        self.bfs(root)
        return root
    
    def dfs_recursion(self, node):
        # Base case
        if not node:
            return 
        # Swap left and right
        node.left, node.right = node.right, node.left
        self.dfs_recursion(node.left)
        self.dfs_recursion(node.right)
        
    def dfs_iteration(self, root):
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)

    def bfs(self, root):
        q = Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            if node:
                node.left, node.right = node.right, node.left
                q.put(node.left)
                q.put(node.right)


        