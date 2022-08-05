class Solution(object):
    def intToRoman(self, num):
        roman = dict()
        roman[1000] = 'M'
        roman[500] = 'D'
        roman[100] = 'C'
        roman[50] = 'L'
        roman[10] = 'X'
        roman[5] = 'V'
        roman[1] = 'I'

        result = ""
        for i in roman.keys():
            if i > num:
                continue

            if str(num).startswith("4") or str(num).startswith("9"):
                # 현재 자리 수 (예를 들면 100)
                numberOfDigits = pow(10, len(str(num)) - 1)

                if str(num).startswith("4"):
                    result += roman[numberOfDigits] + roman[i + 4 * numberOfDigits]
                else:
                    result += roman[numberOfDigits] + roman[10 * numberOfDigits]

                num %= numberOfDigits

            else:
                nums = num // i
                result += nums * roman[i]
                num %= i

        return result

if __name__ == '__main__':
    print(Solution().intToRoman(58))
