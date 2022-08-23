from itertools import product

class Solution(object):
    def letterCombinations(self, digits):
        digits = digits.replace(" ", "")
        if digits == "":
            return []

        digitNum = dict()
        digitNum['2'] = "abc"
        digitNum['3'] = "def"
        digitNum['4'] = "ghi"
        digitNum['5'] = "jkl"
        digitNum['6'] = "mno"
        digitNum['7'] = "pqrs"
        digitNum['8'] = "tuv"
        digitNum['9'] = "wxyz"

        comb = []
        for digit in digits:
            comb.append(digitNum[digit])

        return list("".join(list(t)) for t in product(*comb))

if __name__ == '__main__':
    print(Solution().letterCombinations("67"))


