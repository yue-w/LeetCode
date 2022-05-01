# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:23:51 2020

@author: wyue
"""

def removeDuplicates(nums):
    ##:type nums: List[int]
    ##:rtype: int
    N = len(nums)
    if N==0:
        return 0
    else:
        ## Numbers between index th1 and th2 are duplicated numbers
        th1 = 1
        v = nums[0]
        for i in range(1,N):
            if v == nums[i]:
                continue
            nums[th1] = nums[i]
            v = nums[i]
            th1+=1
    return th1

nums = [0,0,1,1,1,2,2,3,3,4]
lenth = removeDuplicates(nums)
print(lenth)
print(nums[0:lenth])