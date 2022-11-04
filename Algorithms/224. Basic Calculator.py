

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        rst = 0
        
        for char in s:
            if char == ' ':
                continue
            if char == ')':
                num1 = ''
                num2 = ''
                while stack[-1] != '+' and stack[-1] != '-':
                    s2 = stack.pop()
                    if isinstance(s2, str):
                        num2 += s2
                    else:
                        num2 = s2
                        break
                num2 = int(num2)
                op = stack.pop()
                while stack[-1] != '(':
                    s1 = stack.pop()
                    if isinstance(s1, str) and stack[-1] != '+' and stack[-1] != '-':
                        num1 += s1
                    else:
                        num1 = s1
                        break

                    num1 = int(num1)
                    if stack and stack[-1] == '-':
                        num1 = -num1
                        stack.pop()
                        if stack:
                            stack.append('+')
                    if op == '+':
                        num2 = num1 + num2
                    else:
                        num2 = num1 - num2
                    stack.append(num2)
                else:
                    stack.append(char)

                stack.pop() ## pop "("


        while stack:
            if len(stack) == 1:
                return stack[0]
            num1 = ''
            num2 = ''
            while stack and stack[-1] != '+' and stack[-1] != '-':
                s2 = stack.pop()
                if isinstance(s2, str):
                    num2 += s2
                else:
                    num2 = s2
                    continue
            if not stack:
                return num2
            elif len(stack) == 1:
                return -num2
            else:
                op = stack.pop()
            while stack and stack[-1] != '+' and stack[-1] != '-':
                s1 = stack.pop()
                if isinstance(s1, str):
                    num1 += s1
                else:
                    num1 = s1
            num1 = int(num1)
            if stack and stack[-1] == '-':
                num1 = -num1
                stack.pop()
                if stack:
                    stack.append('+')
            if op == '+':
                num2 = num1 + num2
            else:
                num2 = num1 - num2
            stack.append(num2)
                

                
        
if __name__ == '__main__':

    s = Solution()
    string = "(1+(4+5+2)-3)+(6+8)"
    rst = s.calculate(string)
    print(rst)

        