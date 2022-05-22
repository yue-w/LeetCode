
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
        _, val, _ = self.dfs(root, k, 0)
        return val
        
    def dfs(self, node, k, counter):
        ## Base case: leaf
        if not node.left and not node.right:
            if counter == k - 1:
                return True, node.val, k
            else:
                return False, None, counter + 1
        
        if node.left:
            ## Check left sub tree (elements smaller than node)
            found, val, counter = self.dfs(node.left, k, counter)
            if found:
                return found, val, counter
        ## Check node
        if counter == k - 1:
            return True, node.val, k
        else:
            found = False
            counter += 1
            val = None
        ## Check right subtree (elements larger than node)
        if node.right:
            found, val, counter = self.dfs(node.right, k, counter)
            
        return found, val, counter
    
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
            
        

        
        
        