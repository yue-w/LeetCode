from typing import List 


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return self.method1(nums)
        #return self.method2(nums)

    def method1(self, nums):
        """
        remove duplicate from nums
        idea: consider this as a tree. The left path being selecting this node,
        and the right path being not selecting this node. All paths starting from 
        the right path and below the right path should not selecting node with the 
        same value (because the left path tare of selecting of not selecting this 
        value already). ref: https://www.youtube.com/watch?v=Vn2v6ajA7U0&t=417s
        Another way to think about this is:
        for n components with the same value, if we want to select k of them, we 
        will only select the first k of them. So if the previouse one with the 
        same value was not selected, the current one should not be selected. 
        ref: https://github.com/wisdompeak/LeetCode/tree/master/DFS/090.Subsets-II
        """
        self.rst = []
        curr = []
        nums.sort()
        self.dfs(nums, 0, curr)
        return self.rst


    def dfs(self, nums, i, curr):
        ## Base case
        if i >= len(nums):
            self.rst.append(curr[:])
            return
        
        ## Use current level
        curr.append(nums[i])
        self.dfs(nums, i + 1, curr)
        ## recover the state for backtracking
        curr.pop()

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1

       ## Do not use the current level
        self.dfs(nums, i + 1, curr)

    def method2(self, nums):
        """
        Use hashing to remove duplicate
        """
        seen = set()
        self.rst = []
        #self.rst.append([])
        curr = []
        self.dfs2(nums, 0, curr, seen)
        return self.rst
        
    def dfs2(self, nums, i, curr, seen):
        ## Base case
        if i >= len(nums):
            curr_cp = curr[:]
            curr_cp.sort()
            tp = tuple(curr_cp)
            if tp not in seen:
                self.rst.append(curr_cp)
                seen.add(tp)
            return 

        ## use nums[i]
        curr.append(nums[i])
        self.dfs2(nums, i + 1, curr, seen)
        curr.pop()

        ## do not use nums[i]
        self.dfs2(nums, i + 1, curr, seen)

        


if __name__ == '__main__':
    s = Solution()
    nums  = [1, 2, 2]

    print(s.subsetsWithDup(nums))