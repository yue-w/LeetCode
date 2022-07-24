# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:03:23 2020

@author: wyue
"""
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return self.method1(intervals)
    
    def method1(self, intervals):
        """
        Preferred method. Sweeping line. 
        Time: O(nlogn)
        Space: O(1)
        
        The following customerized sorting is used
        ## [1,1] and [1,0] is a tie on '1', by default, the one with smaller 
        ## second element come first.
        b = [[1,1],[2,1],[1,-1],[3,0]]
        b.sort()
        print(b)
        ## [1,1] and [1,0] is a tie on '1', we can change it to making the one with larger 
        ## second element come first.
        a = [[1,1],[2,1],[1,-1],[3,0]]
        a.sort(key=lambda x: (x[0], -x[1]))
        print(a).
        In the following case when a starting point overlap with an end point, 
        make sure the starting point comes first after sorting (to add 1 before subtract 1).
                    1            -1
                    |_____________|
                    
                        1                -1
                        |________________|
                        
                                         1             -1
                                         |_____________|
        """
        
        time_stmps = []
        ## iterate through the time stamps, mark 1 for starting , mark -1 for ending.
        for interval in intervals:
            time_stmps.append((interval[0], 1))
            time_stmps.append((interval[1], -1))
        ## sort time_stmps by time_stamp. 
        ## if there is a tie, let the one with a 'start' come first.
        time_stmps.sort(key=lambda x: [x[0], -x[1]])
        
        rst = []
        cursum = 0
        ## iterate time_stmps, when cursum changes from 0 to a positive number, a new interval start
        ## when cursum changes from a positive number to 0, an interval ends (so add it into the result)
        for stp in time_stmps:
            if cursum == 0 and cursum + stp[1] > 0:
                start = stp[0]
            elif cursum > 0 and cursum + stp[1] == 0:
                end = stp[0]
                rst.append([start, end])
                
            cursum += stp[1]
        return rst

        
    def method2(self, intervals):
        """
        Normal mehtod.
        Time: O(nlogn)
        Space: O(1)
        """
        rst = []
        intervals.sort()
        start1, end1 = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            start2, end2 = intervals[i][0], intervals[i][1]
            if start2 <= end1:
                end1 = max(end1, end2)
                continue
            
            rst.append([start1, end1])
            start1 = start2
            end1 = end2
        rst.append([start1, end1])
            
        
        return rst
                