
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #return self.method1(root, key)
        return self.method2(root, key) ## preferred method
    def method1(self, root, key):
        """
        More codes, but does not delete a pointer that may be pointed by.
        """
        
        def dfs(node, key):
            ## base case:
            if not node:
                return None
            if key < node.val:
                node.left = dfs(node.left, key)
                return node
            elif key > node.val:
                node.right = dfs(node.right, key)
                return node
            
            else: ## key == node.val
                if not node.left: ## only has right child, return right child
                    return node.right
                elif not node.right: ## if only has left child, return left child
                    return node.left 
                else:
                    ## find the smallest node in the right sub tree of node.right
                    cur_root = node
                    new_root  = cur_root.right
                    while new_root.left:
                        cur_root = new_root 
                        new_root  = new_root.left
                        
                    if node != cur_root:
                        cur_root.left = new_root.right
                        new_root.right = node.right
                    new_root.left = node.left
                    return new_root 
            
    
        root = dfs(root, key)
        return root
        
    def method2(self, root, key):
        """
        Less code, but may delete a pointer that is pointed by.
        """
        def dfs(node, key):
            ## base case:
            if not node:
                return None
            if key < node.val:
                node.left = dfs(node.left, key)

            elif key > node.val:
                node.right = dfs(node.right, key)
            
            else: ## key == node.val
                if not node.left: ## only has right child, return right child
                    return node.right
                elif not node.right: ## if only has left child, return left child
                    return node.left 
                else:
                    ## find the left most node in the right subtree
                    left = node.right
                    pre = left
                    while left:
                        pre = left
                        left = left.left
                    val = pre.val
                    node.val = val
                    
                    ## recursion
                    node.right = dfs(node.right, val)
                    
            return node
            
    
        root = dfs(root, key)
        return root


if __name__ == '__main__':
    from tools import deserialize, drawtree
    # root = '[5,3,6,2,4,null,7]'
    # key = 0
    # root = '[50,30,70,null,40,60,80]'
    # key = 50
    root = '[3,2,5,null,null,4,10,null,null,8,15,7]'
    key  = 5
    root = deserialize(root)
    #drawtree(root)
    root = Solution().deleteNode(root, key)
    drawtree(root)
    