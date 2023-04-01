# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:04:58 2020

@author: wyue
"""

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        return self.method1(num)

    def method1(self, num):
        ## number to list
        numlist = [n for n in str(num)]
        ## Sort list in desending order
        revnumlist = sorted(numlist, reverse=True)
        i = 0
        ## find the fist occurance where there is a larger digit 
        ## locates after the current digit
        while i < len(numlist) and numlist[i] == revnumlist[i]:
            i += 1
        ## if revnumlist is monotonic decreasing, return num
        if i == len(numlist):
            return num
        
        index = 0
        ## find the last digit that equals to numlist[i]
        for j in range(i+1, len(numlist)):
            if numlist[j] == revnumlist[i]:
                index = j
        ## swap numlist[i] and numlist[index]
        numlist[i], numlist[index] = numlist[index], numlist[i]
        
        return int(''.join(numlist))

    def method2(self, num):
        A = list(map(int,str(num)))
        

        last = {x: i for i, x in enumerate(A)}
        
        for i, x in enumerate(A):
            for k in range(9, x, -1):
                if last.get(k, 0) > i:

                    A[i], A[last[k]] = A[last[k]], A[i]
                    return int("".join(map(str, A)))
        return num

  
print(Solution().maximumSwap(2736))