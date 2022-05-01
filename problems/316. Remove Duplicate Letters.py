# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 21:14:06 2020

@author: wyue
"""

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {char:i  for i,char in enumerate(s)}
        seen = set()
        stack = []
        for i,char in enumerate(s):
            if char not in seen:
                while stack and char<stack[-1] and dic[stack[-1]]>i:
                    
                    seen.discard(stack.pop())
    
                stack.append(char)
                seen.add(char)
        return ''.join(stack)
            

s = "bcabc"
print(Solution().removeDuplicateLetters(s))