
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        monostack = []
        
        for i in range(len(num)):
            if not monostack:
                monostack.append(num[i])
            else:
                while k and monostack and num[i] < monostack[-1]:
                    monostack.pop()
                    k -= 1
                monostack.append(num[i])
        while k and monostack:
            monostack.pop()
            k -= 1
        
        if not monostack:
            return '0'
        
        ## remove leading 0
        for i in range(len(monostack)):
            if monostack[i] == '0':
                continue
            else:
                return ''.join(monostack[i:])
        return '0' 
                
                    
                    
        
