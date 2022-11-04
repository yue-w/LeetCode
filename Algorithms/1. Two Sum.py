# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 20:32:07 2022

@author: wyue
"""

from collections import defaultdict
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num 
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

    
if __name__ == '__main__':
    s = Solution()
    nums = [3,2,4]
    target = 6
    rst = s.twoSum(nums, target)
    print(rst)