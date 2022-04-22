# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:04:58 2020

@author: wyue
"""

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        A = list(map(int,str(num)))
        

        last = {x: i for i, x in enumerate(A)}
        
        for i, x in enumerate(A):
            for k in range(9, x, -1):
                if last.get(k, 0) > i:

                    A[i], A[last[k]] = A[last[k]], A[i]
                    return int("".join(map(str, A)))
        return num

  
print(Solution().maximumSwap(2737))