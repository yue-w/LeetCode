# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 23:16:17 2020

@author: wyue
"""

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def visit(nestedList, depth):
            res = 0
            for item in nestedList:
                if item.isInteger():
                    res += item.getInteger()*depth
                else:
                    res += visit(item.getList(), depth+1)
            return res
        return visit(nestedList, 1)
        
