
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        Ideas: 
        Stack
        """
        stack = []
        curr = 0
        for c in s:
            if c == ')':
                if curr == 0:
                    curr = 1
                else:
                    curr *= 2
                curr += stack.pop()
            else:
                stack.append(curr)
                curr = 0
        return curr