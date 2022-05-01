# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 18:25:57 2020

@author: wyue
"""

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        
        left = 0
        tem_rst = []
        for char in s:
            if char == '(':
                left += 1
            
            elif char == ')':
                ## Ignore unpaired ')'
                if left==0:
                    continue
                else:
                    left -= 1
            tem_rst.append(char)
        
        rst = []
        
        ## Remove extra '('
        ## Start from right to left!!!!
        for i in range(-1,-len(tem_rst)-1,-1):
            if tem_rst[i] == '(' and left>0:
                left -= 1
                continue
            else:
                rst.append(tem_rst[i])
        rst.reverse()
        return ''.join(rst)

string =  "(t(e)y))d(()(e("
print(Solution().minRemoveToMakeValid(string))