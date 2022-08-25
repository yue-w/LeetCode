
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
        #return self.method1(root, target, k)
        return self.method2(root, target, k)
    
    def method1(self, root, target, k):
        """
        BFS.
        Disadvantage: needs to store the whole tree. Advantage: easier to think.
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

        rst = []
        visited = set()
        while dq and level <= k:
            for _ in range(len(dq)):
                n = dq.popleft()
                visited.add(n)
                if level == k:
                    rst.append(n)

                ## add the next level into the queue if not visited yet
                else:
                    for nxtn in adjlist[n]:
                        if nxtn not in visited:
                            dq.append(nxtn)
         
            level += 1
        return rst
    
    def method2(self, root, target, k):
        """
        DFS. Save space but harder to think. 
        """
        
        def dfs(node, target, k):
            """
            for each node, test whether it is a pivot point (target and a result point
            is on pivot's left and right subtree). If a node is a pivot point, find result
            point on the opposite subtree of target. 
            if node is not pivot, then target is not below node, so search below node for k distance.
            return the distance of target from node
            return -1 is target is not in the sub trees of node
            """
            ## base case:
            ## if node is leaf
            if not node:
                return -1
            
            ## if node is target
            if node.val == target.val:
                search_down(node, k)
                return 0
            
            ## if reaching this point, node is not leaf or target
            ## distance from pivot to left child
            left = dfs(node.left, target, k)
            
            if left != -1:
                ## if node is result
                if left == k - 1:
                    self.rst.append(node.val)

                ## if target is below node, then search right child
                else:
                    search_down(node.right, k - (left + 1) - 1)
                return left + 1
                
            ## distance from pivot to right child 
            right = dfs(node.right, target, k)
            ## if target is not below right child, then search below left child for k distance
            if right != -1:
                ## if node is result
                if right == k - 1:
                    self.rst.append(node.val)
                ## if target is below node.right, wthen serch right child
                else:
                    search_down(node.left, k - (right + 1) - 1)
                return right + 1
        
            return -1
        def search_down(node, t):
            """
            From node, go down t steps. If reach leaf before t step, return.
            Add the node at t steps to result.
            """
            ## base case
            if not node:
                return
            if t == 0:
                self.rst.append(node.val)
            search_down(node.left, t - 1)
            search_down(node.right, t - 1)
            
        self.rst = []
        dfs(root, target, k)
        return self.rst
            
            


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