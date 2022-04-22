# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 12:09:15 2020

@author: wyue
"""
##from collections import defaultdict
from collections import Counter
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        if not T:
            return None
        
        voca = Counter(S)
        # ## Build vocabulary from s
        # for i in range(len(S)):
        #     ## Assumes that no repeated characters in S
        #     if not S[i] in voca:
        #         voca[S[i]] = i
        
        M = len(T)
        rst = [' '] * M
        right = M -1 
        shift = 0
        record = [0]*len(S)
        for j in range(M):
            ## if not in vocabulary, put from right to left.
            if not T[j] in voca:
                rst[right] = T[j]
                right -= 1
            else:
                record[voca[T[j]]] += 1
        index = 0
        for i in range(len(record)):
            for j in range(record[i]):
                rst[index] = S[i]
                index += 1
        
        rstString = ''
        for char in rst:
            rstString+=char
        return rstString
            