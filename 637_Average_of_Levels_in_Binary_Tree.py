# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 08:44:43 2020

@author: wyue
"""
import numpy as np
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


## DFS with a dictionary (defaultdict)
import collections
def aveEveryLevel(root):
    if root == None:
        return [] 
    dic = collections.defaultdict(list)
    helper(root, 0, dic)
    
    ## No need to sort the dictionary. Start from 0 until key not in dict
    rst = []
    
    level = 0
    while level in dic:
        rst.append(np.mean(dic[level]))
        level += 1
    return rst
    
def helper(root, layer, dic):
    dic[layer].append(root.val)

    if root.left:
        helper(root.left, layer+1, dic)
    if root.right:
        helper(root.right, layer+1, dic)


"""
## BFS with a dictionary
import collections
def aveEveryLevel(root):
    if not root:
        return []
    ## Each element in the queue is a tuple (node, level)
    q = collections.deque()
    q.appendleft((root,0.0))
    ## dictionary stores the sum and the # of number
    dic = {}
    while q:
        node, level = q.pop()
        if level not in dic:
            dic[level] = (node.val, 1)
        else:
            val, count = dic[level]
            dic[level] = (val + node.val, count+1)
        if node.left:
            q.appendleft((node.left,level+1))
        if node.right:
            q.appendleft((node.right, level+1))
    i =  0
    rst = []
    while i in dic:
        val, count = dic[i]
        rst.append(val / count)
        i += 1
    return rst
"""

"""
## BFS without dictionary. Best of the three
import collections
def aveEveryLevel(root):
    if not root:
        return []
    q = collections.deque()
    ## The elements in the queue are tuples (sum, count, level)
    q.appendleft(root)
    rst = []
    
    while q:
        total = 0.0
        count = 0
        tem_q = collections.deque()
        while len(q)>0:
            node = q.pop()
            total += node.val
            count += 1

            ## Next layer
            if node.left:
                tem_q.appendleft(node.left)
            if node.right:
                tem_q.appendleft(node.right)
        q = tem_q
        rst.append(total/count)


    return rst
"""



root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(15)
root.left.right = TreeNode(7)

"""
root = TreeNode(4)
root.left = TreeNode(7)
root.right = TreeNode(9)
root.left.left = TreeNode(10)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(6)
root.left.right.right.left = TreeNode(2)
root.right.right = TreeNode(6)
"""
print(aveEveryLevel(root))

