

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        """
        Two pointers
        """
        return max(self.helper(answerKey, k, flip='T'), self.helper(answerKey, k, flip='F'))
    
    def helper(self, answerKey, k, flip = 'T'):
        left = 0
        remain = k
        rst = 0
        for right in range(len(answerKey)):
            if answerKey[right] == flip:
                rst = max(rst, right - left + 1)
            else:
                remain -= 1
                while remain < 0:
                    if answerKey[left] != flip:
                        remain += 1
                    left += 1
                rst = max(rst, right - left + 1)
        return rst

if __name__ == '__main__':
    s = Solution()
    answerKey = "TTFTTFTT"
    k = 1
    rst = s.maxConsecutiveAnswers(answerKey, k)
    print(rst)