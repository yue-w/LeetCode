from typing import List
import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.rst = []
        curr = []
        self.recursion(0, nums, curr)
        return self.rst

    def recursion(self, i, nums, curr):
        ## Base case
        if i >= len(nums):
            self.rst.append(curr[:])
            return
        
        ## use node of this level
        curr.append(nums[i])
        self.recursion(i+1, nums, curr)
        ## recover state in back tracking
        curr.pop()

        ## Do not use this level
        self.recursion(i+1, nums, curr)



    
    # def recursion(self, i, nums):
    #     ## Base case
    #     if not nums[i:]:
    #         return [[]]
    #     num = nums[i]
    #     new = self.recursion(i+1, nums)
    #     new_copy = copy.deepcopy(new)
    #     for n in new_copy:
    #         n.append(num)
    #     ans = new + new_copy
        
    #     return ans


if __name__ == '__main__':
    s = Solution()
    nums  = [0, 1, 4]

    print(s.subsets(nums))