from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        dq = deque()
        dq.append(root)
        nodes = []
        while dq:
            node = dq.popleft()
            if node:
                nodes.append(str(node.val)+',')
                dq.append(node.left)
                dq.append(node.right)
            else:
                nodes.append('*,')
        return ''.join(nodes)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        datastr = data.split(',')
        nodes = []
        for d in datastr:
            if d == '*':
                nodes.append(None)
            elif d:
                nodes.append(TreeNode(int(d)))
        
        i = 0
        j = 1
        while j < len(nodes):
            if nodes[i]:
                nodes[i].left = nodes[j]
                nodes[i].right = nodes[j + 1]
                j += 2
            i += 1
        
        return nodes[0]

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))