
class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Time: O(n^2)
        """
        ## Odd length:
        odd_len = 0
        for i in range(len(s)):
            shift = 0
            while i - shift >= 0 and i + shift < len(s) and s[i - shift] == s[i + shift]:
                odd_len += 1
                shift += 1
    
        ## even length:
        even_len = 0
        for i in range(0, len(s) - 1):
            shift = 0
            if s[i] == s[i + 1]:
                shift = 0
                while i - shift >= 0 and i + 1 + shift < len(s) and s[i - shift] == s[i + 1 + shift]:
                    even_len += 1
                    shift += 1

        return odd_len + even_len


if __name__ == '__main__':
    sol = Solution()
    s = "aaaaa"
    rst = sol.countSubstrings(s)
    print(rst)




    #     pointer = 0
    #     rst = len(s)
    #     rst += self.helper(s, 0)
    #     return rst
    
    # def helper(self, s, index):
    #     ## Base case:
    #     if index >= len(s):
    #         return 0
    #     seen = {}
    #     run_rst = 0
    #     for i in range(index, len(s)):
    #         if s[i] not in seen:
    #             seen[s[i]] = i
    #         else:
    #             pivot = i - 1
    #             if s[pivot] == s[i]:
    #                 run_rst += 1
    #             j = 1
    #             while pivot - j >= 0 and i + j - 1 < len(s) and s[pivot - j] == s[i + j - 1]:
    #                 run_rst += 1
    #                 j += 1
    #             run_rst += self.helper(s, i+1)
                    
    #     return run_rst