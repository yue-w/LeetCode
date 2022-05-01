# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 16:26:26 2020

@author: wyue
https://leetcode.com/problems/merge-sorted-array/
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        assert(len(nums1) == m + n)
        
        ## insert in place and from the the end
        index = len(nums1)-1
        i1 = m-1
        i2 = n-1
        while i2>=0:
            if i1>=0 and nums1[i1]>nums2[i2]:
                nums1[index] = nums1[i1]
                i1 -= 1
            else:
                nums1[index] = nums2[i2] 
                i2 -= 1
            index -=1
            
        
        
        
        
"""
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
"""
nums1 = [4,0,0,0,0,0]
m = 1
nums2 = [1,2,3,5,6]
n = 5
Solution().merge(nums1, m, nums2, n)
print(nums1)