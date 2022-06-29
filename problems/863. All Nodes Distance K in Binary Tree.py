
from typing import List

## Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque, defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        return self.method1(root, target, k)
    
    def method1(self, root, target, k):
        """
        BFS
        Time: O(n)
        Space: O(n)
        where n is the number of nodes.
        """
        # ## special case k == 0 
        # return [target]
    
        ## step 1: build a graph represented by adjcent list
        adjlist = defaultdict(list)
        
        dq = deque() ## enter from right, leave from left
        dq.append(root)
        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                    adjlist[node.val].append(node.left.val)
                    adjlist[node.left.val].append(node.val)
                if node.right:
                    dq.append(node.right)
                    adjlist[node.val].append(node.right.val)
                    adjlist[node.right.val].append(node.val)
        
        ## step 2: from the tree with target as root, use BFS to go k levels down
        level = 0
        dq = deque() ## enter from right, leave from left
        dq.append(target.val)
        found = False
        rst = []
        visited = set()
        while dq and not found:
            for _ in range(len(dq)):
                n = dq.popleft()
                visited.add(n)
                if level == k:
                    rst.append(n)
                    found = True
                ## add the next level into the queue if not visited yet
                else:
                    for nxtn in adjlist[n]:
                        if nxtn not in visited:
                            dq.append(nxtn)
         
            level += 1
        return rst


if __name__ == '__main__':
    #root = [3,5,1,6,2,0,8,null,null,7,4]
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    target = 5
    k = 2
    rst = Solution().distanceK(root, target, k)
    print(rst)