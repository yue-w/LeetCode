# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:00:10 2020

@author: wyue
"""

from collections import defaultdict
class Solution(object):
    """
    ## Method One: AccumulateThenContract + Sliding Window
    def checkInclusion(self, s1, s2):
        if not s1:
            return True
        if len(s1)>len(s2):
            return False
        array = [0]*26
        for char in s1:
            index = ord(char) - ord('a')
            array[index] += 1
        
        for i in range(len(s2) - len(s1)+ 1):
            array_copy = array[:] 
            if self.helper(array_copy, s2[i:i+len(s1)]):
                return True
        return False
            
        
    def helper(self, array, str2):
        for char in str2:
            index = ord(char) - ord('a')
            array[index] -= 1
            if array[index]<0:
                return False
        return sum(array) == 0
    """
    """
    ## Method Two: Hash + Sliding Window
    def checkInclusion(self, s1, s2):
        if not s1:
            return True
        if len(s1)>len(s2):
            return False
        dic = defaultdict(int)
        for char in s1:
            dic[char] += 1
        import copy
        for i in range(len(s2) - len(s1)+ 1):
            dic_copy = copy.deepcopy(dic)
            if self.helper(dic_copy, s2[i:i+len(s1)]):
                return True
        return False
            
        
    def helper(self, dic, str2):
        for char in str2:
            dic[char] -= 1
            if dic[char] <0:
                return False
        return True
        ##return sum(dic) == 0
    """
    ## Method three: two vector + Sliding Window
    def checkInclusion(self, s1, s2):
        if not s1:
            return True
        if len(s1)>len(s2):
            return False
        array1 = [0]*26
        for char in s1:
            index = ord(char) - ord('a')
            array1[index] += 1
        array2 = [0]*26
        ## Sliding window
        windowLen = len(s1)
        for i in range(len(s2)):
            index = ord(s2[i]) - ord('a')
            array2[index] += 1
            if i >= len(s1):
                index = ord(s2[i-windowLen]) - ord('a')
                array2[index] -= 1
            if array1 == array2:
                return True
        return False

        
            

s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1,s2))

