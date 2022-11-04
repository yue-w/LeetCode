from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        curr = 0
        right = 0
        while right < len(chars):
            left = right
            chars[curr] = chars[left]
            
            while right + 1 < len(chars) and chars[right + 1] == chars[left]:
                right += 1
            
            length = right - left + 1
            right += 1
            if length == 1:
                curr += 1
                continue
            length = str(length)
            for i in range(len(length)):
                chars[curr + i + 1] = length[i]
            curr += len(length)
            curr += 1
            
        return curr
                
                
if __name__ == '__main__':
    s = Solution()
    chars = ["a","a","b","b","c","c","c"]
    rst = s.compress(chars)
    print(rst)