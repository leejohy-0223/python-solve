class Solution(object):
    def longestCommonPrefix(self, strs):
        template = strs[0]
        for i in range(1, len(strs)):
            now = strs[i]
            for j in range(len(template)):
                if j > len(now) - 1 or template[j] != now[j]:
                    template = template[:j]
                    break

        return template


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
    # Solution.py().longestCommonPrefix(["dog", "racecar", "car"])
