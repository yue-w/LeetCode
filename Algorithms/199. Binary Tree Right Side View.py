from typing import Optional, List

## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #return self.method1(root)
        return self.method2(root)
    
    def method1(self, root):
        """
        BFS. Preferred method.
        """
        from collections import deque
        if not root:
            return []
        rst = []
        
        dq = deque([root]) ## enter from right, leave from left
        
        while dq:
            rst.append(dq[-1].val)
            for _ in range(len(dq)):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        
        return rst
        
    def method2(self, root):
        """
        DFS (Revers in-order traversal)
        """
        rst = []
        self.dfs(root, rst, 0)
        return rst
        
    def dfs(self, node, rst, level):
        ## base cases
        ## if none
        if not node:
            return
        
        ## current level
        if len(rst) == level:
            rst.append(node.val)
            
        ## next level
        self.dfs(node.right, rst, level + 1)
        self.dfs(node.left, rst, level + 1)

        