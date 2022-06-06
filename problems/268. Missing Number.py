from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #return self.method1(nums)
        #return self.method2(nums)
        return self.method3(nums)

    def method1(self, nums):
        n = len(nums)
        total1 = int((0 + n) * (n + 1) / 2)
        total2 = sum(nums)
        return total1 - total2
    
    def method2(self, nums):
        rst = 0
        n = len(nums)
        for i in range(n + 1):
            rst ^= i
            
        for n in nums:
            rst ^= n
            
        return rst
        
    def method3(self, nums):
        rst = len(nums)        
        
        #for i in range(len(nums)):
        for i in range(len(nums)):
            while i != nums[i] and nums[i] < len(nums) and nums[nums[i]] != nums[i]:
                nums[nums[i]], nums[i] =  nums[i], nums[nums[i]] 

        for i, n in enumerate(nums):
            if i != n:
                return i
        
        return rst

if __name__ == '__main__':
    s = Solution()
    nums = [9,6,4,2,3,5,7,0,1]
    rst = s.missingNumber(nums)
    print(rst)