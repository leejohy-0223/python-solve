class Solution(object):
    def romanToInt(self, s):
        roman = dict()
        roman["M"] = 1000
        roman["CM"] = 900
        roman["D"] = 500
        roman["CD"] = 400
        roman["C"] = 100
        roman["XC"] = 90
        roman["L"] = 50
        roman["XL"] = 40
        roman["X"] = 10
        roman["IX"] = 9
        roman["V"] = 5
        roman["IV"] = 4
        roman["I"] = 1

        i, result = 0, 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i + 2] in roman.keys():
                result += roman[s[i:i + 2]]
                i += 2
            else:
                result += roman[s[i]]
                i += 1
        return result


if __name__ == '__main__':
    print(Solution().romanToInt('MCMXCIV'))