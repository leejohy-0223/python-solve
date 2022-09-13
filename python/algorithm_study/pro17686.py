import re

def solution(files):
    sortedByNumber = sorted(files, key=lambda file: int(re.findall('\d+', file)[0]))
    sortedByStrings = sorted(sortedByNumber, key=lambda file: re.split('\d+', file.lower())[0])
    return sortedByStrings

if __name__ == '__main__':
    # print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))

    # strs = ["MUzI", "muzi", "Muzi", "muZi"]
    # strs.sort(key=str.lower)
    # print(strs)

    tmp = "abc234adf33"
    print(re.findall('\d+', tmp)[0])

    # nums = ["010", "9", "0011", "12", "012", "12", "008"]
    # nums.sort(key=int)
    # print(nums)
