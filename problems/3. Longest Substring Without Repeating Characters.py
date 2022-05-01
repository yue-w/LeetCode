class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.look_up_table(s)
        
    def look_up_table(self, s: str) -> int:
        """
        running: O(n)
        time: constant (128)
        """
        if not s:
            return 0
        maxv = 0
        ## The table stores the last appearance in the table. -1 if not appeared. Remember this trick.
        ## There are 128 characters (ASCII).
        table = [-1] * 128
        left = 0
        for right in range(0, len(s)):
            left = max(left, table[ord(s[right])] + 1)
            table[ord(s[right])] = right   
            maxv = max(maxv, right - left + 1)

        return maxv
    
    def hash(self, s: str) -> int:
        """
        running: O(n)
        time: constant.
        Use set as hash.
        """
        seen = set()
        maxv = 0
        left = 0

        for right in range(left, len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            maxv = max(maxv, right - left + 1)

        return maxv





if __name__ == '__main__':
    solution = Solution()
    s = "abcabcbb"
    rst = solution.lengthOfLongestSubstring(s)
    print(rst)