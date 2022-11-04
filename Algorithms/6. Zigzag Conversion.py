
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]
        
        down = False
        i = 0
        for char in s:
            if i == 0:
                down = True
            elif i == numRows - 1:
                down = False
            rows[i].append(char)
            if down:
                i += 1
            else:
                i -= 1
        rst = []
        for row in rows:
            rst += row
            
        return ''.join(rst)


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    rst = Solution().convert(s, numRows)
    print(rst)