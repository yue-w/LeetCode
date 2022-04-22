# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 23:37:18 2020

@author: wyue
"""
import heapq

def longestSubarray(nums, limit):
    """
    :type nums: List[int]
    :type limit: int
    :rtype: int
    """
    heap_max = []
    heap_min = []
    i = 0
    rst = 0
    for j,v in enumerate(nums):
        heapq.heappush(heap_max,[-v, j])
        heapq.heappush(heap_min,[v, j])
        while -heap_max[0][0] - heap_min[0][0] > limit:
            i = min(heap_min[0][1], heap_max[0][1]) + 1
            while heap_min[0][1]<i:
                heapq.heappop(heap_min)
            while heap_max[0][1]<i:
                heapq.heappop(heap_max)
        rst = max(rst, j - i + 1)
    return rst

nums = [10,1,2,4,7,2]
limit = 5
print(longestSubarray(nums, limit))