
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        #return self.method1(root)
        return self.method2(root)
        #return self.method3(root)
    
    def method1(self, root):
        """
        DFS using recursion. Use negative index to reverse the result list
        """
        def dfs(node, rst, level):
            ## base case
            if not node:
                return 
            
            if len(rst) <= abs(level):
                rst.append([node.val])
            else:
                rst[level].append(node.val)
            dfs(node.left, rst, level + 1)
            dfs(node.right, rst, level + 1)
        
        rst = []
        dfs(root, rst, 0)
        rst.reverse()
        return rst
            
    
    def method2(self, root):
        """
        DFS using stack
        """
        if not root:
            return []
        
        rst = []
        stack = []
        
        stack.append((root, 0))
        while stack:
            node, level = stack.pop()
            if level < len(rst):
                rst[level].append(node.val)
            else:
                rst.append([node.val])
            ## right child
            if node.right:
                stack.append((node.right, level + 1))
            ## left child
            if node.left:
                stack.append((node.left, level + 1))
            ## left child
        rst.reverse()
        return rst
    
    def method3(self, root):
        """
        BFS
        Time: O(logh)
        Space: O(logn)
        """
        if not root:
            return []
        dq = deque()
        dq.append(root)
        rst = deque()
        while dq:
            curr = []
            for _ in range(len(dq)):
                node = dq.popleft()
                curr.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            rst.appendleft(curr)
        
        return rst