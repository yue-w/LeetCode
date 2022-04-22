# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 10:48:46 2020

@author: wyue
"""

class Solution(object):
    def addBinary(self, a, b):
        
        ## Method 1. My method, logic is a mess
        """
        rst = ''
        if len(a)==len(b):
            minlen = len(a)
            case = 'equal'
        elif len(a)<len(b):
            minlen = len(a)
            case = 'ashorter'
        else:
            minlen = len(b)
            case = 'b'
        carry = 0
        for i in range(1,minlen+1):
            num1 = int(a[-i])
            num2 = int(b[-i])
            if num1 + num2 + carry >= 2:
                rst = str(num1 + num2 + carry - 2) + rst
                carry = 1
            else:
                
                rst = str(num1 + num2 + carry) + rst
                carry = 0
        if case == 'equal':
            if carry == 1:
                return '1'+ rst
            else:
                return rst
        elif case == 'ashorter':
            for j in range(i+1, len(b)+1):
                digit = int(b[-j])
                if carry + digit >= 2:
                    rst = str(carry + digit - 2) + rst
                    carry = 1
                else:
                    
                    rst = str(digit+carry) + rst
                    carry = 0
            if carry == 1:
                rst = str(digit) + rst
        else:
            for j in range(i+1, len(a)+1):
                digit = int(a[-j])
                if carry + digit >= 2:
                    rst = str(carry + digit - 2) + rst
                    carry = 1
                else:
                    
                    rst = str(digit+carry) + rst
                    carry = 0
            if carry == 1:
                rst = str(digit) + rst
        return rst
        """
        ## Method 2, better method
        i = len(a) - 1
        j = len(b) - 1
        carry  = 0
        rst = ''
        
        while(i>=0 or j>=0):
            v = carry
            if i>=0:
                v += int(a[i])
            if j>=0:
                v += int(b[j])
            
            rst = str(v%2) + rst
            carry = int(v/2)
            
            if v+carry>=2:
                carry = 1
            else:
                carry = 0
            
            i -= 1
            j -= 1
        
        if carry == 1:
            rst = '1' + rst
        
        return rst

a = "101111"
b = "10"

print(Solution().addBinary(a,b))