# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:34:30 2020

@author: wyue
"""

class Solution(object):
    """
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        rst = []
        st, ed = newInterval
        
        self.insertLeft(st,ed,intervals,rst)
        
        return rst
    
    
    def insertLeft(self,st,ed,intervals,rst):
        if not intervals:
            return rst.append([st,ed])
        left = intervals[0][0]
        right = intervals[0][1]
        if st<=left:
            self.insertRight(st,ed, intervals, rst)
        elif left<st<=right:
            self.insertRight(left, ed, intervals, rst)
        elif st>right:
            rst.append(intervals[0])
            self.insertLeft(st,ed,intervals[1:],rst)
        #else: #(st==right)
            
            
        
    def insertRight(self,st,ed, intervals, rst):
        if not intervals:
            return 
        left = intervals[0][0]
        right = intervals[0][1] 
        if ed<left:
            rst.append([st,ed])
            for intev in intervals:
                rst.append(intev)
            return
        elif ed==left:
            rst.append([st,right])
            if intervals[1:]:
                for intev in intervals[1:]:
                    rst.append(intev)
                return  
                
        elif left<ed<=right:
            rst.append([st,right])
            if intervals[1:]:
                for intev in intervals[1:]:
                    rst.append(intev)
                return
        else:
            #rst.append(intervals[0])
            if intervals[1:]:
                self.insertRight(st,ed, intervals[1:],rst)
            else:
                rst.append([st,ed])
                return
    """
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        left = []
        right = []
        start,end = newInterval[0],newInterval[1]
        
        index = 0
        while index<len(intervals):
            if newInterval[0]>intervals[index][1]:
                left += intervals[index],
                
            elif newInterval[1]<intervals[index][0]:
                right += intervals[index:][0],

            else: #merge
                start = min(start,intervals[index][0])
                end = max(end,intervals[index][1])
            index += 1
        
        return  left + [[start,end]] + right

intervals = [[1,3],[6,9]]
newInterval =  [2,5]
rst = Solution().insert(intervals, newInterval)
print(rst)

        
intervals = [[2,5],[6,7],[8,9]]
newInterval = [0,1]
print(Solution().insert(intervals, newInterval))
