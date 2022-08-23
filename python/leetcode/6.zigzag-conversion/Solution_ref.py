class Solution:
    def convert(self, s: str, numRows: int) -> str:
        interval = 0 if numRows == 1 else -1
        rows, idx = [''] * numRows, 0
        for c in s:
            rows[idx] += c
            if idx == 0 or idx == numRows - 1:
                interval = -interval
            idx += interval

        return ''.join(rows)

if __name__ == '__main__':
    # print(Solution.py().convert("PAYPALISHIRING", 5))
    # print(Solution.py().convert("A", 1))
    # print(Solution.py().convert("ABCD", 3))
    print(Solution().convert("AB", 1))
