# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 17:59:18 2020

@author: wyue
"""

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increase = decrease = True
        for i in range(len(A)-1):
            if A[i]<A[i+1]:
                decrease = False
            if A[i]>A[i+1]:
                increase = False 
        return decrease or increase
        
        
    """
    ## My solution
    def isMonotonic(self, A):
        if len(A) == 1 or len(A) == 2: 
            return True
        
        i = 0
        
        while i<len(A)-1:
            if A[i] == A[i+1]:
                i += 1
            elif A[i]<A[i+1]:
                inc = True
                break
            else:
                inc = False
                break
            i += 1
            
        
        for j in range(i,len(A)-1):
            
            if inc == True:
                if A[j] > A[j+1]:
                    return False
            else:
                if A[j] < A[j+1]:
                    return False
                
        return True
        """
    
