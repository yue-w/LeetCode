from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """
        Binary search, sort
        Use O(n) time to find count of sum that is not larger than
        """
        def count_not_larger(val):
            """
            O(n) time to find pair of differens not larger than val
            two pointers
            """
            count = 0
            j = 1
            n = len(nums)
            for i in range(n):
                while j < n and nums[j] - nums[i] <= val:
                    j += 1
                    """
                    now nums[j] - nums[i] <= val
                    i.e. any intervals with j as the right bound and 
                    any point between i and j as the left bound satisfies 
                    nums[j] - nums[i] <= val, there are j - i - 1 such pairs
                    """
                    count += j - i - 1
            return count

        nums.sort()
        left = 0
        right = max(nums) - min(nums)
        while left < right:
            mid = left + (right - left) // 2
            if count_not_larger(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left

if __name__ == "__main__":
    nums = [9,10,7,10,6,1,5,4,9,8]
    k = 18
    rst = Solution().smallestDistancePair(nums, k)
    print(rst)