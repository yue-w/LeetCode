# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 11:09:39 2020

@author: wyue
"""

class Solution(object):
    def maxProfit(self, prices):
        rst = 0
        minv = prices[0]
        for i in range(1, len(prices)):
            rst = max(rst, prices[i] - minv)
            minv = min(minv, prices[i])

        return rst
        
prices =  [7,1,5,3,6,4]
print(Solution().maxProfit(prices))