class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 0:
            sx = str(-x)[::-1]
            while sx.startswith("0"):
                sx = sx[1:]
            sx = "-" + sx
        else:
            sx = str(x)[::-1]
            while sx.startswith("0"):
                sx = sx[1:]

        rx = int(sx)
        if -2**31 <= rx <= 2**31 + 1:
            return int(rx)
        else:
            return 0

if __name__ == '__main__':
    print(Solution().reverse(2343332213))