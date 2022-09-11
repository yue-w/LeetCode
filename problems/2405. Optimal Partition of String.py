
class Solution:
    def partitionString(self, s: str) -> int:
        """
        Greedy
        """
        rst = 0
        table = [0] * 26
        table[ord(s[0]) - ord('a')] = 1
        for char in s:
            idx = ord(char) - ord('a')
            if table[idx] == 0:
                table[idx] = 1
            else:
                table = [0] * 26
                table[idx] = 1
                rst += 1

        return rst
        