# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:59:35 2020

@author: wyue
"""

class Solution(object):
    def findNthDigit(self, n):

        if n < 10:
            return n
        pwr = 1
        remain = n
        while remain - pwr * 9 * (10 ** (pwr - 1)) > 0:
            remain -= pwr * 9 * (10 ** (pwr - 1))
            pwr += 1
        div = remain // pwr
        remainder = remain % pwr
        if remainder == 0:
            nxtnum = (10 ** (pwr - 1)) - 1 + div
            remainder = pwr
        else:
            nxtnum = (10 ** (pwr - 1)) - 1 + div + 1
        rst = str(nxtnum)[remainder-1]
        
        return int(rst)


        # """
        # :type n: int
        # :rtype: int
        # """
        # i = 1
        # while n > 9*(10**(i-1))*i:
        #     n = n - 9*(10**(i-1))*i
        #     i += 1
        
        # start = 10**(i-1)
        
        # rst_string = str(start + (n-1)//i)[(n-1)%i]
        # rst = int(rst_string)
        

        # return rst

n = 11
print(Solution().findNthDigit(n))