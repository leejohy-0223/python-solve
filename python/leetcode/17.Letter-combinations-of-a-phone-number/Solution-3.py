class Solution(object):
    def letterCombinations(self, digits):
        digits = digits.replace(" ", "")
        if digits == "":
            return []
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        res = []
        self.dfs(digits, dic, res, "", 0)
        return res

    def dfs(self, digits, dic, res, path, index):
        if index == len(digits):
            res.append(path)
            return

        nowString = dic[digits[index]]
        for c in nowString:
            self.dfs(digits, dic, res, path + c, index + 1)


if __name__ == '__main__':
    print(Solution().letterCombinations("67"))
