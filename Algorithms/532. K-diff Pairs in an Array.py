from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        return self.solution1(nums, k)

    def solution1(self, nums, k):
        """
        O(nlogn)
        Sort plut sliding window, do not use hashing map to avoid duplication.
        """
        nums.sort()
        count = 0
        left = 0
        right = 0
        while left < len(nums) and right < len(nums):
            if left == right:
                right += 1
                continue
            if nums[right] - nums[left] < k:
                right += 1
                continue
            else:
                if nums[right] - nums[left] == k:
                    count += 1
                    right += 1
                    ## Remove redundant
                    while right < len(nums) and nums[right] == nums[right - 1]:
                        right += 1
                left += 1
                ## Remove redundant
                while left < right and nums[left] == nums[left - 1] :
                    left += 1

        return count




    def solution2(self, nums, k):
        """
        O(nlogn) sort plus sliding window
        Use hashmap to avoid duplication
        """   
        seen = set()
        nums.sort()
        count = 0
        left = 0
        for right in range(1, len(nums)):
            if nums[right] - nums[left] >= k:
                while left < right and nums[right] - nums[left] >= k :
                    if nums[right] - nums[left] == k:
                        if (nums[right], nums[left]) not in seen:
                            count += 1
                            seen.add((nums[right], nums[left]))
                    left += 1
        return count



    def solution3(self, nums, k):
        """
        Straight forward, TLE.
        O(n^2) TLE
        """    
        seen = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    if (nums[i], nums[j]) not in seen and (nums[j], nums[i]) not in seen:
                        seen.add((nums[i], nums[j]))
    
        return len(seen)

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,1,1]
    k = 0
    print(s.findPairs(nums, k))

"""
Test cases:
1. empty nums
2. 1 elements in nums
3. 2 elements in nums
4. normal cases

"""

