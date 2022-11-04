# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 20:39:16 2022

@author: wyue
"""
from typing import List 
from collections import deque
import copy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Method 3 is preferred. 
        Method 1 is also good.
        """

        #return self.method1(nums)
        #return self.method2(nums)
        return self.method3(nums)

    def method1(self, nums):
        """
        Insert into intervals
        """
        rst = deque()
        rst.append([nums[0]])
        
        for i in range(1, len(nums)):
            n = len(rst)
            for _ in range(n):
                curr = rst.popleft()

                for j in range(len(curr) + 1):
                    curr_cp = curr[:j] + [nums[i]] + curr[j:]     
                    rst.append(curr_cp)
        
        return rst

    def method2(self, nums):
        """
        Use a set remove elements 
        Time: O(n!)
        Space: O(n!)
        """
        mSet = set(nums)
        self.rst = []
        cur_rst = []
        self.method2_recursion(mSet,cur_rst)
        return self.rst
    
            
    def method2_recursion(self, remain_nums, cur_rst):
        ## base case
        if not remain_nums:
            self.rst.append(cur_rst)
            return
 
        #copy_remain_nums = copy.deepcopy(remain_nums)
        for num in remain_nums:
            cur_rst_cp = cur_rst[:] 
            cur_rst_cp.append(num)
            copy_remain_nums = copy.deepcopy(remain_nums)
            copy_remain_nums.remove(num)
            self.method2_recursion(copy_remain_nums, cur_rst_cp)

    def method3(self, nums):
        """
        Brack tracking. 
        Use a deque to remove elements. 
        """
        rst = []
        curr = []
        nums = deque(nums)
        self.method3_recursion(nums, rst, curr)
        return rst


    def method3_recursion(self, remain, rst, curr):
        ## Base case
        if not remain:
            rst.append(curr[:])
            return
        for _ in range(len(remain)):
            val = remain.popleft()
            curr.append(val)
            self.method3_recursion(remain, rst, curr)
            ## Backtracking, revover to original state
            remain.append(val)
            curr.pop()

        


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    rst = s.permute(nums)
    print(rst)