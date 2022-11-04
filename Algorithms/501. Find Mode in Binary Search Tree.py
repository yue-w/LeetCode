from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        """
        In order traversal using recursion.
        The inorder ttraversal of a BST gives the numbers in ascending order.
        Maintain a list and a value.
        """
        #return self.method1(root) 
        return self.method2(root) ## preferred method. No extra space
    
    def method1(self, root):
        """
        Use extra space. 
        Time: O(n)
        Space: O(n)
        """
        self.rst = []
        self.maxfreq = 0
        self.curfreq = 0
        self.preval = None

        def dfs(node):
            """
            In order traversal. 
            """
            ## base case
            if not node:
                return
            dfs(node.left)
            
            count(node.val)
            
            dfs(node.right)
        
        def count(curval):
            if curval == self.preval:
                self.curfreq += 1
            else:
                self.curfreq = 1
                self.preval = curval
                
            if self.curfreq > self.maxfreq:
                self.rst = []
                self.maxfreq = self.curfreq
            if self.curfreq == self.maxfreq:
                self.rst.append(curval)
        
        dfs(root)
        return self.rst
    
    def method2(self, root):
        """
        Reference:
        https://zxi.mytechroad.com/blog/tree/leetcode-501-find-mode-in-binary-search-tree/
        """
        ## two passes, first pass to find the frequence, second pass to find the modes
        self.rst = []
        self.modefreq = float('inf')
        self.maxfreq = 0
        self.curfreq = 0
        self.preval = None
        
        def dfs(node):
            ## base case
            if not node:
                return
            
            dfs(node.left)
            count(node.val)
            dfs(node.right)
            
        def count(curval):
            if curval == self.preval:
                self.curfreq += 1
            else:
                self.curfreq = 1
                self.preval = curval
            
            if self.curfreq > self.maxfreq:
                self.maxfreq = self.curfreq
            if self.curfreq == self.modefreq:
                self.rst.append(curval)
            
        
        ## call dfs first time to set value to maxfrequence
        dfs(root)
        self.modefreq = self.maxfreq
        self.curfreq = 0
        ## call dfs again to find the modes
        dfs(root)
        
        return self.rst

if __name__ == '__main__':
    from tools import deserialize, drawtree
    #root = '[1,1,2,1,null,2,2,null,null,null,null,null,3]'
    root = '[0]'
    root = deserialize(root)
    #drawtree(root)
    rst = Solution().findMode(root)
    drawtree(rst)