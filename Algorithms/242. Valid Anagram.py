
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = [0] * 26
        base = ord('a')
        for char in s:
            index = ord(char) - base
            table[index] += 1
        for char in t:
            index = ord(char) - base
            table[index] -= 1
            if table[index] < 0:
                return False
        return sum(table) == 0
            