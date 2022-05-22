
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Brute force O(n^2)
        Condider both odd and even cases
        """
        n = len(s)
        maxlen = 0
        left = 0
        right = 0
        for i in range(n):
            ## odd case
            l = i
            r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            ## when reached this point, l and r are no longer the boundary,
            ## and the real boundary is l + 1 and r - 1, the length is r - l + 1 - 2
            if maxlen < r - l - 1:
                maxlen = r - l - 1
                left = l + 1
                right = r - 1
            
            ## even case
            l = i 
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if maxlen < r - l - 1:
                maxlen = r - l - 1
                left = l + 1
                right = r - 1
        
        
        return s[left:right+1]

if __name__ == '__main__':
    s = Solution()
    string = 'babad'
    rst = s.longestPalindrome(string)
    print(rst) 
