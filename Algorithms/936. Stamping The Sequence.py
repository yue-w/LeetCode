from typing import List

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        rst = []
        ns = len(stamp)
        nt = len(target)
        stamp = [c for c in stamp]
        target = [c for c in target]
        record = [0] * nt
        while sum(record) != nt:
            idx = self.find_match(stamp, target, record)
            
            if idx == -1:
                return []
            rst.append(idx)
            for i in range(idx, idx+ns):
                record[i] = 1

        rst.reverse()
        return rst
    
    def find_match(self, stamp, target, record):
        """
        return -1 if no match
        """
        ns = len(stamp)
        nt = len(target)
        for i in range(nt-ns+1):
            if sum(record[i:i+ns]) == ns:
                continue
            j = 0
            found = True
            while j < ns:
                if (target[i+j] == stamp[j]) or (record[i+j] == 1):
                    j += 1
                else:
                    found = False
                    break
            if found:
                
                return i
            
        return -1

if __name__ == "__main__":
    stamp = "abca"
    target = "aabcaca"
    rst = Solution().movesToStamp(stamp, target)
    print(rst)