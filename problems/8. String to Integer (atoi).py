

class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        ## find the first index of not space
        first = 0
        while first < len(s):
            if s[first] == ' ':
                first += 1
            else:
                break
        if first == len(s):
            return 0
        if first == len(s) - 1:
            if s[first].isdigit():
                return s[first]
        
        positive = True
        
        if s[first] == '-':
            positive = False
            first += 1
        elif s[first] == '+':
            first += 1
            
        if first >= len(s):
            return 0
        
        stack = []
        
        for i in range(first, len(s)):
            if s[i].isdigit():
                stack.append(s[i])
            else:
                break
        
        base = 1
        rst = 0
        while stack:
            num = int(stack.pop())
            rst += base * num
            base = base * 10
            
        
        if not positive:
            rst = -rst

        LB = - 2**31
        UB = 2**31 - 1
        if rst < LB:
            return LB
        if rst > UB:
            return UB
        else:
            return rst
"""
Clarification:
134.1 is read in as 134 ignore "."?
Leading characters other than white space? e.g. s = '%+'?
what is invalid number?
"""

if __name__ == '__main__':
    s = Solution()
    string = " +1"
    print(s.myAtoi(string))