
from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        """
        Stack, hash
        """

        stack = []
        i = 0
        curr = defaultdict(int)
        while i < len(formula):
            if formula[i] == '(':
                stack.append(curr)
                curr = defaultdict(int)
                i += 1
                
            elif formula[i] == ')':
                ## get the number after ')' if any
                j = i + 1
                while j < len(formula) and formula[j].isdigit():
                    j += 1
                num = 1
                if j > i + 1: # if there are digits
                    num = int(formula[i+1:j])
                
                for k in curr:
                    curr[k] *=  num
                
                i = j
                ## combine curr with the top element in stack.
                temp = stack.pop()
                for k, v in temp.items():
                    curr[k] += v
            
            else: ## element
                ## get the lower case letter if any
                j = i + 1
                while j < len(formula) and 'a' <= formula[j] <= 'z':
                    j += 1
                element = formula[i: j]
                ## get number if any
                i = j 
                while j < len(formula) and formula[j].isdigit():
                    j += 1
                num = 1
                if j > i: # if there are digits
                    num = int(formula[i:j])
                curr[element] += num
                i = j
        rst = []
        key = list(curr.keys())
        key.sort()
        for k in key:
            rst.append(k)
            if curr[k] > 1:
                rst.append(str(curr[k]))

        return ''.join(rst)




if __name__ == '__main__':
    formula = "(Cm39)5(Ga28Sb45Rb8)20(Bk13Fr29As)45"
    rst = Solution().countOfAtoms(formula)
    print(rst)