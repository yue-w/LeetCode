# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 21:14:06 2020

@author: wyue
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        rst = []
        counter = collections.Counter(s)
        seen = set()
        for char in s:
            if char in seen:
                counter[char] -= 1
            else:
                while rst and rst[-1] > char and counter[rst[-1]] > 0:
                    seen.remove(rst[-1])
                    rst.pop()
                rst.append(char)
                counter[char] -= 1
                seen.add(char)

        return ''.join(rst)
            

s = "bcabc"
print(Solution().removeDuplicateLetters(s))