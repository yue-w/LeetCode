from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #return self.method1(nums)
        return self.method2(nums) ## preferred method
    
    def method1(self, nums):
        """
        Hashing.
        Time: O(n)
        Space: O(n)
        """
        nums_set = set(nums)
        seen = set()
        rst = 0
        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            counter = 1
            cur_num = num
            ## go larger
            while cur_num + 1 in nums_set:
                seen.add(cur_num + 1)
                cur_num += 1
                counter += 1
            ## go smaller
            cur_num = num
            while cur_num - 1 in nums_set:
                seen.add(cur_num - 1)
                cur_num -= 1
                counter += 1
            
            rst = max(rst, counter)
        
        return rst
    
    def method2(self, nums):
        """
        Same idea with method1, but a little bit less codes.
        for a number num in nums, if num-1 is not in nums, then num is the 
        lower bound of a continuous sequence, we check its upper bound.
        But if num - 1 is not in nums, then num is not a lower bound, we do
        not check it.
        """
        nums_set = set(nums)
        rst = 0
        for num in nums:
            ## if num - 1 in nums_set, ignore
            if num - 1 in nums_set:
                continue
            ## if num - 1 not in nums_set, num is the lower bound of a continuous
            ## sequence. We count how long it is, update rst.
            curr = 1
            while num + 1 in nums_set:
                curr += 1
                num += 1
            rst = max(rst, curr)
        
        return rst

if __name__ == '__main__':
    nums = [0,3,7,2,5,8,4,6,0,1]
    rst = Solution().longestConsecutive(nums)
    print(rst)