
from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        #return self.template1(nums, k)
        return self.template2(nums, k) 
    
    def template1(self, nums, k):
        """
        DFS
        Method 1: reference https://youtu.be/mBk4I0X46oI
        """
        total = sum(nums)
        if total % k != 0:
            return False
        nums.sort(reverse=True)
        memo = set()
        edge_len = total // k
        groups = [0] * k
        
        def dfs(index):
            ## base case
            if index == len(nums):
                return True

            ## check memo. memo only stores failed ones, because if find a single good one, return 
            if tuple(groups) in memo:
                return False
            
            for i in range(k): 
                if groups[i]  + nums[index] <= edge_len:
                    groups[i] += nums[index]
                    if dfs(index+1):
                        return True                  
                    ## backtracking 
                    groups[i] -=  nums[index]
                    
            memo.add(tuple(groups))
            return False
            
        return dfs(0)
    
    def template2(self, nums, k):
        """
        Template 2
        Reference: https://youtu.be/FQ7du5dpgb8
        """
        total = sum(nums)
        if total % k != 0:
            return False
        nums.sort(reverse=True)
        
        ## False if has not been selected, True if has been selected
        selected = [False] * len(nums)
        
        target = total // k
        
        def dfs(index, groupfound, cursum):
            """
            index: index of the element in nums to be considerred
            groupfound: number of groups have been found
            cursum: the current sum in this group
            """
            ## base case
            if groupfound == k:
                return True
            
            if cursum == target:
                return dfs(0, groupfound+1, 0)
            
            if cursum > target:
                return False
            
            prev = -1
            for i in range(index, len(nums)):
                if selected[i]:
                    continue
                if prev == nums[i]:
                    continue
                prev = nums[i]
                selected[i] = True 

                ## select this number and recurse
                if dfs(i+1, groupfound, cursum + nums[i]):
                    return True

                #backtracking
                selected[i] = False
                
            ## if did not return True, this path failed, return False
            return False
            
        return dfs(0, 0, 0)
            