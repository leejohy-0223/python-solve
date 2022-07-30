class Solution(object):
    def lengthOfLongestSubstring(self, s):
        q = []
        result = 0
        for i in s:
            while i in q:
                q.pop(0)
            q.append(i)
            result = max(result, len(q))
        return result



if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("dvdf"))
