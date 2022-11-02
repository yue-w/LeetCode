
from typing import List

class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        rst = 0
        nums = list(set(nums))
        
        def bit_count_one(n):
            count = 0
            while n:
                count += 1
                n &= n - 1
            return count
        
        array = [0] * len(nums)
        for i, n in enumerate(nums):
            array[i] = bit_count_one(n)
        
        array.sort()
        
        ## (n1, n2), where n1 != n2
        ## two pointers
        n = len(array)
        j = n - 1
        for i in range(n-1):
            while j >= 0 and array[i] + array[j] >= k:
                j -= 1
            if j >= i:
                rst += (n - j - 1)
            else:
                rst += (n - i - 1)
        rst *= 2
        
        ## (n1, n1)
        for n in array:
            if 2 * n >= k:
                rst += 1
                
        return rst
                
        
        
        
            
        