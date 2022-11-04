
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Thoughts: inorder traversal using recursion
        """
        return self.iteration(root, k)
        #return self.recursion(root, k)
    
    def recursion(self, root, k):
        self.remain = k
        self.rst = None
        self.dfs(root, k)
        return self.rst
    
    def dfs(self, node, k):
        """
        in order traversal
        """
        ## Base case
        if not node:
            return
        ## go left for smaller nodes
        self.dfs(node.left, k)
        
        ## add the current node, remain reduce by 1
        self.remain -= 1
        ## if remain equals 0, then this node is the result. Return.
        if self.remain == 0:
            self.rst = node.val
            return
        
        ## if more nodes are needed, go right
        self.dfs(node.right, k)
    
    def iteration(self, root, k):
        stack = []
        curr = root
        counter = 0
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            counter += 1
            if counter == k:
                return curr.val
            curr = curr.right

if __name__ == '__main__':

    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    k = 3
    rst = s.kthSmallest(root, k)
    print(rst)
            
        

        
        
        