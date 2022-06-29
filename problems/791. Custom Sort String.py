# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 12:09:15 2020

@author: wyue
"""
from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ct = Counter(s)
        
        ## a list that stores val in s
        rst = []
        
        ## for the chars in s that also in order
        for o in order:
            if ct[o] > 0:
                rst.append(o * ct[o])
                ct.pop(o)

            
        ## for the chars in s that are not in order
        for key, val in ct.items():
            rst.append(val * key)
        
        return ''.join(rst)
            