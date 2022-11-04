from typing import List

"""
Segment Tree: 
Reference:
https://youtu.be/3faZ-iTte7k
"""
class SegTreeNode:
    def __init__(self, start, end, val=0):
        self.start = start
        self.end = end
        self.val = val
        self.left = None
        self.right = None
    
class NumArray:
    def build_tree(self, start, end):
        """
        Build a SegmentTree, return root.
        Time: O(log(n))
        Space: O(1)
        """
        if start == end:
            return SegTreeNode(start, end, self.nums[start])
            
        mid = start + (end - start) // 2
        root = SegTreeNode(start, end)
        
        if not root.left:
            root.left = self.build_tree(start, mid) 
            root.right = self.build_tree(mid+1, end)
        root.val = root.left.val + root.right.val
        return root
    
    def update_single_node(self, node, idx, val):
        """
        Time: O(logn)
        Space: O(1)
        """
        ## base case
        if node.start == node.end:
            node.val = val
            return
        mid = node.start + (node.end - node.start) // 2
        if idx <= mid:
            self.update_single_node(node.left, idx, val)
        else:
            self.update_single_node(node.right, idx, val)
        ## update the node itself
        node.val = node.left.val + node.right.val

        
    def query_range(self, node, left, right):
        """
        Time: O(logn)
        Space: O(1)
        """
        ## base case:
        if node.start == left and node.end == right:
            return node.val
        mid = node.start + (node.end - node.start) // 2
        if right <= mid:
            return self.query_range(node.left, left, right)
        elif left > mid:
            return self.query_range(node.right, left, right)
        return self.query_range(node.left, left, mid) + self.query_range(node.right, mid + 1, right)
        
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.root = self.build_tree(0, len(nums)-1)

    def update(self, index: int, val: int) -> None:
        self.update_single_node(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.query_range(self.root, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)