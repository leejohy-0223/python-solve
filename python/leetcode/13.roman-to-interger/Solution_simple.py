class Solution(object):
    def romanToInt(self, s):
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            #  4, 9인 케이스(뒤에가 더 큼)
            if roman[s[i]] < roman[s[i + 1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]

        z += roman[s[-1]]
        return z


if __name__ == '__main__':
    print(Solution().romanToInt('MCMXCIV'))