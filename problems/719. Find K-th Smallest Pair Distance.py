from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """
        Binary search, sort
        Use O(n) time to find count of sum that is not larger than
        """
        nums.sort()
        left = 0
        right = max(nums) - min(nums)
        while left < right:
            mid = left + (right - left) // 2
            if self.count_not_larger(nums, mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
        
    def count_not_larger(self, nums, val):
        """
        O(n) time to find pair of sums not larger than val
        two pointers
        """
        count = 0
        i = 0
        for j in range(len(nums)):
            while i < j and nums[j] - nums[i] > val:
                i += 1
            count += j - i
                
        return count

if __name__ == "__main__":
    nums = [9,10,7,10,6,1,5,4,9,8]
    k = 18
    rst = Solution().smallestDistancePair(nums, k)
    print(rst)