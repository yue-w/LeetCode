# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 19:40:13 2020

@author: wyue
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append([x,0])
        else:
            currentMinIndex = self.stack[len(self.stack)-1][1]
            if x<self.stack[currentMinIndex][0]:
                self.stack.append([x, len(self.stack)])
            else:
                min_index = self.stack[len(self.stack)-1][1]
                self.stack.append([x,min_index])
        

    def pop(self):
        """
        :rtype: None
        """
        return self.stack.pop()[0]
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        minIndex = self.stack[len(self.stack)-1][1]
        return self.stack[minIndex][0]

stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
print(stack.getMin())