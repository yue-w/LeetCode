
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = Counter(t)
        count_need = len(t)
        
        ## Record the best results so far
        min_len = len(s) + 1
        bst_left = -1
        bst_right = -1
        
        left = 0
        found_all = False
        for right in range(len(s)):
            char = s[right]
            if char in need:
                count_need -= need[char] > 0
                need[char] -= 1
                
                if count_need == 0:
                    found_all = True
            if found_all:
                while left < right:
                    ## If the char is not in t, throw it away
                    if not s[left] in need:
                        left += 1
                    else:
                        ## if the char is in t, and there are more
                        ## than one such char in the substring, increase
                        ## the counter by 1 and throw it away.
                        if need[s[left]] < 0:
                            need[s[left]] += 1
                            left += 1
                        else:
                            break

                ## Update the best value
                curr_len = right - left + 1
                if min_len > curr_len:
                    min_len = curr_len
                    bst_left = left
                    bst_right = right
        
        
        return s[bst_left: bst_right + 1]

if __name__ == '__main__':
    solution = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    rst = solution.minWindow(s, t)
    print(rst)