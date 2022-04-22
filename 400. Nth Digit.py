# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:59:35 2020

@author: wyue
"""

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        while n > 9*(10**(i-1))*i:
            n = n - 9*(10**(i-1))*i
            i += 1
        
        start = 10**(i-1)
        
        rst_string = str(start + (n-1)//i)[(n-1)%i]
        rst = int(rst_string)
        

        return rst

n = 100
print(Solution().findNthDigit(n))