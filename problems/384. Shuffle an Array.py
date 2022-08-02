import random
from typing import List
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        ## Fisher–Yates shuffle
        nums = self.nums[:]
        for i in range(len(nums)-1, 0, -1):
            index = random.randrange(0, i+1)
            nums[i], nums[index] = nums[index], nums[i]
        return nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()