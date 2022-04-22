# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:34:30 2020

@author: wyue
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        rst = []
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                rst.append(newInterval)
                return rst + intervals[i:]
            elif newInterval[0] > interval[1]:
                rst.append(interval)
            else:
                # merge
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]

        rst.append(newInterval)
        return rst

