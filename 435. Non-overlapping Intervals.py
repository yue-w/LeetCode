# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 19:48:00 2022

@author: wyue
"""
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        total = 0
        ## Sort the interval by the first element
        intervals_sorted = sorted(intervals)
        h1 = intervals_sorted[0][0]
        t1 = intervals_sorted[0][1]
        for i in range(1, len(intervals)):
            h2 = intervals_sorted[i][0]
            t2 = intervals_sorted[i][1]
            if h2 < t1:
                total += 1
                if t2 < t1:
                    t1 = t2
            else:
                h1 = h2
                t1 = t2
        
        return total
    
if __name__ == '__main__':
    s = Solution()
    intervals = intervals = [[1,2],[2,3],[3,4],[1,3]]
    ans = s.eraseOverlapIntervals(intervals)
    assert ans == 1