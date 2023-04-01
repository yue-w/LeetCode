# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 20:38:32 2020

@author: wyue
"""


import heapq
class Solution(object):
    
    ## Method one, sort meetings by start time using heap
    def minMeetingRooms(self, intervals):
        # return self.method1(intervals)
        # return self.method2(intervals)
        # return self.method3(intervals)
        return self.method4(intervals)
    
    def method1(self, intervals):
        
        ## Put meetings in a heap. Pop based on start time.
        if len(intervals) == 0: return 0
        ## endtimes = [[time[1][0]] for time in intervals]
        rst = []
        heapq.heapify(intervals)
        start, end = heapq.heappop(intervals)
        rst.append(end)
        
        while intervals:
            next_start, next_end = heapq.heappop(intervals)
            i = 0
            while i<len(rst):
                if next_start >= rst[i]:
                    rst[i] = next_end
                    break
                i+=1
            if i == len(rst):
                rst.append(next_end)

        return len(rst)
    
    
    def method2(self, intervals):
    ## Method 2, use two list. Sort meetings by start time using built-in function of 
    ## sort 
        if len(intervals) == 0 or intervals is None: 
            return 0
        intervals.sort()
        rst = []
        start, end = intervals[0]
        rst.append(end)
        for i in range(1, len(intervals)):
            next_start, next_end = intervals[i]
            j = 0
            while j<len(rst):
                if next_start >= rst[j]:
                    rst[j] = next_end
                    break
                j+=1
            if j == len(rst):
                rst.append(next_end)
        return len(rst)
        

        
    ## Method 3
    ## Sort start time by list, use a heap for earliest next end time.
    def method3(self, intervals):
        if not intervals: 
            return 0
        intervals.sort()
        rst = []
        start, end = intervals[0]
        
        end_times = []
        end_times.append(end)
        heapq.heapify(end_times)
        max_rooms = 1
        for i in range(1, len(intervals)):
            next_start, next_end = intervals[i]
            if end_times:
                earliest_end = end_times[0]
                if earliest_end <= next_start:
                    heapq.heapreplace(end_times, next_end)
                else:
                    heapq.heappush(end_times, next_end)
                if len(end_times)> max_rooms:
                    max_rooms = len(end_times)
        
        return max_rooms

    def method4(self, intervals):
        stamp = []
        for a, b in intervals:
            """
            start time is -1 and end time is 1 so that 
            when there is a tie, start time comes before 
            end time
            """
            stamp.append((a, 1))
            stamp.append((b, -1))
        
        stamp.sort()
        rst = 0
        curr = 0
        for time, v in stamp:
            curr += v
            rst = max(rst, curr)

        return rst
        
intervals = [[6,15],[13,20],[6,17]]
print(Solution().minMeetingRooms(intervals))
        
        
        
        
        
        
        
        
        