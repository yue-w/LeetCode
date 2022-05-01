# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 12:07:19 2020

@author: wyue
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        rst = []
        for char in p:
            if char == '.':
                return self.dot(s, rst)
            elif char == '*':
                return self.star(s, rst)
            else:
                rst.append(char)
        rst = ''.join(rst)
        if  rst == s:
            return True
        else:
            return False

    def inspect_star(self, s, rst):
        rst = ''.join(rst)
        if  rst == s:
            return True
        else:
            return False
    
    def star(self,s, rst):
        pass