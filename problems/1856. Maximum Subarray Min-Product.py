from typing import List

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        """
        Prefixsum and monotonic stack
        Time: O(n)
        Space: O(n)
        """
        nums = [0] + nums
        prefixsum = [0 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            prefixsum[i] = prefixsum[i-1] + nums[i]
        
        ## use monotonic stack to find the index of next smaller number in nums
        next_smaller = [-1 for _ in range(len(nums))] ## -1 if no next smaller
        stack = []
        for i in range(1, len(nums)):
            while stack and nums[i] < nums[stack[-1]]:
                index = stack.pop()
                next_smaller[index] = i
            ## don't forget to add the current smallest element
            stack.append(i)
        
        ## use monotonic stack to find the index of previous smaller number in nums
        pre_smaller = [-1 for _ in range(len(nums))] ## len(nums) if no pre smaller
        stack = []
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[i] < nums[stack[-1]]:
                index = stack.pop()
                pre_smaller[index] = i
            ## don't forget to add the current smallest element
            stack.append(i)
        
        rst = 0
        for i in range(1, len(nums)):
            minv = nums[i]
            if next_smaller[i] != -1:
                nxtsmller = next_smaller[i] 
            else:
                nxtsmller = len(nums)
            
            if pre_smaller[i] != -1:
                presmller = pre_smaller[i]
            else:
                presmller = 0
            sumv  = prefixsum[nxtsmller - 1] - prefixsum[presmller]
            rst = max(rst, minv * sumv)
        
        M = int(1e9+7)
        return rst % M

if __name__ == "__main__":
    nums = [1,2,3,2]
    rst = Solution().maxSumMinProduct(nums)
    print(rst)
                
