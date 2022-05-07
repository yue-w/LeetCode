
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Monotonic stack
        """
        rst = [0] * len(temperatures)
        ## Monotonic decrease stack
        ## first element is index of the number, second is its value
        stack = []
        stack.append((0, temperatures[0]))
        for i in range(1, len(temperatures)):
            if temperatures[i] <= stack[-1][1]:
                ## append, first element is index of the number, second is its value
                stack.append((i, temperatures[i]))
            else:
                while stack and temperatures[i] > stack[-1][1]:
                    index, val = stack.pop()
                    rst[index] = i - index

                stack.append((i, temperatures[i]))
                    
        return rst