# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 18:25:57 2020

@author: wyue
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        string = [s[i] for i in range(len(s))]
        stack = []
        for i, char in enumerate(string):
            if char == ')':
                if not stack:
                    ## set unpired ')' to a special token, so that we can remove
                    ## them later
                    string[i] = '*'
                else:
                    stack.pop()
            elif char == '(':
                ## record the index of '(', we may use it to
                ## locate it if it is not paired.
                stack.append(i)
        
        ## removed unpired '(' in stack.
        while stack:
            ## set unpired '(' to a special token, so that we can remove
            ## them later
            string[stack.pop()] = '*'

        rst = []
        for char in string:
            if char != '*':
                rst.append(char)

        return ''.join(rst)


string =   "lee(t(c)o)de)"
print(Solution().minRemoveToMakeValid(string))