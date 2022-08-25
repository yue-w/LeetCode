

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        for r in ransomNote:
            counter[r] -= 1
            if counter[r] < 0:
                return False
        return True