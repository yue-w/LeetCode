from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #return self.method1(heights) ## preferred method. 3 pass but straight forward.
        return self.method2(heights)
    def method1(self, heights):
        """
        Monotonic stack. 
        """
        ## get the index of the next smaller (look right)
        n = len(heights)
        nxtsmaller = [n] * n
        stack = []
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                nxtsmaller[stack[-1]] = i
                stack.pop()
            stack.append(i)
        
        ## get the index of the next smaller (look left)
        presmaller = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                presmaller[stack[-1]] = i
                stack.pop()
            stack.append(i)
        
        rst = 0
        for i in range(n):
            area = heights[i] * (nxtsmaller[i] - presmaller[i] - 1)
            rst = max(rst, area)
            
        return rst
    
    def method2(self, heights):
        """
        The idea is the same as method1, but one pass. 
        """
        heights = [0] + heights + [0]
        ## monotonic increasing stack
        stack = []
        rst = 0
        for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    index = stack.pop()
                    height = heights[index]
                    width = i - stack[-1] - 1 
                    rst = max(rst, width * height)
                stack.append(i)
            
        return rst