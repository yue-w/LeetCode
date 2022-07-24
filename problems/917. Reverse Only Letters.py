

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        string = [char for char in s]
        i = 0
        j = len(s) - 1
        while i < j:
            if not string[i].isalpha():
                i += 1
                continue
            if not string[j].isalpha():
                j -= 1
                continue
            
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1

        return ''.join(string)