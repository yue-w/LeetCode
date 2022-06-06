

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Two pointers. Find the most common char, flip others.
        """
#         counts = [0] * 26
#         rst = 0
#         left = 0
        
#         for right in range(len(s)):
#             counts[ord(s[right]) - ord('A')] += 1
            
#             ## if the current window does not satisfy the requirement,
#             ## move left forward, and this will make this window satisfy the
#             ## requirement again
#             max_count = max(counts)
#             if right - left + 1 - max_count > k:
#                 counts[ord(s[left]) - ord('A')] -= 1
#                 left += 1
#             rst = max(rst, right - left + 1)
        
#         return rst
        counts = [0] * 26
        rst = 0
        right = 0
        
        for left in range(len(s)):
            most_common = max(counts)
            ## if the count of flipped chars is less than k, increase right
            while right < len(s) and right - left + 1 - most_common < k:
                counts[ord(s[right]) - ord('A')] += 1
                right += 1
                most_common = max(counts)
                    
            rst = max(rst, right - left)
            counts[ord(s[left]) - ord('A')] -= 1
            left += 1
                
        return rst

if __name__ == '__main__':
    s = Solution()
    string = "ABAB"
    k = 2
    rst = s.characterReplacement(string, k)
    print(rst)