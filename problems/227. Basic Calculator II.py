

from tables import StringCol


class Solution:
    def calculate(self, s: str) -> int:
        return self.method1(s)
        #return self.method2(s)
        
    def method1(self, s):
        """
        A better solution from online
        Use an array and a stack.
        first step deal with * and /, which only
        operate on the last element in the stack. 
        After dealing with * and /, put everything in 
        a stack, then sum all the numbers in the stack
        """
        ## remove space
        ## add a + to the fist number
        string = ['+']
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            string.append(s[i])
        string = ''.join(string)
        
        stack = []
        i = 0
        while i < len(string):
            if string[i] == '+' or string[i] == '-':
                operator = string[i]
                j = i + 1
                while j < len(string) and string[j].isdigit():
                    j += 1
                if operator == '-':
                    num = -int(string[i+1:j])
                    
                else:
                    num = int(string[i+1:j])
                stack.append(int(num))
                i = j 
            else: # * or /
                operator = string[i]
                j = i + 1
                while j < len(string) and string[j].isdigit():
                    j += 1
                num = int(string[i + 1 : j])
                # if operator == '-':
                #     num = -int(string[i+1:j])  
                # else:
                #     num = int(string[i+1:j])
                if operator == '*':
                    stack[-1] *= num
                else:
                    stack[-1] = int(stack[-1] / num)
                i = j 
            
            
        
        return sum(stack)
        
        
    def method2(self, s):
        """
        My initial solution. 
        Time: O(n)
        Space: O(n)
        """
        dic_op = set(['+', '-', '*', '/'])
        
        stack = []
        for i in range(-1, - len(s) - 1, -1):
            if s[i] == ' ':
                continue
            stack.append(s[i])
        
        while stack:
            if stack[-1] == '+':
                stack.pop()
                return stack.pop()
            num1 = self.get_number(stack, dic_op)
            if not stack:
                return num1
            operator = stack.pop()
            ## if * or / Get the second number and compute
            if operator == '*' or operator == '/':
                num2 = self.get_number(stack, dic_op)
                num = self.compute(operator, num1, num2)
                if num < 0:
                    stack.append('+')
                    stack.append(-num)
                else:
                    stack.append(num)
                        
            ## elif + or -, check whether next operator is * or /
            else:
                num2 = self.get_number(stack, dic_op)
                
                ## if there are more operators and it is * or /, 
                ## compute num2 operate num3, and append every thing back, continue
                if stack and stack[-1] in ['*', '/']:
                    operator2 = stack.pop()
                    num3 = self.get_number(stack, dic_op)
                    val = self.compute(operator2, num2, num3)
                    if val < 0:
                        stack.append('+')
                        stack.append(-val)
                    else:
                        stack.append(val)
                    stack.append(operator)
                    stack.append(num1)
                
                ## else compute and append
                else:
                    val = self.compute(operator, num1, num2)
                    stack.append(val)
                        
                
    def get_number(self, stack, dic_op):
        num1 = stack.pop()
        if isinstance(num1, str):
            while stack:
                tem = stack.pop()
                if tem not in dic_op:
                    num1 += tem
                else:
                    num1 = int(num1)
                    stack.append(tem)
                    break                 
        return int(num1)
    
    def compute(self, operator, num1, num2):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        else:
            return int(num1 / num2)
                    
                    

if __name__ == '__main__':
    s = Solution()
    string = "0-2147483647"
    rst = s.calculate(string)
    print(rst)