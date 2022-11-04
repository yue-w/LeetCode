# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:06:51 2020

@author: wyue
231. Power of Two
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return self.method1(n)
    def method1(self, n):
        i = 1
        while i < n:
            i *= 2
        return i == n
    
    def method2(self, n):
        return n and not (n & n - 1)