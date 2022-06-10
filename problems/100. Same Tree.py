
from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #return self.recursion(p, q)
        #return self.iteration_BFS(p, q)
        return self.iteration_DFS(p, q)
        
        
    def recursion(self, p, q):
        ## Base case:
        if not p or not q:
            return p == q
        if p.val != q.val:
            return False
        return self.recursion(p.left, q.left) and self.recursion(p.right, q.right)
    
    def iteration_DFS(self, p, q):
        """
        Preorder traversal using DFS
        """
        stack = []
        node1 = p
        node2 = q
        stack.append((node1, node2))

        while stack:
            node1, node2 = stack.pop()
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                stack.append((node1.right, node2.right))
                stack.append((node1.left, node2.left))
            elif not node1 and not node2:
                continue
            else:
                return False
                
        return True
            
        
    def iteration_BFS(self, p, q):
        dq = deque()
        dq.append((p, q))
        while dq:
            node1, node2 = dq.popleft()
            if not node1 or not node2:
                if node1 != node2:
                    return False
                else:
                    continue
            if node1.val != node2.val:
                return False
            dq.append((node1.left, node2.left))
            dq.append((node1.right, node2.right))
            
        
        return True
        