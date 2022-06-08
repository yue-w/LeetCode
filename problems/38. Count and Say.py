
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        
        string = '11'
        i = 3
        while i <= n:
            left = 0
            right = 0
            newstring = ''
            while right < len(string):
                if right == len(string) - 1:
                    newstring += str(right - left + 1) + str(string[left])
                    break
                else:
                    while right < len(string) - 1 and string[right] == string[right + 1]:
                        right += 1
                    newstring += str(right - left + 1) + str(string[left])
                    right += 1
                    left = right
            string = newstring
            i += 1

        return string


if __name__ == '__main__':
    solution = Solution()
    n = 6
    rst = solution.countAndSay(n)
    print(rst)