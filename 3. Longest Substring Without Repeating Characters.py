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
        ## The table stores the last appearance in the table. -1 if not appeared.
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
        """
        if not s:
            return 0
        seen = {}
        seen[s[0]] = 0
        maxv = 1
        left = 0
        for right in range(1, len(s)):
            if s[right] not in seen:
                seen[s[right]] = right
                maxv = max(maxv, len(seen))
            else:
                maxv = max(maxv, len(seen))
                # shift the left pointer and update dictionary    
                new_left = seen[s[right]]
                while left <= new_left:
                    del seen[s[left]]
                    left += 1
                seen[s[right]] = right   
            
        return maxv




if __name__ == '__main__':
    solution = Solution()
    s = "abcabcbb"
    rst = solution.lengthOfLongestSubstring(s)
    print(rst)