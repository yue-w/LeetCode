# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 20:39:16 2022

@author: wyue
"""
from typing import List 

import copy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        mSet = set(nums)
        self.rst = []
        cur_rst = []
        self.helper(mSet,cur_rst)
        return self.rst
    
            
    def helper(self, remain_nums, cur_rst):
        if remain_nums:
            #copy_remain_nums = copy.deepcopy(remain_nums)
            for num in remain_nums:
                cur_rst_cp = copy.deepcopy(cur_rst)
                cur_rst_cp.append(num)
                copy_remain_nums = copy.deepcopy(remain_nums)
                copy_remain_nums.remove(num)
                self.helper(copy_remain_nums, cur_rst_cp)
        else:
            self.rst.append(cur_rst)
            return
            
if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    rst = s.permute(nums)
    print(rst)