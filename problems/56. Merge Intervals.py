# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:03:23 2020

@author: wyue
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals)
        if len(intervals)<2:
            return intervals
        rst = [intervals[0]]
        i = 1
        while i<len(intervals):
            left = rst[-1][0]
            right = rst[-1][1]
            first = intervals[i][0]
            second = intervals[i][1]
            if first > right:
                rst.append([first,second])
            elif left<=first<=right:
                if second > right:
                    rst[-1] = [left, second]
                else:
                    rst[-1] =  [left,right]
            i += 1
        
        return rst
                