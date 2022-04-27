
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # memo = {}
        # return self.recursion(0, nums, memo)
        return self.greedy(nums)
        
    def recursion(self, pos, nums, memo):
        """
        Dynamic programming
        time: O(n^2)
        """
        ## Base case:
        if pos == len(nums) - 1:
            memo[pos] = True
            return True
        if pos in memo:
            return memo[pos]
        
        for i in range(1, nums[pos] + 1):
            run_rst = self.recursion(pos + i, nums, memo)
            if run_rst:
                memo[pos] = True
                return True
        memo[pos] = False
        
        return False

    def greedy(self, nums):
        """
        time: O(n)
        """
        if len(nums) == 1:
            return True
        end_index = len(nums) - 1
        i = len(nums) - 2
        while i >= 0:
            if i + nums[i] >= end_index:
                end_index = i  
            i -= 1

        return end_index == 0


if __name__ == '__main__':
    s = Solution()
    nums = [2,3,1,1,4]
    print(s.canJump(nums))