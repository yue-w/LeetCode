# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 23:05:50 2020

@author: wyue
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        
        rst = 0
        i = 0
        while i < len(s):
            if s[i] == 'I':
                if i < len(s) - 1 and s[i+1] == 'X':
                    rst += 9
                    i += 2
                elif i < len(s) - 1 and s[i+1] == 'V':
                    rst += 4
                    i += 2
                else:
                    rst += 1
                    i += 1
            elif s[i] == 'X':
                if i < len(s) - 1 and s[i+1] == 'L':
                    rst += 40
                    i += 2
                elif i < len(s) - 1 and s[i+1] == 'C':
                    rst += 90
                    i += 2
                else:
                    rst += 10
                    i += 1
            elif s[i] == 'C':
                if i < len(s) - 1 and s[i+1] == 'D':
                    rst += 400
                    i += 2
                elif i < len(s) - 1 and s[i+1] == 'M':
                    rst += 900
                    i += 2
                else:
                    rst += 100
                    i += 1
            elif s[i] == 'V':
                rst += 5
                i += 1
            elif s[i] == 'L':
                rst += 50
                i += 1
            elif s[i] == 'D':
                rst += 500
                i += 1
            else: # "M"
                rst += 1000
                i += 1
                  
        
        return rst
