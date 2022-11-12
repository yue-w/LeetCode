from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        #return self.method1(nums) ## basic method
        return self.method2(nums) ## better method

    def method1(self, nums):
        """
        Use set to avoid duplicates
        recursion + hash
        """
        def dfs(curr, idx):
            ## base case
            if idx == len(nums):
                return
            
            for i in range(idx, len(nums)):
                if curr and nums[i] < curr[-1]:
                    continue
                curr.append(nums[i])
                if len(curr) > 1:
                    rst.add(tuple(curr))
                dfs(curr, i + 1)
                # backtracking
                curr.pop()
            
        rst = set()
        dfs([], 0)
        return list(rst)
        
    def method2(self, nums):
        """
        Search in an array. 
        Better way to avoid duplicates.
        """
        def dfs(curr, idx):
            """
            Use this example as a template to use a local set (in dfs) to 
            avoid duplicates.
            Example: [4,6,6,7,7]
            All possibilibies starting with the second 6 have been considered
            in the cases starting with the first 6. So we should ignore the 
            second 6.
            """
            ## base case
            if idx == len(nums):
                return
            
            ## hashing local to this dfs
            visited = set()
            for i in range(idx, len(nums)):
                if curr and nums[i] < curr[-1]:
                    continue
                if nums[i] in visited:
                    continue
                visited.add(nums[i])
                curr.append(nums[i])
                if len(curr) > 1:
                    rst.append(curr[:])
                dfs(curr, i+1)
                curr.pop()
        
        rst = []
        dfs([], 0)
        return rst
        
            
        
        
if __name__ == '__main__':
    nums = [4,6,7,7]
    rst = Solution().findSubsequences(nums)
    print(rst)