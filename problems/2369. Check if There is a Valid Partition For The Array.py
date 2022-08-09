from typing import List
from functools import lru_cache
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        return self.method1(nums)
        return self.method2(nums) # template of how to use lru_cache decrator
    def method1(self, nums):
        """
        Write memo.
        """
        def recursion(i):
            """
            call recursion only if there are enough elements, i.e., i is valid
            """
            ## base case:
            if i == len(nums):
                memo[i] = True
                return True
            if i == len(nums) - 1:
                memo[i] = False
                return False
            if i in memo:
                return memo[i]
            ## case 1
            if nums[i] == nums[i+ 1] :
                case1 = recursion(i + 2)
            else:
                case1 = False
            #memo[i + 2] = case1
            if i < len(nums) - 2 and nums[i] == nums[i + 1] and nums[i + 1] == nums[i + 2]:
                case2 = recursion(i + 3)
            else:
                case2 = False

            if i < len(nums) - 2 and nums[i] + 1 == nums[i + 1] and nums[i + 1] + 1 == nums[i + 2]:
                case3 = recursion(i + 3)
            else:
                case3 = False
            """
            Why it is wrong to memo here?
            """
            #memo[i + 3] = (case2 or case3)
            memo[i] = (case1 or case2 or case3)
            return (case1 or case2 or case3)
            
        memo = {}    
            
        return recursion(0)

    def method2(self, nums):
        """
        Use built-in cache
        """
        #@cache
        @lru_cache(None)
        def recursion(i):
            """
            call recursion only if there are enough elements, i.e., i is valid
            """
            ## base case:
            if i == len(nums):

                return True
            if i == len(nums) - 1:

                return False
            ## case 1
            if nums[i] == nums[i+ 1] :
                case1 = recursion(i + 2)
            else:
                case1 = False
            #memo[i + 2] = case1
            if i < len(nums) - 2 and nums[i] == nums[i + 1] and nums[i + 1] == nums[i + 2]:
                case2 = recursion(i + 3)
            else:
                case2 = False

            if i < len(nums) - 2 and nums[i] + 1 == nums[i + 1] and nums[i + 1] + 1 == nums[i + 2]:
                case3 = recursion(i + 3)
            else:
                case3 = False

            return (case1 or case2 or case3)
            
 
            
        return recursion(0)