from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.kadane(nums)

    def kadane(self, nums):
        cur_max = nums[0]
        global_max = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(cur_max + nums[i], nums[i])
            global_max = max(global_max, cur_max)
        return global_max
                