# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 19:40:13 2020

@author: wyue
"""

class MinStack:
    #### method 1 use two stacks:
    def __init__(self):
        self.stack = []
        self.stackmin = []

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append(val)
            self.stackmin.append(min(val, self.stackmin[-1]))
        else:
            self.stack.append(val)
            self.stackmin.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.stackmin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackmin[-1]

stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
print(stack.getMin())