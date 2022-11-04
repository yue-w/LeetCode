from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        return self.method1(nums)
        #return self.method2(nums) ## preferred method
    
    def method1(self, nums):
        """
        Search wraparound
        Time: O(n)
        Space: O(n)
        """
        
        rst = [-1] * len(nums)
        ## monotonic decreasing stack
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                index = stack.pop()
                rst[index] = nums[i]
            stack.append(i)

        ## if there are still elements in the stack.
        ## the first element in the stack is the first
        ## number that has no next greater number. It is 
        ## also the last element in the wrap around search (because of 
        ## the stack is monotonic decreasing).
        if stack:
            for i in range(stack[0] + 1):
                while stack and nums[i] > nums[stack[-1]]:
                    index = stack.pop()
                    rst[index] = nums[i]
        return rst
    
    def method2(self, nums):
        """
        Extend the array.
        Time: O(n)
        Space: O(n)
        """
        
        n = len(nums)
        rst = [-1] * (2*n)
        nums = nums + nums
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                index = stack.pop()
                rst[index] = nums[i]
            stack.append(i)
        
        return rst[:n]


if __name__ == '__main__':
    nums = [1,2,1]
    rst = Solution().nextGreaterElements(nums)
    print(rst)
