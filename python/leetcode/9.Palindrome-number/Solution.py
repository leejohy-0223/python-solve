class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        val = str(x)
        return val == val[::-1]

if __name__ == '__main__':
    print(Solution().isPalindrome(1221))
