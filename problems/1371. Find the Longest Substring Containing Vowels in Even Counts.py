
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        rst = 0
        dic = {}
        dic[0] = -1
        count = [0] * 5
        for i in range(len(s)):
            if s[i] == 'a':
                count[0] += 1
            elif s[i] == 'e':
                count[1] += 1
            elif s[i] == 'i':
                count[2] += 1
            elif s[i] == 'o':
                count[3] += 1
            elif s[i] == 'u':
                count[4] += 1
            code = self.count_to_code(count)
            if code in dic:
                rst = max(rst, i - dic[code])
            else:
                dic[code] = i
        
        return rst
        
    def count_to_code(self, count):
        key = 0
        for i in range(len(count)):
            if count[i] % 2:
                key += 1 << i
        return key

if __name__ == '__main__':
    s = Solution()
    string = "dabca"
    rst = s.findTheLongestSubstring(string)
    print(rst)