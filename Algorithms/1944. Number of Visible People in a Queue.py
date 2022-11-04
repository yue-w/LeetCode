
from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        #return self.method1(heights) 
        return self.method2(heights)
        
    def method1(self, heights):
        """
        Monotonic stack. 
        """
        rst = [0] * len(heights)
        
        ## monotonus decreasing stack (store index of heights)
        stack = []
        
        for i in range(len(heights)):
            while stack and heights[i] >= heights[stack[-1]]:
                index = stack.pop()
                rst[index] += 1
                if stack:
                    rst[stack[-1]] += 1
            stack.append(i)
            
        
        ## if the stack is not empty in the end, it must be a monotonus decreasing
        ## stack, every person can see an extra one more person (the adjacent person in
        ## the stack to the right)
        while stack:
            index = stack.pop()
            rst[index] += 1
        
        rst[-1] = 0
        return rst
    
    def method2(self, heights):
        """
        Preferred method
        Monotonic stack. Same idea with method1, but 
        iterate through heights in reverse order. 
        """
        
        ## monotonic decreasing stack
        stack = []
        rst = [0] * len(heights)
        
        for i in range(len(heights) - 1, -1, -1):
            count = 0
            while stack and heights[i] > heights[stack[-1]]:
                count += 1
                stack.pop()
            if stack:
                count += 1
            stack.append(i)
            rst[i] = count
        return rst