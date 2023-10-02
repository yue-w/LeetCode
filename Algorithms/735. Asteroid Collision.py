from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        n = len(asteroids)
        for i in range(n):
            survive = asteroids[i]
            while stack and (stack[-1] > 0 and survive < 0):
                left = stack.pop()
                if left > abs(survive):
                    survive = left
                elif left == abs(survive):
                    survive = 0
            if survive:
                stack.append(survive)

        return stack