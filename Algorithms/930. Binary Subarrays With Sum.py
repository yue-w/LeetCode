
from typing import List
from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #return self.pre_sum(nums, goal)
        return self.slide_window(nums, goal)


    def pre_sum(self, nums, goal):
        pre_count = defaultdict(int)
        pre_count[0] = 1
        pre_sum = 0
        rst = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            need = pre_sum - goal
            rst += pre_count[need]
            pre_count[pre_sum] += 1
        return rst


    def slide_window(self, nums, goal):
        """
        This code is from forum, don't understand the idea yet.
        """
        l = count = res = s = 0
        for r, i in enumerate(nums):
            s += i
            if i == 1:
                count = 0
            while l <= r and s >= goal:
                if s == goal:
                    count += 1
                s -= nums[l]
                l += 1
            res += count
        return res



if __name__ == '__main__':
    s = Solution()
    nums = [1,0,1,0,1]
    goal = 2
    nums = [0,0,0,0,0]
    goal = 0
    rst = s.numSubarraysWithSum(nums, goal)
    print(rst)