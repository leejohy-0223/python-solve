import re

def solution(files):
    files_init = [list(re.findall('(\D+)(\d+)(.*)', file)[0]) for file in files]
    files = [file + [str(file[0]).lower()] + [int(file[1])] for file in files_init]
    files = sorted(files, key=lambda file: file[4])
    files = sorted(files, key=lambda file: file[3])

    return ["".join(file[0:3]) for file in files]

if __name__ == '__main__':
    # print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
    print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))

    # strs = ["MUzI", "muzi", "Muzi", "muZi"]
    # strs.sort(key=str.lower)
    # print(strs)

    # tmp = "abc234adf33"
    # print(re.findall('\d+', tmp)[0])

    # nums = ["010", "9", "0011", "12", "012", "12", "008"]
    # nums.sort(key=int)
    # print(nums)
