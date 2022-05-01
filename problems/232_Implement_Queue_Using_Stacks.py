# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:31:50 2020

@author: wyue
"""

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.output = []
        
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.input.append(x)

        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.output)>0:
            return self.output.pop()
        else:
            while len(self.input)>0:
                self.output.append(self.input.pop())
            return self.output.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.output)>0:
            return self.output[-1]
        else:
            return self.input[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.input)==0 and len(self.output)==0
mq = MyQueue()
mq.push(1)
mq.push(2)
print(mq.peek())
print(mq.pop())
print(mq.pop())
print(mq.empty())
