class Solution(object):
    def lengthOfLongestSubstring(self, s):
        pos = dict()

        result = 0
        i, j = 0, 0
        for idx, val in enumerate(s):
            if val in pos.keys():
                j = max(j, pos[val] + 1)

            pos[val] = idx
            result = max(result, i - j + 1)


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abbbba"))
