from collections import defaultdict

def solution(s):
    maps = defaultdict(int)

    ns = str(s)[2:len(s) - 2].replace('},{', ' ').split(' ')
    for n in ns:
        values = n.split(',')
        for v in values:
            maps[v] += 1

    sorted_maps = sorted(maps.items(), key=lambda item: item[1], reverse=True)

    for s in sorted_maps:
        print(s[0])

    return [int(s[0]) for s in sorted_maps]

if __name__ == '__main__':
    # print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
    print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))