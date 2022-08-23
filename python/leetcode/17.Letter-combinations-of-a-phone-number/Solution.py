from itertools import product

class Solution(object):
    def letterCombinations(self, digits):
        digits = digits.replace(" ", "")
        if digits == "":
            return []

        digitNum = dict()
        digitNum['2'] = ['a', 'b', 'c']
        digitNum['3'] = ['d', 'e', 'f']
        digitNum['4'] = ['g', 'h', 'i']
        digitNum['5'] = ['j', 'k', 'l']
        digitNum['6'] = ['m', 'n', 'o']
        digitNum['7'] = ['p', 'q', 'r', 's']
        digitNum['8'] = ['t', 'u', 'v']
        digitNum['9'] = ['w', 'x', 'y', 'z']

        comb = []
        for digit in digits:
            comb.append(digitNum[digit])

        # comb = ["mno", "pqrs"]
        # *comb = mno pqrs
        print(comb) # 리스트 자체가 하나의 인자로 들어간다.
        print(*comb) # mno, pqrs가 각각 product 인자로 들어간다.

        return list("".join(list(t)) for t in product(*comb))

if __name__ == '__main__':
    print(Solution().letterCombinations("67"))


