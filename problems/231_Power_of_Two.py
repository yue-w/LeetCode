# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:06:51 2020

@author: wyue
231. Power of Two
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0: return False
        while True:
            if n == 1:
                return True
            else:
                if n%2 == 0:
                    n = n/2
                else:
                    return False