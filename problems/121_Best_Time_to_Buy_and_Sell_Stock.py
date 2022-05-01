# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 11:09:39 2020

@author: wyue
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        ## Brute search
        """
        if len(prices)<2: return 0
        maxV = 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                if prices[j]-prices[i] > maxV:
                    maxV =  prices[j]-prices[i] 
        return maxV
        """
                
        if len(prices)<2: return 0
        
        minp = float('inf')
        maxv = 0
        for i in range(len(prices)):
            if prices[i]<minp:
                minp = prices[i]
            elif prices[i] - minp > maxv:
                maxv = prices[i] - minp
        return maxv
prices =  [7,1,5,3,6,4]
print(Solution().maxProfit(prices))