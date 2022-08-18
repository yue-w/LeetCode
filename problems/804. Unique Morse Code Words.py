

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",\
                 ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",\
                 "...","-","..-","...-",".--","-..-","-.--","--.."]
        seen = set()
        for word in words:
            trans = []
            for w in word:
                idx = ord(w) - ord('a')
                trans.append(codes[idx])
            trans_word = ''.join(trans)
            seen.add(trans_word)
            
        return len(seen)