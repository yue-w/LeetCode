
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Monotonic stack
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []
        ## elements in stack, (tem, index)
        for i in range(n):
            while stack and stack[-1][0] < temperatures[i]:
                tem, idx = stack.pop()
                answer[idx] = i - idx
            stack.append((temperatures[i], i))

        return answer