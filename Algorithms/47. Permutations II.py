
from collections import deque
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums = deque(nums)
        rst = []
        curr = []
        self.recursion(nums, rst, curr)
        return rst
        
    def recursion(self, nums, rst, curr):
        ## Basse case
        if not nums:
            rst.append(curr[:])
            return
        former = None
        for _ in range(len(nums)):
            first = nums.popleft()
            if first == former:
                nums.append(first)
                continue
            ## record the current value to avoid duplication
            former = first
            curr.append(first)
            self.recursion(nums, rst, curr)
            ## Backtracking, reset state
            nums.append(first)
            curr.pop()

if __name__ == '__main__':
    s = Solution()
    nums = [3,2,1]
    rst = s.permuteUnique(nums)
    print(rst)