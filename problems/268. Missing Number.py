from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #return self.method1(nums)
        #return self.method2(nums) ## XOR preferred method
        return  self.method3(nums)
    def method1(self, nums):
        """
        Trick.
        Time: O(n)
        Space: O(1)
        """
        n = len(nums)
        total1 = int((0 + n) * (n + 1) / 2)
        total2 = sum(nums)
        return total1 - total2
    
    def method2(self, nums):
        """
        XOR.
        Time: O(n)
        Space: O(1)
        """
        rst = 0
        n = len(nums)
        for i in range(n + 1):
            rst ^= i
            
        for n in nums:
            rst ^= n
            
        return rst
    
    def method3(self, nums):
        """
        indexing sort
        Time: O(n)
        Space: O(n)
        """
        #### indexing sort
        rst = len(nums)
        for i in range(len(nums)):
            if i == nums[i]:
                continue
            while nums[i] != i and nums[i] < len(nums):
                ## swap
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return rst

if __name__ == '__main__':
    s = Solution()
    nums = [9,6,4,2,3,5,7,0,1]
    rst = s.missingNumber(nums)
    print(rst)