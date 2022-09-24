

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        node = root
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        Return the next smallest number
        """
        node = self.stack.pop()
        val = node.val
        if node.right:
            node = node.right
            self.stack.append(node)
            while node.left:
                node = node.left
                self.stack.append(node)
        
        return val
        

    def hasNext(self) -> bool:
        if self.stack:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()