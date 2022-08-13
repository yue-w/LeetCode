from typing import List
"""
A good problem to avoid duplication when searching in an array.
Reference:
https://github.com/wisdompeak/LeetCode/tree/master/DFS/301.Remove-Invalid-Parentheses
Rule:
Note s as the string to search from, and curr as the string selected so far,
when considering index i,
Case 1: s[i] == curr[-1]. must add s[i] into curr
Case 2: s[i] != curr[-1]. try both adding s[i] into curr and not adding s[i] into curr.
        calling recurion on the two sub cases.
The essence of the rule above is: if we select m same characters in the final result, they must be
the last m continuous characters. This helps avoid duplication.
Example:
s = '(((())'
the two '(' we select must be the last continuouse two '(' 
"""
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def dfs(curr, unmatchedleft, idx):
            ## base cases:
            if unmatchedleft < 0:
                return
            if len(curr) > finallength:
                return
            if idx == len(s):
                if len(curr) == finallength:
                    if unmatchedleft == 0:
                        rst.append(''.join(curr))
                return
            
            if s[idx] != '(' and s[idx] != ')':
                curr.append(s[idx])
                dfs(curr, unmatchedleft, idx + 1)
                curr.pop()
            else: #'(' or ')'
                ## if curr[-1] == s[idx], must select
                if curr and curr[-1] == s[idx]:
                    if s[idx] == '(':
                        unmatchedleft += 1
                    else: 
                        unmatchedleft -= 1
                    curr.append(s[idx])
                    dfs(curr, unmatchedleft, idx + 1)
                    ## backtracking
                    curr.pop()
                else: # select or not select
                    if s[idx] == '(':
                        unmatchedleftcp = unmatchedleft + 1
                    else: 
                        unmatchedleftcp = unmatchedleft - 1
                    ## path 1: select
                    curr.append(s[idx])
                    dfs(curr, unmatchedleftcp, idx + 1)
                    ## backtracking
                    curr.pop()
                    
                    ## path 2: not select
                    dfs(curr, unmatchedleft, idx + 1)
                    

        def count_unmatched(s):   
            ## count num of unmatched parenthesis
            left = 0
            right = 0
            for c in s:
                if c != '(' and c != ')':
                    continue
                if c == '(':
                    left += 1
                else:
                    if left > 0:
                        left -= 1
                    else:
                        right += 1
            unmatched = left + right
            return unmatched

        todelete = count_unmatched(s)
        finallength = len(s) - todelete

        rst = []

        dfs([], 0, 0)

        if not rst:
            return ['']
        return rst
            
if __name__ == '__main__':
    s = "(j))(" #")(v)((m(())()("
    rst = Solution().removeInvalidParentheses(s)
    print(rst)