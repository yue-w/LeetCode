# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 21:14:06 2020

@author: wyue
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        Time: O(n)
        Space: O(n)        
        """
        ## whether the char has been added into the result
        added = [False for _ in range(26)]
        
        ## the index of the last occurance of the char
        last_occurance = [0 for _ in range(26)]
        for i, char in enumerate(s):
            last_occurance[ord(char) - ord('a')] = i
        
        ## keep a monotonic increasing stack
        stack = []
        
        for i, char in enumerate(s):
            ## if the char has been added, continue
            if added[ord(char) - ord('a')]:
                continue
            #### keep poping values from stack in the following cases are all satisfied:
            ## 1. char is smaller than stack[-1]
            ## 2. the last occurance of stack[-1] is larger than i
            ## 3. stack is not empty
            while stack and char < stack[-1] and last_occurance[ord(stack[-1]) - ord('a')] > i:
                topchar = stack.pop()
                added[ord(topchar) - ord('a')] = False
            stack.append(char)
            added[ord(char) - ord('a')] = True
        return ''.join(stack)
            

s = "bcabc"
print(Solution().removeDuplicateLetters(s))