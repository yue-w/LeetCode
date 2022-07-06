
from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
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