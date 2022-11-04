

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #return self.method1(inorder, postorder)
        #return self.method2(inorder, postorder)
        return self.method3(inorder, postorder) # preferred method, more efficient
    
    def method1(self, inorder, postorder):
        root = self.recursion(inorder, postorder)
        
        return root
        
    def recursion(self, inorder, postorder):
        ## base case:
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        if not inorder:
            return None
        
        node = TreeNode(postorder[-1])
        
        
        ## left subtree
        i = 0
        while inorder[i] != node.val:
            i += 1
        
        new_inorder = inorder[:i]
        new_postorder = postorder[:i]
        node.left = self.recursion(new_inorder, new_postorder)
        
        ## right subtree
        new_inorder = inorder[i+1:]
        new_postorder = postorder[i: -1]
        node.right = self.recursion(new_inorder, new_postorder)
        
        return node

    def method2(self, inorder, postorder):
        ## indexs are inclusive
        root = self.recursion2(inorder, postorder, 0, len(inorder) - 1, 0, 
        len(postorder) - 1)
        
        return root
        
    def recursion2(self, inorder, postorder, instart, inend, postart, poend):
        """
        instart, inend: starting and ending index of inorder
        postart, poend: starting and ending index of postorder
        """
        ## base case:
        if inend == instart:
            return TreeNode(inorder[inend])
        if inend < instart:
            return None
        
        node = TreeNode(postorder[poend])
        
        
        ## left subtree
        counter = 0
        while inorder[counter + instart] != node.val:
            counter += 1
        
        node.left = self.recursion2(inorder, postorder, instart, instart + counter - 1, postart, postart + counter - 1)
        
        ## right subtree
        node.right = self.recursion2(inorder, postorder, instart + counter + 1, inend, postart + counter, poend-1)
        
        return node
    
    def method3(self, inorder, postorder):
        dic = {inorder[i]:i for i in range(len(inorder))}
        ## indexs are inclusive
        root = self.recursion3(dic, inorder, postorder, 0, len(inorder) - 1)
        
        return root
        
    def recursion3(self, dic, inorder, postorder, low, high):
        ## base case:
        if low > high:
            return None
        mid = dic[postorder.pop()]        
        node = TreeNode(inorder[mid])

        node.right = self.recursion3(dic, inorder, postorder, mid + 1, high)
        node.left = self.recursion3(dic, inorder, postorder, low, mid -1 )
        return node

if __name__ == '__main__':
    # inorder = [1,2,3,4]
    # postorder = [3,2,4,1]
    inorder = [2,1]
    postorder = [2,1]
    rst = Solution().buildTree(inorder, postorder)
    print(rst.val)
    
