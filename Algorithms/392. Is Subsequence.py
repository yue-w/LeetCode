

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #return self.method1(s, t)
        return self.method2(s, t) # follow up
        
    def method1(self, s, t):
        """
        Time: O(s * t)
        """
        if not s and not t:
            return True
        idt = 0
        while idt < len(t):
            ids = 0
            while ids < len(s) and idt < len(t):
                if s[ids] == t[idt]:
                    ids += 1
                    idt += 1
                else:
                    idt += 1    
            if ids == len(s):
                return True
            
        return False
    
    def method2(self, s, t):
        """
        For follow up.
        for each character in t, record its index of occurance
        for every s, the running time is O(|s|*logt)
        """
        from collections import defaultdict
        import bisect
        table = defaultdict(list)
        for i in range(len(t)):
            table[t[i]].append(i)
        
        cur_idx = -1
        for c in s:
            idx_c_in_t = table[c]

            i = cur_idx
            # use binary search to find the smallest next index in t equals s[i]
            idx = bisect.bisect_right(idx_c_in_t, cur_idx)
            if idx < len(idx_c_in_t) and t[idx_c_in_t[idx]] == c:
                cur_idx = idx_c_in_t[idx]
            else:
                return False
        
        return True
            

if __name__ == '__main__':
    s = "acb"
    t = "ahbgdc"
    rst = Solution().isSubsequence(s, t)
    print(rst)
        