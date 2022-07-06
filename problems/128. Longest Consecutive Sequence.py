from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        """
        return self.method1(nums)

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
        rst = 0
        seen = {n for n in nums}
        
        while seen:
            counter = 1
            pivot = seen.pop()
            pivot_p = pivot + 1
            while pivot_p in seen:
                counter += 1
                seen.remove(pivot_p)
                pivot_p += 1
                
            pivot_m = pivot - 1
            while pivot_m in seen:
                counter += 1
                seen.remove(pivot_m)
                pivot_m -= 1
                
            rst = max(rst, counter)
            
            
        return rst

if __name__ == '__main__':
    nums = [0,3,7,2,5,8,4,6,0,1]
    rst = Solution().longestConsecutive(nums)
    print(rst)