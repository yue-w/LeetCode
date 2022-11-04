# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:38:13 2020

@author: wyue
"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack_n = []
        stack_b = []
        rst = ''
        
        
        if len(stack_n) == 0:
            rst += char
                
s = "2[abc]3[cd]ef"
print(Solution().decodeString(s))                
                        
"""

        stack = []
        run_str = ''
        rst = ''
        numLeft = 0
        stack_l = []
        for char in s:
            if char == ']':
                while stack[-1] != '[':
                    run_str = stack.pop() + run_str
                ## delete the '['
                stack.pop()
                stack_l.pop()
                ## get the number
                num = int(stack.pop())
                
                if len(stack_l)>0:
                    stack.append(num*run_str)
                else:
                     rst += num*run_str
                run_str = ''
            
            elif char == '[':
                stack_l.append(char)
                stack.append(char)
            else:
                stack.append(char)

        return rst
        
"""