
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ## Two pointers
        ## Time O(n)
        ## Space O(1)
        if len(nums) < 2:
            return len(nums)
            
        left = 2
        right = 2
        
        while right < len(nums):      
            ## index left is the index of the first invalid number.              
            if nums[left - 2] != nums[right]:
                nums[left] = nums[right]
                left += 1
            right += 1

        return left 

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,2,2,3]
    k = s.removeDuplicates(nums)
    print(nums[:k])