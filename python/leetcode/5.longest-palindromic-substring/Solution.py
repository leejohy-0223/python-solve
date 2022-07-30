class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # odd case
            tmp = self.finder(i, i, s)
            if len(res) < len(tmp):
                res = tmp

            # even case
            tmp = self.finder(i, i + 1, s)
            if len(res) < len(tmp):
                res = tmp

        return res

    def finder(self, left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

if __name__ == '__main__':
    print(Solution().longestPalindrome("babad"))
